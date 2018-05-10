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

STIX 2.0 requires implementations to [support JSON serialization](https://docs.google.com/document/d/1dIrh1Lp3KAjEMm8o2VzAmuV0Peu-jt9aAh1IHrjAroM/pub#h.vj2dopx186bb), while STIX 1.x was defined using XML. Though both XML and JSON have benefits, the CTI TC determined that JSON was more lightweight, and sufficient to express the semantics of cyber threat intelligence information. It is simpler to use and increasingly preferred by developers.

## STIX Domain Objects

All objects in STIX 2 are [at the top-level](https://docs.google.com/document/d/1dIrh1Lp3KAjEMm8o2VzAmuV0Peu-jt9aAh1IHrjAroM/pub#h.1j0vun2r7rgb), rather than being embedded in other objects. These objects are called STIX Domain Objects (SDO). Some object properties use a reference to another object’s id directly (e.g., created\_by\_ref), but most relationships are expressed using the top-level Relationship object.

The generic TTP (tactics, techniques, procedures) and Exploit Target types from STIX 1.X have been split into separate top-level objects (Attack Pattern, Malware, Tool and Vulnerability) with specific purposes in STIX 2.

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
      "kill_chain_name": "mandiant-attack-
                          lifecycle-model",
      "phase_name": "initial-compromise"
    }
  ]
 }
```
</div>
</div>

## Relationships as Top-Level Objects

STIX 2.0 introduces a top-level [Relationship object](https://docs.google.com/document/d/1dIrh1Lp3KAjEMm8o2VzAmuV0Peu-jt9aAh1IHrjAroM/pub#h.l326yout8qc1), which links two other top-level objects via a named relationship type. STIX 2 content can be thought of as a connected graph, where nodes are SDOs and edges are Relationship Objects. The STIX 2 specification suggests different named relationships, but content producers are able to define their own. In STIX 1.X relationships were “embedded” in other objects. The types of relationships supported was restricted by the STIX 1.X specification. Because STIX 1.X relationships themselves were not top-level objects, you could not express a relationship between two objects without changing one of them. In CTI, it is often desirable for others to assert a relationship. Using this new Relationship object, others, besides the original content creator, can add to the shared knowledge in an independent way.

<div class="col-md-offset-3 col-md-6" markdown="1">
{:.text-center}
### Sample Relationship

```json
 {
    "type": "relationship",
    "id": "relationship--01",
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

[Data markings](https://docs.google.com/document/d/1dIrh1Lp3KAjEMm8o2VzAmuV0Peu-jt9aAh1IHrjAroM/pub#h.j0uqagkk6m9n) no longer use a serialization specific language, e.g., XPath. In STIX 2, there are two types of data markings: object marking – applicable to a whole object, and granular markings – applicable to a property or properties of an object. Data markings scope is only within the object where they are defined.

## Indicator Pattern Language

Indicator patterns in STIX 1.x were expressed using XML syntax. This made all but the simplest patterns difficult to create and to understand. STIX 2.0 takes a different approach, specifying [a language for patterns](https://docs.google.com/document/d/1nK1RXcE2aMvQoG1Kgr3aTBtHZ1IyehzOk7vU0n5FUGY/pub) which is independent of the serialization language. Patterns written in the STIX patterning language are more compact and easier to read. Additionally, there is no confusion between patterns and observations, because a pattern is not a top-level object, but a property of an indicator object.

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
  "created": "2017-02-09T12:11:11.415Z",
  "modified": "2017-02-09T12:11:11.415Z",
  "name": "HTRAN Hop Point Accessor",
  "pattern": "[ipv4-addr:value = 
                      '10.1.0.0/15']",
  "labels": [ "malicious-activity" ],
  "valid_from": "2015-05-15T09:00:00.000000Z",
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

## Coming Attractions

STIX 2.0 establishes a foundation for future development with the intent to add several new SDOs and develop support for other critical CTI concepts. A small number of minor revisions will be developed over the coming months to iteratively mature STIX 2. By establishing a foundation that supports the most critical CTI sharing use cases, the CTI TC hopes to gain critical feedback and implementation experience early while also allowing future development of STIX to be more focused on a smaller set of selected topics. Work on STIX 2.1 is already underway with concepts such as incidents, confidence, internationalization, and malware under active development. At the same time organizations are actively building capabilities that utilize STIX 2.0.
