---
layout: page
title: Examples and Tutorials
categories: stix
hide_title: true
---

STIX 2.0 Examples
=================

The examples below demonstrate how to use STIX 2.0 concepts for common use cases. They are useful for linking multiple concepts together and provide more detail regarding STIX objects and properties.


{:.table .table-hover .table-example .table-desc}

| Example                                 | STIX Types                                        | Description                                 |
| --------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| [Defining Campaigns vs. Intrusion Sets vs. Threat Actors](/cti-documentation/examples/defining-campaign-ta-is)      | ![Attack Pattern Icon]({{ site.baseurl }}/img/icons/attack_pattern.png) ![Campaign Icon]({{ site.baseurl }}/img/icons/campaign.png) ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png) ![Intrusion Set Icon]({{ site.baseurl }}/img/icons/intrusion_set.png)![Threat Actor Icon]({{ site.baseurl }}/img/icons/threat_actor.png) | Intrusion Sets in STIX are represented as an attack package consisting of potentially several campaigns, threat actors and attack patterns. This example helps explain the differences between the Campaign, Intrusion Set, and Threat Actor objects and demonstrates a scenario where all three are used together.|
| --------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| [Identifying a Threat Actor Profile](/cti-documentation/examples/identifying-a-threat-actor-profile)      | ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png) ![Threat Actor Icon]({{ site.baseurl }}/img/icons/threat_actor.png) | Threat Actors often have several discernible characteristics such as aliases, goals and motivations which can be captured within a STIX Threat Actor object. In this example, the threat actor can also be attributed to an Identity object which models more basic identifiable information. |
| --------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| [Indicator for Malicious URL](/cti-documentation/examples/indicator-for-malicious-url)             | ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png) ![Malware Icon]({{ site.baseurl }}/img/icons/malware.png) | This example models a STIX Indicator object that represents a malicious URL using STIX patterning language. The Indicator indicates that it's a delivery mechanism for a piece of malware. |
| --------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| [Malware Indicator for File Hash](/cti-documentation/examples/malware-indicator-for-file-hash)         | ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png) ![Malware Icon]({{ site.baseurl }}/img/icons/malware.png) | File hashes for malware variants can be captured within an Indicator STIX Domain Object and then associated with a Malware object which provides more detail about the malware.  |
| --------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| [Sighting of an Indicator](/cti-documentation/examples/sighting-of-an-indicator) | ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png) ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png) ![Sighting Icon]({{ site.baseurl }}/img/icons/sighting.png) | Indicators on one organization's network are often spotted on other organizations' networks. When this is the case, a Sighting STIX Relationship Object (SRO) can be issued to relay that this specific indicator was seen. This example discusses how a company can use a Sighting for a STIX Indicator object.
| --------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| [Sighting of Observed-data](/cti-documentation/examples/sighting-of-observed-data) | ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png) ![Observed-data Icon]({{ site.baseurl }}/img/icons/observed_data.png) ![Sighting Icon]({{ site.baseurl }}/img/icons/sighting.png) ![Malware Icon]({{ site.baseurl }}/img/icons/malware.png) | Observed data represent machine-generated raw information and are different from Indicators which dictate more of an intelligence assertion. These Observed-data SDO's can still be shared and referenced within a Sighting SRO. This example demonstrates the usage of Observed-data and their relation to other STIX objects.
| --------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| [Threat Actor Leveraging Attack Patterns and Malware](/cti-documentation/examples/threat-actor-leveraging-attack-patterns-and-malware) | ![Attack Pattern Icon]({{ site.baseurl }}/img/icons/attack_pattern.png) ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png) ![Malware Icon]({{ site.baseurl }}/img/icons/malware.png) ![Threat Actor Icon]({{ site.baseurl }}/img/icons/threat_actor.png) | Threat actors can often be characterized by the attack patterns they leverage and the malware varieties they use. This example describes how to represent a threat actor who uses a phishing attack pattern to deliver a form of malware. |
| --------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| [Using Marking Definitions](/cti-documentation/examples/using-marking-definitions) | ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png) ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png) ![Amber Marking Icon]({{ site.baseurl }}/img/icons/tlp_amber.png) ![Statement Marking Icon]({{ site.baseurl }}/img/icons/restricted_marking.png) | Sometimes when creating STIX objects it may be useful to provide guidance or permissions on how those objects may be used. In this example, Marking Definition objects are created and applied to an Indicator object to specify restrictions and copyright information. |
| --------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| [Using Granular Markings](/cti-documentation/examples/using-granular-markings) | ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png) ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png) ![Green Marking Icon]({{ site.baseurl }}/img/icons/tlp_green.png) ![Amber Marking Icon]({{ site.baseurl }}/img/icons/tlp_amber.png) ![Red Marking Icon]({{ site.baseurl }}/img/icons/tlp_red.png) | Whereas object markings in STIX can limit or restrict how entire objects are used, granular markings delve deeper into the objects and focus on restricting specific individual properties. This example demonstrates how to enforce different TLP markings on multiple properties of an Indicator SDO. |

