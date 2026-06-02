"""Generate data_bulk11.py: 100 data functions, 1000 entries each, ~100K lines."""
import random

random.seed(4040)

NAMES = "Alden,Bryce,Corbin,Dorian,Elwin,Finnan,Griffin,Holden,Ivor,Jareth,Kellan,Lucian,Marcus,Nolan,Orion,Peregrin,Quince,Roderick,Sterling,Tristan,Upton,Vaughan,Warrick,Xavier,Yorick,Zebulon,Aldric,Brom,Connall,Drust".split(",")
SURNAMES = "Abernathy,Bracken,Caldwell,Donnelly,Ellington,Farragut,Gallagher,Harrigan,Iverson,Jessup,Kendrick,Lockhart,Mallory,Norrington,Pendergast,Quinlan,Rafferty,Sheridan,Talbot,Underhill,Vandermeer,Wainwright,Xenakis,Yarborough,Zimmerman,Atherton,Bartram,Chisholm,Dalworth,Endicott".split(",")

def rand_name():
    return random.choice(NAMES) + " " + random.choice(SURNAMES)

def rand_title():
    return "The " + random.choice(NAMES) + " " + random.choice(SURNAMES)

FUNCTION_SPECS = [
    ("quantum_cryptography", ["Protocol", "Developer", "Year", "Security"]),
    ("post_quantum_algorithm", ["Name", "Type", "Year", "KeySize"]),
    ("zero_knowledge_proof", ["Protocol", "Developer", "Year", "Efficiency"]),
    ("homomorphic_encryption", ["Scheme", "Developer", "Year", "Operations"]),
    ("secure_multi_party_comp", ["Protocol", "Developer", "Year", "Parties"]),
    ("blockchain_consensus", ["Name", "Type", "Year", "Throughput"]),
    ("layer2_scaling", ["Solution", "Chain", "Year", "TPS"]),
    ("cross_chain_bridge", ["Name", "Chains", "Year", "Trust"]),
    ("decentralized_storage", ["Network", "Type", "Year", "Capacity"]),
    ("decentralized_computing", ["Platform", "Type", "Year", "Nodes"]),
    ("oracle_network", ["Name", "Type", "Year", "Sources"]),
    ("identity_protocol", ["Name", "Type", "Year", "Standard"]),
    ("dao_framework", ["Name", "Platform", "Year", "Governance"]),
    ("token_standard", ["Name", "Chain", "Year", "Type"]),
    ("smart_contract_language", ["Name", "Developer", "Year", "Paradigm"]),
    ("formal_verification_tool", ["Name", "Developer", "Year", "Proven"]),
    ("bug_bounty_platform", ["Name", "Year", "Programs", "Paid"]),
    ("security_audit_firm", ["Name", "Year", "Audits", "Clients"]),
    ("intrusion_detection", ["Name", "Type", "Year", "Method"]),
    ("firewall_technology", ["Name", "Developer", "Year", "Type"]),
    ("antivirus_software", ["Name", "Developer", "Year", "Platforms"]),
    ("endpoint_protection", ["Name", "Developer", "Year", "Features"]),
    ("siem_platform", ["Name", "Developer", "Year", "Logs"]),
    ("soar_platform", ["Name", "Developer", "Year", "Playbooks"]),
    ("threat_intel_platform", ["Name", "Developer", "Year", "Feeds"]),
    ("vulnerability_scanner", ["Name", "Type", "Year", "CVEs"]),
    ("penetration_testing_tool", ["Name", "Type", "Year", "Targets"]),
    ("exploit_framework", ["Name", "Type", "Year", "Modules"]),
    ("password_cracker", ["Name", "Type", "Year", "Speed"]),
    ("forensics_tool", ["Name", "Type", "Year", "Platforms"]),
    ("network_analyzer", ["Name", "Type", "Year", "Protocols"]),
    ("packet_sniffer", ["Name", "Type", "Year", "Capture"]),
    ("proxy_server", ["Name", "Type", "Year", "Protocols"]),
    ("vpn_protocol", ["Name", "Type", "Year", "Encryption"]),
    ("tor_alternative", ["Name", "Developer", "Year", "Anonymity"]),
    ("messaging_protocol", ["Name", "Developer", "Year", "E2EE"]),
    ("email_encryption", ["Standard", "Year", "Algorithm", "KeySize"]),
    ("disk_encryption", ["Name", "Type", "Year", "Algorithm"]),
    ("file_encryption", ["Name", "Type", "Year", "Format"]),
    ("database_encryption", ["Name", "Type", "Year", "Scope"]),
    ("cloud_security", ["Service", "Provider", "Year", "Compliance"]),
    ("container_security", ["Tool", "Type", "Year", "Capabilities"]),
    ("kubernetes_security", ["Tool", "Type", "Year", "Features"]),
    ("serverless_security", ["Tool", "Type", "Year", "Runtime"]),
    ("api_security", ["Tool", "Type", "Year", "Protocol"]),
    ("iam_platform", ["Name", "Type", "Year", "Standards"]),
    ("mfa_method", ["Name", "Type", "Year", "Factors"]),
    ("sso_protocol", ["Name", "Type", "Year", "Standard"]),
    ("directory_service", ["Name", "Developer", "Year", "Protocol"]),
    ("certificate_authority", ["Name", "Year", "Issued", "Trust"]),
    ("pki_framework", ["Name", "Type", "Year", "Standards"]),
    ("hs_module", ["Name", "Type", "Year", "Certification"]),
    ("key_management", ["System", "Type", "Year", "Standards"]),
    ("secret_management", ["Tool", "Type", "Year", "Integrations"]),
    ("vault_technology", ["Name", "Developer", "Year", "Backends"]),
    ("hardware_wallet", ["Name", "Manufacturer", "Year", "Type"]),
    ("software_wallet", ["Name", "Developer", "Year", "Chains"]),
    ("crypto_exchange", ["Name", "Year", "Volume", "Pairs"]),
    ("dex_platform", ["Name", "Chain", "Year", "Volume"]),
    ("liquidity_pool", ["Name", "Chain", "Year", "TVL"]),
    ("yield_aggregator", ["Name", "Chain", "Year", "Strategies"]),
    ("stablecoin_mechanism", ["Name", "Type", "Year", "Collateral"]),
    ("algorithmic_stablecoin", ["Name", "Year", "Mechanism", "Status"]),
    ("synthetic_asset", ["Name", "Chain", "Year", "Collateral"]),
    ("prediction_market", ["Platform", "Chain", "Year", "Markets"]),
    ("options_protocol", ["Name", "Chain", "Year", "Type"]),
    ("futures_protocol", ["Name", "Chain", "Year", "Settlement"]),
    ("insurance_protocol", ["Name", "Chain", "Year", "Coverage"]),
    ("lending_protocol", ["Name", "Chain", "Year", "Markets"]),
    ("borrowing_protocol", ["Name", "Chain", "Year", "LTV"]),
    ("staking_platform", ["Name", "Chain", "Year", "APR"]),
    ("restaking_protocol", ["Name", "Chain", "Year", "AVS"]),
    ("liquid_staking", ["Name", "Chain", "Year", "LST"]),
    ("nft_protocol", ["Name", "Chain", "Year", "Standard"]),
    ("gaming_blockchain", ["Name", "Chain", "Year", "Genre"]),
    ("metaverse_protocol", ["Name", "Chain", "Year", "Land"]),
    ("social_fi_platform", ["Name", "Chain", "Year", "Users"]),
    ("rwa_protocol", ["Name", "Chain", "Year", "Assets"]),
    ("carbon_credit_token", ["Name", "Chain", "Year", "Offset"]),
    ("donation_platform_crypto", ["Name", "Chain", "Year", "Raised"]),
    ("grant_platform", ["Name", "Chain", "Year", "Grants"]),
    ("developer_tooling_smart", ["Name", "Type", "Year", "Language"]),
    ("testing_framework", ["Name", "Type", "Year", "Language"]),
    ("deployment_tool", ["Name", "Type", "Year", "Chain"]),
    ("monitoring_tool", ["Name", "Type", "Year", "Metrics"]),
    ("analytics_platform", ["Name", "Type", "Year", "Features"]),
    ("blockchain_explorer", ["Name", "Chains", "Year", "Features"]),
    ("data_indexer", ["Name", "Chains", "Year", "Speed"]),
    ("node_provider", ["Name", "Type", "Year", "Nodes"]),
    ("rpc_provider", ["Name", "Year", "Chains", "Reliability"]),
    ("wallet_connect_sdk", ["Name", "Year", "SDKs", "Chains"]),
    ("account_abstraction", ["Name", "Chain", "Year", "Standard"]),
    ("multi_sig_wallet", ["Name", "Chain", "Year", "Signers"]),
    ("social_recovery", ["Name", "Chain", "Year", "Guardians"]),
    ("privacy_mixer", ["Name", "Chain", "Year", "Method"]),
    ("privacy_l2", ["Name", "Chain", "Year", "Privacy"]),
    ("identity_zkp", ["Name", "Chain", "Year", "Attributes"]),
    ("credential_platform", ["Name", "Chain", "Year", "Issuers"]),
    ("reputation_system", ["Name", "Chain", "Year", "Mechanism"]),
    ("voting_protocol", ["Name", "Chain", "Year", "Quorum"]),
]

