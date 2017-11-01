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


## STIX 2 Objects
STIX Objects categorize each piece of information with specific attributes to be populated. Chaining multiple objects together through relationships allow for easy or complex representations of CTI. Below is a list of what can be represented through STIX. More detail and visual representations can be found [here.]({{ site.baseurl }}/examples/visualized-sdo-relationships)

#### STIX 2 defines twelve STIX Domain Objects (SDOs):

{: .table .table-hover .table-example .table-desc}
| Object | Name | Description |
| :---: | :---: | --- |
| ![Attack Pattern Icon]({{ site.baseurl }}/img/icons/attack_pattern.png "Attack Pattern Icon") | [**Attack Pattern**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.axjijf603msy){: target="_blank"} | A type of Tactics, Techniques, and Procedures (TTP) that describes ways threat actors attempt to compromise targets. |
| ![Campaign Icon]({{ site.baseurl }}/img/icons/campaign.png "Campaign Icon") | [**Campaign**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.pcpvfz4ik6d6){: target="_blank"} | A grouping of adversarial behaviors that describes a set of malicious activities or attacks that occur over a period of time against a specific set of targets. |
| ![Course of Action Icon]({{ site.baseurl }}/img/icons/course_of_action.png "Course of Action Icon") | [**Course of Action**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.a925mpw39txn){: target="_blank"} | An action taken to either prevent an attack or respond to an attack. |
| ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png "Identity Icon") | [**Identity**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.wh296fiwpklp){: target="_blank"} | Individuals, organizations, or groups, as well as classes of individuals, organizations, or groups. 
| ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png "Indicator Icon") | [**Indicator**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.muftrcpnf89v){: target="_blank"} | Contains a pattern that can be used to detect suspicious or malicious cyber activity. |
| ![Intrusion Set Icon]({{ site.baseurl }}/img/icons/intrusion_set.png "Intrusion Set Icon") | [**Intrusion Set**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.5ol9xlbbnrdn){: target="_blank"} | A grouped set of adversarial behaviors and resources with common properties believed to be orchestrated by a single threat actor. |
| ![Malware Icon]({{ site.baseurl }}/img/icons/malware.png "Malware Icon") | [**Malware**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.s5l7katgbp09){: target="_blank"} | A type of TTP, also known as malicious code and malicious software, used to compromise the confidentiality, integrity, or availability of a victim’s data or system. |
| ![Observed Data Icon]({{ site.baseurl }}/img/icons/observed_data.png "Observed Data Icon") | [**Observed Data**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.p49j1fwoxldc){: target="_blank"} | Conveys information observed on a system or network (e.g., an IP address). |
| ![Report Icon]({{ site.baseurl }}/img/icons/report.png "Report Icon") | [**Report**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.n8bjzg1ysgdq){: target="_blank"} | Collections of threat intelligence focused on one or more topics, such as a description of a threat actor, malware, or attack technique, including contextual details. |
| ![Threat Actor Icon]({{ site.baseurl }}/img/icons/threat_actor.png "Threat Actor Icon") | [**Threat Actor**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.k017w16zutw){: target="_blank"} |Individuals, groups, or organizations believed to be operating with malicious intent. |
| ![Tool Icon]({{ site.baseurl }}/img/icons/tool.png "Tool Icon") | [**Tool**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.z4voa9ndw8v){: target="_blank"} | Legitimate software that can be used by threat actors to perform attacks. |
| ![Vulnerability Icon]({{ site.baseurl }}/img/icons/vulnerability.png "Vulnerability Icon") | [**Vulnerability**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.q5ytzmajn6re){: target="_blank"} | A mistake in software that can be directly used by a hacker to gain access to a system or network. |

#### STIX 2 defines two STIX Relationship Objects (SROs):

{:.table .table-hover .table-example .table-desc}
| Object | Name | Description |
| :---: | :---:| --- |
| ![Relationship Icon]({{ site.baseurl }}/img/icons/relationship.png "Relationship Icon") | [**Relationship**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.e2e1szrqfoan){: target="_blank"} | Used to link two SDOs and to describe how they are related to each other. |
| ![Sighting Icon]({{ site.baseurl }}/img/icons/sighting.png "Sighting Icon") | [**Sighting**](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/edit#heading=h.a795guqsap3r){: target="_blank"} | Denotes the belief that an element of CTI was seen (e.g., indicator, malware). |


## A look at the structure

STIX 2 objects are represented in JSON. The following is a JSON-based example of a [STIX 2.0 Campaign object](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.pcpvfz4ik6d6){: target="_blank"}:

```
{  
    "type": "campaign",  
    "id": "campaign--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",  
    "created": "2016-04-06T20:03:00.000Z",  
    "name": "Green Group Attacks Against Finance",  
    "description": "Campaign by Green Group against targets in the financial services sector."  
}
```

<div class="pull-right text-center about-fig" markdown="span">
![STIX 2 Relationship Example]({{ site.baseurl }}/img/stix2_relationship_example_2.png)
**STIX 2 Relationship Example**
</div>

Complete information for STIX 2 is available on the [OASIS Cyber Threat Intelligence (CTI) Technical Committee (TC)](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cti){: target="_blank"} website. [Specification documents, schemas and tools]({{ site.baseurl }}/resources) are also available.


Objects Overview
----------------

The video below provides an overview of STIX 2 objects. It highlights the four types of objects in STIX 2: STIX Domain Objects (SDOs), STIX Relationship Objects (SROs), Marking Definition objects, and Bundle objects.

<div class="video-wrapper">
    <div class="video-container">
        <iframe src="https://www.youtube.com/embed/iAnd3rApMcA?ecver=2" width="640" height="360" frameborder="0"></iframe>
    </div>
    <!-- /video --><br><br>
</div>
<!-- /video-wrapper -->