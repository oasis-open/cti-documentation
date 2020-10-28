from stix2.v21 import (File, Identity, Malware, ObservedData, Sighting, WindowsRegistryKey, Bundle)

identityOscorp = Identity(
    id="identity--987eeee1-413a-44ac-96cc-0a8acdcc2f2c",
    created="2017-04-14T13:07:49.812Z",
    modified="2017-04-14T13:07:49.812Z",
    name="Oscorp Industries",
    identity_class="organization",
    contact_information="norman@oscorp.com",
    sectors=["technology"], 
    spec_version="2.1",
    type="identity"
)

identityPym = Identity(
    id="identity--7865b6d2-a4af-45c5-b582-afe5ec376c33",
    created="2017-04-14T13:07:49.812Z",
    modified="2017-04-14T13:07:49.812Z",
    name="Pym Technologies",
    identity_class="organization",
    contact_information="hank@pymtech.com",
    sectors=["technology"], 
    spec_version="2.1",
    type="identity"
)

malware = Malware(
    id="malware--ae560258-a5cb-4be8-8f05-013d6712295f",
    created="2014-02-20T09:16:08.989Z",
    modified="2014-02-20T09:16:08.989Z",
    created_by_ref="identity--7865b6d2-a4af-45c5-b582-afe5ec376c33",
    name="Online Job Site Trojan",
    description="Trojan that is disguised as the executable file resume.pdf., it also creates a registry key.",
    malware_types=["remote-access-trojan"], 
    spec_version="2.1",
    type="malware",
    is_family="false"
)

file_malicious = File(
    hashes={
        "MD5": "1717b7fff97d37a1e1a0029d83492de1",
        "SHA-1": "c79a326f8411e9488bdc3779753e1e3489aaedea"
    },
    name="resume.pdf",
    size=83968,
    id="file--364fe3e5-b1f4-5ba3-b951-ee5983b3538d"
)

winRegKey = WindowsRegistryKey(
    key="HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Services\\WSALG2",
    spec_version="2.1",
    id="windows-registry-key--16b80d14-d574-5620-abad-10ff304b1c26"
)

observedDataFile = ObservedData(
    id="observed-data--cf8eaa41-6f4c-482e-89b9-9cd2d6a83cb1",
    created="2017-02-28T19:37:11.213Z",
    modified="2017-02-28T19:37:11.213Z",
    first_observed="2017-02-27T21:37:11.213Z",
    last_observed="2017-02-27T21:37:11.213Z",
    number_observed=1,
    created_by_ref="identity--7865b6d2-a4af-45c5-b582-afe5ec376c33",
    object_refs=[
        "file--364fe3e5-b1f4-5ba3-b951-ee5983b3538d"
    ], 
    spec_version="2.1",
    type="observed-data"
)

observedDataRegKey = ObservedData(
    id="observed-data--a0d34360-66ad-4977-b255-d9e1080421c4",
    created="2017-02-28T19:37:11.213Z",
    modified="2017-02-28T19:37:11.213Z",
    first_observed="2017-02-27T21:37:11.213Z",
    last_observed="2017-02-27T21:37:11.213Z",
    number_observed=1,
    created_by_ref="identity--7865b6d2-a4af-45c5-b582-afe5ec376c33",
    object_refs=[
        "windows-registry-key--16b80d14-d574-5620-abad-10ff304b1c26"
    ], 
    spec_version="2.1",
    type="observed-data"
)

sighting = Sighting(
    id="sighting--779c4ae8-e134-4180-baa4-03141095d971",
    created_by_ref="identity--987eeee1-413a-44ac-96cc-0a8acdcc2f2c",
    created="2017-02-28T19:37:11.213Z",
    modified="2017-02-28T19:37:11.213Z",
    first_seen="2017-02-28T19:07:24.856Z",
    last_seen="2017-02-28T19:07:24.857Z",
    count=1,
    sighting_of_ref="malware--ae560258-a5cb-4be8-8f05-013d6712295f",
    where_sighted_refs=["identity--987eeee1-413a-44ac-96cc-0a8acdcc2f2c"],
    observed_data_refs=["observed-data--cf8eaa41-6f4c-482e-89b9-9cd2d6a83cb1", "observed-data--a0d34360-66ad-4977-b255-d9e1080421c4"], 
    spec_version="2.1",
    type="sighting"
)

bundle = Bundle(objects=[identityPym, identityOscorp, malware, observedDataFile, observedDataRegKey, sighting])