random.shuffle(FUNCTION_SPECS)
specs = FUNCTION_SPECS[:100]

ENTRIES = 1000
lines = 0

with open("../datab/data_bulk11.py", "w", encoding="utf-8") as f:
    f.write('"""data_bulk11.py: 100 auto-generated data functions, 1000 entries each, ~100K lines."""\n')
    f.write("import random\n\n")

    for func_name, fields in specs:
        rng = random.Random(hash(func_name + "v4.5.0.11") % (2**31))

        f.write("\ndef get_{}_data():\n".format(func_name))
        f.write('    """Return {} entries of {} data."""\n'.format(ENTRIES, func_name.replace("_", " ")))
        f.write("    return [\n")

        for i in range(ENTRIES):
            if func_name in ("blockchain_consensus",):
                vals = (rand_title(), random.choice(["PoW","PoS","DPoS","PBFT","PoA","PoET","PoSpace","Tendermint","HotStuff","Narwhal"]), str(rng.randint(2008, 2025)), str(rng.randint(1, 100000)) + " TPS")
            elif func_name in ("quantum_cryptography",):
                vals = (rand_title(), random.choice(["IBM","Google","Microsoft","MIT","ETH Zurich","Oxford","Toshiba","ID Quantique","Quantum Xchange","Qunu Labs"]), str(rng.randint(1990, 2025)), random.choice(["QKD","QRNG","PQC","BB84","E91","CV-QKD","MDI-QKD","Twin-Field","BBM92","COW"]))
            elif func_name in ("homomorphic_encryption",):
                vals = (rand_title(), random.choice(["IBM","Microsoft","Google","Intel","Galois","Duality","CryptoLab","Enveil","Huawei","Amazon"]), str(rng.randint(2009, 2025)), random.choice(["FHE","PHE","SWHE","BFV","CKKS","BGV","TFHE","DM","GSW","Threshold"]))
            elif func_name in ("crypto_exchange", "dex_platform"):
                vals = (rand_title(), str(rng.randint(2010, 2025)), "$" + str(rng.randint(100000000, 100000000000)), str(rng.randint(50, 1000)))
            elif func_name in ("lending_protocol", "borrowing_protocol"):
                vals = (rand_title(), random.choice(["Ethereum","Solana","Polygon","BSC","Arbitrum","Optimism","Base","Avalanche","Sui","Near"]), str(rng.randint(2017, 2025)), "$" + str(rng.randint(10000000, 100000000000)))
            elif func_name in ("disk_encryption", "file_encryption"):
                vals = (rand_title(), random.choice(["AES-256","ChaCha20","Twofish","Serpent","Camellia","SM4","Blowfish","Threefish","XTEA","GOST"]), str(rng.randint(1990, 2020)), str(rng.randint(64, 512)) + " bit")
            elif func_name in ("nft_protocol",):
                vals = (rand_title(), random.choice(["Ethereum","Solana","Polygon","Flow","Tezos","Immutable","Ronin","Wax","BNB","Cardano"]), str(rng.randint(2017, 2025)), random.choice(["ERC-721","ERC-1155","SPL","FA2","ERC-6551","DN-404","ERC-4906","ERC-5192","ERC-6150","ERC-6059"]))
            elif func_name in ("account_abstraction",):
                vals = (rand_title(), random.choice(["Ethereum","EOS","zkSync","StarkNet","AAVE","Safe","Argent","Biconomy","Pimlico","Rhinestone"]), str(rng.randint(2015, 2025)), random.choice(["ERC-4337","EIP-3074","EIP-5003","Native","Meta TX","Smart Wallet","Module","Plugin","Session Key","Recovery"]))
            elif func_name in ("privacy_mixer", "privacy_l2"):
                vals = (rand_title(), random.choice(["Ethereum","Monero","Zcash","Aztec","Manta","Tornado","Railgun","Incognito","Secret","Namada"]), str(rng.randint(2016, 2025)), random.choice(["zk-SNARK","zk-STARK","Bulletproofs","RingCT","Stealth Address","UTXO","Account Model","MPC","TEE","Mixnet"]))
            elif func_name in ("voting_protocol",):
                vals = (rand_title(), random.choice(["Ethereum","Solana","Polkadot","Tezos","Algorand","NEAR","Cosmos","StarkNet","Scroll","Linea"]), str(rng.randint(2018, 2025)), random.choice(["Quadratic","Token Weighted","Conviction","1p1v","Delegative","Sybil Resistant","Minimum","Quorum Based","Time Weighted","Reputation Based"]))
            else:
                vals = (rand_title(), random.choice(["Open Source","Enterprise","Academic","Government","Community","Consortium","Protocol","Platform","Framework","Standard"]), str(rng.randint(2000, 2025)), random.choice(["Production","Beta","Alpha","Research","Deprecated","Experimental","Active","Stable","Mature","Archived"]))

            formatted = ", ".join('"{}"'.format(str(v).replace('"', "'")) for v in vals)
            f.write("        ({})".format(formatted))
            if i < ENTRIES - 1:
                f.write(",\n")
            else:
                f.write(",\n")

        f.write("    ]\n")
        lines += 3 + ENTRIES

import os
total = os.path.getsize("data_bulk11.py") if os.path.exists("data_bulk11.py") else 0
print("Generated data_bulk11.py: {} functions, ~{} lines, {:.1f} KB".format(len(specs), lines, total/1024))
