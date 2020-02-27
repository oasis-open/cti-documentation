---
layout: page
title: Introduction to STIX
categories: stix
---

## What is STIX?
Structured Threat Information Expression (STIX™) is a language and serialization format used to exchange cyber threat intelligence (CTI). STIX is open source and free allowing those interested to [contribute]({{ site.baseurl }}/contribute) and [ask questions]({{ site.baseurl }}/faq) freely.


## Why should you care?
Contributing and ingesting CTI becomes a lot easier. With STIX, all aspects of suspicion, compromise and attribution can be represented clearly with objects and descriptive relationships. STIX information can be visually represented for an analyst or stored as JSON to be quickly machine readible. STIX's openness allows for integration into existing tools and products or utilized for your specific analyst or network needs.

<div class="row">
  <div class="info-box pull-left med-info-box col-md-12 well">
    Already know some STIX?
    <div>
      <a style="padding: 6px 50px 6px 50px; margin-left: 3%;" class="btn btn-primary btn-spec" data-toggle="tooltip" title="Examples" href="{{site.baseurl}}/stix/examples">
        <span class="glyphicon glyphicon-education"></span> View Examples
      </a>

      <a style="margin-right: 10%; margin-left: 10%;" class="btn btn-primary btn-spec" data-toggle="tooltip" title="Introductory Walkthrough"   href="{{site.baseurl}}/stix/walkthrough">
        <span class="glyphicon glyphicon-road"></span> View Introductory Walkthrough
      </a>

      <a class="btn btn-primary btn-spec" data-toggle="tooltip" title="STIX Version Comparison" href="{{site.baseurl}}/stix/compare"><span class="glyphicon glyphicon-duplicate"></span> STIX 1.x &amp; STIX 2 Comparison
      </a>

    </div>
  </div>
</div>


## STIX 2.1 Objects
STIX Objects categorize each piece of information with specific attributes to be populated. Chaining multiple objects together through relationships allow for easy or complex representations of CTI. Below is a list of what can be represented through STIX. More detail and visual representations can be found [here.]({{ site.baseurl }}/examples/visualized-sdo-relationships)

#### STIX 2.1 defines twelve STIX Domain Objects (SDOs):

