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

labeled_sdo_names='
attack-pattern
campaign
course-of-action
grouping
identity
indicator
infrastructure
intrusion-set
location
malware
malware-analysis
note
observed-data
opinion
report
threat-actor
tool
vulnerability
'

labeled_other_paths='
sro/relationship
sro/sighting
marking/tlp-amber
marking/tlp-green
marking/tlp-red
marking/statement-marking
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

for name in $labeled_sdo_names; do
    labeled="img/icons/labeled/sdo/$name.svg"
    if [ ! -f "$labeled" ]; then
        echo "Missing labeled icon: $labeled" >&2
        failed=1
        continue
    fi
    if ! grep -q '<title>[^<][^<]*</title>' "$labeled"; then
        echo "Missing labeled SVG title: $labeled" >&2
        failed=1
    fi
    if ! grep -q 'aria-label=' "$labeled"; then
        echo "Missing labeled SVG aria-label: $labeled" >&2
        failed=1
    fi
    if ! grep -q 'viewBox="0 0 96 96"' "$labeled"; then
        echo "Unexpected labeled SVG viewBox: $labeled" >&2
        failed=1
    fi
    if ! grep -q '<rect ' "$labeled" || ! grep -q '<path data-label=' "$labeled"; then
        echo "Labeled SVG lacks a filled tile or outlined label: $labeled" >&2
        failed=1
    fi
done

for path in $labeled_other_paths; do
    labeled="img/icons/labeled/$path.svg"
    if [ ! -f "$labeled" ]; then
        echo "Missing labeled icon: $labeled" >&2
        failed=1
        continue
    fi
    if ! grep -q '<title>[^<][^<]*</title>' "$labeled"; then
        echo "Missing labeled SVG title: $labeled" >&2
        failed=1
    fi
    if ! grep -q 'aria-label=' "$labeled"; then
        echo "Missing labeled SVG aria-label: $labeled" >&2
        failed=1
    fi
    if ! grep -q 'viewBox="0 0 96 96"' "$labeled"; then
        echo "Unexpected labeled SVG viewBox: $labeled" >&2
        failed=1
    fi
    if ! grep -q '<rect ' "$labeled" || ! grep -q '<path data-label=' "$labeled"; then
        echo "Labeled SVG lacks a filled tile or outlined label: $labeled" >&2
        failed=1
    fi
done

if git grep -n -E 'img/icons/(attack_pattern|bundle|campaign|course_of_action|grouping|identity|indicator|infrastructure|intrusion_set|location|malware|malware_analysis|note|observed_data|opinion|relationship|report|restricted_marking|sighting|threat_actor|tlp_amber|tlp_green|tlp_red|tlp_white|tool|vulnerability)\.png' -- '*.md' '*.html' '*.svg'; then
    echo "Found documentation references that still use migrated PNG icons." >&2
    failed=1
fi

if git grep -n -E 'img/icons/labeled/' -- 'stix/intro.md' 'stix/walkthrough.md'; then
    echo "Found redundant labeled tiles next to printed object names." >&2
    failed=1
fi

if git grep -n -E 'img/icons/(attack_pattern|campaign|course_of_action|grouping|identity|indicator|infrastructure|intrusion_set|location|malware|malware_analysis|note|observed_data|opinion|report|threat_actor|tool|vulnerability)\.svg' -- 'examples/visualized-sdo-relationships.md' 'img/relationships/*.svg'; then
    echo "Found unlabeled glyphs in a context that relies on the artwork for identification." >&2
    failed=1
fi

if git grep -n -E 'img/icons/(attack_pattern|campaign|identity|indicator|intrusion_set|malware|observed_data|relationship|restricted_marking|sighting|threat_actor|tlp_amber|tlp_green|tlp_red)\.svg' -- 'stix/examples.md'; then
    echo "Found an unlabeled glyph in the example type cells." >&2
    failed=1
fi

if find img/icons/labeled -type f -name '*.svg' -exec grep -l -E '<script|javascript:|href="https?://|xlink:href=|<image|<text|font-' {} + | grep .; then
    echo "Found executable, external, or font-dependent content in a labeled SVG." >&2
    failed=1
fi

svg_references=$(
    git grep -h -E -o 'img/icons/(attack_pattern|bundle|campaign|course_of_action|grouping|identity|indicator|infrastructure|intrusion_set|location|malware|malware_analysis|note|observed_data|opinion|relationship|report|restricted_marking|sighting|threat_actor|tlp_amber|tlp_green|tlp_red|tlp_white|tool|vulnerability)\.svg' -- '*.md' '*.html' '*.svg' |
        wc -l |
        tr -d ' '
)

labeled_references=$(
    git grep -h -E -o 'img/icons/labeled/[a-z0-9_/-]+\.svg' -- '*.md' '*.html' '*.svg' |
        wc -l |
        tr -d ' '
)

relationship_references=$(
    git grep -h -E -o 'img/icons/(labeled/)?[a-z0-9_/-]+\.svg' -- 'img/relationships/*.svg' |
        wc -l |
        tr -d ' '
)

echo "Validated 26 SVG/PNG compatibility pairs."
echo "Validated 24 labeled SVG tiles."
echo "Found $svg_references migrated SVG references."
echo "Found $labeled_references labeled SVG references."
echo "Found $relationship_references nested relationship-diagram references."

exit "$failed"
