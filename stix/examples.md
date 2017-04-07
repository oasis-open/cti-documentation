---
layout: page
title: STIX Examples
categories: stix
---

The examples below demonstrate how to use STIX 2.0 concepts for common use cases. They are useful for linking multiple concepts together and provide more detail regarding STIX objects and properties.


{:.table .table-hover .table-example .table-desc}

| Example                                 | STIX Types                                        | Description                                 |
| --------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| [Identifying a Threat Actor Profile](/cti-documentation/examples/identifying-a-threat-actor-profile)      | ![Threat Actor Icon]({{ site.baseurl }}/img/icons/threat_actor.png)  ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png) | Threat Actors often have several discernible characteristics such as aliases, goals and motivations which can be captured within a STIX Threat Actor object. In this example, the threat actor can also be attributed to an Identity object which models more basic identifiable information. |
| --------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| [Indicator for Malicious URL](/cti-documentation/examples/indicator-for-malicious-url)             | ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png) ![Malware Icon]({{ site.baseurl }}/img/icons/malware.png) | This example models a STIX Indicator object that represents a malicious URL using STIX patterning language. The Indicator indicates that it's a delivery mechanism for a piece of malware. |
| --------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| [Malware Indicator for File Hash](/cti-documentation/examples/malware-indicator-for-file-hash)         | ![Indicator Icon]({{ site.baseurl }}/img/icons/indicator.png) ![Malware Icon]({{ site.baseurl }}/img/icons/malware.png) | File hashes for malware variants can be captured within an Indicator STIX Domain Object and then associated with a Malware object which provides more detail about the malware.  |
| --------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| [Threat Actor Leveraging Attack Patterns and Malware](/cti-documentation/examples/threat-actor-leveraging-attack-patterns-and-malware) | ![Threat Actor Icon]({{ site.baseurl }}/img/icons/threat_actor.png) ![Identity Icon]({{ site.baseurl }}/img/icons/identity.png) ![Attack Pattern Icon]({{ site.baseurl }}/img/icons/attack_pattern.png) ![Malware Icon]({{ site.baseurl }}/img/icons/malware.png) | Threat actors can often be characterized by the attack patterns they leverage and the malware varieties they use. This example describes how to represent a threat actor who uses a phishing attack pattern to deliver a form of malware. |
