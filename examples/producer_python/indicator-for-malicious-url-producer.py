import stix2

indicator = stix2.Indicator(
    id="indicator--d81f86b9-975b-bc0b-775e-810c5ad45a4f",
    created="2014-06-29T13:49:37.079Z",
    modified="2014-06-29T13:49:37.079Z",
    name="Malicious site hosting downloader",
    description="This organized threat actor group operates to create profit from all types of crime.",
    labels=["malicious-activity"],
    pattern="[url:value = 'http://x4z9arb.cn/4712/']",
    valid_from="2014-06-29T13:49:37.079000Z"
)

foothold = stix2.KillChainPhase(
    kill_chain_name="mandiant-attack-lifecycle-model",
    phase_name="establish-foothold"
)

malware = stix2.Malware(
    id="malware--162d917e-766f-4611-b5d6-652791454fca",
    created="2014-06-30T09:15:17.182Z",
    modified="2014-06-30T09:15:17.182Z",
    name="x4z9arb backdoor",
    labels=["backdoor", "remote-access-trojan"],
    description="This malware attempts to download remote files after establishing a foothold as a backdoor.",
    kill_chain_phases=[foothold]
)

relationship = stix2.Relationship(indicator, 'indicates', malware)

bundle = stix2.Bundle(objects=[indicator, malware, relationship])
