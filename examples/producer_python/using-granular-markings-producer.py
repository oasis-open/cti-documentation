from stix2.v21 import (GranularMarking, ThreatActor, Identity, Indicator, Relationship, Bundle, TLP_RED, TLP_AMBER, TLP_GREEN)

granular_red = GranularMarking(
        marking_ref=TLP_RED.id,
        selectors=["description"]
)

granular_amber = GranularMarking(
        marking_ref=TLP_AMBER.id,
        selectors=["indicator_types.[1]"]
)

granular_green = GranularMarking(
        marking_ref=TLP_GREEN.id,
        selectors=["indicator_types.[0]", "name", "pattern"]
)

identity = Identity(
    id="identity--b38dfe21-7477-40d1-aa90-5c8671ce51ca",
    created="2017-04-27T16:18:24.318Z",
    modified="2017-04-27T16:18:24.318Z",
    name="Gotham National Bank",
    contact_information="contact@gothamnational.com",
    identity_class="organization",
    sectors=["financial-services"],
    spec_version="2.1",
    type="identity"
)

threat_actor = ThreatActor(
    id="threat-actor--8b6297fe-cae7-47c6-9256-5584b417849c",
    created="2017-04-27T16:18:24.318Z",
    modified="2017-04-27T16:18:24.318Z",
    created_by_ref="identity--b38dfe21-7477-40d1-aa90-5c8671ce51ca",
    name="The Joker",
    threat_actor_types=["terrorist", "criminal"],
    aliases=["Joe Kerr", "The Clown Prince of Crime"],
    roles=["director"],
    resource_level="team",
    primary_motivation="personal-satisfaction",
    object_marking_refs=[TLP_RED],
    spec_version="2.1",
    type="threat-actor"
)

indicator = Indicator(
    id="indicator--1ed8caa7-a708-4706-b651-f1186ede6ca1",
    created="2017-04-27T16:18:24.318Z",
    modified="2017-04-27T16:18:24.318Z",
    created_by_ref="identity--b38dfe21-7477-40d1-aa90-5c8671ce51ca",
    name="Fake email address",
    description="Known to be used by The Joker.",
    indicator_types=["malicious-activity", "attribution"],
    pattern="[email-message:from_ref.value MATCHES '.+\\\\banking@g0thamnatl\\\\.com$']",
    pattern_type="stix",
    valid_from="2017-04-27T16:18:24.318Z",
    granular_markings=[granular_red, granular_amber, granular_green],
    spec_version="2.1",
    type="indicator"
)

rel = Relationship(
    id="relationship--3d1dd3cc-eb47-4704-9c77-ceff2971b95c",
    created="2017-04-27T16:18:24.318Z",
    modified="2017-04-27T16:18:24.318Z",
    relationship_type='indicates',
    source_ref="indicator--1ed8caa7-a708-4706-b651-f1186ede6ca1",
    target_ref="threat-actor--8b6297fe-cae7-47c6-9256-5584b417849c",
    object_marking_refs=[TLP_RED],
    spec_version="2.1",
    type="relationship"
)

bundle = Bundle(objects=[identity, indicator, threat_actor, rel])
