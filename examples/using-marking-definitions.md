---
layout: page
title: Using Marking Definitions
categories: examples
---

Being able to structure the handling of data through the use of data markings is vital for organizations who share cyber threat intelligence (CTI). This benefit allows STIX producers to limit the accessibility of objects and also communicates terms of use and copyright information.

**Scenario**
------------

This scenario focuses on a STIX producer, “Stark Industries”, who imposes object markings on an indicator object. Before sharing this indicator, Stark creates a “Statement” marking definition and selects a “Traffic Light Protocol” (TLP) marking definition to apply to the indicator. These marking definitions incorporate copyright information and restrict the usage of the indicator based on its TLP marking type.

**Data model**
--------------

First, we start with the producer of the STIX content in this scenario, Stark Industries. The information relevant to this company can be represented using an [Identity](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_wh296fiwpklp) STIX Domain Object (SDO). Like with all STIX objects, an <span class="sdo">**id**</span> attribute uniquely identifies Stark Industries and can be referenced within all the objects they generate with the <span class="sdo">**created\_by\_ref**</span> property. Although <span class="sdo">**created\_by\_ref**</span> is optional, this is helpful for attributing the created marking definitions directly to Stark. The Identity object is also useful for listing other relevant details about Stark such as <span class="sdo">**contact\_information**</span> and what type of identity they are with the <span class="sdo">**identity\_class**</span> field.

Next, Stark used a couple of STIX [Marking Definition](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_k5fndj2c7c1k) objects to restrict the handling of the Indicator object and to incorporate copyright information. In the first instance, Stark chose a [TLP Marking Object Type](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_yd3ar14ekwrs) to communicate appropriate restrictions for the indicator. For this Marking Definition object, the <span class="sdo">**definition\_type**</span> must be <span class="values">tlp</span> and the <span class="sdo">**definition**</span> field must contain one of the four types of TLP. In this example, the TLP restriction type is <span class="values">amber</span>. This provides limited disclosure to only appropriate recipients who have a need to know. To read about this restriction and the other types of TLP, check out [US-CERT’s TLP Definitions and Usage](https://www.us-cert.gov/tlp).

A second marking type created by Stark Industries called [Statement](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_3ru8r05saera), is used to represent their copyright information and is applied to all objects they produce. This is similar in format to the TLP Marking Definition object, except the <span class="sdo">**definition\_type**</span> in this case must be <span class="values">statement</span> and there is a <span class="sdo">**created\_by\_ref**</span> field since TLP is already pre-defined in the STIX 2.1 specification. The <span class="sdo">**definition**</span> field contains any type of copyright information you want to convey. For this organization, it simply states <span class="values">Copyright @ Stark Industries 2017</span>. This property could also communicate any terms of use, or you could incorporate both since Statement allows for multiple marking types.

A point of emphasis worth noting is that Marking Definition objects cannot be versioned like other STIX objects. For instance, if Stark Industries wanted to update their Statement information or add terms of use to the marking definition, they would have to generate a new Marking Definition object with the Indicator SDO updated to point to this new definition. They could not add or change their current Statement marking and simply update the <span class="sdo">**modified**</span> property like with other objects, because there is no required <span class="sdo">**modified**</span> property with Marking Definition objects. To understand more about versioning objects, check out this helpful tutorial video on [How to Use Versioning in STIX 2](https://www.youtube.com/watch?v=s4c4PHUfttE).

Finally, Stark can apply these marking definitions to the [Indicator](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_muftrcpnf89v) SDO that contains the malicious IP address they discovered on their network. These object markings are embedded within the Indicator object in the <span class="sdo">**object\_marking\_refs**</span> property and reference the Marking Definition object <span class="sdo">**id**</span>’s for both Statement and TLP. Once referenced, these markings apply to the Indicator object. It’s worth mentioning that this property and the <span class="sdo">**created\_by\_ref**</span> property presented earlier represent one of just a few embedded relationships in STIX 2.1. In most cases, to establish a relationship between objects in STIX, such as between an Indicator and Threat Actor SDO, you would create a [Relationship](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_e2e1szrqfoan) STIX Relationship Object (SRO).

Other than object marking references, the rest of the Indicator object contains properties that detail information about the IP address. The <span class="sdo">**pattern**</span> property, for instance, is based on the [STIX patterning language](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_e8slinrhxcc9) and represents an IPv4 address as a comparison expression: <span class="values">\[ipv4-addr:value = '10.0.0.0'\]</span>. Stark also knows this is a nefarious IP and relays this information with the <span class="sdo">**indicator_types**</span> property indicating this IP is associated with <span class="values">malicious-activity</span>. Due to the fact this was a known bad IP present on their network, it is advantageous for Stark to be able to apply the appropriate TLP marking definitions to this indicator.

A diagram of this scenario below shows both the Identity and Indicator SDO’s as well as the Marking Definition objects [(An interactive version can be found here)](https://oasis-open.github.io/cti-stix-visualization/?url=https://raw.githubusercontent.com/oasis-open/cti-documentation/master/examples/example_json/using-marking-definitions.json){: target="_blank"}:

![Using Marking Definitions Diagram]({{ site.baseurl }}/img/Using-marking-definitions.PNG)

**Further Reading**
-------------------

To read more about the objects in this example as well as common properties and vocabularies, check out the links below:

-   [Common Properties](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_xzbicbtscatx)
-   [Vocabularies](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_izngjy1g98l2)
-   [Identity](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_wh296fiwpklp)
-   [Indicator](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_muftrcpnf89v)
-   [Relationship](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_e2e1szrqfoan)
-   [Marking Definitions](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_k5fndj2c7c1k)
-   [Statement Object Marking Type](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_3ru8r05saera)
-   [TLP Object Marking Type](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_yd3ar14ekwrs)
-   [STIX Patterning](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_e8slinrhxcc9)

**Implementation**
------------------

{% include start_tabs.html tabs="JSON|Python Producer|Python Consumer" name="using-marking-defs" %}{% highlight json linenos %}
{% include_relative example_json/using-marking-definitions.json %}
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
{% include_relative producer_python/using-marking-definitions-producer.py %}
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
{% include_relative consumer_python/using-marking-definitions-consumer.py %}
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
{% endhighlight %}{% include end_tabs.html %}
