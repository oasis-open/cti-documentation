---
layout: page
title: FAQ
categories: FAQ
hide_title: true
---

Frequently Asked Questions
===================================================

<div class="faq-btn">
  <a class="btn btn-primary btn-spec" data-toggle="tooltip" title="Official FAQ Google Doc" target="_blank" href="https://docs.google.com/document/d/1V5tE78N10McUq1xUOHV1RTVsOoYmiq_xt2PY1YI8bsU/pub">
    <span class="glyphicon glyphicon-list-alt"></span> Official FAQ Google Doc
  </a>

  <a class="btn btn-primary btn-spec" data-toggle="tooltip" title="Question Submission" target="_blank" href="https://www.oasis-open.org/committees/comments/index.php?wg_abbrev=cti">
    <span class="glyphicon glyphicon-envelope"></span> Question not found? Send it in!
  </a>
</div>

<div>
1. TOC
{:toc}
</div>
<div>
## General ##
</div>
<div>
### What is STIX™? ###
STIX — the Structured Threat Information eXpression — is a language and serialization format used to exchange cyber threat intelligence (CTI). STIX enables organizations to share CTI with one another in a consistent and machine-readable manner, allowing security communities to better understand what computer-based attacks they are likely to see and to better prepare for and/or respond to those attacks faster and more effectively. STIX is designed to improve many different capabilities, such as collaborative threat analysis, automated threat exchange, automated detection and response, and more.
</div>

<div>
### What is TAXII™? ###
TAXII — the Trusted Automated Exchange of Intelligence Information — is an application layer protocol for the communication of CTI in a simple and scalable manner over HTTPS. TAXII enables organizations to share CTI by defining a standard API that aligns with common sharing models. TAXII is specifically designed to support the exchange of CTI represented in STIX.
</div>

<div>
### Who controls STIX™ and TAXII™? ###
The STIX and TAXII standards are governed by the OASIS Cyber Threat Intelligence Technical Committee (CTI TC). STIX and TAXII were created in 2012 under the auspices of the US Department of Homeland Security. In June of 2015, DHS licensed all of the intellectual property and trademarks associated with STIX and TAXII to OASIS, a nonprofit consortium that drives the development, convergence and adoption of open standards for the global information society. Since June of 2015, the CTI TC has been working to create the next generation of STIX and TAXII standards.
</div>

<div>
### What are the current versions of STIX™ and TAXII™? ###
In 2021, OASIS approved STIX 2.1 and TAXII 2.1 as OASIS Standards. See the [Resources]({{ site.baseurl }}/resources) page for links to the latest specs.
</div>

