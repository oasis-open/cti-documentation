#!/bin/bash

find . -iname "*.json" -print0 | xargs -0 stix2_validator