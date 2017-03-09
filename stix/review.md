---
layout: page
title: STIX Review
categories: stix
hide_title: true
---

STIX 2.0 Public Review – Frequently Asked Questions
===================================================

Why STIX 2.0?
--------------

STIX has been very successful in many ways: it has demonstrated that machine-readable cyber threat intelligence can be widely shared and used operationally. Both commercial and government threat intelligence feeds provide it and many threat intelligence tools produce and/or consume it.

As with anything, however, in developing and implementing STIX 1.x the community (both vendors and consumers) have found that it also had some shortcomings. These included excessive complexity and excessive flexibility. In addition, STIX 1.x used XML, which has fallen out of favor with much of the developer community.

STIX 2 is a redesign of STIX that has the same goals and builds on the same foundational concepts but in a way that addresses those shortcomings. It is not backwards-compatible but is intended to be a replacement for STIX 1.x.

STIX 2.0 is the first release of STIX 2 and is intended to be a framework on which future capabilities can be built. In fact, while STIX 2.0 is currently under review, the community is already working on additional capabilities to add in STIX 2.1. All of the releases in the STIX 2 series will build on each other such that upgrading from one version to the next should be easy (unlike the change from STIX 1 to STIX 2).

STIX 2.0 also represents a shift in governance to a standards body: STIX 1.x was developed and published on behalf of the United States Department of Homeland Security (DHS) by MITRE (a U.S. government funded research lab). In 2015, DHS transitioned governance of STIX (and TAXII) to OASIS, an international consensus standards body. STIX 2.0 was developed and published by the OASIS Cyber Threat Intelligence Technical Committee (CTI TC), with participants from across the public and private sectors, vendors and end user organizations from around the world.

What happened to CybOX?
-----------------------

One of the lessons learned in STIX 1.x and CybOX 2.x was that having and talking about two separate specifications was clunky. It made it harder to explain and harder to write and release software due to the various version interdependencies. To address this, the CTI TC voted to merge CybOX into STIX as “STIX Cyber Observables”. The STIX specification was split into 5 separate documents, two of which (parts 3 and 4) describe “STIX Cyber Observables”.

What else changed between STIX 1 and STIX 2?
--------------------------------------------

Several major design decisions were made:

1.  While STIX 1.x is XML, STIX 2.0 is JSON. Specifically, the STIX 2.0 Mandatory-To-Implement (MTI) representation is JSON – all conforming implementations of STIX must support the JSON representation at a minimum. Other representations of STIX 2 are permitted, but to date, none have been defined.

2.  STIX 1.x has 9 top-level objects, some of which were fairly broad in scope. STIX 2.0 has 14 top-level objects but each of them is much more focused.

3.  STIX 1.x was intended to be extremely flexible, with a lot of optionality. STIX 2.0 focuses on standardizing a minimal baseline to improve compatibility.

4.  While STIX 1.x was designed as a graph, the STIX 2.0 data model more explicitly aligns with graph structures (as nodes and edges, what STIX 2.0 calls STIX Domain Objects and STIX Relationship Objects).

STIX 2.0 is described as a “minimally viable product” (MVP). What does “minimally viable product” really mean?
--------------------------------------------------------------------------------------------------------------

To focus on creating a successful interchange specification for the most critical use cases – primarily indicator exchange and basic threat intelligence sharing - the CTI TC maintained a strict scope for STIX 2.0. Borrowing the “agile” approach from software development, STIX 2.0 supports those essential use cases while also creating a framework from which to extend to support the more advanced use cases. As products begin to implement STIX 2.0, actual use will reveal enhancements that can be added to future iterations of STIX 2.

This does mean, however, that some features of STIX 1.x or CybOX 2.x are *not* included in STIX 2.0. Some of those features (for example, malware) are stubs in 2.0 that will be expanded in 2.1. Other features (for example, Incident) were completely deferred to STIX 2.1 or a later release.

Keep in mind that STIX 2 is a consensus specification and relies on broad input. If there’s a feature you think STIX should include, please consider [joining the TC](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cti) to help us develop it.

What is planned for STIX 2.1?
-----------------------------

The CTI TC currently plans to add the following to STIX 2.1:

-   **Confidence** that a producer has in its data

-   the ability to represent text content across several languages (**Internationalization**)

-   expanded **Malware** and **Course of Action** objects, which are intentional stubs in 2.0

-   support for representing security **Incidents** and **Events**

-   an **Infrastructure** object representing external infrastructure leveraged in an attack

-   several new **Cyber Observable Objects**, such as hardware devices

-   **Opinion** and **Intel Note** objects, for representing agreement or additional notes on other producers’ intelligence

Additional features may be added based on input from TC members and the broader cyber threat intelligence community.

What should I be commenting on?
-------------------------------

You can comment on anything you want, but the technical committee is particularly interested in getting opinions on:

-   **Implementability**

    -   Does STIX 2.0 seem straightforward to implement?

    -   If you have a product or service doing cyber threat intelligence, does it seem like you could develop support for STIX 2 in it?

    -   Are there any changes that could be made to make implementation easier?

-   **Clarity**

    -   Are the descriptions and requirements clear and easy to understand?

    -   Are there any changes we could make to the text or to STIX itself that would improve clarity?

-   **Interoperability**

    -   Is the specification sufficient to permit interoperability between two independently-developed systems?

    -   Are there changes to the specifications that would improve compatibility or interoperability between products?

-   **Coverage:**

    -   Does STIX let you express what you need to express in the domain of cyber threat intelligence?

    -   Is it missing anything that you think needs to be included to meet the definition of “minimally viable product”?

    -   Keep in mind this is just the first release, and many things are already scheduled to be included in 2.1 and later releases.

How can I provide comments?
---------------------------

Please see the OASIS [public review landing page](https://www.oasis-open.org/committees/comments/index.php?wg_abbrev=cti) for instructions on how you can provide comments.

Do you have any more examples or other documentation?
-----------------------------------------------------

Yes! We hope the specification has enough examples and descriptive text to make it easy to understand (if it doesn’t, let us know!) but we also have additional documentation under development. In particular there’s a [walkthrough](walkthrough) and a [STIX 1.x vs. STIX 2.0 comparison](compare).

Does the Technical Community provide any tooling or utilities to work with STIX?
--------------------------------------------------------------------------------

Also yes! See the [open repos](resources) page for a listing.
