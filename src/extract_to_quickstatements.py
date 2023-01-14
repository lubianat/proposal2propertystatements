from wdcuration import render_qs_url

proposal_page = (
    "https://www.wikidata.org/wiki/Wikidata:Property_proposal/CiNii_Research_ID"
)

property_proposal = """
{{Property proposal
|status			= ready
|description		= {{TranslateThis
 | en = 19-digits identifier in CiNii Research
 | ja = CiNii Researchで使用される19桁の識別子
 }}
|subject item           = {{Q|115920372}}
|infobox parameter	= 
|datatype		= external-id
|domain			= {{Q|106559804}}, {{Q|732577}}, {{Q|1298668}}, {{Q|15809982}}
|allowed values		= <nowiki>[1-9]\d{18}</nowiki>
|allowed units          = 
|source			= {{Q|115921722}}, [[:w:ja:Template:CiNii Research]]
|example 1		= {{Q|105949}} → [https://cir.nii.ac.jp/crid/1030003658315966466 1030003658315966466]
|example 2		= {{Q|8739}} → [https://cir.nii.ac.jp/crid/1140000791739227520 1140000791739227520]
|example 3		= {{Q|11383920}} → [https://cir.nii.ac.jp/crid/1030285133353879936 1030285133353879936], [https://cir.nii.ac.jp/crid/1030285133821492864 1030285133821492864]
|example 4		= {{Q|55385556}} → [https://cir.nii.ac.jp/crid/1010000781827953028 1010000781827953028], [https://cir.nii.ac.jp/crid/1050001202560747520 1050001202560747520]
|example 5		= {{Q|3554851}} → [https://cir.nii.ac.jp/crid/1362825894493916800 1362825894493916800], [https://cir.nii.ac.jp/crid/1572824499129263616 1572824499129263616], [https://cir.nii.ac.jp/crid/1573105975389388928 1573105975389388928], [https://cir.nii.ac.jp/crid/1573668925345822208 1573668925345822208], [https://cir.nii.ac.jp/crid/1573950400319221888 1573950400319221888]
|example 6		= {{Q|106910410}} → [https://cir.nii.ac.jp/crid/1130000794733479936 1130000794733479936]
|example 7		= {{Q|183883}} → [https://cir.nii.ac.jp/crid/1130000793680077824 1130000793680077824]
|example 8      = {{Q|107396565}} → [https://cir.nii.ac.jp/crid/1541417145276398336 1541417145276398336]
|example 9		= {{Q|151794}} → [https://cir.nii.ac.jp/crid/1140563741735693184 1140563741735693184], [https://cir.nii.ac.jp/crid/1580009750427316224 1580009750427316224]
|example 10		= {{Q|11527570}} → [https://cir.nii.ac.jp/crid/1140000791822845696 1140000791822845696], [https://cir.nii.ac.jp/crid/1140563741606120192 1140563741606120192]
|planned use            = 
|number of ids          = 
|expected completeness  = {{Q|21873886}}
|formatter URL		= https://cir.nii.ac.jp/crid/$1
|implied notability = 
|external links         = https://cir.nii.ac.jp/crid/
|see also               = {{P|349}}, {{P|1054}}, {{P|2687}}, {{P|5029}}, {{P|7783}}, {{P|9776}}, {{P|9836}}
|robot and gadget jobs	= Add statement to items using {{P|271}}, {{P|1739}}, {{P|2409}}, {{P|4787}}, {{P|9776}}, etc.
|subpage		= CiNii Research ID
|topic			= authority control
|applicable stated in value = {{Q|10726338}}
|single value constraint      = <del>yes, but there are several exceptions</del><ins>no</ins>
|distinct values constraint   = yes
|Wikidata project  = [[Wikidata:WikiProject Authority control|WikiProject Authority control]], [[Wikidata:WikiProject Japan|WikiProject Japan]]
}}
"""


property_id = "P11496"


def convert_infobox_to_dict(property_proposal):
    property_proposal_items = property_proposal.split("\n|")

    property_proposal_dict = {
        a.split("=")[0].strip(): a.split("=")[1].strip()
        for a in property_proposal_items
        if "=" in a
    }
    return property_proposal_dict


property_proposal_dict = convert_infobox_to_dict(property_proposal)

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

description_box = convert_infobox_to_dict(property_proposal_dict["description"])

qs = f"""
{property_id}|P1630|"{property_proposal_dict['formatter URL']}"
{property_id}|P1629|{property_proposal_dict['subject item']}
{property_proposal_dict['subject item']}|P1687|{property_id}
{property_id}|P1793|"{property_proposal_dict['allowed values']}"
{property_id}|P3254|"{proposal_page}"
{property_id}|P2429|{property_proposal_dict['expected completeness']}
"""

if property_proposal_dict["distinct values constraint"] == "yes":

    qs += f"""{property_id}|P2302|Q21502410
"""

for value in [a.strip() for a in property_proposal_dict["see also"].split(",")]:
    qs += f"""{property_id}|P1659|{value}
"""

for k, v in property_proposal_dict.items():
    if "example" in k:
        subject = v.split(" → ")[0]

        objects = v.split(" → ")[1].split(", ")

        for object in objects:
            formatted_object = object.split(" ")[1].replace("]", "")
            qs += f"""
{subject}|{property_id}|"{formatted_object}"|S854|"{proposal_page}"
{property_id}|P1855|{subject}|{property_id}|"{formatted_object}"|S854|"{proposal_page}"
            """

print(render_qs_url(qs))
