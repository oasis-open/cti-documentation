---
layout: page
title: Examples
categories: stix
hide_title: true
---

STIX 2.0 Examples
=================

The examples below demonstrate how to use STIX 2.0 concepts for common use cases. They are useful for linking multiple concepts together and provide more detail regarding STIX objects and properties.

Done with examples? [Check out the spec!]({{ site.baseurl }}/resources#stix-20-specification)

<script src="{{ site.baseurl }}/js/example_filter.js"></script>

{% assign SDO_list = "Attack Pattern,Campaign,Course of Action,Identity,Indicator,Intrusion Set,Malware,Observed Data,Report,Threat Actor,Tool,Vulnerability" %}
{% assign SRO_list = "Sighting,Relationship" %}
<div class="btn-group">
    <button style="width: 150px;" type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
      STIX Type Filter <span class="caret"></span></button>
    <ul id="tag-filterer" class="dropdown-menu" role="menu" aria-labelledby="filterMenu">
        <li role="presentation"><a class="tag-filter" role="menuitem" tabindex="-1" href="#">None</a></li>
        <li role="presentation" class="divider"></li>
        <li role="presentation" class="dropdown-header">STIX Domain Objects</li>
        {% assign SDO = SDO_list | split:"," | sort %}
        {% for tag in SDO %}
        <li role="presentation"><a class="tag-filter" role="menuitem" tabindex="-1" href="#">{{tag}}</a></li>
        {% endfor %}
        <li role="presentation" class="divider"></li>
        <li role="presentation" class="dropdown-header">STIX Relationship Objects</li>
        {% assign SRO = SRO_list | split:"," | sort %}
        {% for tag in SRO %}
        <li role="presentation"><a class="tag-filter" role="menuitem" tabindex="-1" href="#">{{tag}}</a></li>
        {% endfor %}
    </ul>
</div>

{:.table .table-hover .table-example .table-desc .table-anchor .table-img #examples-table}

| Example | STIX Types | Description |
| --- | --- | --- |
| [Identifying a Threat Actor Profile](/cti-documentation/examples/identifying-a-threat-actor-profile) | ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png){: data-tag="Identity" title="Identity"} ![Threat Actor Icon]({{ site.baseurl }}/img/icons/threat_actor.png){: data-tag="Threat Actor" title="Threat Actor"} | Threat Actors often have several discernible characteristics such as aliases, goals and motivations which can be captured within a STIX Threat Actor object. In this example, the threat actor can also be attributed to an Identity object which models more basic identifiable information. |
| [Defining Campaigns vs. Intrusion Sets vs. Threat Actors](/cti-documentation/examples/defining-campaign-ta-is)  | ![Attack Pattern Icon]({{ site.baseurl }}/img/icons/attack_pattern.png){: data-tag="Attack Pattern" title="Attack Pattern"} ![Campaign Icon]({{ site.baseurl }}/img/icons/campaign.png){: data-tag="Campaign" title="Campaign"} ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png){: data-tag="Identity" title="Identity"} ![Intrusion Set Icon]({{ site.baseurl }}/img/icons/intrusion_set.png){: data-tag="Intrusion Set" title="Intrusion Set"} ![Threat Actor Icon]({{ site.baseurl }}/img/icons/threat_actor.png){: data-tag="Threat Actor" title="Threat Actor"} | Intrusion Sets in STIX are represented as an attack package consisting of potentially several campaigns, threat actors and attack patterns. This example helps explain the differences between the Campaign, Intrusion Set, and Threat Actor objects and demonstrates a scenario where all three are used together.|
| [Identifying a Threat Actor Profile](/cti-documentation/examples/identifying-a-threat-actor-profile)      | ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png){: data-tag="Identity" title="Identity"} ![Threat Actor Icon]({{ site.baseurl }}/img/icons/threat_actor.png){: data-tag="Threat Actor" title="Threat Actor"} | Threat Actors often have several discernible characteristics such as aliases, goals and motivations which can be captured within a STIX Threat Actor object. In this example, the threat actor can also be attributed to an Identity object which models more basic identifiable information. |
| [Indicator for Malicious URL](/cti-documentation/examples/indicator-for-malicious-url)             | ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png){: data-tag="Indicator" title="Indicator"} ![Malware Icon]({{ site.baseurl }}/img/icons/malware.png){: data-tag="Malware" title="Malware"} | This example models a STIX Indicator object that represents a malicious URL using STIX patterning language. The Indicator indicates that it's a delivery mechanism for a piece of malware. |
| [Malware Indicator for File Hash](/cti-documentation/examples/malware-indicator-for-file-hash)         | ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png){: data-tag="Indicator" title="Indicator"} ![Malware Icon]({{ site.baseurl }}/img/icons/malware.png){: data-tag="Malware" title="Malware"} | File hashes for malware variants can be captured within an Indicator STIX Domain Object and then associated with a Malware object which provides more detail about the malware.  |
| [Sighting of an Indicator](/cti-documentation/examples/sighting-of-an-indicator) | ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png){: data-tag="Identity" title="Identity"} ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png){: data-tag="Indicator" title="Indicator"} ![Sighting Icon]({{ site.baseurl }}/img/icons/sighting.png){: data-tag="Sighting" title="Sighting"} | Indicators on one organization's network are often spotted on other organizations' networks. When this is the case, a Sighting STIX Relationship Object(SRO) can be issued to relay that this specific indicator was seen. This example discusses how a company can use a Sighting for a STIX Indicator object.
| [Sighting of Observed-data](/cti-documentation/examples/sighting-of-observed-data) | ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png){: data-tag="Identity" title="Identity"} ![Observed-data Icon]({{ site.baseurl }}/img/icons/observed_data.png){: data-tag="Observed Data" title="Observed Data"} ![Sighting Icon]({{ site.baseurl }}/img/icons/sighting.png){: data-tag="Sighting" title="Sighting"} ![Malware Icon]({{ site.baseurl }}/img/icons/malware.png){: data-tag="Malware" title="Malware"} | Observed data represent machine-generated raw information and are different from Indicators which dictate more of an intelligence assertion. These Observed-data SDO's can still be shared and referenced within a Sighting SRO. This example demonstrates the usage of Observed-data and their relation to other STIX objects.
| [Threat Actor Leveraging Attack Patterns and Malware](/cti-documentation/examples/threat-actor-leveraging-attack-patterns-and-malware) | ![Attack Pattern Icon]({{ site.baseurl }}/img/icons/attack_pattern.png){: data-tag="Attack Pattern" title="Attack Pattern"} ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png){: data-tag="Identity" title="Identity"} ![Malware Icon]({{ site.baseurl }}/img/icons/malware.png){: data-tag="Malware" title="Malware"} ![Threat Actor Icon]({{ site.baseurl }}/img/icons/threat_actor.png){: data-tag="Threat Actor" title="Threat Actor"} | Threat actors can often be characterized by the attack patterns they leverage and the malware varieties they use. This example describes how to represent a threat actor who uses a phishing attack pattern to deliver a form of malware. |
| [Using Marking Definitions](/cti-documentation/examples/using-marking-definitions) | ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png){: data-tag="Identity" title="Identity"} ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png){: data-tag="Indicator" title="Indicator"} ![Amber Marking Icon]({{ site.baseurl }}/img/icons/tlp_amber.png){: title="Marking Definition"} ![Statement Marking Icon]({{ site.baseurl }}/img/icons/restricted_marking.png){: title="Marking Definition"} | Sometimes when creating STIX objects it may be useful to provide guidance or permissions on how those objects may be used. In this example, Marking Definition objects are created and applied to an Indicator object to specify restrictions and copyright information. |
| [Using Granular Markings](/cti-documentation/examples/using-granular-markings) | ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png){: data-tag="Identity" title="Identity"} ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png){: data-tag="Indicator" title="Indicator"} ![Green Marking Icon]({{ site.baseurl }}/img/icons/tlp_green.png){: title="Marking Definition"} ![Amber Marking Icon]({{ site.baseurl }}/img/icons/tlp_amber.png){: title="Marking Definition"} ![Red Marking Icon]({{ site.baseurl }}/img/icons/tlp_red.png){: title="Marking Definition"} | Whereas object markings in STIX can limit or restrict how entire objects are used, granular markings delve deeper into the objects and focus on restricting specific individual properties. This example demonstrates how to enforce different TLP markings on multiple properties of an Indicator SDO. 
| [Visualized SDO Relationships](/cti-documentation/examples/visualized-sdo-relationships) | ![Relationship Icon]({{ site.baseurl }}/img/icons/relationship.png){: data-tag="Relationship" title="Relationship"} | This example iterates over all SDOs and visually represents possible relationships of each SDO to another. Visual representations can simplify understanding and are often easier to interpret then text alone. |

