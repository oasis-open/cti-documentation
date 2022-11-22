---
layout: page
title: Sighting of Observed-data
categories: examples
---

While indicators of compromise represent intelligence assertions behind attacks, raw observed information help formulate the basis behind this intelligence. In many cases, it may be beneficial for organizations to share this observed data among each other. Similar to indicators, sightings can contain references to observed data objects that were spotted on other organizations’ networks and could signal information about a type of malware present. This may potentially allow for further intelligence assertions to be made based on this sighted raw information.

**Scenario**
------------

This scenario consists of two cyber threat companies, Pym and Oscorp, who share threat intelligence with one another. Pym Technologies originally shared a [Malware](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_s5l7katgbp09) STIX Domain Object (SDO) with Oscorp. Oscorp later believes they have spotted this Malware object on their own network based upon some captured observed data which contains hashes that match the malware as well as registry keys that the malware created. To represent this, Oscorp issues a [Sighting](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_a795guqsap3r) STIX Relationship Object (SRO) that holds references to these observed data and relays that this could be a sighting-of this particular malware.

**Data model**
--------------

In this example, there are two [Identity](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_wh296fiwpklp) STIX Domain Objects (SDOs) used for the two companies: Pym and Oscorp. The Identity objects document relevant information about the two organizations, such as what sector they are in and relevant contact information. Both organizations are producers and consumers of STIX intelligence, so their <span class="sdo">**id**</span>’s can be referenced within objects using the <span class="sdo">**created\_by\_ref**</span> property to indicate they are the originators of the STIX objects they generate. It is worth noting that Identity SDO’s can also be used to represent individuals, attack targets, government agencies, and groups, to name a few.

The Identity objects at the very minimum need a value for the required <span class="sdo">**name**</span> property. In this example, the <span class="sdo">**identity\_class**</span> property is also used, and it is important for categorizing the type of identity Pym and Oscorp represen: <span class="values">organization</span>, in this case. This value comes from the [identity class open vocabulary](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_be1dktvcmyu), which contains suggested values for labeling Identities.

Pym Technologies first created a Malware SDO to represent details about the type of malware in this scenario. This specific malware type is labeled as a <span class="values">remote-access-trojan</span>, and is an executable disguised as a pdf file that creates multiple registry keys. Pym then shared this intelligence with Oscorp.

Oscorp Industries, which now has this Malware object, believes it has seen this malware on its own networks and created a Sighting object to represent this. The Sighting SRO is a special type of STIX relationship that contains properties about the object seen such as the <span class="sdo">**id**</span> of the Malware SDO (with <span class="sdo">**sighting\_of\_ref**</span>), a <span class="sdo">**count**</span> property that indicates the number of times this malware was seen, as well as timestamps for when it was first and last seen. In addition, a listing of Observed-Data <span class="sdo">**id**</span>s is included to communicate any necessary information that may support the sighting of this malware.

[Observed Data](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_p49j1fwoxldc) SDO’s contain references to cyber observables (e.g. IP addresses, files, URL’s) that were captured on systems and networks. In this scenario, Oscorp observed both [file](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_99bl2dibcztv) and [registry key](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_luvw8wjlfo3y) information. They can model this information within 2 different Observed-Data objects. Although you are able to include references to multiple cyber observable objects within one Observed-Data instance, the cyber observables must be related to each other. In this case, the file and registry data are not directly related so their references are contained in separate Observed-Data instances. You can read more about STIX [objects](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_nrhq5e9nylke) and cyber observable [objects](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_mlbmudhl16lr), which are covered in parts 4 and 6 of the STIX 2.1 specification, respectively.

For Observed-Data objects, either the <span class="sdo">**object\_refs**</span> (preferred) or <span class="sdo">**objects**</span> (deprecated) property must be included, and all other Observed-Data specific properties are required. So for each of these objects, Oscorp had to provide when each instance was <span class="sdo">**first\_observed**</span> and <span class="sdo">**last\_observed**</span>, as well as a count (<span class="sdo">**number\_observed**</span>) of the number of times the data was observed. In addition, they can provide references to the actual cyber observable objects in the <span class="sdo">**object\_refs**</span> property. The first Observed-Data instance in this example (Observed Data 1 in the diagram below) contains information about the file that was seen. So, data like a listing of <span class="sdo">**hashes**</span>, the file’s <span class="sdo">**name**</span>, and its <span class="sdo">**size**</span> were included to represent the file. In the second Observed-Data instance, Oscorp models Windows Registry values such as the registry <span class="sdo">**key**</span> that the suspected malware created.

Finally, it is worth mentioning that none of the objects in this scenario use the standard [Relationship](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_e2e1szrqfoan) SRO which is typically used to relate objects with one another. The Sighting SRO is used instead for the sighting of the Malware object and all other relationships in the diagram below are embedded within the objects. For instance, the Sighting object contains several embedded relationships including what was observed, who the object was created by, and where the sighting was seen.

A diagram of this scenario is depicted below [(An interactive version can be found here)](https://oasis-open.github.io/cti-stix-visualization/?url=https://raw.githubusercontent.com/oasis-open/cti-documentation/master/examples/example_json/sighting-of-observed-data.json){: target="_blank"}:

![Sighting of Observed-data]({{ site.baseurl }}/img/Sighting-of-observed-data.PNG)

**Further Reading**
-------------------

To read more about the objects in this example as well as common properties and vocabularies, check out the links below:

-   [Common Properties](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_xzbicbtscatx)
-   [Vocabularies](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_izngjy1g98l2)
-   [Identity](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_wh296fiwpklp)
-   [Sighting](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_a795guqsap3r)
-   [Observed Data](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_p49j1fwoxldc)
-   [Malware](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_s5l7katgbp09)
-   [Cyber Observable Objects](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_mlbmudhl16lr)
-   [Relationship](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_e2e1szrqfoan)

**Implementation**
------------------

{% include start_tabs.html tabs="JSON|Python Producer|Python Consumer" name="sighting-data" %}{% highlight json linenos %}
{% include_relative example_json/sighting-of-observed-data.json %}
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
{% include_relative producer_python/sighting-of-observed-data-producer.py %}
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
{% include_relative consumer_python/sighting-of-observed-data-consumer.py %}
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
{% endhighlight %}{% include end_tabs.html %}
