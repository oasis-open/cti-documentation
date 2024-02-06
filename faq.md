---
layout: page
title: FAQ
categories: FAQ
hide_title: true
---

Frequently Asked Questions
===================================================

<div class="faq-btn">

  <a class="btn btn-primary btn-spec" data-toggle="tooltip" title="Question Submission" target="_blank" href="https://www.oasis-open.org/committees/comments/index.php?wg_abbrev=cti">
    <span class="glyphicon glyphicon-envelope"></span> Question not found? Send it in!
  </a>
</div>

## General ##

### What is STIX? ###

STIX — the Structured Threat Information eXpression — is a language and serialization format used to exchange cyber threat intelligence (CTI). STIX enables organizations to share CTI with one another in a consistent and machine-readable manner, allowing security communities to better understand what computer-based attacks they are likely to see and to better prepare for and/or respond to those attacks faster and more effectively. STIX is designed to improve many different capabilities, such as collaborative threat analysis, automated threat exchange, automated detection and response, and more.

### What is TAXII? ###

TAXII — the Trusted Automated Exchange of Intelligence Information — is an application layer protocol for the communication of CTI in a simple and scalable manner over HTTPS. TAXII enables organizations to share CTI by defining a standard API that aligns with common sharing models. TAXII is specifically designed to support the exchange of CTI represented in STIX.

### Who controls STIX and TAXII? ###
The STIX and TAXII standards are governed by the OASIS Cyber Threat Intelligence Technical Committee (CTI TC). STIX and TAXII were created in 2012 under the auspices of the US Department of Homeland Security. In June of 2015, DHS licensed all of the intellectual property and trademarks associated with STIX and TAXII to OASIS, a nonprofit consortium that drives the development, convergence and adoption of open standards for the global information society.

### What are the current versions of STIX and TAXII? ###

In 2021, OASIS approved STIX 2.1 and TAXII 2.1 as OASIS Standards. See the [Resources]({{ site.baseurl }}/resources) page for links to the latest specs.

Looking for information about STIX 1?  See [The Transition to STIX/TAXII 2]({{ site.baseurl }}/stix/compare)

### Are there “real-world” examples of STIX 2 content I can look at? ###

