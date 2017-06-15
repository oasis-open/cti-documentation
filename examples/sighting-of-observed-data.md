---
layout: page
title: Sighting of Observed-data
categories: examples
---

While indicators of compromise represent intelligence assertions behind attacks, raw observed information help formulate the basis behind this intelligence. In many cases, it may be beneficial for organizations to share this observed data among each other. Similar to indicators, sightings can contain references to observed data objects that were spotted on other organizations’ networks and could signal information about a type of malware present. This may potentially allow for further intelligence assertions to be made based on this sighted raw information.

**Scenario**
------------

This scenario consists of two cyber threat companies, Pym and Oscorp, who share threat intelligence with one another. Pym Technologies originally shared a [Malware](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.s5l7katgbp09) STIX Domain Object (SDO) with Oscorp. Oscorp later believes they have spotted this Malware object on their own network based upon some captured observed data which contains hashes that match the malware as well as registry keys that the malware created. To represent this, Oscorp issues a [Sighting](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.a795guqsap3r) STIX Relationship Object (SRO) that holds references to these observed data and relays that this could be a sighting-of this particular malware.

**Data model**
--------------

In this example, there are two [Identity](https://docs.google.com/document/d/1S5XhY6F5OT599b0OuHtUf8IBzFvNY8RysFHIj93DgsY/edit#heading=h.wh296fiwpklp) STIX Domain Objects (SDOs) used for the two companies: Pym and Oscorp. The Identity objects document relevant information about the two organizations, such as what sector they are in and relevant contact information. Both organizations are producers and consumers of STIX intelligence, so their <span class="sdo">**id**</span>’s can be referenced within objects using the <span class="sdo">**created\_by\_ref**</span> property to indicate they are the originators of the STIX objects they generate. It is worth noting that Identity SDO’s can also be used to represent individuals, attack targets, government agencies, and groups, to name a few.

The Identity objects at the very minimum need a couple of required properties: <span class="sdo">**name**</span> and <span class="sdo">**identity\_class**</span>. The <span class="sdo">**identity\_class**</span> field is important for categorizing the type of identity Pym and Oscorp represent, which is <span class="values">organization</span> in this case. This value comes from the [identity class open vocabulary](https://docs.google.com/document/d/1HRVFn2kAxBOTMbEb3KRu8tjMoHm-KRAI-2R8CTzGil4/edit#heading=h.be1dktvcmyu), which contains suggested values for labeling Identities.

Pym Technologies first created a Malware SDO to represent details about the type of malware in this scenario. This specific malware type is labeled as a <span class="values">remote-access-trojan</span>, and is an executable disguised as a pdf file that creates multiple registry keys. Pym then shared this intelligence with Oscorp.

Oscorp Industries, which now has this Malware object, believes it has seen this malware on its own networks and created a Sighting object to represent this. The Sighting SRO is a special type of STIX relationship that contains properties about the object seen such as the <span class="sdo">**id**</span> of the Malware SDO (with <span class="sdo">**sighting\_of\_ref**</span>), a <span class="sdo">**count**</span> property that indicates the number of times this malware was seen, as well as timestamps for when it was first and last seen. In addition, a listing of Observed-data <span class="sdo">**id**</span>’s is included to communicate any necessary information that may support the sighting of this malware.

[Observed Data](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.p49j1fwoxldc) SDO’s contain cyber observable information that was captured on systems and networks such as IP addresses, files, and URL’s. In this scenario, Oscorp observed both [file](https://docs.google.com/document/d/1aH4z7AOi7YKSCYcdlF6cW_FKFLHg3zKg0a-a_UrEros/edit#heading=h.99bl2dibcztv) and [registry key](https://docs.google.com/document/d/1aH4z7AOi7YKSCYcdlF6cW_FKFLHg3zKg0a-a_UrEros/edit#heading=h.u7n4ndghs3qq) information. They can model this information within 2 different Observed-data objects. Although you are able to include multiple cyber observable objects within one Observed-data instance, they must be related to each other. In this case, the file and registry data are not directly related so they are contained in separate Observed-data. You can read more about STIX cyber observable [concepts](https://docs.google.com/document/d/1ti4Ei_ii_Uc4izHNZlYmBP9NgD5-iVWC--y-3HmGZyg/edit) and [objects](https://docs.google.com/document/d/167aIyr5BIAJJORzjT11U25cGSBJ0cBNSdkheNJFz6l8/edit) covered in parts 3 and 4 of the STIX 2.0 specification respectively.

Besides the [common properties](https://docs.google.com/document/d/1dIrh1Lp3KAjEMm8o2VzAmuV0Peu-jt9aAh1IHrjAroM/edit#heading=h.xzbicbtscatx) universal to all objects, Observed-data’s properties are all required. So for each of these objects, Oscorp had to provide when each instance was <span class="sdo">**first\_observed**</span> and <span class="sdo">**last\_observed**</span>, as well as a count of the number of times the data was observed with the field <span class="sdo">**number\_observed**</span>. In addition, they needed to provide the actual cyber observable objects in the <span class="sdo">**objects**</span> property. The first Observed-data in this example (Observed Data 1 in the diagram below) contains information about the file that was seen. So, data like a listing of <span class="sdo">**hashes**</span>, the file’s <span class="sdo">**name**</span>, and its <span class="sdo">**size**</span> were included to represent the file. In the second Observed-data object, Oscorp models Windows Registry values such as the registry <span class="sdo">**key**</span> that the suspected malware created.

Finally, it is worth mentioning that none of the objects in this scenario use the standard [Relationship](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.e2e1szrqfoan) SRO which is typically used to relate objects with one another. The Sighting SRO is used instead for the sighting of the Malware object and all other relationships in the diagram below are embedded within the objects. For instance, the Sighting object contains several embedded relationships including what was observed, who the object was created by and where the sighting was seen.

A diagram of this scenario is depicted below:

![Sighting of Observed-data]({{ site.baseurl }}/img/Sighting-of-observed-data.PNG)

**Further Reading**
-------------------

To read more about the objects in this example as well as common properties and vocabularies, check out the links below:

-   [STIX Common Properties](https://docs.google.com/document/d/1HRVFn2kAxBOTMbEb3KRu8tjMoHm-KRAI-2R8CTzGil4/edit#heading=h.xzbicbtscatx)
-   [Vocabularies](https://docs.google.com/document/d/1HRVFn2kAxBOTMbEb3KRu8tjMoHm-KRAI-2R8CTzGil4/edit#heading=h.iit7tolczlxv)
-   [Identity](https://docs.google.com/document/d/1nipwFIaFwkHo4Gzw-qxZQpCjP_5tX7rbI3Ic5C56Z88/edit#heading=h.wh296fiwpklp)
-   [Sighting](https://docs.google.com/document/d/1S5XhY6F5OT599b0OuHtUf8IBzFvNY8RysFHIj93DgsY/edit#heading=h.a795guqsap3r)
-   [Observed Data](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.p49j1fwoxldc)
-   [Malware](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.s5l7katgbp09)
-   [Cyber Observable Concepts](https://docs.google.com/document/d/1ti4Ei_ii_Uc4izHNZlYmBP9NgD5-iVWC--y-3HmGZyg/edit)
-   [Cyber Observable Objects](https://docs.google.com/document/d/167aIyr5BIAJJORzjT11U25cGSBJ0cBNSdkheNJFz6l8/edit)
-   [Relationship](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.e2e1szrqfoan)

**JSON**
------------------

```
{
  "type": "bundle",
  "id": "bundle--a836f05a-f235-4b4b-b523-bd87e40478a1",
  "spec_version": "2.0",
  "objects": [
    {
      "type": "identity",
      "id": "identity--987eeee1-413a-44ac-96cc-0a8acdcc2f2c",
      "created": "2017-04-14T13:07:49.812Z",
      "modified": "2017-04-14T13:07:49.812Z",
      "name": "Oscorp Industries",
      "identity_class": "organization",
      "contact_information": "norman@oscorp.com",
      "sectors": [
        "technology"
      ]
    },
    {
      "type": "identity",
      "id": "identity--7865b6d2-a4af-45c5-b582-afe5ec376c33",
      "created": "2017-04-14T13:07:49.812Z",
      "modified": "2017-04-14T13:07:49.812Z",
      "name": "Pym Technologies",
      "identity_class": "organization",
      "contact_information": "hank@pymtech.com",
      "sectors": [
        "technology"
      ]
    },
    {
      "type": "malware",
      "id": "malware--ae560258-a5cb-4be8-8f05-013d6712295f",
      "created_by_ref": "identity--7865b6d2-a4af-45c5-b582-afe5ec376c33",
      "created": "2014-02-20T09:16:08.989000Z",
      "modified": "2014-02-20T09:16:08.989000Z",
      "name": "Online Job Site Trojan",
      "description": "Trojan that is disguised as the executable file resume.pdf., it also creates a registry key.",
      "labels": [
        "remote-access-trojan"
      ]
    },
    {
      "type": "sighting",
      "id": "sighting--779c4ae8-e134-4180-baa4-03141095d971",
      "created_by_ref": "identity--987eeee1-413a-44ac-96cc-0a8acdcc2f2c",
      "created": "2017-02-28T19:37:11.213Z",
      "modified": "2017-02-28T19:37:11.213Z",
      "first_seen": "2017-02-28T19:07:24.856Z",
      "last_seen": "2017-02-28T19:07:24.856Z",
      "count": 1,
      "sighting_of_ref": "malware--ae560258-a5cb-4be8-8f05-013d6712295f",
      "where_sighted_refs": [
        "identity--987eeee1-413a-44ac-96cc-0a8acdcc2f2c"
      ],
      "observed_data_refs": [
        "observed-data--cf8eaa41-6f4c-482e-89b9-9cd2d6a83cb1",
        "observed-data--a0d34360-66ad-4977-b255-d9e1080421c4"
      ]
    },
    {
      "type": "observed-data",
      "id": "observed-data--cf8eaa41-6f4c-482e-89b9-9cd2d6a83cb1",
      "created_by_ref": "identity--987eeee1-413a-44ac-96cc-0a8acdcc2f2c",
      "created": "2017-02-28T19:37:11.213Z",
      "modified": "2017-02-28T19:37:11.213Z",
      "first_observed": "2017-02-27T21:37:11.213Z",
      "last_observed": "2017-02-27T21:37:11.213Z",
      "number_observed": 1,
      "objects": {
        "0": {
          "type": "file",
          "hashes": {
            "MD5": "1717b7fff97d37a1e1a0029d83492de1",
            "SHA-1": "c79a326f8411e9488bdc3779753e1e3489aaedea"
          },
          "name": "resume.pdf",
          "size": 83968
        }
      }
    },
    {
      "type": "observed-data",
      "id": "observed-data--a0d34360-66ad-4977-b255-d9e1080421c4",
      "created_by_ref": "identity--987eeee1-413a-44ac-96cc-0a8acdcc2f2c",
      "created": "2017-02-28T19:37:11.213Z",
      "modified": "2017-02-28T19:37:11.213Z",
      "first_observed": "2017-02-27T21:37:11.213Z",
      "last_observed": "2017-02-27T21:37:11.213Z",
      "number_observed": 1,
      "objects": {
        "0": {
          "type": "windows-registry-key",
          "key": "HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Services\\WSALG2"
        }
      }
    }
  ]
}
```
