import stix2
import re

for obj in bundle.objects:
    if obj == threat_actor:
        print("------------------")
        print("== THREAT ACTOR ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Description: " + obj.description)
        print("Threat Actor Types: " + str(obj.threat_actor_types))
        print("Aliases: " + str(obj.aliases))
        print("First Seen: " + str(obj.first_seen)
        print("Last Seen: " + str(obj.last_seen))
        print("Roles: " + str(obj.roles))
        print("Goals: " + str(obj.goals))
        print("Sophistication: " + obj.sophistication)
        print("Resource Level: " + obj.resource_level)
        print("Primary Motivation: " + obj.primary_motivation)
        print("Secondary Motivations: " + str(obj.secondary_motivations))
        print("Personal Motivations: " + str(obj.personal_motivations))

    elif obj == identity1:
        print("------------------")
        print("== IDENTITY ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Description: " + obj.description)
        print("Roles: " + str(obj.roles))
        print("Identity Class: " + obj.identity_class)
        print("Sectors: " + str(obj.sectors))
        print("Contact Information: " + obj.contact_information)

    elif obj == identity2:
        print("------------------")
        print("== IDENTITY ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Description: " + obj.description)
        print("Roles: " + str(obj.roles))
        print("Identity Class: " + obj.identity_class)
        print("Sectors: " + str(obj.sectors))
        print("Contact Information: " + obj.contact_information)

    elif obj == attack_pattern1:
        print("------------------")
        print("== ATTACK PATTERN ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Description: " + obj.description)
        print("Type: " + obj.type)
        print("Aliases: " + str(obj.aliases))
        print("Kill Chain Phases: " + str(obj.kill_chain_phases))
        print("External References: " + str(obj.external_references))

    elif obj == attack_pattern2:
        print("------------------")
        print("== ATTACK PATTERN ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Description: " + obj.description)
        print("Type: " + obj.type)
        print("Aliases: " + str(obj.aliases))
        print("Kill Chain Phases: " + str(obj.kill_chain_phases))
        print("External References: " + str(obj.external_references))


    elif obj == campaign1:
        print("------------------")
        print("== CAMPAIGN ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Description: " + obj.description)
        print("Type: " + obj.type)
        print("Aliases: " + str(obj.aliases))
        print("First Seen: " + str(obj.first_seen))
        print("Last Seen: " + str(obj.last_seen))
        print("Objective: " + obj.objective)

    elif obj == campaign2:
        print("------------------")
        print("== CAMPAIGN ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Description: " + obj.description)
        print("Type: " + obj.type)
        print("Aliases: " + str(obj.aliases))
        print("First Seen: " + str(obj.first_seen))
        print("Last Seen: " + str(obj.last_seen))
        print("Objective: " + obj.objective)

    elif obj == intrusionset:
        print("------------------")
        print("== INTRUSION SET ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Description: " + obj.name)
        print("Type: " + obj.type)
        print("Aliases: " + str(obj.aliases))
        print("First Seen: " + str(obj.first_seen))
        print("Last Seen: " + str(obj.last_seen))
        print("Goals: " + str(obj.goals))
        print("Resource Level: " + obj.resource_level)
        print("Primary Motivation: " + obj.primary_motivation)
        print("Secondary Motivations: " + str(obj.secondary_motivations))

    elif re.search('relationship*', str(obj)):
        print("------------------")
        print("== RELATIONSHIP ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Description: " + obj.description)
        print("Type: " + obj.type)
        print("Relationship Type: " + obj.relationship_type)
        print("Source Ref: " + obj.source_ref)
        print("Target Ref: " + obj.target_ref)
        print("Start Time: " + str(obj.start_time))
        print("Stop Time: " + str(obj.stop_time))
