---
layout: page
title: Getting Started with STIX 2.0
categories: stix
---

## Overview

This guide provides information on several of the tools and resources available which can help you get started with STIX 2.0. Before getting started, it would be beneficial for you to have a basic understanding of STIX 2. Some of the most helpful information can be found here:

-   [About STIX](about)—Gives a general overview of STIX and the objects used in STIX 2.

-   [STIX Review](review)—Provides an FAQ-style review of STIX 2.0. Also, each part of the STIX 2.0 specification is located here.

-   [Comparing STIX 1 to STIX 2](compare)—If you’re familiar with STIX 1.x, this will help you get caught up on the key differences.

-   [Walkthrough](walkthrough)—Provides a practical use case for using STIX showing how organizations may share threat info using STIX 2.

-   [Examples and Tutorials](examples)—Focuses on other use cases and helps clarify certain objects while linking multiple concepts together. There are also threat report conversions and useful tutorial videos.

## JSON Schemas

One of the biggest changes between STIX 1.x and STIX 2.0 is the transition from XML to JSON. So before getting started with creating objects and properties, it may be helpful to have some knowledge of JSON. An introduction to JSON can be found at [www.json.org](http://www.json.org).

Prior to creating your STIX objects you may want to review the [JSON schemas]( https://github.com/oasis-open/cti-stix2-json-schemas) as well as the examples (see link above in the Overview section) to understand the properties for each object and the relationships among objects. The schemas were built to follow the STIX 2.0 specification and enforce several of the MUST requirements indicated in the spec. However, there are limits to what the schemas can enforce, so some requirements needed to be implemented with the Stix 2 validator tool (see next section). To understand the checks not enforced by the schemas, check out the README guide from the stix2-json-schemas repository on github.

A sample of how an object is structured can be seen below:

```
{
"$schema": "http://json-schema.org/draft-04/schema#",
"title": "attack-pattern",
"description": "Attack Patterns are a type of TTP that describe ways that adversaries attempt to compromise targets. ",
"type": "object",
"allOf": [
{
"$ref": "../common/core.json"
},
{
"properties": {
"type": {
"type": "string",
"description": "The type of this object, which MUST be the literal \`attack-pattern\`.",
"enum": ["attack-pattern"]
},
"id": {
"title": "id",
"pattern": "^attack-pattern--"
},
"name": {
"type": "string",
"description": "The name used to identify the Attack Pattern."
},
"description": {
"type": "string",
"description": "A description that provides more details and context about the Attack Pattern."
},
"kill_chain_phases": {
"type": "array",
"description": "The list of kill chain phases for which this attack pattern is used.",
"items": {
"$ref": "../common/kill-chain-phase.json"
},
"minItems": 1
}}}
],
"required": ["name"]
}

```

## STIX Validator

The [STIX validator](https://github.com/oasis-open/cti-stix-validator) tool is a useful resource for validating that STIX JSON content conforms to the 2.0 specification. It goes beyond what is checked in the schemas, and enforces MUST requirements the schemas cannot capture. Feel free to download this tool (instructions on github) in order to check that your created content abides by STIX 2 requirements.

## Pattern Validator

Another [validating tool](https://github.com/oasis-open/cti-pattern-validator) you can use helps check STIX [patterns](https://docs.google.com/document/d/1nK1RXcE2aMvQoG1Kgr3aTBtHZ1IyehzOk7vU0n5FUGY/pub). STIX patterns are expressions that represent Cyber Observable objects within a STIX Indicator SDO. They are helpful for modeling intelligence that indicates cyber activity. This tool simply makes sure patterning syntax adheres to the patterning expression. For instance, the pattern,

```
[file:hashes.'SHA-256' = 'ef537f25c895bfa782526529a9b63d97aa631564d5d789c2b765448c8635fb6c']
```

would pass the pattern validator tool whereas something like,

```
[file:hashes.'SHA-256'= 'example.exe']
```

would not. This tool can be used via command line or as a Python library.

## STIX Visualization

Since many of the relationships among STIX objects can be difficult to see by simply looking at a block of JSON, the STIX visualization tool is provided to help convert this JSON into a more concise, legible diagram. The visualization tool also reinforces the common comparison of STIX 2.0 to a graph with nodes and edges. It converts the SDOs into nodes and the SROs into the edges connecting each node. The tool is browser-based and also interactive, allowing you to drag nodes around to visualize the objects in different ways. By clicking on the nodes and edges, you can also obtain more information about the SDOs and SROs. There are several ways to upload JSON as well, including via file, copy and paste, or a link to a valid URL. A sample of this diagram can be seen below:

![STIX Viz Diagram]({{ site.baseurl }}/img/STIXdiagram4.png)

When clicking on the Malware SDO above (Poison Ivy Variant d1c6), the visualizer allows you to see the properties of that particular object:

![Viz Output]({{ site.baseurl }}/img/viz-output.png)

## STIX Elevator

If you are familiar with the first version of STIX, which was modeled using XML, you may have STIX 1.x content that you would like to convert to STIX 2.0. The [elevator](https://github.com/oasis-open/cti-stix-elevator) tool helps serve that purpose and will provide a best-effort conversion from 1.x to 2.0. There are limitations with this tool, as it cannot transform STIX 2.0 content into 1.x, and it makes some assumptions from the 1.x content that it needs to convert to 2.0. Nonetheless, it is a useful tool for transitioning your old STIX content into the new version.

For instance, putting this STIX 1.x XML content into the elevator (NOTE: STIX_Package information is truncated):
```xml
<stix:STIX_Package id="example:Package-8fab937e-b694-11e3-b71c-0800271e87d2" version="1.2">
<stix:Indicators>
<stix:Indicator id="example:Indicator-d81f86b9-975b-bc0b-775e-810c5ad45a4f" xsi:type="indicator:IndicatorType">
<indicator:Title>Malicious site hosting downloader</indicator:Title>
<indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.0">URL Watchlist</indicator:Type>
<indicator:Observable id="example:Observable-ee59c28e-d922-480e-9b7b-a79502696505">
<cybox:Object id="example:URI-b13ae3fc-80af-49c2-9de9-f713abc070ba">
<cybox:Properties xsi:type="URIObj:URIObjectType" type="URL">
<URIObj:Value condition="Equals">http://x4z9arb.cn/4712</URIObj:Value>
</cybox:Properties>
</cybox:Object>
</indicator:Observable>
</stix:Indicator>
</stix:Indicators>
</stix:STIX_Package>
```

Results in the following STIX 2.0 JSON output:
```
{
    "id": "bundle--8fab937e-b694-11e3-b71c-0800271e87d2",
    "objects": [
        {
            "created": "2017-09-26T10:36:01.961Z",
            "id": "indicator--d81f86b9-975b-bc0b-775e-810c5ad45a4f",
            "labels": [
                "url-watchlist"
            ],
            "modified": "2017-09-26T10:36:01.961Z",
            "name": "Malicious site hosting downloader",
            "pattern": "[url:value = 'http://x4z9arb.cn/4712']",
            "type": "indicator",
            "valid_from": "2017-09-26T10:36:01.961333Z"
        }
    ],
    "spec_version": "2.0",
    "type": "bundle"
}
```

## STIX Pattern Matcher
The [pattern matching](https://github.com/oasis-open/cti-pattern-matcher) tool provides a way for you to compare STIX Observed Data against STIX Indicator patterns. It’s useful for determining whether the observed data matches the pattern criteria. This allows you to make sure the indicator intelligence represents the observed data correctly. However, it is worth mentioning that this tool is currently a prototype.

## Python STIX 2 API

Finally, the STIX 2 API provides a variety of features and functionality for creating STIX 2.0 content. The [README]( https://github.com/oasis-open/cti-python-stix2\#cti-python-stix2) provides the best synopsis of the API, but a brief list of the functionality is included below:

-   Serializes/de-serializes JSON content

-   Data Marking

-   Versioning

-   Resolving STIX IDs across many sources

-   Creates SDOs, SROs, and bundles
