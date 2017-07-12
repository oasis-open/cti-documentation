import stix2

granular_red = stix2.GranularMarking(
        marking_ref=stix2.TLP_RED.id,
        selectors=["description"]
)

granular_amber = stix2.GranularMarking(
        marking_ref=stix2.TLP_AMBER.id,
        selectors=["labels.[1]"]
)

granular_green = stix2.GranularMarking(
        marking_ref=stix2.TLP_GREEN.id,
        selectors=["labels.[0]", "name", "pattern"]
)

identity = stix2.Identity(
    id="identity--b38dfe21-7477-40d1-aa90-5c8671ce51ca",
    created="2017-04-27T16:18:24.318Z",
    modified="2017-04-27T16:18:24.318Z",
    name="Gotham National Bank",
    contact_information="contact@gothamnational.com",
    identity_class="organisation",
    sectors=["financial-services"]
)

threat_actor = stix2.ThreatActor(
    id="threat-actor--8b6297fe-cae7-47c6-9256-5584b417849c",
    created="2017-04-27T16:18:24.318Z",
    modified="2017-04-27T16:18:24.318Z",
    created_by_ref="identity--b38dfe21-7477-40d1-aa90-5c8671ce51ca",
    name="The Joker",
    labels=["terrorist", "criminal"],
    aliases=["Joe Kerr", "The Clown Prince of Crime"],
    roles=["director"],
    resource_level="team",
    primary_motivation="personal-satisfaction",
    object_marking_refs=[stix2.TLP_RED]
)

indicator = stix2.Indicator(
    id="indicator--1ed8caa7-a708-4706-b651-f1186ede6ca1",
    created="2017-04-27T16:18:24.318Z",
    modified="2017-04-27T16:18:24.318Z",
    created_by_ref="identity--b38dfe21-7477-40d1-aa90-5c8671ce51ca",
    name="Fake email address",
    description="Known to be used by The Joker.",
    labels=["malicious-activity", "attribution"],
    pattern="[email-message:from_ref.value MATCHES '.+\\\\banking@g0thamnatl\\\\.com$']",
    valid_from="2017-04-27T16:18:24.318Z",
    granular_markings=[granular_red, granular_amber, granular_green]
)

rel = stix2.Relationship(
    id="relationship--3d1dd3cc-eb47-4704-9c77-ceff2971b95c",
    created="2017-04-27T16:18:24.318Z",
    modified="2017-04-27T16:18:24.318Z",
    relationship_type='indicates',
    source_ref="indicator--1ed8caa7-a708-4706-b651-f1186ede6ca1",
    target_ref="threat-actor--8b6297fe-cae7-47c6-9256-5584b417849c",
    object_marking_refs=[stix2.TLP_RED]
)

bundle = stix2.Bundle(objects=[identity, indicator, threat_actor, rel])
