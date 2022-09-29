---
layout: page
title: Comparing STIX 1.X/CybOX 2.X with STIX 2
short_title: Comparing STIX 1 and 2
categories: stix
---

## The Transition to STIX™/TAXII™ 2 ##

### Why were new versions of STIX™ and TAXII™ created? ###

While STIX and TAXII 1 have been widely adopted and deployed around the world by operational sharing communities, the CTI TC recognized that these specifications were difficult to implement. The primary sources of that difficulty were excessive complexity in certain advanced XML constructs (e.g., XSI types) and the choice of XML as a representation. The community also learned that having multiple ways of doing things and excessive optionality in the data model led to differences in data-modelling and challenges in interoperability. As a result the CTI TC decided to rework the data model and serialization for STIX 2. Similarly, armed with the lessons learned over the years the community made the decision to rework TAXII as an HTTP Representational State Transfer (RESTful) based design.

### One Standard ###

In 2016, the OASIS Cyber Threat Intelligence (CTI) Technical Committee (TC) decided to merge the two specifications into one. Cyber Observable eXpression (CybOX™) objects are now called STIX Cyber Observables.

Now when you discuss “STIX”, you are talking about the one standard needed for sharing cyber threat intelligence!

## STIX™ 1 vs STIX™ 2 FAQ


### What are the key differences between STIX™ 1 and STIX™ 2? ###

- JSON vs. XML

Whereas STIX 1 was serialized using eXtensible Mark-up Language (XML), STIX 2 specifies JavaScript Object Notation (JSON) as the “Mandatory To Implement” (MTI) serialization, i.e. it requires implementations to, at a minimum, [support JSON serialization](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_vj2dopx186bb). Though both XML and JSON have their own benefits, the CTI TC determined that JSON was more lightweight, preferred by most developers, and easier to understand while being sufficient to express the semantics of STIX.

- STIX™ Domain Objects

STIX 1 allowed certain objects to be defined within other objects (e.g., a TTP could be defined within an Indicator) in addition to being defined outside any other object (i.e., at the “top-level” of a STIX document). In STIX 2, all objects in STIX 2.x are [at the top-level](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_nrhq5e9nylke), rather than being embedded in other objects. This change simplifies the parsing and storage of STIX 2 objects.

During the development of the STIX 2 SDOs the community felt that the generic TTP object (tactics, techniques, procedures) and Exploit Target object from STIX 1 were semantically-overloaded, so these have been split into separate top-level objects (Attack Pattern, Malware, Tool and Vulnerability) with a tighter focus on their respective use-cases in STIX 2.

**Note**: The IDs in these examples have been simplified to them easier to read. STIX 2 requires that IDs contain UUIDs after the `--`.

<div class="row">
<div class="col-md-7" markdown="1">
{:.text-center}
### STIX 1 Sample Object

```xml
<stix:TTPs>
 <stix:TTP id="attack-pattern:ttp-01" xsi:type='ttp:TTPType'
           version="1.1">
   <ttp:Title>Initial Compromise</ttp:Title>
    <ttp:Behavior>
     <ttp:Attack_Patterns>
      <ttp:Attack_Pattern capec_id="CAPEC-163">
       <ttp:Description>Spear Phishing</ttp:Description>
        </ttp:Attack_Pattern>
      </ttp:Attack_Patterns>
    </ttp:Behavior>
 </stix:TTP>
</stix:TTPs>
<stix:TTPs>
 <stix:Kill_Chains>
  <stixCommon:Kill_Chain id="stix:TTP-02"
                         name="mandiant-attack-lifecycle-model">
  <stixCommon:Kill_Chain_Phase name="initial-compromise"
                               phase_id="stix:TTP-03"/>
 </stix:Kill_Chains>
</stix:TTPs>
```
</div>

<div class="col-md-5" markdown="1">
{:.text-center}
### STIX 2 Sample SDO

```json
{
    "type": "attack-pattern",

    "id": "attack-pattern--01",
    "spec_version": "2.1",
    "created": "2015-05-15T09:11:12.515Z",
    "modified": "2015-05-15T09:11:12.515Z",
    "name": "Initial Compromise",
    "external_references": [
      {
        "source_name": "capec",
        "description": "spear phishing",
        "external_id": "CAPEC-163"
      }
    ],
    "kill_chain_phases": [
      {
        "kill_chain_name": "mandiant-attack-lifecycle-model",
        "phase_name": "initial-compromise"
      }
    ]
   }
```
</div>
</div>

