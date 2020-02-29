from stix2.v21 import (Bundle)

for obj in bundle.objects:
    if obj == identity:
        print("------------------")
        print("== IDENTITY ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Identity Class: " + obj.identity_class)
        print("Contact Information: " + obj.contact_information)
        print("Sectors: " + str(obj.sectors))

    elif obj == indicator:
        print("------------------")
        print("== INDICATOR ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Created by Ref: " + obj.created_by_ref)
        print("Name: " + obj.name)
        print("Indicator Types: " + obj.indicator_types[0])
        print("Pattern: " + obj.pattern)
        print("Valid From: " + str(obj.valid_from))
        print("Object Marking Refs: " + str(obj.object_marking_refs))

    elif obj == marking_def_amber:
        print("------------------")
        print("== MARKING DEFINITION ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Definition Type: " + obj.definition_type)
        print("Definition: " + str(obj.definition))

    elif obj == marking_def_statement:
        print("------------------")
        print("== MARKING DEFINITION ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Definition Type: " + obj.definition_type)
        print("Definition: " + str(obj.definition))
