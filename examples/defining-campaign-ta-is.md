---
layout: page
title: Defining Campaigns vs. Threat Actors vs. Intrusion Sets
categories: examples
---

Cyber attacks are often leveraged by threat actors as part of a coordinated campaign against a specific target. These campaigns typically have a goal or objective in mind. Sometimes, these campaigns are orchestrated by threat actors from a nation state, crime syndicate or other nefarious organization and contain similar properties, behaviors and attributes in order to achieve many objectives over a significant period of time. This entire attack package is known as an intrusion set.

**Scenario**
------------

This scenario represents an advanced persistent threat (APT) intrusion set that is suspected to be funded by the country “Franistan”. Their target is the Branistan People’s Party (BPP), one of the political parties of the country “Branistan”. This intrusion set consists of a couple of sophisticated campaigns and attack patterns against the BPP’s website. One campaign seeks to insert false information into the BPP’s web pages, while another is a DDoS effort against the BPP web servers.

**Data model**
--------------

To start with, information about Franistan and the Branistan People’s Party is modeled using [Identity STIX Domain Objects (SDO’s)](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.wh296fiwpklp). As mentioned in other STIX examples (for instance, see [Identifying a Threat Actor Profile](identifying-a-threat-actor-profile)), this object is used specifically for representing common identifiable information about Franistan and BPP. The Identity objects in this scenario are best used to help establish relationships among other objects using the STIX Relationship Object (SRO). For example, Franistan is attributed to a threat actor and the BPP is a target of an intrusion set and multiple campaigns.

