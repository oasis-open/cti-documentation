import stix2

threat_actor = stix2.ThreatActor(
    id="threat-actor--56f3f0db-b5d5-431c-ae56-c18f02caf500",
    created="2016-08-08T15:50:10.983Z",
    modified="2016-08-08T15:50:10.983Z",
    name="Fake BPP (Branistan Peoples Party)",
    labels=["nation-state"],
    roles=["director"],
    goals=["Influence the election in Branistan"],
    resource_level="government"
    primary_motivation="ideology",
    secondary_motivations=["dominance"],
    sophistication="strategic"
)

identity1 = stix2.Identity(
    id="identity--8c6af861-7b20-41ef-9b59-6344fd872a8f",
    created="2016-08-08T15:50:10.983Z",
    modified="2016-08-08T15:50:10.983Z",
    name="Franistan Intelligence",
    identity_class="organisation"
)

ref_bpp = stix2.ExternalReference(
    source_name="website",
    url="http://www.bpp.bn"
)

identity2 = stix2.Identity(
    id="identity--ddfe7140-2ba4-48e4-b19a-df069432103b",
    created="2016-08-08T15:50:10.983Z",
    modified="2016-08-08T15:50:10.983Z",
    name="Branistan Peoples Party",
    identity_class="organisation"
    external_references= [ref_bpp]
)

ref_capec1 = stix2.ExternalReference(
    source_name="capec",
    url="https://capec.mitre.org/data/definitions/148.html",
    external_id="CAPEC-148"
)

ref_capec2 = stix2.ExternalReference(
    source_name="capec",
    url="https://capec.mitre.org/data/definitions/488.html",
    external_id="CAPEC-488"
)

attack_pattern1 = stix2.AttackPattern(
    id="attack-pattern--19da6e1c-71ab-4c2f-886d-d620d09d3b5a",
    created="2016-08-08T15:50:10.983Z",
    modified="2017-01-30T21:15:04.127Z",
    name="Content Spoofing",
    external_references=[ref_capec1]
)

attack_pattern2 = stix2.AttackPattern(
    id="attack-pattern--f6050ea6-a9a3-4524-93ed-c27858d6cb3c",
    created="2016-08-08T15:50:10.983Z",
    modified="2017-01-30T21:15:04.127Z",
    name="HTTP Flood",
    external_references=[ref_capec2]
)

campaign1 = stix2.Campaign(
    id="campaign--e5268b6e-4931-42f1-b379-87f48eb41b1e",
    created="2016-08-08T15:50:10.983Z",
    modified="2016-08-08T15:50:10.983Z",
    name="Operation Bran Flakes",
    description="A concerted effort to insert false information into the BPP's web pages.",
    aliases=["OBF"],
    first_seen="2016-01-08T12:50:40.123Z",
    objective="Hack www.bpp.bn"
)

campaign2 = stix2.Campaign(
    id="campaign--1d8897a7-fdc2-4e59-afc9-becbe04df727",
    created="2016-08-08T15:50:10.983Z",
    modified="2016-08-08T15:50:10.983Z",
    name="Operation Raisin Bran",
    description="A DDOS campaign to flood BPP web servers.",
    aliases=["ORB"],
    first_seen="2016-02-07T19:45:32.126Z",
    objective="Flood www.bpp.bn"
)

intrusionset = stix2.IntrusionSet(
    id="intrusion-set--ed69450a-f067-4b51-9ba2-c4616b9a6713",
    created="2016-08-08T15:50:10.983Z",
    modified="2016-08-08T15:50:10.983Z",
    name="APT BPP",
    description="An advanced persistent threat that seeks to disrupt Branistan's election with multiple attacks.",
    first_seen="2016-01-08T12:50:40.123Z",
    resource_level="government",
    primary_motivation="ideology",
    goals=["Influence the Branistan election", "Disrupt the BPP"],
    secondary_motivations=["dominance"],
    aliases=["Bran-teaser"]
)

relationship1 = stix2.Relationship(campaign1, 'attributed-to', threat_actor)
relationship2 = stix2.Relationship(campaign2, 'attributed-to', threat_actor)
relationship3 = stix2.Relationship(campaign1, 'attributed-to', intrusionset)
relationship4 = stix2.Relationship(campaign2, 'attributed-to', intrusionset)
relationship5 = stix2.Relationship(intrusionset, 'attributed-to', threat_actor)
relationship6 = stix2.Relationship(intrusionset, 'targets', identity2)
relationship7 = stix2.Relationship(intrusionset, 'uses', attack_pattern1)
relationship8 = stix2.Relationship(intrusionset, 'uses', attack_pattern2)
relationship9 = stix2.Relationship(campaign1, 'targets', identity2)
relationship10 = stix2.Relationship(campaign2, 'targets', identity2)
relationship11 = stix2.Relationship(campaign1, 'uses', attack_pattern1)
relationship12 = stix2.Relationship(campaign2, 'uses', attack_pattern2)
relationship13 = stix2.Relationship(threat_actor, 'impersonates', identity2)
relationship14 = stix2.Relationship(threat_actor, 'targets', identity2)
relationship15 = stix2.Relationship(threat_actor, 'attributed-to', identity1)
relationship16 = stix2.Relationship(campaign2, 'targets', identity2)
relationship17 = stix2.Relationship(threat_actor, 'uses', attack_pattern1)
relationship18 = stix2.Relationship(threat_actor, 'uses', attack_pattern2)

bundle = stix2.Bundle(objects=[threat_actor, identity1, identity2, attack_pattern1, attack_pattern2, campaign1, campaign2, intrusionset, relationship1, relationship2, relationship3, relationship4, relationship5, relationship6, relationship7, relationship8, relationship9, relationship10, relationship11, relationship12, relationship13, relationship14, relationship15, relationship16, relationship17, relationship18])
