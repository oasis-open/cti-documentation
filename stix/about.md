---
layout: default
title: About STIX
categories: stix
---

<div class="row">
<div class="col-md-12" markdown="1">

**About STIX**
==============

Structured Threat Information Expression (STIX™) is a language for describing cyber threat information in a standardized and structured manner to enable the exchange of cyber threat intelligence (CTI). STIX characterizes an extensive set of CTI to include indicators of adversary activity, as well as contextual information characterizing cyber adversary motivations, capabilities, and activities and best courses of action for defense and mitigation.

A set of specifications provide the normative description of STIX 2.0. While STIX 2.0 is defined to be independent of any specific serialization, JSON is the mandatory-to-implement serialization and informative [JSON schemas](https://github.com/oasis-open/cti-stix2-json-schemas) are available. The following is a JSON-based example of a STIX 2.0 Campaign object:

```
{  
    "type": "campaign",  
    "id": "campaign--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",  
    "created": "2016-04-06T20:03:00.000Z",  
    "name": "Green Group Attacks Against Finance",  
    "description": "Campaign by Green Group against targets in the financial services sector."  
}
```

<div class="figure pull-right text-center" markdown="span">
![STIX 2.0 Relationship Example]({{ site.baseurl }}/img/stix2_relationship_example.png){: .figure-img .img-fluid}
**STIX 2.0 Relationship Example**
</div>

In addition to describing a set of STIX Domain Objects (SDOs), STIX 2.0 enables relationships to be defined *between* objects. As the example shows, a Campaign may be attributed to a Threat Actor and may target a Vulnerability while an Indicator indicates the Campaign.

A companion CTI specification, [TAXII](https://docs.google.com/document/d/1yvqWaPPnPW-2NiVCLqzRszcx91ffMowfT5MmE9Nsy_w/edit?pref=2&pli=1)™, is designed specifically to transport STIX Objects. However, the structures and serializations of STIX do not rely on any specific transport mechanism, and STIX provides a “Bundle,” a container for STIX Objects to allow for transportation of bulk STIX data, especially over non-TAXII communication mechanisms.

Complete information for STIX 2.0 is available on the [OASIS Cyber Threat Intelligence (CTI) Technical Committee (TC) website](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cti). [Specification documents](https://docs.google.com/document/d/1yvqWaPPnPW-2NiVCLqzRszcx91ffMowfT5MmE9Nsy_w/edit?pref=2&pli=1) and [schemas and tools](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cti#openrepo) are also available.

**STIX 2.0**
-------------

The twelve SDOs included in STIX 2.0 (listed below) represent a minimally viable product (MVP) that fulfills basic consumer and producer requirements for CTI sharing. Objects and properties not included in STIX 2.0, but deemed necessary by the community, will be included in future releases.

-   **Attack Pattern** – a type of Tactics, Techniques, and Procedures (TTP) that describes ways threat actors attempt to compromise targets.

-   **Campaign** – a grouping of adversarial behaviors that describes a set of malicious activities or attacks that occur over a period of time against a specific set of targets.

-   **Course of Action** – an action taken to either prevent an attack or respond to an attack.

-   **Identity** – individuals, organizations, or groups, as well as classes of individuals, organizations, or groups.

-   **Indicator** – contains a pattern that can be used to detect suspicious or malicious cyber activity.

-   **Intrusion Set** – a grouped set of adversarial behaviors and resources with common properties believed to be orchestrated by a single threat actor.

-   **Malware** – a type of TTP, also known as malicious code and malicious software, used to compromise the confidentiality, integrity, or availability of a victim’s data or system.

-   **Observed Data** – conveys information observed on a system or network (e.g., an IP address).

-   **Report** – collections of threat intelligence focused on one or more topics, such as a description of a threat actor, malware, or attack technique, including contextual details.

-   **Threat Actor** – individuals, groups, or organizations believed to be operating with malicious intent.

-   **Tool** – legitimate software that can be used by threat actors to perform attacks.

-   **Vulnerability** – a mistake in software that can be directly used by a hacker to gain access to a system or network.

STIX 2.0 defines two STIX Relationship Objects (SROs):

-   **Relationship** – used to link two SDOs and to describe how they are related to each other.

-   **Sighting** – denotes the belief that an element of CTI was seen (e.g., indicator, malware).

A STIX 2.0 architecture diagram is shown below. Each block with an *underlined title* corresponds to one of five parts of the [STIX 2.0 specification](https://docs.google.com/document/d/1yvqWaPPnPW-2NiVCLqzRszcx91ffMowfT5MmE9Nsy_w/edit?pref=2&pli=1).

<div class="figure center-block text-center" markdown="span">
![STIX 2.0 Architecture]({{ site.baseurl }}/img/stix2_architecture.png){: .figure-img .img-fluid}
**STIX 2.0 Architecture**
</div>


**STIX 1.x vs STIX 2.0**
------------------------

STIX 1.x was designed to be flexible, enabling STIX producers to describe data in multiple ways; as a result, STIX 1.x consumers had difficulty working with STIX data from different producers. To address this issue, STIX 2.0 was significantly redesigned toward an overall simplification and a focus on core use cases; although STIX 2.0 defines more required fields, all fields have a single purpose.

STIX 1.x is represented in XML, which was thought to be excessively complicated. Consequently, the OASIS CTI TC opted to represent STIX 2.0 using JSON. In fact, STIX 2.0 is a *serialization-independent* specification (i.e., the STIX 2.0 specification is normative, not the JSON-based schema), but all STIX 2.0-compatible tools must support JSON as a serialization format (and may support other serializations as well).

STIX 1.x leveraged the Cyber Observable Expression (CybOX™) language, but to make it easier for STIX users to work with cyber observable data, the necessary elements of CybOX have been embedded in STIX 2.0 as the STIX Cyber Observables module. CybOX will no longer be supported as a separate specification.

Other key changes in STIX 2.0 include splitting TTPs into separate top-level objects (Attack Pattern, Malware, Tool) and defining relationships as top-level objects.

</div>
</div>