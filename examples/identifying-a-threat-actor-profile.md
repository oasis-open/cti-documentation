---
layout: page
title: Identifying a Threat Actor Profile
categories: examples
---

Commercial threat intelligence providers and well-resourced government agencies often attribute malicious activity to a particular threat actor or actor group.

**Scenario**
------------

In this scenario, a threat actor group named “Disco Team” is modeled using STIX Threat Actor and Identity objects. Disco Team operates primarily in Spanish and they have been known to steal credit card information for financial gain. They use the e-mail alias “disco-team@stealthemail.com” publicly and are known alternatively as “Equipo del Discoteca”.

**Data model**
--------------

Threat actor identification is, as you would expect, represented using the [Threat Actor](https://docs.google.com/document/d/1S5XhY6F5OT599b0OuHtUf8IBzFvNY8RysFHIj93DgsY/edit#heading=h.k017w16zutw) STIX Domain Object (SDO). Information relevant to threat actors, such as goals and motivations, can be captured within this object. Other basic information not specific to threat actors, such as contact information, is best represented using an Identity SDO. Identity objects can also be used for more than threat actors in STIX. They can model organizations, government agencies, and information sources to name a few.

It is important to note that the Disco Team group operates as a Threat Actor and not an [Intrusion Set](https://docs.google.com/document/d/1S5XhY6F5OT599b0OuHtUf8IBzFvNY8RysFHIj93DgsY/edit#heading=h.5ol9xlbbnrdn) in this scenario. They could potentially support an intrusion set, but that information is unknown. An Intrusion Set is best used to describe an entire attack set that would include multiple campaigns and purposes. In this instance, Disco Team is a self-named threat actor operating with one purpose in mind.

The <span class="sdo">**name**</span> and <span class="sdo">**labels**</span> properties are the only required properties needed for a Threat Actor SDO. The <span class="sdo">**labels**</span> field is important for describing what type of threat actor Disco Team is. Because Disco Team is regarded as large, organized, and driven to steal financial information, they are best represented with the label <span class="values">crime-syndicate</span>.

The Threat Actor SDO can also model optional properties that construct a more complete threat actor profile. The <span class="sdo">**aliases**</span> field, for instance, contains a list of other names this threat actor is known to be called. A threat actor may also have one or more <span class="sdo">**roles**</span> that describe more about what they do. For instance, a threat actor could sponsor or direct attacks, author malware, or operate malicious infrastructure. In the case of Disco Team, they operate as an <span class="values">agent</span>, carrying out attacks that steal financial information on behalf of themselves.

Like most threat actors, Disco Team has a specific goal in mind for their attacks. Therefore, a list of <span class="sdo">**goals**</span> describes what the threat actor is trying to do. In this case, Disco Team’s only goal is stealing credit card credentials. Threat actors also have varying degrees of expertise, so the <span class="sdo">**sophistication**</span> level of the attacker, if known, can describe the attacker’s skill and knowledge. Disco Team is labeled as <span class="values">expert</span> due to advanced attack methods and proficiency with tools or malicious code. Their <span class="sdo">**resource\_level**</span> of <span class="values">organization</span> indicates that they are large and well-funded, more so than smaller individuals or teams. Finally, threat actors usually have one or several motivations behind their attacks. The <span class="sdo">**primary\_motivation**</span> field describes the main reason for attacking. Some threat actors may seek notoriety or dominance, while others are strictly doing it for revenge or personal satisfaction. For Disco Team, obtaining financial information falls under the motivation of <span class="values">personal-gain</span>.

Basic identifying information of the threat actor can be modeled with the [Identity](https://docs.google.com/document/d/1nipwFIaFwkHo4Gzw-qxZQpCjP_5tX7rbI3Ic5C56Z88/edit#heading=h.wh296fiwpklp) SDO. For Disco Team, they are a type of <span class="values">organization</span>, which the <span class="sdo">**identity\_class**</span> field captures. This is due to this threat actor being more formal and organized, rather than an <span class="values">individual</span> hacker or informal <span class="values">group</span> of hackers. Another property that captures <span class="sdo">**contact\_information**</span>, if known for the identity, represents any email addresses or phone numbers. For Disco Team, an email address is provided.

Now that the information for Disco Team is represented in the Threat Actor and Identity SDO’s, the [Relationship](https://docs.google.com/document/d/1nipwFIaFwkHo4Gzw-qxZQpCjP_5tX7rbI3Ic5C56Z88/edit#heading=h.e2e1szrqfoan) SRO links the two objects together. In this example, the <span class="sdo">**source\_ref**</span> threat actor id is <span class="values">attributed-to</span> the <span class="sdo">**target\_ref**</span> identity id:

A diagram of this relationship below shows the Threat Actor and Identity SDO’s and the Relationship SRO:

![Identifying a TA Profile Diagram]({{ site.baseurl }}/img/Identifying-a-TA-profile.PNG)

**Further Reading**
-------------------

To read more about the objects in this example as well as common properties and vocabularies, check out the links below:

-   [Common Properties](https://docs.google.com/document/d/1HRVFn2kAxBOTMbEb3KRu8tjMoHm-KRAI-2R8CTzGil4/edit#heading=h.xzbicbtscatx)
-   [Vocabularies](https://docs.google.com/document/d/1HRVFn2kAxBOTMbEb3KRu8tjMoHm-KRAI-2R8CTzGil4/edit#heading=h.iit7tolczlxv)
-   [Threat Actor](https://docs.google.com/document/d/1nipwFIaFwkHo4Gzw-qxZQpCjP_5tX7rbI3Ic5C56Z88/edit#heading=h.k017w16zutw)
-   [Identity](https://docs.google.com/document/d/1nipwFIaFwkHo4Gzw-qxZQpCjP_5tX7rbI3Ic5C56Z88/edit#heading=h.wh296fiwpklp)
-   [Relationship](https://docs.google.com/document/d/1nipwFIaFwkHo4Gzw-qxZQpCjP_5tX7rbI3Ic5C56Z88/edit#heading=h.e2e1szrqfoan)

**JSON**
------------------

```
{
  "type": "bundle",
  "id": "bundle--c9567f73-3803-415c-b06e-2b0622830e5d",
  "spec_version": "2.0",
  "objects": [
    {
      "type": "threat-actor",
      "id": "threat-actor--dfaa8d77-07e2-4e28-b2c8-92e9f7b04428",
      "created": "2014-11-19T23:39:03.893348Z",
      "modified": "2014-11-19T23:39:03.893348Z",
      "name": "Disco Team Threat Actor Group",
      "description": "This organized threat actor group operates to create profit from all types of crime.",
      "labels": [
        "crime-syndicate"
      ],
      "aliases": [
        "Equipo del Discoteca"
      ],
      "roles": [
        "agent"
      ],
      "goals": [
        "Steal Credit Card information"
      ],
      "sophistication": "expert",
      "resource_level": "organization",
      "primary_motivation": "personal-gain"
    },
    {
      "type": "identity",
      "id": "identity--733c5838-34d9-4fbf-949c-62aba761184c",
      "created": "2016-08-23T18:05:49.307000Z",
      "modified": "2016-08-23T18:05:49.307000Z",
      "name": "Disco Team",
      "description": "Disco Team is the name of an organized threat actor crime-syndicate.",
      "identity_class": "organization",
      "contact_information": "disco-team@stealthemail.com"
    },
    {
      "type": "relationship",
      "id": "relationship--966c5838-34d9-4fbf-949c-62aba7611837",
      "created": "2016-08-23T18:05:49.307000Z",
      "modified": "2016-08-23T18:05:49.307000Z",
      "relationship_type": "attributed-to",
      "source_ref": "threat-actor--dfaa8d77-07e2-4e28-b2c8-92e9f7b04428",
      "target_ref": "identity--733c5838-34d9-4fbf-949c-62aba761184c"
    }
  ]
}
```