Next, the details of the advanced persistent threat in this example are represented within the [Intrusion Set SDO](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.5ol9xlbbnrdn). This Intrusion Set object, which is labeled with the <span class="sdo">**name**</span> <span class="values">APT BPP</span>, contains any motivations as well as goals the intrusion set is trying to achieve. Some of the objectives for APT BPP, listed in the <span class="sdo">**goals**</span> property, are to <span class="values">Influence the Branistan election</span> and <span class="values">Disrupt the BPP</span>. Therefore, their motivations are similar, with their <span class="sdo">**primary\_motivation**</span> being <span class="values">ideology</span>, and one of their <span class="sdo">**secondary\_motivations**</span> being <span class="values">dominance</span>. Also, since they are suspected to be highly funded and resourced by Franistan, their <span class="sdo">**resource\_level**</span> would be <span class="values">government</span>. The values for motivations and resource level come from the open vocabularies [Attack Motivation](https://docs.google.com/document/d/1dIrh1Lp3KAjEMm8o2VzAmuV0Peu-jt9aAh1IHrjAroM/pub#h.dvmbnm1zpjbt) and [Attack Resource level](https://docs.google.com/document/d/1dIrh1Lp3KAjEMm8o2VzAmuV0Peu-jt9aAh1IHrjAroM/pub#h.nlxwwbc73m4e) respectively.

Like with many intrusion sets, there can be multiple threat actors (see [Threat Actor SDO](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.k017w16zutw)) and campaigns that play a part. In this scenario, there is one threat actor simply called <span class="values">Fake BPP</span> whose goal is to also influence the election in Branistan. The motivations and <span class="sdo">**resource\_level**</span> are also the same as the Intrusion Set SDO, which makes sense since this Threat Actor has been associated with this APT. Fake BPP is suspected to be funded by Franistan, which means the <span class="sdo">**labels**</span> property that characterizes this threat actor would be <span class="values">nation-state</span>. Other pertinent information can be found in the <span class="sdo">**roles**</span> and <span class="sdo">**sophistication**</span> properties. In this case, Fake BPP is the orchestrator of these attacks against Branistan, so the <span class="sdo">**roles**</span> field would label them as a <span class="values">director</span>. Since they are known to be well-funded and advanced state actors associated with APT-level attacks, Fake BPP’s <span class="sdo">**sophistication**</span> level would be considered <span class="values">strategic</span>. The values for <span class="sdo">**roles**</span> and <span class="sdo">**sophistication**</span> can be found in the open vocabularies of the 2.0 specification under [Threat Actor Role](https://docs.google.com/document/d/1dIrh1Lp3KAjEMm8o2VzAmuV0Peu-jt9aAh1IHrjAroM/pub#h.u6befh8d18r) and [Threat Actor Sophistication](https://docs.google.com/document/d/1dIrh1Lp3KAjEMm8o2VzAmuV0Peu-jt9aAh1IHrjAroM/pub#h.8jm676xbnggg) respectively.

A couple of different campaigns have been linked to this threat actor and are a part of this intrusion set. These details are appropriately captured within 2 Campaign SDOs. The first campaign, called <span class="values">Operation Bran Flakes</span>, was orchestrated by Fake BPP in order to hack the Branistan People’s Party’s website www.bpp.bn and inject fake information into it’s web pages. The 2^nd^ reported attack campaign, titled <span class="values">Operation Raisin Bran</span>, occurred later and attempted to flood the BPP web servers to deny legitimate users from accessing the site.

In addition to the attack details modeled in the Campaign objects, [Attack Pattern](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.axjijf603msy) SDO’s help classify these specific attacks using Common Attack Pattern Enumeration and Classification ([CAPEC](https://capec.mitre.org/)). Within these type of objects, you can find references to the CAPEC ID’s under the <span class="sdo">**external\_references**</span> property. For instance, the first campaign which attempted to insert false information would fall under <span class="sdo">**external\_id**</span> <span class="values">CAPEC-148</span>, or “Content Spoofing”. The 2^nd^ Attack Pattern SDO which is associated with the denial of service campaign, references <span class="sdo">**external\_id**</span> <span class="values">CAPEC-488</span>, or “HTTP Flood”.

Now that we have covered all the STIX Domain Objects in this example, we can examine the relationships, or [STIX Relationship Objects](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.e2e1szrqfoan) (SROs), among them. The attack patterns are used by the threat actor, intrusion set, and campaigns in this scenario, so there are multiple SROs created to represent these relationships. In all of these relationships, the <span class="sdo">**source\_ref**</span> would reference either the threat actor, intrusion set, or campaign ID’s, and the <span class="sdo">**target\_ref**</span> would point to either of the attack pattern ID’s mentioned in this example. The <span class="sdo">**relationship\_type**</span> property would simply be labeled <span class="values">uses</span>.

The next common relationship involves the Identity SDO of the Branistan People’s Party. In this case, the campaigns, intrusion set, and threat actor all target this identity, so the <span class="sdo">**target\_ref**</span> field would contain the identity ID of the BPP with the <span class="sdo">**relationship\_type**</span> being <span class="values">targets</span>. In addition to these relationships, the threat actor, Fake BPP, is involved in other relationships between the Identity objects. Since Fake BPP is linked to the nation of Franistan, this Threat Actor SDO is related to the Franistan Identity SDO with a <span class="sdo">**relationship\_type**</span> of <span class="values">attributed-to</span>. Also, in one of the attacks mentioned earlier, Fake BPP attempted to take over the real BPP’s website and post content posing as the real BPP, so another relationship is needed indicating that Fake BPP <span class="values">impersonates</span> the real BPP.

Finally, there are several more relationships that link the campaigns, intrusion set, and threat actor together. Both campaigns are <span class="values">attributed-to</span> the Intrusion Set and Threat Actor SDOs (in separate relationships). Also, due to Intrusion Set representing the entire attack package orchestrated by this Threat Actor, the Intrusion Set SDO is <span class="values">attributed-to</span> the Threat Actor object as well.

The following diagrams help visualize the relationships between the SDOs in this scenario.
[An interactive version can be found here.](https://oasis-open.github.io/cti-stix-visualization/?url=https://raw.githubusercontent.com/oasis-open/cti-documentation/master/examples/example_json/defining-campaigns-threat-actors-intrusion-sets.json){: target="_blank"} The first diagram below serves to represent the connections among the Intrusion Set, Threat Actor, and Campaign objects:

![Identifying a TA Profile Diagram]({{ site.baseurl }}/img/campaign-ta-is-1.PNG)

The 2nd diagram below models the relationships among the Identity objects and Intrusion Set, Threat Actor, and Campaign SDOs:

![Identifying a TA Profile Diagram]({{ site.baseurl }}/img/campaign-ta-is-identity-2.PNG)

Finally, the 3rd diagram captures relationships between the Attack Pattern SDOs and the Intrusion Set, Threat Actor, and Campaign objects:

![Identifying a TA Profile Diagram]({{ site.baseurl }}/img/campaign-ta-is-ap-3.PNG)

**Further Reading**
-------------------

To read more about the objects in this example as well as common properties and vocabularies, check out the links below:

-   [Common Properties](https://docs.google.com/document/d/1dIrh1Lp3KAjEMm8o2VzAmuV0Peu-jt9aAh1IHrjAroM/pub#h.xzbicbtscatx)
-   [Vocabularies](https://docs.google.com/document/d/1dIrh1Lp3KAjEMm8o2VzAmuV0Peu-jt9aAh1IHrjAroM/pub#h.iit7tolczlxv)
-   [Intrusion Set](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.5ol9xlbbnrdn)
-   [Campaign](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.pcpvfz4ik6d6)
-   [Threat Actor](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.k017w16zutw)
-   [Identity](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.wh296fiwpklp)
-   [Attack Pattern](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.axjijf603msy)
-   [Relationship](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.e2e1szrqfoan)

**Implementation**
------------------

{% include start_tabs.html tabs="JSON|Python Producer|Python Consumer" name="campaign-is-ta" %}{% highlight json linenos %}
{% include_relative example_json/defining-campaigns-threat-actors-intrusion-sets.json %}
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
{% include_relative producer_python/defining-campaigns-threat-actors-intrusion-sets-producer.py %}
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
{% include_relative consumer_python/defining-campaigns-threat-actors-intrusion-sets-consumer.py %}
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
{% endhighlight %}{% include end_tabs.html %}