- STIX™ Cyber-observable Objects
 
STIX 2.1 defines cyber observable object at the top-level, as opposed to STIX 1 and 2.0. In STIX 1, every CybOX object needed to be wrapped in an Observable object.  Similarly in STIX 2.0, a cyber observable needed to be wrapped in an Observed Data object.  This made it difficult to defined a cyber observable just once (e.g., an IPv4 address) and use it in many different contexts. This is possible with the introduction of [STIX Cyber-Observable Objects (SCOs)](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_mlbmudhl16lr).
 
**Note**: The IDs in these examples have been simplified to them easier to read. STIX 2 requires that IDs contain UUIDs after the `--`.

<div class="row">
<div class="col-md-7" markdown="1">
{:.text-center}
### STIX 1 Sample Object

```xml
<cybox:Observable id="stix:observable-01">
            <cybox:Title>IP: 219.90.112.203</cybox:Title>
            <cybox:Object id="stix:object-02">
                <cybox:Properties category="ipv4-addr" xsi:type="AddressObj:AddressObjectType">
                    <AddressObj:Address_Value condition="Equals">219.90.112.203</AddressObj:Address_Value>
             </cybox:Properties>
            </cybox:Object>
        </cybox:Observable>
```
</div>

<div class="col-md-5" markdown="1">
{:.text-center}
### STIX 2 Sample SCO

```json
{
            "id": "ipv4-addr--02",
            "type": "ipv4-addr",
            "value": "219.90.112.203"
        }
```
</div>
</div>

There are fewer objects in STIX™ 2 than in CybOX 2.1.  For STIX 2, the community focused on developing objects that saw significant usage in practice. Many CybOX objects were defined but never (or rarely) used.  If there is a need for additional SCOs, they can be added in a future release.

### I was using CybOX™ <Object X> before, but now I can't find it, what should I do? ###

If you were using a CybOX object and it's not a part of STIX 2, let us know! Create the object as a STIX 2.1 Extension and submit it to the [CTI STIX Common Object repository](https://github.com/oasis-open/cti-stix-common-objects) to give it greater visibility.