{: .table .table-hover .table-example .table-desc}
| Object | Name | Description |
| :---: | :---: | --- |
| ![Attack Pattern Icon]({{ site.baseurl }}/img/icons/attack_pattern.png "Attack Pattern Icon") | [**Attack Pattern**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070618){: target="_blank"} | A type of TTP that describe ways that adversaries attempt to compromise targets. |
| ![Campaign Icon]({{ site.baseurl }}/img/icons/campaign.png "Campaign Icon") | [**Campaign**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070621){: target="_blank"} |  A grouping of adversarial behaviors that describes a set of malicious activities or attacks (sometimes called waves) that occur over a period of time against a specific set of targets.  |
| ![Course of Action Icon]({{ site.baseurl }}/img/icons/course_of_action.png "Course of Action Icon") | [**Course of Action**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070624){: target="_blank"} | A recommendation from a producer of intelligence to a consumer on the actions that they might take in response to that intelligence. |
| ![Grouping Icon]({{ site.baseurl }}/img/icons/grouping.png "Grouping Icon" =50x50) | [**Grouping**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070627){: target="_blank"} | Explicitly asserts that the referenced STIX Objects have a shared context, unlike a STIX Bundle (which explicitly conveys no context). |
| ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png "Identity Icon") | [**Identity**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070630){: target="_blank"} | Actual individuals, organizations, or groups (e.g., ACME, Inc.) as well as classes of individuals, organizations, systems or groups (e.g., the finance sector).
| ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png "Indicator Icon") | [**Indicator**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070633){: target="_blank"} | Contains a pattern that can be used to detect suspicious or malicious cyber activity. |
| ![Infrastructure]({{ site.baseurl }}/img/icons/infrastructure.png "Infrastructure Icon") | [**Infrastructure**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070636){: target="_blank"} | Represents a type of TTP and describes any systems, software services and any associated physical or virtual resources intended to support some purpose (e.g., C2 servers used as part of an attack, device or server that are part of defence, database servers targeted by an attack, etc.). |
| ![Intrusion Set Icon]({{ site.baseurl }}/img/icons/intrusion_set.png "Intrusion Set Icon") | [**Intrusion Set**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070639){: target="_blank"} | A grouped set of adversarial behaviors and resources with common properties that is believed to be orchestrated by a single organization. |
| ![Location Icon]({{ site.baseurl }}/img/icons/location.png "Location Icon") | [**Location**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070642){: target="_blank"} | Represents a geographic location. |
| ![Malware Icon]({{ site.baseurl }}/img/icons/malware.png "Malware Icon") | [**Malware**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070645){: target="_blank"} | A type of TTP that represents malicious code. |
| ![Malware Analysis Icon]({{ site.baseurl }}/img/icons/malware-analysis.png "Malware Analysis Icon") | [**Malware Analysis**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070648){: target="_blank"} | The metadata and results of a particular static or dynamic analysis performed on a malware instance or family. |
| ![Note Icon]({{ site.baseurl }}/img/icons/note.png "Note Icon") | [**Note**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070651){: target="_blank"} | Conveys informative text to provide further context and/or to provide additional analysis not contained in the STIX Objects, Marking Definition objects, or Language Content objects which the Note relates to. |
| ![Observed Data Icon]({{ site.baseurl }}/img/icons/observed_data.png "Observed Data Icon") | [**Observed Data**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070654){: target="_blank"} | Conveys information about cyber security related entities such as files, systems, and networks using the STIX Cyber-observable Objects (SCOs). |
| ![Opinion Icon]({{ site.baseurl }}/img/icons/opinion.png "Opinion Icon") | [**Opinion**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070657){: target="_blank"} | An assessment of the correctness of the information in a STIX Object produced by a different entity. |
| ![Report Icon]({{ site.baseurl }}/img/icons/report.png "Report Icon") | [**Report**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070660){: target="_blank"} | Collections of threat intelligence focused on one or more topics, such as a description of a threat actor, malware, or attack technique, including context and related details. |
| ![Threat Actor Icon]({{ site.baseurl }}/img/icons/threat_actor.png "Threat Actor Icon") | [**Threat Actor**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070663){: target="_blank"} | Actual individuals, groups, or organizations believed to be operating with malicious intent. |
| ![Tool Icon]({{ site.baseurl }}/img/icons/tool.png "Tool Icon") | [**Tool**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070666){: target="_blank"} | Legitimate software that can be used by threat actors to perform attacks. |
| ![Vulnerability Icon]({{ site.baseurl }}/img/icons/vulnerability.png "Vulnerability Icon") | [**Vulnerability**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070669){: target="_blank"} | A mistake in software that can be directly used by a hacker to gain access to a system or network. |

#### STIX 2 defines two STIX Relationship Objects (SROs):

{:.table .table-hover .table-example .table-desc}
| Object | Name | Description |
| :---: | :---:| --- |
| ![Relationship Icon]({{ site.baseurl }}/img/icons/relationship.png "Relationship Icon") | [**Relationship**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070673){: target="_blank"} | Used to link together two SDOs or SCOs in order to describe how they are related to each other. |
| ![Sighting Icon]({{ site.baseurl }}/img/icons/sighting.png "Sighting Icon") | [**Sighting**](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070677){: target="_blank"} | Denotes the belief that something in CTI (e.g., an indicator, malware, tool, threat actor, etc.) was seen.  |


## A look at the structure

STIX 2 objects are represented in JSON. The following is a JSON-based example of a [STIX 2.1 Campaign object](https://docs.oasis-open.org/cti/stix/v2.1/csprd01/stix-v2.1-csprd01.html#_Toc16070621){: target="_blank"}:

```json
{
    "type": "campaign",
    "id": "campaign--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
    "spec_version": "2.1",
    "created": "2016-04-06T20:03:00.000Z",
    "modified": "2016-04-06T20:03:23.000Z",
    "name": "Green Group Attacks Against Finance",
    "description": "Campaign by Green Group against targets in the financial services sector."
}
```

<div class="pull-right text-center about-fig" markdown="span">
![STIX 2 Relationship Example]({{ site.baseurl }}/img/stix2_relationship_example_2.png)
**STIX 2 Relationship Example**
</div>

Complete information for STIX 2 is available on the [OASIS Cyber Threat Intelligence (CTI) Technical Committee (TC)](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cti){: target="_blank"} website. [Specification documents, schemas and tools]({{ site.baseurl }}/resources) are also available.
