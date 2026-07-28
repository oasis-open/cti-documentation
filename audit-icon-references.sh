#!/bin/sh

set -eu

icon_names='
attack_pattern
bundle
campaign
course_of_action
grouping
identity
indicator
infrastructure
intrusion_set
location
malware
malware_analysis
note
observed_data
opinion
relationship
report
restricted_marking
sighting
threat_actor
tlp_amber
tlp_green
tlp_red
tlp_white
tool
vulnerability
'

failed=0

for name in $icon_names; do
    for extension in png svg; do
        path="img/icons/$name.$extension"
        if [ ! -f "$path" ]; then
            echo "Missing icon: $path" >&2
            failed=1
        fi
    done

    svg="img/icons/$name.svg"
    if ! grep -q '<title>[^<][^<]*</title>' "$svg"; then
        echo "Missing SVG title: $svg" >&2
        failed=1
    fi
    if ! grep -q 'aria-label=' "$svg"; then
        echo "Missing SVG aria-label: $svg" >&2
        failed=1
    fi
    if ! grep -q 'width="77" height="77"' "$svg"; then
        echo "Unexpected SVG intrinsic dimensions: $svg" >&2
        failed=1
    fi
done

if git grep -n -E 'img/icons/(attack_pattern|bundle|campaign|course_of_action|grouping|identity|indicator|infrastructure|intrusion_set|location|malware|malware_analysis|note|observed_data|opinion|relationship|report|restricted_marking|sighting|threat_actor|tlp_amber|tlp_green|tlp_red|tlp_white|tool|vulnerability)\.png' -- '*.md' '*.html' '*.svg'; then
    echo "Found documentation references that still use migrated PNG icons." >&2
    failed=1
fi

svg_references=$(
    git grep -h -E -o 'img/icons/(attack_pattern|bundle|campaign|course_of_action|grouping|identity|indicator|infrastructure|intrusion_set|location|malware|malware_analysis|note|observed_data|opinion|relationship|report|restricted_marking|sighting|threat_actor|tlp_amber|tlp_green|tlp_red|tlp_white|tool|vulnerability)\.svg' -- '*.md' '*.html' '*.svg' |
        wc -l |
        tr -d ' '
)

relationship_references=$(
    git grep -h -E -o 'img/icons/[a-z0-9_]+\.svg' -- 'img/relationships/*.svg' |
        wc -l |
        tr -d ' '
)

echo "Validated 26 SVG/PNG compatibility pairs."
echo "Found $svg_references migrated SVG references."
echo "Found $relationship_references nested relationship-diagram references."

exit "$failed"
