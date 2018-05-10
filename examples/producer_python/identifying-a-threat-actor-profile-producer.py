import stix2

threat_actor = stix2.ThreatActor(
    id="threat-actor--dfaa8d77-07e2-4e28-b2c8-92e9f7b04428",
    created="2014-11-19T23:39:03.893Z",
    modified="2014-11-19T23:39:03.893Z",
    name="Disco Team Threat Actor Group",
    description="This organized threat actor group operates to create profit from all types of crime.",
    labels=["crime-syndicate"],
    aliases=["Equipo del Discoteca"],
    roles=["agent"],
    goals=["Steal Credit Card Information"],
    sophistication="expert",
    resource_level="organization",
    primary_motivation="personal-gain"
)

identity = stix2.Identity(
    id="identity--733c5838-34d9-4fbf-949c-62aba761184c",
    created="2016-08-23T18:05:49.307Z",
    modified="2016-08-23T18:05:49.307Z",
    name="Disco Team",
    description="Disco Team is the name of an organized threat actor crime-syndicate.",
    identity_class="organization",
    contact_information="disco-team@stealthemail.com"
)

relationship = stix2.Relationship(threat_actor, 'attributed-to', identity)

bundle = stix2.Bundle(objects=[threat_actor, identity, relationship])
