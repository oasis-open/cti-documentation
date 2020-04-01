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
        print("Sectors: " + str(obj.sectors))
        print("Contact Information: " + obj.contact_information)

    elif obj == indicator:
        print("------------------")
        print("== INDICATOR ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Created: " + str(obj.created))
        print("Modified: " + str(obj.modified))
        print("Name: " + obj.name)
        print("Type: " + obj.type)
        print("Indicator Types: " + str(obj.indicator_types))
        print("Pattern: " + obj.pattern)
        print("Pattern Type: " + obj.pattern_type)
        print("Valid From: " + str(obj.valid_from))

    elif obj == marking_def_amber:
        print("------------------")
        print("== MARKING DEFINITION ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Type: " + obj.type)
        print("Created: " + str(obj.created))
        print("Definition Type: " + obj.definition_type)
        print("Definition: " + str(obj.definition))

    elif obj == marking_def_statement:
        print("------------------")
        print("== MARKING DEFINITION ==")
        print("------------------")
        print("ID: " + obj.id)
        print("Type: " + obj.type)
        #print("Name: " + obj.name)
        print("Created: " + str(obj.created))
        print("Definition Type: " + obj.definition_type)
        print("Definition: " + str(obj.definition))
