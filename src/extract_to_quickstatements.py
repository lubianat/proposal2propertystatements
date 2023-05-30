import requests
from bs4 import BeautifulSoup
from wdcuration import render_qs_url


def fetch_proposal_page(id_name):
    url = f"https://www.wikidata.org/w/index.php?title=Wikidata:Property_proposal/{id_name}&action=edit"
    r = requests.get(url)
    html = r.text
    return html


def parse_html_to_dict(html):
    soup = BeautifulSoup(html, "lxml")
    entries = soup.find("textarea")
    page = entries.text
    property_proposal_dict = convert_infobox_to_dict(page)
    property_proposal_dict = clean_up_dict(property_proposal_dict)
    return property_proposal_dict


def convert_infobox_to_dict(property_proposal):
    property_proposal_items = property_proposal.split("\n|")
    property_proposal_dict = {
        a.split("=")[0].strip(): a.split("=")[1].strip()
        for a in property_proposal_items
        if "=" in a
    }
    return property_proposal_dict


def clean_up_dict(property_proposal_dict):
    clean_up_pairs = [
        ("{", ""),
        ("}", ""),
        ("|", ""),
        ("QQ", "Q"),
        ("<nowiki>", ""),
        ("</nowiki>", ""),
    ]
    for pair in clean_up_pairs:
        property_proposal_dict = {
            k: v.replace(pair[0], pair[1]) for k, v in property_proposal_dict.items()
        }
    return property_proposal_dict


def create_quickstatements(property_proposal_dict, id_name, property_id):
    proposal_page = (
        f"https://www.wikidata.org/wiki/Wikidata:Property_proposal/{id_name}"
    )
    qs = form_qs_string(property_proposal_dict, proposal_page, property_id)
    if "see also" in property_proposal_dict:
        for value in [a.strip() for a in property_proposal_dict["see also"].split(",")]:
            qs += f"""{property_id}|P1659|{value}\n"""
    qs = add_examples_to_quickstatements(
        property_proposal_dict, proposal_page, property_id, qs
    )
    return qs


def form_qs_string(property_proposal_dict, proposal_page, property_id):
    if property_proposal_dict["datatype"] == "Quantity":
        qs = f"""
            {property_id}|P1629|{property_proposal_dict['subject item']}
            {property_proposal_dict['subject item']}|P1687|{property_id}
            {property_id}|P3254|"{proposal_page}"
        """
    else:
        qs = f"""
            {property_id}|P1630|"{property_proposal_dict['formatter URL']}"
            {property_id}|P1629|{property_proposal_dict['subject item']}
            {property_id}|P1687|{property_id}
            {property_id}|P3254|"{proposal_page}"
            {property_id}|P2429|{property_proposal_dict['expected completeness']}
        """
    if property_proposal_dict["distinct values constraint"] == "yes":
        qs += f"""{property_id}|P2302|Q21502410\n"""
    return qs


def add_examples_to_quickstatements(
    property_proposal_dict, proposal_page, property_id, qs
):
    import re

    special_separator = "''visited by''"
    for k, v in property_proposal_dict.items():
        if "example" in k:
            if property_proposal_dict["datatype"] == "item":
                qids = re.findall("Q[0-9]+", v)
                if len(qids) < 2:
                    continue
                subject = qids[0]
                object = qids[1]
                qs += f"""
                    {subject}|{property_id}|{object}|S854|"{proposal_page}"
                    {property_id}|P1855|{subject}|{property_id}|{object}|S854|"{proposal_page}"
                """
            else:
                if "Statement" in v:
                    subject = re.findall("Statement(Q[0-9]*)", v)[0]
                else:
                    subject = v.split(" → ")[0]
                    subject = v.split(special_separator)[0]
                try:
                    objects = v.split(" → ")[1].split(", ")
                except IndexError:
                    objects = [v]
                for object in objects:
                    formatted_object = object.split(" ")[-1].replace("]", "")
                    qs += f"""
                        {subject}|{property_id}|"{formatted_object}"|S854|"{proposal_page}"
                        {property_id}|P1855|{subject}|{property_id}|"{formatted_object}"|S854|"{proposal_page}"
                    """
    return qs


def main(id_name, property_id):
    html = fetch_proposal_page(id_name)
    property_proposal_dict = parse_html_to_dict(html)
    qs = create_quickstatements(property_proposal_dict, id_name, property_id)
    print(qs)
    print(render_qs_url(qs))


id_name = "attracts"
property_id = "P11801"
main(id_name, property_id)
