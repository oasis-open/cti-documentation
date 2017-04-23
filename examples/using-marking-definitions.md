---
layout: page
title: Using Marking Definitions
categories: examples
---

Being able to structure the handling of data through the use of data markings is vital for organizations who share cyber threat intelligence (CTI). This benefit allows STIX producers to limit the accessibility of objects and also communicates terms of use and copyright information.

**Scenario**
------------

This scenario focuses on a STIX producer, “Stark Industries”, who imposes object markings on an indicator object. Before sharing this indicator, Stark creates both “Statement” and “Traffic Light Protocol” (TLP) marking definitions to apply to the indicator. These marking definitions incorporate copyright information and restrict the usage of the indicator based on its TLP marking type.

**Data model**
--------------

First, we start with the producer of the STIX content in this scenario, Stark Industries. The information relevant to this company can be represented using an [Identity](https://docs.google.com/document/d/1S5XhY6F5OT599b0OuHtUf8IBzFvNY8RysFHIj93DgsY/edit#heading=h.wh296fiwpklp) STIX Domain Object (SDO). Like with all STIX objects, an <span class="sdo">**id**</span> attribute uniquely identifies Stark Industries and can be referenced within all the objects they generate with the <span class="sdo">**created\_by\_ref**</span> property. Although <span class="sdo">**created\_by\_ref**</span> is optional, this is helpful for attributing the created marking definitions directly to Stark. The Identity object is also useful for listing other relevant details about Stark such as <span class="sdo">**contact\_information**</span> and what type of identity they are with the <span class="sdo">**identity\_class**</span> field.

Next, Stark created a couple of STIX [Marking Definition](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.k5fndj2c7c1k) objects to restrict the handling of the Indicator object and to incorporate copyright information. In the first instance, Stark uses the [TLP Marking Object Type](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.yd3ar14ekwrs) to communicate appropriate restrictions for the indicator. For this Marking Definition object, the <span class="sdo">**definition\_type**</span> must be <span class="values">tlp</span> and the <span class="sdo">**definition**</span> field must contain one of the four types of TLP. In this example, the TLP restriction type is <span class="values">amber</span>. This provides limited disclosure to only appropriate recipients who have a need to know. To read about this restriction and the other types of TLP, check out [US-CERT’s TLP Definitions and Usage](https://www.us-cert.gov/tlp).

A second marking type, [Statement](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.3ru8r05saera), is used for Stark Industries’ copyright information and is applied to all objects they produce. This is similar in format to the TLP Marking Definition object, except the <span class="sdo">**definition\_type**</span> in this case must be <span class="values">statement</span>. The <span class="sdo">**definition**</span> field contains any type of terms of use or copyright information you want to convey. For this organization, it simply states <span class="values">Copyright @ Stark Industries 2017</span>. This property could also communicate any terms of use, or you could incorporate both since Statement allows for multiple marking types.

A point of emphasis worth noting is that Marking Definition objects cannot be versioned like other STIX objects. For instance, if Stark Industries wanted to update their Statement information or add terms of use to the marking definition, they would have to generate a new Marking Definition object with the Indicator SDO updated to point to this new definition. They could not add or change their current Statement marking and simply update the modified property.

Finally, Stark can apply these marking definitions to the [Indicator](https://docs.google.com/document/d/1S5XhY6F5OT599b0OuHtUf8IBzFvNY8RysFHIj93DgsY/edit#heading=h.muftrcpnf89v) SDO that contains the malicious IP address they discovered on their network. These object markings are embedded within the Indicator object in the <span class="sdo">**object\_marking\_refs**</span> property and reference the Marking Definition object <span class="sdo">**id**</span>’s for both Statement and TLP. Once referenced, both of Stark’s markings apply to the Indicator object. It’s worth mentioning that this property and the <span class="sdo">**created\_by\_ref**</span> property presented earlier represent one of just a few embedded relationships in STIX 2.0. In most cases, to establish a relationship between objects in STIX, such as between an Indicator and Threat Actor SDO, you would create a [Relationship](https://docs.google.com/document/d/1S5XhY6F5OT599b0OuHtUf8IBzFvNY8RysFHIj93DgsY/edit#heading=h.e2e1szrqfoan) STIX Relationship Object (SRO).

Other than object marking references, the rest of the Indicator object contains properties that detail information about the IP address. The <span class="sdo">**pattern**</span> property, for instance, is based on the [STIX patterning language](https://docs.google.com/document/d/1suvd7z7YjNKWOwgko-vJ84jfGuxSYZjOQlw5leCswPY/edit) and represents an IPv4 address as a comparison expression: <span class="values">\[ipv4addr:value = '10.0.0.0'\]</span>. Stark also knows this is a nefarious IP and relays this information with the <span class="sdo">**labels**</span> property indicating this IP is associated with <span class="values">malicious-activity</span>. Due to the fact this was a known bad IP present on their network, it is advantageous for Stark to be able to apply the appropriate TLP marking definitions to this indicator.

A diagram of this scenario below shows both the Identity and Indicator SDO’s as well as the Marking Definition objects:

![Using Marking Definitions Diagram]({{ site.baseurl }}/img/Using-marking-definitions.PNG)

**Further Reading**
-------------------

To read more about the objects in this example as well as common properties and vocabularies, check out the links below:

-   [Common Properties](https://docs.google.com/document/d/1HRVFn2kAxBOTMbEb3KRu8tjMoHm-KRAI-2R8CTzGil4/edit#heading=h.xzbicbtscatx)
-   [Vocabularies](https://docs.google.com/document/d/1HRVFn2kAxBOTMbEb3KRu8tjMoHm-KRAI-2R8CTzGil4/edit#heading=h.iit7tolczlxv)
-   [Identity](https://docs.google.com/document/d/1nipwFIaFwkHo4Gzw-qxZQpCjP_5tX7rbI3Ic5C56Z88/edit#heading=h.wh296fiwpklp)
-   [Indicator](https://docs.google.com/document/d/1S5XhY6F5OT599b0OuHtUf8IBzFvNY8RysFHIj93DgsY/edit#heading=h.muftrcpnf89v)
-   [Marking Definitions](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.j0uqagkk6m9n)
-   [Statement Object Marking Type](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.3ru8r05saera)
-   [TLP Object Marking Type](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.yd3ar14ekwrs)
-   [STIX Patterning](https://docs.google.com/document/d/1suvd7z7YjNKWOwgko-vJ84jfGuxSYZjOQlw5leCswPY/edit)

**JSON**
------------------

```
{
  "type": "bundle",
  "id": "bundle--b56c1e2e-a40c-44ca-83dd-09e25936d273",
  "spec_version": "2.0",
  "objects": [
    {
      "type": "identity",
      "id": "identity--611d9d41-dba5-4e13-9b29-e22488058ffc",
      "created": "2017-04-14T13:07:49.812Z",
      "modified": "2017-04-14T13:07:49.812Z",
      "name": "Stark Industries",
      "identity_class": "organization",
      "contact_information": "info@stark.com",
      "sectors": [
        "defense"
      ],
    },
    {
      "type": "marking-definition",
      "id": "marking-definition--05ac6c05-8b38-43f2-996d-e6715571090b",
      "created": "2017-04-14T13:07:49.812Z",
      "modified": "2017-04-14T13:07:49.812Z",
      "created_by_ref": "identity--611d9d41-dba5-4e13-9b29-e22488058ffc",
      "definition_type": "tlp",
      "definition": {
        "tlp": "amber"
      }
    },
    {
      "type": "marking-definition",
      "id": "marking-definition--d771aceb-3148-4315-b4b4-130b888533d0",
      "created": "2017-04-14T13:07:49.812Z",
      "modified": "2017-04-14T13:07:49.812Z",
      "created_by_ref": "identity--611d9d41-dba5-4e13-9b29-e22488058ffc",
      "definition_type": "statement",
      "definition": {
        "statement": "Copyright © Stark Industries 2017."
      }
    },
    {
      "type": "indicator",
      "id": "indicator--33fe3b22-0201-47cf-85d0-97c02164528d",
      "created": "2017-04-14T13:07:49.812Z",
      "modified": "2017-04-14T13:07:49.812Z",
      "created_by_ref": "identity--611d9d41-dba5-4e13-9b29-e22488058ffc",
      "name": "Known malicious IP Address",
      "labels": [
        "malicious-activity"
      ],
      "pattern": "[ipv4addr:value = '10.0.0.0']",
      "valid_from": "2017-04-14T13:07:49.812Z",
      "object_marking_refs": [
        "marking-definition--05ac6c05-8b38-43f2-996d-e6715571090b",
        "marking-definition--d771aceb-3148-4315-b4b4-130b888533d0"
      ]
    }
  ]
}
```