If you're a TC member, post to the cti-cybox@lists.oasis-open.org list. If you're not, post to cti-comment@lists.oasis-open.org (instructions here: https://www.oasis-open.org/committees/comments/index.php?wg_abbrev=cti).

- Relationships as Top-Level Objects

STIX 2 introduces a top-level [STIX Relationship Object (SRO)](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_cqhkqvhnlgfh), which links two other top-level objects via a named relationship type. The STIX 2 data-model was designed to be a connected graph, wherein nodes are SDOs (or SCOs) and edges are SROs. The STIX 2 specification includes a default set of named relationships, but content producers are also able to define their own relationships. In contrast, STIX 1 defined relationships as properties that were “embedded” in other objects. The types of relationships supported were restricted by the STIX 1 specification. Accordingly, because STIX 1 relationships themselves were not top-level objects, you could not express a relationship between two objects without changing one of them. As only the creator of an SDO is allowed to make changes to it, this effectively prevented “third-party” relationships, where an entity other than the creator of one or both of the objects asserts a relationship between them. In the workflows around CTI, it is often desirable for others to assert a relationship; for example, a threat analyst might want to assert a relationship between an indicator and a threat actor even though the analyst was not the original creator of either object. Using the new graph-based STIX data-model in STIX 2, others (i.e., not just the original content creator) can define new relationships between entities in order to add to the shared knowledge. The following graphic shows an illustration of this for the Indicator SDO.

![STIX Illustration of Indicator Relationships]({{ site.baseurl }}/img/stix2-indicator-diagram-72dpi-v1.png){: .figure-img .img-fluid}

<div class="col-md-offset-3 col-md-6" markdown="1">
{:.text-center}
### Sample Relationship

```json
{
    "type": "relationship",
    "id": "relationship--01",
    "spec_version": "2.1",
    "created": "2017-02-09T11:13:27.431Z",
    "modified": "2017-02-09T11:13:27.431Z",
    "relationship_type": "uses",
    "source_ref": "attack-pattern--03",
    "target_ref": "tool--04"
 }
```
</div>
<div class="center-block text-center about-fig" markdown="span">
![STIX 2 Diagram 3]({{ site.baseurl }}/img/NewSTIXdiagram3.PNG)
**Attack Pattern SDO that "Uses" a Tool SDO**
</div>

- Streamlined Model

Experience with STIX 1 showed that a common subset of capabilities were widely-used and well-understood while many others were problematic, poorly-understood, and in many cases never used. In addition, almost all object properties in STIX 1 were optional, presenting significant parsing challenges for consumers of STIX 1 content. At a high-level, the breadth of capabilities and multiple ways of representing semantically identical content in STIX 1 was an impediment to interoperable sharing of CTI, leading sharing communities to formally define how different types of CTI would be represented via STIX 1 Profiles.

STIX 2 takes a radically different approach. Many more properties are required, and the number of objects and properties have been reduced to a core set of well-understood features, modeled in such a way as to eliminate the problem of multiple ways of encoding semantically-equivalent CTI. Future releases of STIX will incorporate additional concepts as they are needed.

It is understood that certain communities will need to exchange data not defined within the STIX 2 specification. This need is addressed via the ability to use [extensions defintions](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_32j232tfvtly) Note: using custom objects and properties in STIX 2 has been deprecated.

- Data Markings

As part of the move from XML to JSON, [data markings](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_95gfoglikdzh) no longer use XPath. In STIX 2, there are two types of data markings: object markings – applicable to an entire object, and granular markings – applicable to one or more object properties within a single object. In order to clarify the semantics of markings, all objects must be marked individually - there is no inheritance of markings in STIX 2.

- STIX™ Patterning Language

Indicator patterns in STIX 1 were an area where the "many ways of expressing semantically-equivalent content" problem was particularly manifested. As a result, for a consumer of STIX 1 content, rigorously parsing all but the simplest patterns was unnecessarily difficult. STIX 2 takes a radically different approach by defining a human-readable, SQL-like Indicator [Patterning Language](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_e8slinrhxcc9), which is independent of the serialization language. Indicator patterns in STIX 1.x were expressed using XML syntax. This made all but the simplest patterns difficult to create and to understand. As a result, patterns written in the STIX Patterning Language are more compact and far easier to read.

<div class="row">
<div class="col-md-7" markdown="1">
{:.text-center}
### STIX 1 Indicator Example

```xml
<stix:Indicator id="example:indicator-01"
                timestamp="2017-02-09T12:11:11.415000+00:00"
                xsi:type='indicator:IndicatorType'>
 <indicator:Title>HTRAN Hop Point Accessor</indicator:Title>
</stix:Indicator>
<stix:TTPs>
 <stix:Kill_Chains>
  <stixCommon:Kill_Chain id="stix:TTP-02"
                         name="mandiant-attack-lifecycle-model">
  <stixCommon:Kill_Chain_Phase name="establish-foothold"
                               phase_id="stix:TTP-03"/>
 </stix:Kill_Chains>
</stix:TTPs>
<indicator:Observable id="example:Observable-04">
 <cybox:Object id="example:Object-05">
  <cybox:Properties xsi:type="AddressObj:AddressObjectType"
                    category="ipv4-addr">
  <AddressObj:Address_Value condition="Equals">10.1.0.0/15
  </AddressObj:Address_Value>
 </cybox:Object>
</indicator:Observable>
```
</div>

<div class="col-md-5" markdown="1">
{:.text-center}
### STIX 2 Indicator Example with Pattern

```json
  {
    "type": "indicator",
    "id": "indicator--01",
    "spec_version": "2.1",
    "created": "2017-02-09T12:11:11.415Z",
    "modified": "2017-02-09T12:11:11.415Z",
    "name": "HTRAN Hop Point Accessor",
    "pattern": "[ipv4-addr:value = '10.1.0.0/15']",
    "valid_from": "2015-05-15T09:00:00.000Z",
    "indicator_types": ["malicious-activity"],
    "pattern_type": "stix",
    "kill_chain_phases": [
      {
        "kill_chain_name":
          "mandiant-attack-lifecycle-model",
        "phase_name": "establish-foothold"
      }
    ]
   }
```
</div>
</div>

- Observations vs. Patterns

In STIX 1, the duality between Observations and Patterns (i.e., a pattern was essentially an observation with an operator) was a point of confusion for many end users. STIX 2 resolves this issue by having a separate pattern construct that uses its own language (see above) and is a property of an Indicator object instead of a top-level object. Accordingly, there is no semantic overlap in STIX 2 between the specification of observations using the Observed Data object and patterns via the Indicator object, as these entities were designed to be distinct.

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


### STIX™ 1 had XML Namespaces. Is there something similar in STIX™ 2? ###

STIX 1 made use of XML namespaces for two purposes:

- Individual elements and attributes were namespaced to separate out elements from one object type (e.g., indicator) from those of another type (e.g., incident).
- Namespaces in the "id" field were used to indicate the producer of the STIX object.
While it is common practice for XML content to make use of namespaces, most JSON content does not. For this reason STIX 2 does not use namespaces. For more reasoning on this, see: https://www.mnot.net/blog/2011/10/12/thinking_about_namespaces_in_json

STIX 2 uses a property, created_by_ref, to replace the second usage of namespaces. In other words, in STIX 1 you would examine the namespace of an ID attribute value on an object to determine who created it, while in STIX 2 you look in the created_by_ref property.

### What happened to CybOX™? ###

During the design and development of STIX 2, the CTI TC concluded that due to the tightly-coupled nature of STIX and the Cyber Observable eXpression (CybOX) language that CybOX should be merged into STIX. These objects are now characterized as Cyber Observable objects within STIX and are defined in the STIX specification.

The TC felt that it would be easier for the market to understand and adopt STIX if it was a single standard. This consolidation eliminated the need for a complex interoperability matrix between the two standards.

### What are the key differences between TAXII™ 1 and TAXII™ 2? ###

- HTTPS as the Transport Protocol

TAXII 1 was designed to the TAXII application protocol to be hosted on top of multiple underlying transport protocols. While, in theory this seemed like a good design choice, in practice TAXII 1 was only ever implemented (to our knowledge) on top of HTTP. Because the TAXII 1 protocol could not assume any particular underlying transport, this required that TAXII reimplement features and capabilities that were already provided by HTTP. In contrast, TAXII 2 is explicitly designed to serve as an application layer protocol on top of HTTPS and as such can rely on the full set of services provided by HTTPS implementations. The result is that the TAXII 2 protocol is smaller and simpler and should prove to be much easier to implement.

- RESTful Interface

TAXII 2 provides a RESTful interface to data and services. RESTful is an architectural style for networked hypermedia applications; it is primarily used to build Web services that are lightweight, maintainable, and scalable. RESTful is not dependent on any protocol, but almost every RESTful service uses HTTP as its underlying protocol. As is noted above, TAXII 2 is built on top of HTTPS the secure HTTP analogue.

### Are there tools to help me migrate between STIX™ 1 and STIX™ 2? ###

Yes. The [STIX Elevator](https://github.com/oasis-open/cti-stix-elevator) does a best-effort conversion of STIX 1 content into STIX 2. The [STIX Slider](https://github.com/oasis-open/cti-stix-elevator) converts STIX 2 to STIX 1.

### What are the latest versions of STIX™ and TAXII™ 1? ###

The most recent (and final) version of the STIX 1 specifications is STIX 1.2.1, the specifications can be found here: http://docs.oasis-open.org/cti/stix/v1.2.1/stix-v1.2.1-part1-overview.html

The most recent (and final) version of the TAXII 1 specifications is TAXII 1.1.1, the specifications can be found here: http://docs.oasis-open.org/cti/taxii/v1.1.1/taxii-v1.1.1-part1-overview.html

### Will there be any further revisions of STIX™ 1.2.1, CybOX™ 2.1.1, or TAXII™ 1.1.1? ###

No. The CTI TC community will be focusing on advancing STIX and TAXII 2+. However, OASIS rules ensure that all OASIS specifications are available in perpetuity and therefore STIX 1.2.1, CybOX 2.1.1, and TAXII 1.1.1 will remain available to anyone who wishes to use them.

### What is happening with all of the tools and APIs that MITRE built for STIX™ 1, CybOX™ 2, and TAXII™ 1? ###

The tools and APIs that MITRE built for STIX™ 1, CybOX™ 2, and TAXII™ 1 remain available on Github, but have been deemed end-of-life. Users are encouraged to update to STIX 2.1. In case of a small bug fix or emergency security update, MITRE may update the tools at their discretion. Please contact MITRE directly for assistance.
 