<div>
### Are there “real-world” examples of STIX™ 2 content I can look at? ###
There are two example threat reports in the [CTI STIX2 JSON Schemas repository](https://github.com/oasis-open/cti-stix2-json-schemas/tree/master/examples/threat-reports).

The [cti-common-objects repository](https://github.com/oasis-open/cti-stix-common-objects) contains many, many samples.

Many threat intelligence providers offer their intelligence in the STIX format.

Finally, there are several examples in the [Examples]({{ site.baseurl }}/stix/examples) section of this site.
</div>

<div>
### Are there APIs and Tools for STIX™ and TAXII™ 2? ###
Yes, see the Github repositories for the [CTI TC open repositories](https://github.com/oasis-open?utf8=%E2%9C%93&q=cti-&type=&language=).

The list of repositories on the [Resources]({{ site.baseurl }}/resources) page contains direct links to useful tools.
</div>

<div>
### How do I verify my software is STIX™/TAXII™ 2 interoperable? ###
The Interoperability Subcommittee of the CTI TC has developed a 2-Part Committee Note that establishes a step-by-step guide to a self-certification process. Once a Producer of STIX feeds, a vendor providing a Threat Intelligence Platform (TIP), a vendor providing a Security Incident and Event Management (SIEM) tool, a vendor that provides threat mitigation systems (TMS), or a vendor that provides threat detection systems (TDS) executes the steps outlined, demonstrates successful interoperability, and documents such, that supplier may submit a statement to OASIS testifying to the self-certification.We are using TMS to refer to tools such as firewalls and intrusion prevention systems. We are using TDS to refer to tools such as intrusion detection software and web proxies.

The self-certification process is intended to be policed by market forces. If a vendor or supplier self-certifies and is shown to be misrepresenting its products the OASIS Community will remove the vendor from the STIX/TAXII 2 compatible products list after verification of the claim.

The vendor or supplier will need to re-test the attested product and submit documentation as per the Interoperability Specification to once again achieve listing on the interoperability list.

See the [Resources]({{ site.baseurl }}/resources) page for direct links to the STIX™ and TAXII™ Interoperability specifications.
</div>

<div>
### I'm implementing STIX™ and/or TAXII™ 2 and I have a question about something in the specification. What should I do? ###
We have a very active and supportive community.  If you post your question on CTI Users List you will likely receive a response from one of our community members.

Email cti-users at lists.oasis-open.org or file an issue in the [CTI TC's repository](https://github.com/oasis-tcs/cti-stix2/issues) on Github.
</div>

<div>
## The Transition to STIX™/TAXII™ 2 ##
</div>

<div>
### Why were new versions of STIX™ and TAXII™ created? ###
While STIX and TAXII 1 have been widely adopted and deployed around the world by operational sharing communities, the CTI TC recognized that these specifications were difficult to implement. The primary sources of that difficulty were excessive complexity in certain advanced XML constructs (e.g., XSI types) and the choice of XML as a representation. The community also learned that having multiple ways of doing things and excessive optionality in the data model led to differences in data-modelling and challenges in interoperability. As a result the CTI TC decided to rework the data model and serialization for STIX 2. Similarly, armed with the lessons learned over the years the community made the decision to rework TAXII as an HTTP Representational State Transfer (RESTful) based design.
</div>

<div>
### What are the key differences between STIX™ 1 and STIX™ 2? ###

- JSON vs. XML

Whereas STIX 1 was serialized using eXtensible Mark-up Language (XML), STIX 2 specifies JavaScript Object Notation (JSON) as the “Mandatory To Implement” (MTI) serialization, i.e. it requires implementations to, at a minimum, support JSON serialization. Though both XML and JSON have their own benefits, the CTI TC determined that JSON was more lightweight, preferred by most developers, and easier to understand while being sufficient to express the semantics of STIX.

- STIX™ Domain Objects

STIX 1 allowed certain objects to be defined within other objects (e.g., a TTP could be defined within an Indicator) in addition to being defined outside any other object (i.e., at the “top-level” of a STIX document). In STIX 2, all STIX Domain Objects (SDOs) are peers that are defined at the top-level of a STIX document, rather than being embedded in other objects. This change simplifies the parsing and storage of STIX 2 objects.

During the development of the STIX 2 SDOs the community felt that the generic TTP object (tactics, techniques, procedures) and Exploit Target object from STIX 1 were semantically-overloaded, so these have been split into separate top-level objects (Attack Pattern, Malware, Tool and Vulnerability) with a tighter focus on their respective use-cases in STIX 2.

- Relationships as Top-Level Objects

STIX 2 introduces a top-level STIX Relationship Object (SRO), which links STIX Domain Objects (SDOs) via a named relationship type. The STIX 2 data-model was designed to be a connected graph, wherein nodes are SDOs and edges are SROs. The STIX 2 specification includes a default set of named relationships, but content producers are also able to define their own relationships. In contrast, STIX 1 defined relationships as properties that were “embedded” in other objects. The types of relationships supported were restricted by the STIX 1 specification. Accordingly, because STIX 1 relationships themselves were not top-level objects, you could not express a relationship between two objects without changing one of them. As only the creator of an SDO is allowed to make changes to it, this effectively prevented “third-party” relationships, where an entity other than the creator of one or both of the objects asserts a relationship between them. In the workflows around CTI, it is often desirable for others to assert a relationship; for example, a threat analyst might want to assert a relationship between an indicator and a threat actor even though the analyst was not the original creator of either object. Using the new graph-based STIX data-model in STIX 2, others (i.e., not just the original content creator) can define new relationships between entities in order to add to the shared knowledge. The following graphic shows an illustration of this for the Indicator SDO.

![STIX Illustration of Indicator Relationships]({{ site.baseurl }}/img/stix2-indicator-diagram-72dpi-v1.png){: .figure-img .img-fluid}

- Streamlined Model

Experience with STIX 1 showed that a common subset of capabilities were widely-used and well-understood while many others were problematic, poorly-understood, and in many cases never used. In addition, almost all object properties in STIX 1 were optional, presenting significant parsing challenges for consumers of STIX 1 content. At a high-level, the breadth of capabilities and multiple ways of representing semantically identical content in STIX 1 was an impediment to interoperable sharing of CTI, leading sharing communities to formally define how different types of CTI would be represented via STIX 1 Profiles.

STIX 2 takes a radically different approach. Many more properties are required, and the number of objects and properties have been reduced to a core set of well-understood features, modeled in such a way as to eliminate the problem of multiple ways of encoding semantically-equivalent CTI. Future releases of STIX will incorporate additional concepts as they are needed.

It is understood that certain communities will need to exchange data not defined within the STIX 2 specification. This need is addressed via the ability to use custom objects and properties within STIX 2.

- Data Markings

As part of the move from XML to JSON, Data markings no longer use XPath. In STIX 2, there are two types of data markings: object markings – applicable to an entire object, and granular markings – applicable to one or more object properties within a single object. In order to clarify the semantics of markings, all objects must be marked individually - there is no inheritance of markings in STIX 2.

- STIX™ Patterning Language

Indicator patterns in STIX 1 were an area where the "many ways of expressing semantically-equivalent content" problem was particularly manifested. As a result, for a consumer of STIX 1 content, rigorously parsing all but the simplest patterns was unnecessarily difficult. STIX 2 takes a radically different approach by defining a human-readable, SQL-like Indicator Patterning Language. As a result, patterns written in the STIX Patterning Language are more compact and far easier to read.

- Observations vs. Patterns

In STIX 1, the duality between Observations and Patterns (i.e., a pattern was essentially an observation with an operator) was a point of confusion for many end users. STIX 2 resolves this issue by having a separate pattern construct that uses its own language (see above) and is a property of an Indicator object instead of a top-level object. Accordingly, there is no semantic overlap in STIX 2 between the specification of observations using the Observed Data object and patterns via the Indicator object, as these entities were designed to be distinct.
</div>

<div>
### What are the key differences between STIX™ 2.0 and STIX™ 2.1? ###
STIX 2.1 differs from STIX 2.0 in the following ways:

- New objects: Grouping, Infrastructure, Language-Content (internationalization), Location, Malware-Analysis, Note, Opinion
- Objects that have undergone significant change: Malware, all SCOs
- New concepts: Confidence
- STIX Cyber-observable Objects can now be directly related using STIX Relationship Objects
- Renamed conflicting properties on Directory Object, File Object, Process Object, and Windows Registry Key Object.
- Added relationship from Indicator to Observed Data called "based-on".
- Added a description to Sighting and added a name to Location.
- Made some SCO relationships external on Domain-Name, IPv4-Addr, and IPv6-Addr.
- Added STIX Extension mechanisms and deprecated custom properties, objects, and extensions.

</div>

<div>
### STIX™ 1 had XML Namespaces. Is there something similar in STIX™ 2? ###
STIX 1 made use of XML namespaces for two purposes:

- Individual elements and attributes were namespaced to separate out elements from one object type (e.g., indicator) from those of another type (e.g., incident).
- Namespaces in the "id" field were used to indicate the producer of the STIX object.
While it is common practice for XML content to make use of namespaces, most JSON content does not. For this reason STIX 2 does not use namespaces. For more reasoning on this, see: https://www.mnot.net/blog/2011/10/12/thinking_about_namespaces_in_json

STIX 2 uses a property, created_by_ref, to replace the second usage of namespaces. In other words, in STIX 1 you would examine the namespace of an ID attribute value on an object to determine who created it, while in STIX 2 you look in the created_by_ref property.
</div>

<div>
### What happened to CybOX™? ###
During the design and development of STIX 2, the CTI TC concluded that due to the tightly-coupled nature of STIX and the Cyber Observable eXpression (CybOX) language that CybOX should be merged into STIX. These objects are now characterized as Cyber Observable objects within STIX and are defined in the STIX specification.

The TC felt that it would be easier for the market to understand and adopt STIX if it was a single standard. This consolidation eliminated the need for a complex interoperability matrix between the two standards.
</div>

<div>
### What are the key differences between TAXII™ 1 and TAXII™ 2? ###

- HTTPS as the Transport Protocol

TAXII 1 was designed to the TAXII application protocol to be hosted on top of multiple underlying transport protocols. While, in theory this seemed like a good design choice, in practice TAXII 1 was only ever implemented (to our knowledge) on top of HTTP. Because the TAXII 1 protocol could not assume any particular underlying transport, this required that TAXII reimplement features and capabilities that were already provided by HTTP. In contrast, TAXII 2 is explicitly designed to serve as an application layer protocol on top of HTTPS and as such can rely on the full set of services provided by HTTPS implementations. The result is that the TAXII 2 protocol is smaller and simpler and should prove to be much easier to implement.

- RESTful Interface

TAXII 2 provides a RESTful interface to data and services. RESTful is an architectural style for networked hypermedia applications; it is primarily used to build Web services that are lightweight, maintainable, and scalable. RESTful is not dependent on any protocol, but almost every RESTful service uses HTTP as its underlying protocol. As is noted above, TAXII 2 is built on top of HTTPS the secure HTTP analogue.
</div>

<div>
### Are there tools to help me migrate between STIX™ 1 and STIX™ 2? ###
Yes. The [STIX Elevator](https://github.com/oasis-open/cti-stix-elevator) does a best-effort conversion of STIX 1 content into STIX 2. The [STIX Slider](https://github.com/oasis-open/cti-stix-elevator) converts STIX 2 to STIX 1.
</div>

<div>
### What are the latest versions of STIX™ and TAXII™ 1? ###
The most recent (and final) version of the STIX 1 specifications is STIX 1.2.1, the specifications can be found here: http://docs.oasis-open.org/cti/stix/v1.2.1/stix-v1.2.1-part1-overview.html

The most recent (and final) version of the TAXII 1 specifications is TAXII 1.1.1, the specifications can be found here: http://docs.oasis-open.org/cti/taxii/v1.1.1/taxii-v1.1.1-part1-overview.html
</div>

<div>
### Will there be any further revisions of STIX™ 1.2.1, CybOX™ 2.1.1, or TAXII™ 1.1.1? ###
No. The CTI TC community will be focusing on advancing STIX and TAXII 2+. However, OASIS rules ensure that all OASIS specifications are available in perpetuity and therefore STIX 1.2.1, CybOX 2.1.1, and TAXII 1.1.1 will remain available to anyone who wishes to use them.
</div>

<div>
### What is happening with all of the tools and APIs that MITRE built for STIX™ 1, CybOX™ 2, and TAXII™ 1? ###
The DHS-sponsored open-source tooling developed by MITRE will be maintained with bug and security fixes.
</div>

<div>
## STIX™ 2 Core Design Principles ##
</div>

<div>
### What are the core design principles of STIX™ 2? ###
- Flatter is better than nested
- Only one way to do something
- Focus on most used/needed use cases first - 80/20 rule
- Don’t reinvent the wheel - use other standards where possible
- It’s easier to add objects and properties than it is to take them away
- It's easier to make a required property optional later than to make an optional property required.
</div>

<div>
### What are the criteria for adding a new STIX™ Domain Object (SDO)? ###
SDOs are used to represent independent concepts. An item becomes an SDO when it is expected to evolve on its own outside the context of any other objects. In other cases, objects become SDOs when there are multiple relationships between it and other SDOs, when a third-party needs to add relationships to/from that SDO and other SDOs, and when you need to express confidence on the object separately from the other objects it might be embedded in.
</div>

<div>
### Why are some relationships "embedded" and others are "external"? ###
External relationships (represented using an SRO) are used whenever third-parties might want to add to the relationship and/or to express an independent confidence assertion on the relationship. For example, the relationship between an Indicator and a Malware object is represented as an external relationship because you might only be sure to a medium degree of confidence that the Indicator is effective in detecting the Malware without false-negatives.

Embedded relationships (represented using a property in an object with the ID of another object) are used when the relationship is a fact about the object. For example, the Producer that created an indicator is not up for debate; it's definitely from a particular Producer and they know that they created the SDO. Similarly, the contents of a Report are what they are. If later on it's determined that the Report should have different contents, it can be updated by the original Producer, but applying confidence or allowing third parties to arbitrarily add new objects to an existing Report doesn't make sense.
</div>

<div>
## Specific STIX™ 2 Design Decisions ##
</div>

<div>
### Why are IDs in UUIDv4 format vs UUIDv5? ###
First, to explain the differences between UUIDv4 and UUIDv5:

UUIDv4 is randomly generated, so each UUIDv4 ID is essentially just an ID that you can assign to any object you want.
UUIDv5 is a hash-based ID, where the ID is generated from the object that you want to ID.

STIX 2.1 introduced UUIDv5 for SCOs. STIX Domain Objects, STIX Relationship Objects, STIX Meta Objects, and STIX Bundle Object should continue to use UUIDv4.
</div>

<div>
### Why are timestamps in RFC3339 format instead of UNIX format? ###
The CTI TC had to pick one way of encoding timestamps. There was no lack of debate, but in the end, the community consensus settled on RFC3339.
</div>

<div>
### Why do timestamps have to be in UTC time? ###
Requiring that all timestamps be represented in UTC reduces ambiguity for consumers parsing STIX data. For STIX content producers, this has the additional benefit of one less thing they have to worry about from an interoperability perspective.
</div>

<div>
### Why are labels required on some objects and not others? ###
Labels (often referred to as “tags” in other contexts) are meant to help producers and consumers categorize objects. Labels are required on objects when there's a predefined vocabulary with suggested (not required) values to use for that object type. For example, the Report object has a predefined vocabulary and so labels are required, whereas Attack Pattern does not not have a predefined labels vocabulary and so in this case labels aren't required.
</div>

<div>
### Why does the Observed-Data object not have a name and description? ###
Observed Data will almost always be created and consumed by automated processes, and therefore there wasn't a strong need to add a name or description field. This can be revisited if a compelling use case emerges in future.
</div>

<div>
### Why can't Data Markings be versioned? ###
Data markings are applied to objects by referencing the ID of the data marking from the object. For example, to say a Campaign is marked with a copyright statement, the Campaign would have the ID of the Data Marking representing the copyright statement in its list of data markings (object_marking_refs). Because IDs are not specific to a single version of an object, the community felt that data markings should not be versionable. Making data markings versioned would allow producers to change the data markings and have that change automatically applied to any objects already referencing that marking.
</div>

<div>
### Why aren't Cyber Observables objects top-level objects? ###
There were several considerations that led to this decision. Unlike the other higher-level STIX Domain Objects (e.g,Threat Actor, Campaign, etc.), Cyber Observables are almost exclusively machine produced and therefore not intended to be globally unique. Accordingly, Cyber Observables do not have the same requirements as the SDOs in terms of needing capabilities such as versioning and confidence. In addition, given their nature as elements that provide supporting evidence to other SDOs such as Observed Data, Cyber Observables do not require the ability to support the creation of non-factual (i.e., asserted) relationships via the STIX Relationship Objects. These factors, and also the desire for a more streamlined data model (as having Cyber Observables as top-level objects would significantly increase the number of such objects in STIX), led to the decision to use Cyber Observables in an embedded form rather than making them top-level objects.

In STIX 2.1, STIX Cyber Observerable Objects were promoted to Core Objects. Previously, in STIX 2.0, Cyber-observable Objects could only exist as objects within an Observed Data object. It is still possible to represent Cyber-observable Objects in this way, but this method has been deprecated.
</div>

<div>
### Why are the IDs in the Cyber Observable container not just STIX IDs? ###
Cyber Observables are not globally unique and therefore need to be unique only to their respective container. Therefore, the decision was made to use a simplified, non-UUID ID structure for ease of use in terms of content creation and parsing.
</div>

<div>
### Why are there stub objects in STIX™ 2.0 and 2.1? ###
The stub objects in STIX 2.0 (COA and Malware) and STIX 2.1 (Incident) were designed to capture basic unstructured data and serve as a placeholder for future enhancements. For example, the Malware stub can be used to provide malware names and descriptions in STIX 2.0 (useful for high-level threat intel and IOC sharing) but does not have capabilities to represent malware analysis data. Marking them as stub objects was intended to clearly demonstrate that these objects are not complete (due to time and resource constraints) and will be enhanced in future releases of STIX. The Incident object is being prototyped as a STIX 2.1 Extension object and is available in the [CTI STIX Common Object repo](https://github.com/oasis-open/cti-stix-common-objects/tree/main/extension-definition-specifications/incident-core).
</div>

<div>
### What happened to TAXII channels? ###
During the planning of TAXII 2.0 the TC considered the inclusion of a channels feature to address the publish-subscribe use-case. However, the CTI TC decided to solve the major use-case of request-response first. The publish-subscribe use case was deferred to a later release.
</div>

<div>
### Why are Note and Opinion separate objects? ###
The TC had an extensive discussion on the topic, including a ballot, and concluded that the use cases were sufficiently different to warrant separate objects. While the Note and Opinion objects bear significant architectural similarity, the underlying semantics (driven by their respective use cases) were such that making them separate SDOs was the logical choice.

The Note object should be used to provide additional details or further analysis on an object. The Opinion object should be used to provide an opinion on the correctness of another object. Still wondering which to use? Do you want to provide a value on a scale from "strongly disagree" to "strongly disagree" about the object you're talking about? If so, use Opinion, if not, use Note.
</div>

<div>
### What is the TC’s stance on forward/backward compatibility? ###
The TC will make a best effort to avoid making either forwards or backwards-breaking changes in minor releases. That said, on occasion breaking changes may need to be made. For example, with stub objects the TC will more than likely make forward and backward-breaking changes, but these objects are marked as such and should not be considered stable. Other forward or backward breaking changes will be done carefully and only when the TC deems that the justification of doing so justifies the potential impact on implementers.
</div>

<div>
### Why are there fewer objects in STIX™ 2.0/Cyber Observables than there were in the previous versions? ###
The community focused on developing objects that saw significant usage in practice. Many CybOX objects were defined but never (or rarely) used.
</div>

<div>
### I was using CybOX™ <Object X> before, but now I can't find it, what should I do? ###
If you were using a CybOX object and it's not a part of STIX 2, let us know! Create the object as a STIX 2.1 Extension and submit it to the [CTI STIX Common Object repository](https://github.com/oasis-open/cti-stix-common-objects) to give it greater visibility.

If you're a TC member, post to the cti-cybox@lists.oasis-open.org list. If you're not, post to cti-comment@lists.oasis-open.org (instructions here: https://www.oasis-open.org/committees/comments/index.php?wg_abbrev=cti).
</div>

<div>
### Why is Location an SDO? ###
Location was made an SDO for several reasons:

- To allow for easily linking several locations to an object
- To provide confidence that a given object is at that location
- To allow third parties to provide information about a location for another object
- To allow for re-use of Location objects

</div>

<div>
### Why did the TC not use normative text to describe a material change in versioning? ###
The reason the TC selected this wording is because it is not possible to create formal definition of a "material change" based on STIX itself.

You can't base a material change based on the number of properties that have changed. There may not be a correlation between the number of properties changed and whether or not those changes are material. Since one can't create a formal definition for a material change based on STIX itself, it makes little sense to have a formal normative statement like MUST or SHOULD around its usage.
</div>