There are two example threat reports in the [CTI STIX2 JSON Schemas repository](https://github.com/oasis-open/cti-stix2-json-schemas/tree/master/examples/threat-reports).

The [cti-common-objects repository](https://github.com/oasis-open/cti-stix-common-objects) contains many, many samples.

Many threat intelligence providers offer their intelligence in the STIX format.

Finally, there are several examples in the [Examples]({{ site.baseurl }}/stix/examples) section of this site.

### Are there APIs and Tools for STIX and TAXII 2? ###

Yes, see the Github repositories for the [CTI TC open repositories](https://github.com/oasis-open?utf8=%E2%9C%93&q=cti-&type=&language=).

The list of repositories on the [Resources]({{ site.baseurl }}/resources) page contains direct links to useful tools.

### How do I verify my software is STIX/TAXII 2 interoperable? ###

The Interoperability Subcommittee of the CTI TC has developed a 2-Part Committee Note that establishes a step-by-step guide to a self-certification process for various personas. Once a Producer of STIX feeds content, a vendor providing a Threat Intelligence Platform (TIP), a vendor providing a Security Incident and Event Management (SIEM) tool, a vendor that provides threat mitigation systems (TMS), or a vendor that provides threat detection systems (TDS) executes the steps outlined, demonstrates successful interoperability, and documents such, that supplier may submit a statement to OASIS testifying to the self-certification. We are using TMS to refer to tools such as firewalls and intrusion prevention systems. We are using TDS to refer to tools such as intrusion detection software and web proxies.

The self-certification process is intended to be policed by market forces. If a vendor or supplier self-certifies and is shown to be misrepresenting its products the OASIS Community will remove the vendor from the STIX/TAXII 2 compatible products list after verification of the claim.

The vendor or supplier will need to re-test the attested product and submit documentation as per the Interoperability Specification to once again achieve listing on the interoperability list.

See the [Resources]({{ site.baseurl }}/resources) page for direct links to the STIX and TAXII Interoperability specifications.

### I'm implementing STIX and/or TAXII 2 and I have a question about something in the specification. What should I do? ###
We have a very active and supportive community.  If you post your question on CTI Users List you will likely receive a response from one of our community members.

Email cti-users at lists.oasis-open.org or file an issue in the [CTI TC's repository](https://github.com/oasis-tcs/cti-stix2/issues) on Github.

## STIX 2 Core Design Principles ##

### What are the core design principles of STIX 2? ###

- Flatter is better than nested
- Only one way to do something
- Focus on most used/needed use cases first - 80/20 rule
- Don’t reinvent the wheel - use other standards where possible
- It’s easier to add objects and properties than it is to take them away
- It's easier to make a required property optional later than to make an optional property required.

### What are the criteria for adding a new STIX Domain Object (SDO)? ###
SDOs are used to represent independent concepts. An item becomes an SDO when it is expected to evolve on its own outside the context of any other objects. In other cases, objects become SDOs when there are multiple relationships between it and other SDOs, when a third-party needs to add relationships to/from that SDO and other SDOs, and when you need to express confidence on the object separately from the other objects it might be embedded in.

New SDOs should be proposed as extension objects and may be submitted to the CTI Common Objects repository for development and testing.

### Why are some relationships "embedded" and others are "external"? ###

External relationships (represented using an SRO) are used whenever third-parties might want to add to the relationship and/or to express an independent confidence assertion on the relationship. For example, the relationship between an Indicator and a Malware object is represented as an external relationship because you might only be sure to a medium degree of confidence that the Indicator is effective in detecting the Malware without false-negatives.

Embedded relationships (represented using a property in an object with the ID of another object) are used when the relationship is a fact about the object. For example, the Producer that created an indicator is not up for debate; it's definitely from a particular Producer and they know that they created the SDO. Similarly, the contents of a Report are what they are. If later on it's determined that the Report should have different contents, it can be updated by the original Producer, but applying confidence or allowing third parties to arbitrarily add new objects to an existing Report doesn't make sense.

## Specific STIX 2 Design Decisions ##

### When are IDs in UUIDv4 format vs UUIDv5? ###
First, to explain the differences between UUIDv4 and UUIDv5:

UUIDv4 is randomly generated, so each UUIDv4 ID is essentially just an ID that you can assign to any object you want.
UUIDv5 is a hash-based ID, where the ID is generated from the object that you want to ID.

UUIDv5s should be used for SCOs that do not vary between generating systems. For example, an IPv4 address should have a single UUIDv5-style identifier, so that IPv4 address objects do not proliferate for the same IP address. However, for IPv4 localhost you may wish to use UUIDv4.

STIX 2.1 introduced UUIDv5 for SCOs. STIX Domain Objects, STIX Relationship Objects, STIX Meta Objects, and STIX Bundle Object should continue to use UUIDv4. UUIDv5 could be used for SROs and SDOs as described in section 2.9 of the specification.

### Why are timestamps in RFC3339 format instead of UNIX format? ###

The CTI TC had to pick one way of encoding timestamps. There was no lack of debate, but in the end, the community consensus settled on RFC3339.

### Why do timestamps have to be in UTC time? ###

Requiring that all timestamps be represented in UTC reduces ambiguity for consumers parsing STIX data. For STIX content producers, this has the additional benefit of one less thing they have to worry about from an interoperability perspective.

### Why does the Observed-Data object not have a name and description? ###

Observed Data will almost always be created and consumed by automated processes, and therefore there wasn't a strong need to add a name or description field. This can be revisited if a compelling use case emerges in future.

### Why can't Data Markings be versioned? ###

Data markings are applied to objects by referencing the ID of the data marking from the object. For example, to say a Campaign is marked with a copyright statement, the Campaign would have the ID of the Data Marking representing the copyright statement in its list of data markings (object_marking_refs). Because IDs are not specific to a single version of an object, the community felt that data markings should not be versionable. Making data markings versioned would allow producers to change the data markings and have that change automatically applied to any objects already referencing that marking.

### Are Cyber Observables objects top-level objects? ###

IN STIX 2.0, they were not. There were several considerations that led to this decision. Unlike the other higher-level STIX Domain Objects (e.g,Threat Actor, Campaign, etc.), Cyber Observables are almost exclusively machine produced and therefore not intended to be globally unique. Accordingly, Cyber Observables do not have the same requirements as the SDOs in terms of needing capabilities such as versioning and confidence. In addition, given their nature as elements that provide supporting evidence to other SDOs such as Observed Data, Cyber Observables do not require the ability to support the creation of non-factual (i.e., asserted) relationships via the STIX Relationship Objects. These factors, and also the desire for a more streamlined data model (as having Cyber Observables as top-level objects would significantly increase the number of such objects in STIX), led to the decision to use Cyber Observables in an embedded form rather than making them top-level objects.

In STIX 2.1, after much discussion, STIX Cyber Observerable Objects (SCOs) were promoted to top-level objects. The STIX 2.0 specification made it difficult to defined a cyber observable just once (e.g., an IPv4 address) and use it in many different contexts.  Addtionally, as top-level objects, they can also be used in relationships, which was determed to be desirable.

It is still possible to represent Cyber-observable Objects using the method described for STIX 2.0, but this method has been deprecated.

### Why are there stub objects in STIX 2.0 and 2.1? ###

The stub objects in STIX 2.0 (COA and Malware) and STIX 2.1 (Incident) were designed to capture basic unstructured data and serve as a placeholder for future enhancements. For example, the Malware stub can be used to provide malware names and descriptions in STIX 2.0 (useful for high-level threat intel and IOC sharing) but does not have capabilities to represent malware analysis data. Marking them as stub objects was intended to clearly demonstrate that these objects are not complete (due to time and resource constraints) and will be enhanced in future releases of STIX.

The Incident object is being prototyped as a STIX 2.1 Extension object and is available in the [CTI STIX Common Object repo](https://github.com/oasis-open/cti-stix-common-objects/tree/main/extension-definition-specifications/incident-core).

### What happened to TAXII channels? ###

During the planning of TAXII the TC considered the inclusion of a channels feature to address the publish-subscribe use-case. However, the CTI TC decided to solve the major use-case of request-response first. The publish-subscribe use case was deferred to a later release.

### Why are Note and Opinion separate objects? ###

The TC had an extensive discussion on the topic, including a ballot, and concluded that the use cases were sufficiently different to warrant separate objects. While the Note and Opinion objects bear significant architectural similarity, the underlying semantics (driven by their respective use cases) were such that making them separate SDOs was the logical choice.

The Note object should be used to provide additional details or further analysis on an object. The Opinion object should be used to provide an opinion on the correctness of another object. Still wondering which to use? Do you want to provide a value on a scale from "strongly disagree" to "strongly disagree" about the object you're talking about? If so, use Opinion, if not, use Note.

### What is the TC’s stance on forward/backward compatibility? ###

The TC will make a best effort to avoid making either forwards or backwards-breaking changes in minor releases. That said, on occasion breaking changes may need to be made. For example, with stub objects the TC will more than likely make forward and backward-breaking changes, but these objects are marked as such and should not be considered stable. Other forward or backward breaking changes will be done carefully and only when the TC deems that the justification of doing so justifies the potential impact on implementers.

### Why is Location an SDO? ###

Location was made an SDO for several reasons:

- To allow for easily linking several locations to an object
- To provide confidence that a given object is at that location
- To allow third parties to provide information about a location for another object
- To allow for re-use of Location objects

### Why did the TC not use normative text to describe a material change in versioning? ###

The reason the TC selected this wording is because it is not possible to create formal definition of a "material change" based on STIX itself.

You can't base a material change based on the number of properties that have changed. There may not be a correlation between the number of properties changed and whether or not those changes are material. Since one can't create a formal definition for a material change based on STIX itself, it makes little sense to have a formal normative statement like MUST or SHOULD around its usage.
