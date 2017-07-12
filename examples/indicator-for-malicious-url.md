---
layout: page
title: Indicator for Malicious URL
categories: examples
---


A very common method for delivering malware to potential targets is to host it at a particular URL. Targets are then directed to that URL via a phishing e-mail or a link from another site and, when they reach it, are exploited. Sharing lists of malicious URLs can be an effective and cheap way to limit exposure to malicious code.

**Scenario**
------------

This scenario consists of an indicator for the URL <span class="values">http://x4z9arb.cn/4712/</span>, which is known to be malicious, and a backdoor piece of malware associated with the URL. The site has been shown to host this backdoor malware, and the malware has been known to download remote files.

**Data model**
--------------

Malicious URL values are just one of many indicators that can be represented using the [Indicator](https://docs.google.com/document/d/1nipwFIaFwkHo4Gzw-qxZQpCjP_5tX7rbI3Ic5C56Z88/edit#heading=h.muftrcpnf89v) STIX Domain Object (SDO). This is accomplished using the Indicator SDO’s <span class="sdo">**pattern**</span> property which is based on the [STIX patterning](https://docs.google.com/document/d/1VHy5FIAj2rBlrRlNH3lRCBa5EfrxSDGemG4PrI9JG4I/edit) language. Using this language, the URL can be structured using a comparison expression: <span class="values">\[url:value= 'http://x4z9arb.cn/4712/'\]</span>.

This Indicator object must also contain a <span class="sdo">**labels**</span> property that provides more context about the URL. The URL in this scenario is known to be malicious so the appropriate label for this Indicator is <span class="values">malicious-activity</span>. This value is taken from an [Indicator Label](https://docs.google.com/document/d/1HRVFn2kAxBOTMbEb3KRu8tjMoHm-KRAI-2R8CTzGil4/edit#heading=h.cvhfwe3t9vuo) open vocabulary which contains other useful labels for categorizing indicators.

Another required field for Indicator objects called <span class="sdo">**valid\_from**</span> dictates the time from which this URL should be considered worthwhile intelligence. In this case, the URL is valid from the time the object was created.

The malware associated with the URL in this scenario is a type of backdoor and can be modeled using the STIX [Malware](https://docs.google.com/document/d/1nipwFIaFwkHo4Gzw-qxZQpCjP_5tX7rbI3Ic5C56Z88/edit#heading=h.s5l7katgbp09) SDO. Like with the Indicator object, Malware objects can be further classified using a <span class="sdo">**labels**</span> property that comes from the [Malware Label](https://docs.google.com/document/d/1HRVFn2kAxBOTMbEb3KRu8tjMoHm-KRAI-2R8CTzGil4/edit#heading=h.8cyb6e9yqzwr) open vocabulary. For instance, a piece of malware might be classified as a keylogger, spyware, worm, virus, etc. In this example, the malware affiliated with the URL is a type of <span class="values">backdoor</span> and <span class="values">remote-access-trojan</span>.

A Malware SDO can also be useful for capturing kill chain information about the malware instance. It is known that this piece of malware attempts to establish a backdoor foothold and download remote files. Therefore, the Malware object represents this with a <span class="sdo">**kill\_chain\_phases**</span> list which contains both the name of the kill chain used and the phase within that kill chain. For this scenario, the Mandiant Attack Lifecycle Model was used as the kill chain and contains the <span class="sdo">**phase\_name**</span> <span class="values">establish-foothold</span>. Other kill chains such as Lockheed Martin’s or organization-specific ones can be used as well.

Finally, a [Relationship](https://docs.google.com/document/d/1nipwFIaFwkHo4Gzw-qxZQpCjP_5tX7rbI3Ic5C56Z88/edit#heading=h.e2e1szrqfoan) SRO can be used to link the Indicator and Malware objects. The URL Indicator <span class="values">indicates</span> the backdoor Malware object. In this relationship, the indicator id is the <span class="sdo">**source\_ref**</span>, and the malware id is the <span class="sdo">**target\_ref**</span>.

A diagram of this relationship below shows the Indicator and Malware SDO’s and the Relationship SRO between them:

![Indicator for malicious url]({{ site.baseurl }}/img/Indicator-for-malicious-url.PNG)

**Further Reading**
-------------------

To read more about the objects in this example as well as common properties and STIX patterning, check out the links below:

-   [Common Properties](https://docs.google.com/document/d/1HRVFn2kAxBOTMbEb3KRu8tjMoHm-KRAI-2R8CTzGil4/edit#heading=h.xzbicbtscatx)
-   [Vocabularies](https://docs.google.com/document/d/1HRVFn2kAxBOTMbEb3KRu8tjMoHm-KRAI-2R8CTzGil4/edit#heading=h.iit7tolczlxv)
-   [Malware](https://docs.google.com/document/d/1nipwFIaFwkHo4Gzw-qxZQpCjP_5tX7rbI3Ic5C56Z88/edit#heading=h.s5l7katgbp09)
-   [Indicator](https://docs.google.com/document/d/1nipwFIaFwkHo4Gzw-qxZQpCjP_5tX7rbI3Ic5C56Z88/edit#heading=h.muftrcpnf89v)
-   [Relationship](https://docs.google.com/document/d/1nipwFIaFwkHo4Gzw-qxZQpCjP_5tX7rbI3Ic5C56Z88/edit#heading=h.e2e1szrqfoan)
-   [STIX Patterning](https://docs.google.com/document/d/1suvd7z7YjNKWOwgko-vJ84jfGuxSYZjOQlw5leCswPY/edit#heading=h.jphmvccraytb)

**Implementation**
------------------

{% include start_tabs.html tabs="JSON|Python Producer|Python Consumer" name="indicator-url" %}{% highlight xml linenos %}
{% include_relative example_json/indicator-for-malicious-url.json %}
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
{% include_relative producer_python/indicator-for-malicious-url-producer.py %}
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
{% include_relative consumer_python/indicator-for-malicious-url-consumer.py %}
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
{% endhighlight %}{% include end_tabs.html %}