STIX 2.0 Threat Reports
==================

The following threat reports have been converted into STIX 2.0.

{:.table .table-hover .table-example .table-desc}

| Threat Report                             | JSON Representation                                       | Description                                 |
| --------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| [Mandiant's APT1 Report](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)  |  [APT1 JSON](https://oasis-open.github.io/cti-documentation/stix/examples/example_json/apt1.zip) | This in-depth threat report by Mandiant focuses on a sophisticated advanced persistent threat simply called "APT1". Mandiant concluded that this extensive APT conducted cyber espionage campaigns potentially with sponsorship by the Chinese government. Within the STIX 2 JSON for this report, there are several Campaign, Threat Actor, Indicator, Attack Pattern and Malware objects, as well as an Intrusion Set SDO used to model APT1. Along with these SDOs, there are multiple relationships linking these objects together. Feel free to download this converted report to see all of the SDOs and SROs used.  |  
| [Fireeye's Poison Ivy Report](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-poison-ivy.pdf)  | [Poison Ivy JSON](https://oasis-open.github.io/cti-documentation/stix/examples/example_json/poisonivy.zip) | Fireeye's threat report on Poison Ivy covers how this remote access tool (RAT) was used by different campaigns and threat actors. In this converted report, there are several variants of PIVY malware represented by the Malware SDO, as well as Campaign, Threat Actor, Attack Pattern, and Vulnerability objects. Relationship SROs help link the malware variants to the campaigns and threat actors and demonstrate the vulnerabilities PIVY exploits. The JSON representation is available for download.   |


STIX 2.0 Tutorials
==================

The following tutorials help to clarify common STIX 2.0 concepts.

STIX Versioning
---------------

The first video focuses on STIX 2.0 versioning. It discusses what STIX object versioning is, why objects are versioned, and who can version objects.


<div class="video-wrapper">
	<div class="video-container">
		<iframe src="https://www.youtube.com/embed/s4c4PHUfttE?ecver=2" width="640" height="360" frameborder="0"></iframe>
	</div>
	<!-- /video --><br><br>
</div>
<!-- /video-wrapper -->

Objects Overview
----------------

The next video provides an overview of STIX 2.0 objects. It highlights the four types of objects in STIX 2: STIX Domain Objects (SDOs), STIX Relationship Objects (SROs), Marking Definition objects, and Bundle objects.

<div class="video-wrapper">
	<div class="video-container">
		<iframe src="https://www.youtube.com/embed/iAnd3rApMcA?ecver=2" width="640" height="360" frameborder="0"></iframe>
	</div>
	<!-- /video --><br><br>
</div>
<!-- /video-wrapper -->

Common Properties
----------------

This video discusses the common properties that are universal to all STIX Domain Objects (SDOs) and STIX Relationship Objects (SROs).

<div class="video-wrapper">
	<div class="video-container">
		<iframe src="https://www.youtube.com/embed/dv-Zt4k1zt0?ecver=2" width="640" height="360" frameborder="0"></iframe>
	</div>
	<!-- /video --><br><br>
</div>
<!-- /video-wrapper -->
