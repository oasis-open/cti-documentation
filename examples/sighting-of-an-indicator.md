---
layout: page
title: Sighting of an Indicator
categories: examples
---

A major benefit of cyber threat intelligence sharing and collaboration is the ability to alert other companies and agencies ahead of time that an indicator is present on a system or network. This allows for a more proactive approach in addressing cyber threats. In many cases, an indicator that was spotted on one network is also seen on another network. Being able to share that a particular indicator was seen elsewhere is vital to other organizations consuming this information.

**Scenario**
------------

This scenario consists of two cyber threat companies, Alpha and Beta, who share threat intelligence. A malicious URL was seen on Alpha’s network and an indicator was generated to capture this information. Alpha then shares this information with company Beta who later sees this indicator on their systems. Beta then creates a sighting of this indicator to share that this indicator has been spotted.

**Data model**
--------------

In this example, there are two [Identity](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.wh296fiwpklp) STIX Domain Objects (SDOs) used for the two companies: Alpha and Beta. The Identity objects document relevant information about the two organizations, such as what sector they are in, what they do, and contact information. Both organizations are producers and consumers of STIX intelligence, so their <span class="sdo">**id**</span>’s can be referenced within objects using the <span class="sdo">**created\_by\_ref**</span> property to indicate they are the originators of the STIX objects they generate. It is worth noting that Identity SDO’s can also be used to represent individuals, attack targets, government agencies, and groups, to name a few.

Identity objects at the very minimum need a couple of required properties: <span class="sdo">**name**</span> and <span class="sdo">**identity\_class**</span>. The <span class="sdo">**identity\_class**</span> field is important for categorizing the type of identity Alpha and Beta represent. In both their cases, this field would be populated with the value <span class="values">organization</span>. This term comes from the [identity class open vocabulary](https://docs.google.com/document/d/1dIrh1Lp3KAjEMm8o2VzAmuV0Peu-jt9aAh1IHrjAroM/pub#h.be1dktvcmyu), which contains suggested values for labeling identities.

The other fields within the Identity SDO are optional but help to structure a complete profile of the identity. For instance, it might be useful to know the list of roles an individual or group may perform, which is captured with the <span class="sdo">**labels**</span> property. Since both companies in this scenario deal with cyber threats, it makes sense to have them labeled as <span class="values">cyber security</span>. If you know the list of <span class="sdo">**sectors**</span> the identities may belong to or any relevant <span class="sdo">**contact\_information**</span>, this can be provided as well for these objects. For example, knowing that some STIX object creators are in the financial sector may provide more context as to why they are seeing certain indicators or being targeted by specific threat actors. Both of the companies in this example operate in the <span class="values">technology</span> sector, which comes from the [industry sector open vocabulary](https://docs.google.com/document/d/1dIrh1Lp3KAjEMm8o2VzAmuV0Peu-jt9aAh1IHrjAroM/pub#h.oogrswk3onck).

Next, the Alpha company uses an [Indicator](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.muftrcpnf89v) SDO to capture information about the malicious URL they discovered on their network. Using the [STIX patterning language](https://docs.google.com/document/d/1nK1RXcE2aMvQoG1Kgr3aTBtHZ1IyehzOk7vU0n5FUGY/pub), Alpha represents the URL as a comparison expression in the <span class="sdo">**pattern**</span> property: <span class="values">\[url:value = 'http://paypa1.banking.com'\]</span>. Since Alpha knows this URL is nefarious, they label this Indicator as <span class="values">malicious-activity</span> using the <span class="sdo">**labels**</span> field which comes from the [indicator label open vocabulary](https://docs.google.com/document/d/1dIrh1Lp3KAjEMm8o2VzAmuV0Peu-jt9aAh1IHrjAroM/pub#h.cvhfwe3t9vuo).

The Beta company receives this indicator intelligence from Alpha and implements it on their own network to look for this specific URL. Once they spot it, they generate a [Sighting](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.a795guqsap3r) STIX Relationship Object (SRO), which is a special type of relationship object that differs from the regular Relationship SRO. For instance, Sighting contains unique properties like <span class="sdo">**count**</span>, <span class="sdo">**first\_seen**</span>, and <span class="sdo">**last\_seen**</span> that convey when a SDO was seen within a particular timeframe as well as the number of times this SDO was seen. Alternatively, a standard Relationship SRO is simply used to connect two SDO’s together and does not provide the same type of intelligence assertions.

In this example, Beta’s Sighting object captures information about Alpha’s Indicator which they spotted on their network. Since they are the creator of this object as well as the victim in this instance, Beta’s Identity ID is represented in the <span class="sdo">**created\_by\_ref**</span> and <span class="sdo">**where\_sighted\_refs**</span> properties respectively. It is worth mentioning that the <span class="sdo">**where\_sighted\_refs**</span> field is a list, so it can also list other Identity SDO ID’s where this indicator was seen. Another reference, <span class="sdo">**sighting\_of\_ref**</span>, contains the ID of the SDO that was sighted, which in this case is the Indicator object. This is a required property due to the fact you cannot have a Sighting without an object to sight.

In some cases, an indicator like a URL can be spotted several times on a network over a significant period of time. For this scenario, however, Beta only spotted the URL once which results in the **count** field reflecting an integer value of “1”. Since it was just seen once, the <span class="sdo">**first\_seen**</span>, and <span class="sdo">**last\_seen**</span> properties portray the same timestamp.

A diagram of this scenario below shows the Identity and Indicator SDO’s and the Sighting SRO [(An interactive version can be found here)](https://oasis-open.github.io/cti-stix-visualization/?url=https://raw.githubusercontent.com/oasis-open/cti-documentation/master/examples/example_json/sighting-of-an-indicator.json){: target="_blank"}:

![Sighting of an Indicator]({{ site.baseurl }}/img/sighting-of-an-indicator.PNG)

**Further Reading**
-------------------

To read more about the objects in this example as well as common properties and vocabularies, check out the links below:

-   [Common Properties](https://docs.google.com/document/d/1dIrh1Lp3KAjEMm8o2VzAmuV0Peu-jt9aAh1IHrjAroM/pub#h.xzbicbtscatx)
-   [Vocabularies](https://docs.google.com/document/d/1dIrh1Lp3KAjEMm8o2VzAmuV0Peu-jt9aAh1IHrjAroM/pub#h.iit7tolczlxv)
-   [Identity](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.wh296fiwpklp)
-   [Sighting](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.a795guqsap3r)
-   [Indicator](https://docs.google.com/document/d/1IvkLxg_tCnICsatu2lyxKmWmh1gY2h8HUNssKIE-UIA/pub#h.muftrcpnf89v)
-   [STIX patterning language](https://docs.google.com/document/d/1nK1RXcE2aMvQoG1Kgr3aTBtHZ1IyehzOk7vU0n5FUGY/pub)

**Implementation**
------------------

{% include start_tabs.html tabs="JSON|Python Producer|Python Consumer" name="sighting-indicator" %}{% highlight json linenos %}
{% include_relative example_json/sighting-of-an-indicator.json %}
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
{% include_relative producer_python/sighting-of-an-indicator-producer.py %}
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
{% include_relative consumer_python/sighting-of-an-indicator-consumer.py %}
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
{% endhighlight %}{% include end_tabs.html %}
