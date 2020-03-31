from stix2.v21 import (Identity, Indicator, Sighting, Bundle)

identityAlpha = Identity(
    id="identity--39012926-a052-44c4-ae48-caaf4a10ee6e",
    created="2017-02-24T15:50:10.564Z",
    modified="2017-02-24T15:50:10.564Z",
    name="Alpha Threat Analysis Org.",
    identity_class="organization",
    contact_information="info@alpha.org",
    roles=["Cyber Security"],
    sectors=["technology"], 
    spec_version="2.1",
    type="identity"
)

identityBeta = Identity(
    id="identity--5206ba14-478f-4b0b-9a48-395f690c20a2",
    created="2017-02-26T17:55:10.442Z",
    modified="2017-02-26T17:55:10.442Z",
    name="Beta Cyber Intelligence Company",
    identity_class="organization",
    contact_information="info@beta.com",
    roles=["Cyber Security"],
    sectors=["technology"], 
    spec_version="2.1",
    type="identity"
)

indicator = Indicator(
    id="indicator--9299f726-ce06-492e-8472-2b52ccb53191",
    created_by_ref="identity--39012926-a052-44c4-ae48-caaf4a10ee6e",
    created="2017-02-27T13:57:10.515Z",
    modified="2017-02-27T13:57:10.515Z",
    name="Malicious URL",
    description="This URL is potentially associated with malicious activity and is listed on several blacklist sites.",
    indicator_types=["malicious-activity"],
    pattern="[url:value = 'http://paypa1.banking.com']",
    pattern_type="stix",
    valid_from="2015-06-29T09:10:15.915Z", 
    spec_version="2.1",
    type="indicator"
)

sighting = Sighting(
    id="sighting--8356e820-8080-4692-aa91-ecbe94006833",
    created_by_ref="identity--5206ba14-478f-4b0b-9a48-395f690c20a2",
    created="2017-02-28T19:37:11.213Z",
    modified="2017-02-28T19:37:11.213Z",
    first_seen="2017-02-27T21:37:11.213Z",
    last_seen="2017-02-27T21:37:11.214Z",
    count=1,
    sighting_of_ref="indicator--9299f726-ce06-492e-8472-2b52ccb53191",
    where_sighted_refs=["identity--5206ba14-478f-4b0b-9a48-395f690c20a2"], 
    spec_version="2.1",
    type="sighting"
)

bundle = Bundle(objects=[indicator, identityAlpha, identityBeta, sighting])
