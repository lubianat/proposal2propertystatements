page = """
=== {{TranslateThis | anchor = en
| en = Digital Library of Mathematical Functions ID
<!-- |xx = property names in some other languages -->
}} ===
{{Property proposal
|status			= done
|description		= {{TranslateThis
 | en = identifier for a function in the NIST Digital Library of Mathematical Functions
<!-- | xx = descriptions in other languages -->
 }}
|subject item           = Q24534
|infobox parameter	= "id" in [[:en:template:Dlmf]] 
|datatype		= external-id
|domain			= items of type {{Q|Q11348}}
|allowed values		= <nowiki>((\d+\.)+)E\d+</nowiki>
|allowed units          = <!-- units that are allowed for values of this property if the datatype is quantity -->
|source			= [https://dlmf.nist.gov/ NIST Digital Library of Mathematical Functions &mdash; online companion to the NIST Handbook of Mathematical Functions]
<!-- you should provide 3 examples at least-->
|example 1		= {{Statement|Q385019|Digital Library of Mathematical Functions ID|[https://dlmf.nist.gov/27.2.E13 27.2.E13]}} 
|example 2		= {{Statement|Q168698|Digital Library of Mathematical Functions ID|[https://dlmf.nist.gov/4.2.E19 4.2.E19]}}
|example 3		= {{Statement|Q6520159|Digital Library of Mathematical Functions ID|[https://dlmf.nist.gov/1.14.E1 1.14.E1]}}
|example 4		= {{Statement|Q187235|Digital Library of Mathematical Functions ID|[https://dlmf.nist.gov/25.2.E1 25.2.E1]}}
|example 5		= {{Statement|Q1264373|Digital Library of Mathematical Functions ID|[https://dlmf.nist.gov/4.14.E7 4.14.E7]}}
<!-- if convenient, include more examples by following the same pattern:
|example ... =  {{Statement|subject|property|value}}
-->
|planned use            = improving items about mathematical functions
|number of ids          = currently ca. 13k
|expected completeness  = Q21873886
|formatter URL		= https://dlmf.nist.gov/$1
|implied notability = {{Q|62589320}}
|external links         = dlmf.nist.gov
|see also               = <!-- other, related properties -->
|robot and gadget jobs	= <!-- Should or are bots or gadgets doing any task with this? (Checking other properties for consistency, collecting data, etc.) -->
|subpage		= Digital Library of Mathematical Functions ID
|topic			= authority control
|applicable stated in value = <!-- If the proposed property (for an external identifier) is to be used in references, create an item for its database or website suitable as value for "stated in" (P248) and add this here. It is added to properties with P9073 on creation. The item used as value can be the same as used with "subject item". -->
|single value constraint      = yes
|distinct values constraint   = yes
|Wikidata project  = {{Q|Q8487137}}
}}

====Motivation====
When it comes to structured information about mathematical functions, {{Q|Q24534}} is a reference work that is widely used both within and beyond the Wikimedia ecosystem. Mapping to it in a systematic fashion by way of such a property would help improve Wikidata's coverage of functions too. [[User:Daniel Mietchen|Daniel Mietchen]] ([[User talk:Daniel Mietchen|<span class="signature-talk">{{int:Talkpagelinktext}}</span>]]) 22:21, 29 December 2022 (UTC)
:{{Ping project|Mathematics}} --[[User:Daniel Mietchen|Daniel Mietchen]] ([[User talk:Daniel Mietchen|<span class="signature-talk">{{int:Talkpagelinktext}}</span>]]) 22:23, 29 December 2022 (UTC)

===={{int:Talk}}====
* {{s}} external identifier. I would also suggest properties like [[Property:P829|OEIS ID]] for people looking for other similar properties (external identifiers). [[User:Jsamwrites|John Samuel]] ([[User:Jsamwrites|talk]]) 07:58, 30 December 2022 (UTC)
* {{s}} Nice. [[User:ArthurPSmith|ArthurPSmith]] ([[User talk:ArthurPSmith|<span class="signature-talk">{{int:Talkpagelinktext}}</span>]]) 15:21, 31 December 2022 (UTC)
* {{s}} —'''[[User:The-erinaceous-one|<span style="color: SaddleBrown ;"> The Erinaceous One 🦔</span>]]''' 07:34, 2 January 2023 (UTC)
* {{s}} To discover the link to a formula one can hover over the circled "i" and look for "permalink" (Stating it here because I needed a moment to find this.). Looks like a great source. [[User:Toni 001|Toni 001]] ([[User talk:Toni 001|<span class="signature-talk">{{int:Talkpagelinktext}}</span>]]) 08:32, 5 January 2023 (UTC)
* {{s}} An excellent resource, great find! [[Special:Contributions/2A00:23C4:AF01:DA01:F0AE:7E64:9233:2629|2A00:23C4:AF01:DA01:F0AE:7E64:9233:2629]] 10:13, 6 January 2023 (UTC)

* {Created as {{P|P11497}} ~~~~ 
"""

import re


a = re.findall("User:(.*?)\|", page)

ping = "{{ping|" + "|".join(list(set(a))) + "}}"
print(ping)
