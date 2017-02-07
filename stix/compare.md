---
layout: page
title: Comparing STIX 1.x/CybOX 2.x with STIX 2.0
short_title: Comparing STIX 1 and 2
categories: stix
---

<div class="row">
<div class="col-md-12" markdown="1">

Here is a quick overview of the differences between STIX 1.x/CybOX 2.x and STIX 2.0.

One standard
---

First, the OASIS Cyber Threat Intelligence (CTI) Technical Committee (TC) decided to merge the two specifications into one. CybOX objects are now called STIX Cyber Observables.

Now when you discuss “STIX”, you are talking about the one standard needed for sharing cyber threat intelligence!

JSON vs. XML
---

STIX 2.0 requires implementations to [support JSON serialization](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.vj2dopx186bb), while STIX 1.x was defined using XML. Though both XML and JSON have benefits, the CTI TC determined that JSON was more lightweight, and sufficient to express the semantics of cyber threat intelligence information. It is simpler to use and increasingly preferred by developers.

STIX Domain Objects
---

All objects in STIX 2.0 are [at the top-level](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.1j0vun2r7rgb), rather than being embedded in other objects. These objects are called STIX Domain Objects (SDO). Some object properties use a reference to another object’s id directly (e.g., created\_by\_ref), but most relationships are expressed using the top-level Relationship object.

The generic TTP (tactics, techniques, procedures) and Exploit Target types from STIX 1.x have been split into separate top-level objects (Attack Pattern, Malware, Tool and Vulnerability) with specific purposes in STIX 2.0.

Relationships as top-level objects
---

STIX 2.0 introduces a top-level [Relationship object](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.l326yout8qc1), which links two other top-level objects via a named relationship type. STIX 2.0 content can be thought of as a connected graph, where nodes are SDOs and edges are Relationship Objects. The STIX 2.0 specification suggests different named relationships, but content producers are able to define their own. In STIX 1.x relationships were “embedded” in other objects. The types of relationships supported was restricted by the STIX 1.x specification. Because STIX 1.x relationships themselves were not top-level objects, you could not express a relationship between two objects without changing one of them. In CTI, it is often desirable for others to assert a relationship. Using this new Relationship object, others, besides the original content creator, can add to the shared knowledge in an independent way.

Streamlined Model
---

Experience with STIX 1.x showed that a common set of features were widely used and well understood while many other features lacked shared understanding and had only limited, if any use at all. In addition, almost all properties of objects were optional. Overall, the breadth of STIX 1.x was an impediment to sharing intelligence, and necessitated a formal agreement among threat groups on what should be shared (i.e., profiles).

STIX 2.0 takes a different approach – many properties are required, and the number of objects and properties have been reduced to a core set of well understood features. Future releases of STIX will incorporate additional concepts as they are needed.

However, the need to incorporate concepts not yet in the specification is enabled through the ability to use custom properties and custom objects.

Data Markings
---

[Data markings](https://docs.google.com/document/d/1IcA5KhglNdyX3tO17bBluC5nqSf70M5qgK9nuAoYJgw/edit#heading=h.j0uqagkk6m9n) no longer use a serialization specific language, e.g., XPath. In STIX 2.0, there are two types of data markings: object marking – applicable to a whole object, and granular markings – applicable to a property or properties of an object. Data markings scope is only within the object where they are defined.

Indicator Pattern Language
---

Indicator patterns in STIX 1.x were expressed using XML syntax. This made all but the simplest patterns difficult to create and to understand. STIX 2.0 takes a different approach, specifying [a language for patterns](https://docs.google.com/document/d/1suvd7z7YjNKWOwgko-vJ84jfGuxSYZjOQlw5leCswPY) which is independent of the serialization language \[5\]. Patterns written in the STIX patterning language are more compact and easier to read. Additionally, there is no confusion between patterns and observations, because a pattern is not a top-level object, but a property of an indicator object.

Coming Attractions
---

STIX 2.0 does not currently support several CTI concepts, such as Incidents, Confidence, Assets and Infrastructure, Impact Assessment, Personas, Victims and Victim Targeting. Many of these are under development for STIX 2.1, which is currently being defined. Likewise, only the most “popular” cyber observable objects are currently supported. Again, more will be added in future releases.

</div>
</div>