STIX 2.0 Threat Reports
==================

The following threat reports have been converted into STIX 2.0.

{:.table .table-hover .table-example .table-desc .table-anchor}

| Threat Report                             | JSON Representation                                       | Description                                 |
| --------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| [Mandiant's APT1 Report](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf){:target="_blank"}  |  [APT1 JSON](https://oasis-open.github.io/cti-documentation/examples/example_json/apt1.zip) | This in-depth threat report by Mandiant focuses on a sophisticated advanced persistent threat simply called "APT1". Mandiant concluded that this extensive APT conducted cyber espionage campaigns potentially with sponsorship by the Chinese government. Within the STIX 2 JSON for this report, there are several Campaign, Threat Actor, Indicator, Attack Pattern and Malware objects, as well as an Intrusion Set SDO used to model APT1. Along with these SDOs, there are multiple relationships linking these objects together. Feel free to download this converted report to see all of the SDOs and SROs used.  |  
| [Fireeye's Poison Ivy Report](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-poison-ivy.pdf){:target="_blank"}  | [Poison Ivy JSON](https://oasis-open.github.io/cti-documentation/examples/example_json/poisonivy.zip) | Fireeye's threat report on Poison Ivy covers how this remote access tool (RAT) was used by different campaigns and threat actors. In this converted report, there are several variants of PIVY malware represented by the Malware SDO, as well as Campaign, Threat Actor, Attack Pattern, and Vulnerability objects. Relationship SROs help link the malware variants to the campaigns and threat actors and demonstrate the vulnerabilities PIVY exploits. The JSON representation is available for download.   |
| [IMDDOS Botnet Report](https://www.coresecurity.com/publication/imddos-botnet-discovery-and-analysis){:target="_blank"} | [IMDDOS Threat Modeling Exercise](https://gist.github.com/rjsmitre/79775df68b0d1c7c0985b4fe7f115586) --- [Visulized](https://oasis-open.github.io/cti-stix-visualization/?url=https://gist.githubusercontent.com/rjsmitre/79775df68b0d1c7c0985b4fe7f115586/raw/d5d2a3e7b4ae52ff7153a8b7b5b57dd066611803/imddos.json){: target="_blank"} | This report by Damballa discusses the Chinese IMDDOS botnet. For this report, several OASIS CTI-TC team members came up with solutions. This conversion to STIX 2.0 models Indicator, Malware, and Threat Actor SDOs, along with the corresponding Relationship objects linking them together.
