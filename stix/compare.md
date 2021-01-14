---
layout: page
title: Comparing STIX 1.X/CybOX 2.X with STIX 2
short_title: Comparing STIX 1 and 2
categories: stix
---


## One Standard

First, the OASIS Cyber Threat Intelligence (CTI) Technical Committee (TC) decided to merge the two specifications into one. Cyber Observable eXpression (CybOX™) objects are now called STIX Cyber Observables.

Now when you discuss “STIX”, you are talking about the one standard needed for sharing cyber threat intelligence!

## JSON vs. XML

STIX 2.x requires implementations to [support JSON serialization](https://docs.oasis-open.org/cti/stix/v2.1/cs01/stix-v2.1-cs01.html#_vj2dopx186bb), while STIX 1.x was defined using XML. Though both XML and JSON have benefits, the CTI TC determined that JSON was more lightweight, and sufficient to express the semantics of cyber threat intelligence information. It is simpler to use and increasingly preferred by developers.

## STIX Domain Objects

All objects in STIX 2.x are [at the top-level](https://docs.oasis-open.org/cti/stix/v2.1/cs01/stix-v2.1-cs01.html#_1j0vun2r7rgb), rather than being embedded in other objects. These objects are called STIX Domain Objects (SDO). Some object properties use a reference to another object’s id directly (e.g., created\_by\_ref), but most relationships are expressed using the top-level Relationship object.

The generic TTP (tactics, techniques, procedures) and Exploit Target types from STIX 1.X have been split into separate top-level objects (Attack Pattern, Malware, Tool and Vulnerability) with specific purposes in STIX 2.

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

## Relationships as Top-Level Objects

STIX 2.x introduces a top-level [Relationship object](https://docs.oasis-open.org/cti/stix/v2.1/cs01/stix-v2.1-cs01.html#_o3xe01pbsgzj), which links two other top-level objects via a named relationship type. STIX 2.x content can be thought of as a connected graph, where nodes are SDOs and edges are Relationship Objects. The STIX 2.x specification suggests different named relationships, but content producers are able to define their own. In STIX 1.X relationships were “embedded” in other objects. The types of relationships supported was restricted by the STIX 1.X specification. Because STIX 1.X relationships themselves were not top-level objects, you could not express a relationship between two objects without changing one of them. In CTI, it is often desirable for others to assert a relationship. Using this new Relationship object, others, besides the original content creator, can add to the shared knowledge in an independent way.

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

## Streamlined Model

Experience with STIX 1.X showed that a common set of features were widely used and well understood while many other features lacked shared understanding and had only limited, if any use at all. In addition, almost all properties of objects were optional. Overall, the breadth of STIX 1.x was an impediment to sharing intelligence, and necessitated a formal agreement among threat groups on what should be shared (i.e., profiles).

STIX 2 takes a different approach – many properties are required, and the number of objects and properties have been reduced to a core set of well understood features. Future releases of STIX will incorporate additional concepts as they are needed.

However, the need to incorporate concepts not yet in the specification is enabled through the ability to use custom properties and custom objects.

## Data Markings

[Data markings](https://docs.oasis-open.org/cti/stix/v2.1/cs01/stix-v2.1-cs01.html#_95gfoglikdzh) no longer use a serialization specific language, e.g., XPath. In STIX 2.x, there are two types of data markings: object marking – applicable to a whole object, and granular markings – applicable to a property or properties of an object. Data markings scope is only within the object where they are defined.

## Indicator Pattern Language

Indicator patterns in STIX 1.x were expressed using XML syntax. This made all but the simplest patterns difficult to create and to understand. STIX 2.x takes a different approach, specifying [a language for patterns](https://docs.oasis-open.org/cti/stix/v2.1/cs01/stix-v2.1-cs01.html#_e8slinrhxcc9) which is independent of the serialization language. Patterns written in the STIX patterning language are more compact and easier to read. Additionally, there is no confusion between patterns and observations, because a pattern is not a top-level object, but a property of an indicator object.

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
