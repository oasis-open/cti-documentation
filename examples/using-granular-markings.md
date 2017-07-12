---
layout: page
title: Using Granular Markings
categories: examples
---

Having finer, more granular restrictions over what cyber threat intelligence is shared is beneficial for organizations who are hesitant to sharing certain information. This element of control allows STIX producers to limit the accessibility of specific data to organizations with which they share intelligence.

**Scenario**
------------

This scenario focuses on a STIX producer, “Gotham National Bank”, who imposes granular markings on an Indicator object. Before sharing this indicator, Gotham selects a few “Traffic Light Protocol” (TLP) marking definitions to apply to the indicator. These marking definitions help restrict the usage of certain properties of the indicator based on its TLP marking type.

**Data model**
--------------

The producer of STIX objects in this scenario, Gotham National Bank, can be represented with an [Identity](https://docs.google.com/document/d/1S5XhY6F5OT599b0OuHtUf8IBzFvNY8RysFHIj93DgsY/edit#heading=h.wh296fiwpklp) STIX Domain Object (SDO). Like with all STIX objects, an <span class="sdo">**id**</span> attribute uniquely identifies Gotham National and can be referenced within all the objects they generate with the <span class="sdo">**created\_by\_ref**</span> property. Although <span class="sdo">**created\_by\_ref**</span> is optional, this is helpful for attributing the Indicator SDO directly to Gotham and allows any consumers to see who applied the TLP markings to the Indicator. The Identity object is also useful for listing other relevant details about Gotham such as <span class="sdo">**contact\_information**</span> and what type of identity they are with the <span class="sdo">**identity\_class**</span> field.

In order to enforce limitations on specific properties of the Indicator object, Gotham decided to use TLP Marking Definition objects. This particular marking definition type, which can be seen within the STIX 2.0 specification under [TLP Marking Object Type](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.yd3ar14ekwrs), helps specify the type of restriction they want to impose. For instance, in this scenario, they needed to utilize three defined TLP marking definitions, each with a different restriction type. With all of these objects, the <span class="sdo">**definition\_type**</span> is required and must be <span class="values">tlp</span>. In addition, the <span class="sdo">**definition**</span> property is also required and must contain one of the four types of TLP. Gotham needed three of the four types of TLP definitions, which were <span class="values">green</span>, <span class="values">amber</span>, and <span class="values">red</span>. To read about each of the four types of TLP and what restrictions they specify, check out [US-CERT’s TLP Definitions and Usage](https://www.us-cert.gov/tlp). Knowing these types is useful for the level of restriction you would like to provide for both objects and properties of objects.

A point of emphasis worth noting is that the TLP Marking Object Types defined in the STIX 2.0 specification must be used to represent TLP markings. Gotham or any other producer could not create their own TLP markings but could create organization-specific [Statement Marking Object Types](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.3ru8r05saera). Both of these types, TLP and Statement, also cannot be versioned like other STIX objects, which is why there is no <span class="sdo">**modified**</span> property on either of these types. To understand more about versioning objects, check out this helpful tutorial video on [How to Use Versioning in STIX 2](https://www.youtube.com/watch?v=s4c4PHUfttE).

Now that Gotham has selected the appropriate TLP Marking Object types, they can be applied to other STIX objects or properties of objects. In the first part of this scenario, they are attached to properties of an [Indicator](https://docs.google.com/document/d/1S5XhY6F5OT599b0OuHtUf8IBzFvNY8RysFHIj93DgsY/edit#heading=h.muftrcpnf89v) SDO Gotham generated. This Indicator was created to represent a fake email address suspected in emailing the bank's members asking for their credentials. Due to the sensitivity of some of the information contained within this Indicator, they applied different TLP markings to individual portions of this object with the <span class="sdo">**granular\_markings**</span> property. This property is a list that contains Marking Definition object ID references with the <span class="sdo">**marking\_ref**</span> field, and a <span class="sdo">**selectors**</span> property that specifies the content that should be marked with this marking definition. For instance, Gotham felt the need to apply a strict TLP: Red marking to the <span class="sdo">**description**</span> field since this gives certain sensitive intelligence about the threat actor in this scenario (discussed later). To illustrate further, within the <span class="sdo">**granular\_markings**</span> field of the Indicator, the <span class="sdo">**marking\_ref**</span> property would contain the marking definition ID for TLP: Red and the <span class="sdo">**selectors**</span> list would hold the value <span class="values">description</span>.

For other Indicator properties, Gotham used less restrictive TLP markings than TLP: Red. One required Indicator property is a list of <span class="sdo">**labels**</span>, which gives more context about the type of indicator being modeled. In this property list, Gotham labeled this indicator as both <span class="values">malicious-activity</span> and <span class="values">attribution</span>. Both labels in the list come from the STIX 2.0 specification's [Indicator Label Open Vocabulary](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.cvhfwe3t9vuo). Gotham decided to apply the less restrictive TLP: Green marking to <span class="values">malicious-activity</span> and felt a the more restrictive TLP: Amber marking was needed for <span class="values">attribution</span>. In order to communicate two different markings like this on the <span class="sdo">**labels**</span> property, the first label in the list is represented as <span class="values">labels\[0\]</span>, and the second as <span class="values">labels\[1\]</span>. To illustrate this, the JSON sample below shows how these would be marked if we were just marking the <span class="sdo">**labels**</span> field only (Note: Marking Definition ID starting with "f88..." is TLP: Amber and the ID starting with "340..." is TLP: Green):

```
{
"granular_markings": [  
  {
    "marking_ref": "marking-definition--f88d31f6-486f-44da-b317-01333bde0b82",
    "selectors": [    
      "labels.[1]"
    ]
  },
  {
    "marking_ref": "marking-definition--34098fce-860f-48ae-8e50-ebd3cc5e41da",
    "selectors": [
      "labels.[0]",      
    ]
  }
]}
```

Along with these Indicator <span class="sdo">**labels**</span>, Gotham chose to mark the properties <span class="sdo">**name**</span> and <span class="sdo">**pattern**</span> as TLP: Green. They can mark any property they would like but cannot mark invalid properties such as <span class="values">labels\[3\]</span>, or <span class="values">kill\_chain\_phases\[0\]</span> since these are not present currently within this Indicator SDO.

Gotham also created a [Threat Actor SDO](https://docs.google.com/document/d/1S5XhY6F5OT599b0OuHtUf8IBzFvNY8RysFHIj93DgsY/edit#heading=h.k017w16zutw) to capture information about the threat actor this Indicator indicates. In this example, the threat actor, whose <span class="sdo">**name**</span> is known as <span class="values">The Joker</span>, has been attributed to the fake email indicator. Along with <span class="sdo">**name**</span>, this object helps to structure other information about The Joker such as <span class="sdo">**aliases**</span>, <span class="sdo">**roles**</span>, and a <span class="sdo">**primary_motivation**</span>. Since all of this intelligence is considered sensitive to Gotham National, they marked the entire object as TLP: Red using [object markings](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.bnienmcktc0n) instead of granular markings. This is accomplished through a property inherent in all SDO's and STIX Relationship Object's (SRO's) called <span class="sdo">**object_marking_refs**</span>, which lists all the marking definition IDs that apply to this object. Unlike the <span class="sdo">**granular\_markings**</span> property that would apply to different fields within Threat Actor, the <span class="sdo">**object_marking_refs**</span> applies to the entire Threat Actor SDO.  

The final piece of intelligence in this scenario is a [Relationship SRO](https://docs.google.com/document/d/1S5XhY6F5OT599b0OuHtUf8IBzFvNY8RysFHIj93DgsY/edit#heading=h.e2e1szrqfoan) that connects the Indicator and Threat Actor SDO's together. In this relationship, a <span class="sdo">**relationship_type**</span> property specifies that this Indicator <span class="values">indicates</span> the Threat Actor. Due to the fact this Relationship object links to a TLP: Red marked object, Gotham also marked it as TLP: Red once again using the <span class="sdo">**object_marking_refs**</span> field within Relationship.

The full JSON representation can be seen at the very end of this example and a diagram of the scenario is illustrated below:

![Using Granular Markings Diagram]({{ site.baseurl }}/img/Using-granular-markings.PNG)

**Further Reading**
-------------------

To read more about the objects in this example as well as common properties and vocabularies, check out the links below:

-   [Common Properties](https://docs.google.com/document/d/1HRVFn2kAxBOTMbEb3KRu8tjMoHm-KRAI-2R8CTzGil4/edit#heading=h.xzbicbtscatx)
-   [Vocabularies](https://docs.google.com/document/d/1HRVFn2kAxBOTMbEb3KRu8tjMoHm-KRAI-2R8CTzGil4/edit#heading=h.iit7tolczlxv)
-   [Identity](https://docs.google.com/document/d/1nipwFIaFwkHo4Gzw-qxZQpCjP_5tX7rbI3Ic5C56Z88/edit#heading=h.wh296fiwpklp)
-   [Indicator](https://docs.google.com/document/d/1S5XhY6F5OT599b0OuHtUf8IBzFvNY8RysFHIj93DgsY/edit#heading=h.muftrcpnf89v)
-   [Threat Actor](https://docs.google.com/document/d/1S5XhY6F5OT599b0OuHtUf8IBzFvNY8RysFHIj93DgsY/edit#heading=h.k017w16zutw)
-   [Relationship](https://docs.google.com/document/d/1S5XhY6F5OT599b0OuHtUf8IBzFvNY8RysFHIj93DgsY/edit#heading=h.e2e1szrqfoan)
-   [Marking Definitions](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.j0uqagkk6m9n)
-   [Granular Markings](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.robezi5egfdr)
-   [Object Markings](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.bnienmcktc0n)
-   [Statement Marking Object Type](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.3ru8r05saera)
-   [TLP Object Marking Type](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.yd3ar14ekwrs)
-   [STIX Patterning](https://docs.google.com/document/d/1suvd7z7YjNKWOwgko-vJ84jfGuxSYZjOQlw5leCswPY/edit)
-   [Using Versioning in STIX 2](https://www.youtube.com/watch?v=s4c4PHUfttE)

**Implementation**
------------------

{% include start_tabs.html tabs="JSON|Python Producer|Python Consumer" name="using-granular" %}{% highlight json linenos %}
{% include_relative example_json/using-granular-markings.json %}
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
{% include_relative producer_python/using-granular-markings-producer.py %}
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
{% include_relative consumer_python/using-granular-markings-consumer.py %}
{% endhighlight %}{% include tab_separator.html %}{% highlight python linenos %}
{% endhighlight %}{% include end_tabs.html %}
