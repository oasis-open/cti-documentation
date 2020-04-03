---
layout: page
title: Introduction to TAXII
categories: taxii
---

Trusted Automated Exchange of Intelligence Information (TAXII™) is an application protocol for exchanging CTI over HTTPS. ​TAXII defines a RESTful API (a set of services and message exchanges) and a set of requirements for TAXII Clients and Servers. As depicted below, TAXII defines two primary services to support a variety of common sharing models:

-   **Collection** - A Collection is an interface to a logical repository of CTI objects provided by a TAXII Server that allows a producer to host a set of CTI data that can be requested by consumers: TAXII Clients and Servers exchange information in a request-response model.

-   **Channel** - Maintained by a TAXII Server, a Channel allows producers to push data to many consumers and consumers to receive data from many producers: TAXII Clients exchange information with other TAXII Clients in a publish-subscribe model. Note: The TAXII 2.1 specification reserves the keywords required for Channels but does not specify Channel services. Channels and their services will be defined in a later version of TAXII.

<div class="center-block text-center" markdown="span">
![TAXII Collections and Channels]({{ site.baseurl }}/img/taxii_diagram2.png)
</div>

Collections and Channels can be organized in different ways. For example, they can be grouped to support the needs of a particular trust group.

A TAXII server instance can support one or more API Roots. API Roots are logical groupings of TAXII Channels and Collections and can be thought of as instances of the TAXII API available at different URLs, where each API Root is the "root" URL of that particular instance of the TAXII API.

TAXII relies on existing protocols when possible. In particular, TAXII Servers are discovered within a network via DNS Service records (and/or by a Discovery Endpoint, described in the next section). In addition, TAXII uses HTTPS as the transport for all communications, and it uses HTTP for content negotiation and authentication.

TAXII was specifically designed to support the exchange of CTI represented in STIX, and support for exchanging STIX 2.1 content is mandatory to implement. However, TAXII can also be used to share data in other formats. It is important to note that STIX and TAXII are independent standards: the structures and serializations of STIX do not rely on any specific transport mechanism, and TAXII can be used to transport non-STIX data.

TAXII design principles include minimizing operational changes needed for adoption; easy integration with existing sharing agreements, and support for all widely used threat sharing models: hub-and-spoke, peer-to-peer, source-subscriber.

## What's New in TAXII 2.1
TAXII 2.1 differs from TAXII 2.0 in the following ways:
 
* The DNS SRV record was changed from taxii to taxii2
* The discovery URL was changed from /taxii/ to /taxii2/
* The Manifest Resource was changed to represent individual versions of an object, instead of an object with all of its versions
* Item based pagination was removed from this version of the specification
* The section on content negotiation was updated
* The media types were changed throughout the document
* Clarification was added to say that API Roots can be relative paths as well as absolute paths
* Changed version value in API Roots to match media type
* Changed status resource to allow status on success and pending
* Add TAXII media type as Accept type in 5.4 and 5.6 since a TAXII error message could be returned
* HTTP Basic is now a SHOULD implement for the Server
* Added a DELETE object by ID endpoint
* Added a versions endpoint for object by ID.
* Added section on Server Implementation Considerations
* Added a limit URL parameter
* Added a next URL parameter
* Added a spec_versions match filter parameter
* Removed STIX media types and STIX Bundle and replaced with TAXII Envelope
* Added clarifying text around TAXII timestamps needing millisecond precision
* Cleaned up and deemphasized text around support for content other than STIX
* Added user-agent HTTP header description

### [TAXII 2.1 Specification Document]({{ site.baseurl }}/resources.html#taxii-21-specification)
