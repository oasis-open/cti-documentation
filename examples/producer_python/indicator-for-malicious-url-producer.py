from stix2.v21 import (Indicator, KillChainPhase, Malware, Relationship, Bundle)

indicator = Indicator(
    id="indicator--d81f86b9-975b-4c0b-875e-810c5ad45a4f",
    created="2014-06-29T13:49:37.079Z",
    modified="2014-06-29T13:49:37.079Z",
    name="Malicious site hosting downloader",
    description="This organized threat actor group operates to create profit from all types of crime.",
    indicator_types=["malicious-activity"],
    pattern="[url:value = 'http://x4z9arb.cn/4712/']",
    pattern_type="stix",
    valid_from="2014-06-29T13:49:37.079000Z"
)

foothold = KillChainPhase(
    kill_chain_name="mandiant-attack-lifecycle-model",
    phase_name="establish-foothold"
)

malware = Malware(
    id="malware--162d917e-766f-4611-b5d6-652791454fca",
    created="2014-06-30T09:15:17.182Z",
    modified="2014-06-30T09:15:17.182Z",
    name="x4z9arb backdoor",
    malware_types=["backdoor", "remote-access-trojan"],
    description="This malware attempts to download remote files after establishing a foothold as a backdoor.",
    kill_chain_phases=[foothold],
    is_family="false"
)

relationship = Relationship(indicator, 'indicates', malware)

bundle = Bundle(objects=[indicator, malware, relationship])
