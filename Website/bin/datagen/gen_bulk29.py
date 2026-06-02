"""Generate data_bulk29.py and data_bulk30.py: 500K+ lines total."""
import random, os

SEED = 2940
random.seed(SEED)

TOPICS29 = [
    "firewall_policy", "intrusion_detection", "antivirus_engine", "malware_analysis", "ransomware_decrypt",
    "phishing_detect", "social_engineering", "zero_day_exploit", "vulnerability_scan", "penetration_test",
    "network_segment", "vpn_tunnel", "ssl_tls_cert", "public_key_infra", "certificate_authority",
    "digital_signature", "hash_function", "symmetric_cipher", "asymmetric_cipher", "key_exchange",
    "blockchain_security", "smart_contract_audit", "decentralized_id", "multi_sig_wallet", "token_security",
    "identity_access_mgmt", "single_sign_on", "multi_factor_auth", "biometric_verify", "zero_trust",
    "endpoint_detect", "endpoint_response", "edr_agent", "xdr_platform", "siem_system",
    "security_orchestration", "soar_playbook", "threat_intel", "ioc_collection", "ttp_mapping",
    "incident_response", "forensic_analysis", "disk_forensics", "memory_forensics", "network_forensics",
    "log_analysis", "event_correlation", "alert_triage", "containment_strat", "recovery_plan",
    "security_audit", "compliance_check", "gdpr_requirement", "hipaa_control", "pci_dss_scope",
    "iso_27001", "nist_framework", "cissp_domain", "risk_assessment", "threat_modeling",
    "security_awareness", "phishing_sim", "secure_coding", "code_review", "dependency_check",
    "web_app_firewall", "sql_injection", "xss_protection", "csrf_token", "api_security",
    "cloud_security", "aws_iam", "azure_ad", "gcp_iam", "container_sec",
    "kubernetes_sec", "docker_scan", "serverless_sec", "saas_security", "casb_gateway",
    "network_protocol", "tcp_ip_stack", "dns_resolution", "dhcp_lease", "arp_spoof",
    "bgp_routing", "ospf_protocol", "vlan_tagging", "subnet_masking", "cidr_notation",
    "router_config", "switch_config", "access_control_list", "port_security", "spanning_tree",
    "load_balancer", "reverse_proxy", "cdn_edge", "dns_filter", "traffic_shaping",
    "bandwidth_mgmt", "qos_policy", "latency_optimize", "jitter_reduce", "packet_loss",
    "snmp_monitor", "netflow_analyze", "wireshark_capture", "tcpdump_filter", "packet_analyst",
    "wireless_security", "wpa3_config", "radius_server", "eap_tls", "mac_filter",
    "iot_security", "firmware_analysis", "embedded_secure", "device_auth", "ota_update",
    "database_security", "sql_encrypt", "audit_trail", "backup_encrypt", "data_masking",
    "dlp_policy", "data_classify", "data_retention", "data_wipe", "secure_delete",
    "email_security", "spam_filter", "dkim_sign", "dmarc_policy", "spf_record",
    "cyber_threat_intel", "attack_surface", "red_team_op", "blue_team_def", "purple_team_ex",
    "bug_bounty", "responsible_disclosure", "cve_tracking", "cpe_match", "cvss_score",
    "adversary_emulation", "tactic_technique", "detection_rule", "sigma_rule", "yara_rule",
    "network_baseline", "traffic_anomaly", "protocol_analyze", "packet_capture", "flow_export",
    "honeypot_deploy", "sandbox_analysis", "reverse_engineering", "binary_patching", "shellcode_analyze",
    "memory_protect", "aslr_bypass", "dep_bypass", "stack_canary", "sehop_mitigate",
    "secure_boot", "measured_boot", "tpm_attest", "uefi_secure", "bootkit_detect",
    "rootkit_detect", "kernel_protect", "driver_sign", "code_integrity", "app_control",
    "sensitive_data", "pii_protection", "encrypt_rest", "encrypt_transit", "key_rotation",
    "privilege_audit", "user_behavior", "ueba_analytics", "insider_threat", "data_exfil",
    "cloud_access", "cloud_workload", "micro_segment", "service_mesh", "api_gateway_sec",
    "container_runtime", "image_scan", "registry_trust", "pod_security", "network_policy",
    "serverless_harden", "function_perm", "event_inject", "third_party_risk", "vendor_assess",
    "supply_chain_sec", "sbom_generate", "provenance_track", "build_pipeline", "deploy_pipeline",
]
TOPICS30_EXTRA = [
    "vertical_garden", "rooftop_farm", "urban_agriculture", "community_garden", "school_garden",
    "climate_smart_ag", "drought_tolerant", "heat_resist_crop", "flood_tolerant_crop", "salt_tolerant",
    "agri_robotics", "harvest_robot", "weeding_robot", "pruning_robot", "sorting_machine",
    "machine_vision_crop", "deep_learning_plant", "predictive_yield", "crop_modeling", "phenotyping",
    "genome_select", "marker_assisted", "genomic_pred", "trait_introgression", "speed_breeding",
    "seed_treatment", "seed_coating", "seed_priming", "germination_test", "seed_vigor",
    "nursery_mgmt", "transplant_method", "hardening_off", "grafting_tech", "rootstock_select",
    "pruning_method", "canopy_mgmt", "trellis_system", "espalier_train", "fruit_thin",
    "vineyard_mgmt", "grape_variety", "wine_production", "olive_orchard", "citrus_grove",
    "soil_amend", "lime_apply", "gypsum_use", "biochar_add", "mycorrhizal_inoc",
    "compost_tea", "vermicompost", "bokashi_ferment", "anaerobic_digest", "biofertilizer",
    "water_conserve", "rainwater_catch", "greywater_reuse", "efficient_nozzle", "soil_moist_sensor",
    "evapotranspire", "crop_coefficient", "irrigation_sched", "deficit_irrig", "partial_root_dry",
    "frost_protect", "windbreak_design", "shade_house", "high_tunnel", "low_tunnel",
]
TOPICS30 = [
    "crop_rotation", "soil_preparation", "seed_selection", "planting_schedule", "irrigation_method",
    "drip_irrigation", "sprinkler_system", "flood_irrigation", "water_management", "drainage_system",
    "fertilizer_type", "nitrogen_fix", "phosphorus_uptake", "potassium_cycle", "compost_recipe",
    "organic_matter", "cover_cropping", "green_manure", "mulching_technique", "tillage_method",
    "no_till_farming", "conservation_till", "contour_plowing", "terrace_farming", "strip_cropping",
    "pest_management", "integrated_pest", "biological_control", "natural_predator", "pheromone_trap",
    "insecticide_type", "herbicide_apply", "fungicide_spray", "disease_resist", "crop_variety",
    "weed_suppression", "mechanical_weed", "flame_weed", "crop_competition", "allelopathy",
    "harvest_timing", "combine_harvest", "threshing_method", "grain_storage", "silo_management",
    "post_harvest", "cold_chain", "controlled_atmos", "drying_process", "packaging_fresh",
    "livestock_nutrition", "feed_formulation", "forage_type", "silage_production", "pasture_mgmt",
    "animal_health", "vaccination_sched", "disease_detect", "biosecurity_measure", "quarantine_proto",
    "breeding_program", "genetic_select", "artificial_insem", "embryo_transfer", "herd_genetics",
    "dairy_production", "milking_system", "milk_quality", "cheese_making", "yogurt_culture",
    "poultry_farming", "broiler_house", "layer_system", "egg_processing", "chicken_health",
    "aquaculture_fish", "fish_farming", "pond_mgmt", "water_quality_fish", "feed_aquatic",
    "beekeeping", "hive_mgmt", "honey_extract", "pollination_svc", "queen_rearing",
    "precision_agri", "gps_farming", "drone_crop", "satellite_imaging", "yield_monitor",
    "variable_rate", "soil_sensor", "weather_station", "climate_model", "growing_degree",
    "greenhouse_ctrl", "hydroponic_sys", "aeroponic_grow", "vertical_farming", "controlled_env",
    "plant_breeding", "hybrid_seed", "gmo_crop", "gene_editing", "crispr_plant",
    "food_safety", "haccp_plan", "food_testing", "contaminant_check", "traceability_sys",
    "food_processing", "canning_method", "freezing_tech", "dehydration_food", "fermentation_food",
    "food_preserve", "additive_type", "shelf_life", "sensory_eval", "nutrition_label",
    "agricultural_econ", "farm_budget", "commodity_price", "supply_demand", "market_access",
    "rural_develop", "farm_subsidy", "crop_insurance", "land_tenure", "coop_model",
    "sustainable_agri", "regenerative_farm", "carbon_sequester", "agroforestry", "silvopasture",
    "permaculture_design", "food_forest", "polyculture", "biodiversity_farm", "ecosystem_svc",
    "soil_health", "microbiome_soil", "earthworm_activity", "soil_testing", "ph_adjustment",
    "organic_certify", "non_gmo_verify", "fair_trade_cert", "rainforest_ally", "biodynamic_farm",
] + TOPICS30_EXTRA

random.shuffle(TOPICS29)
random.shuffle(TOPICS30)

ENTRIES = 1500
PREFIXES = ["Alpha","Beta","Gamma","Delta","Epsilon","Zeta","Eta","Theta","Iota","Kappa","Lambda","Mu","Nu","Xi","Omicron","Pi","Rho","Sigma","Tau","Upsilon","Phi","Chi","Psi","Omega"]
SUFFIXES = ["A","B","C","D","E","F","G","H","J","K","L","M","N","P","Q","R","S","T","U","V","W","X","Y","Z"]
LEVELS = ["Low","Medium","High","Critical","Optimal","Suboptimal","Degraded","Failing","Excellent","Good","Fair","Poor"]
STATUSES = ["Active","Inactive","Pending","Review","Approved","Rejected","Standby","Fault","Online","Offline","Maintenance","Commissioning"]

def generate_bulk(filename, topics, entries=ENTRIES):
    func_count = 0
    with open(filename, "w", encoding="utf-8") as f:
        f.write('"""{}: {} data functions, {} entries each."""\n'.format(os.path.basename(filename), len(topics), entries))
        f.write("import random\n\n")
        for spec in topics:
            frng = random.Random(hash(spec + "v5.4.0") % (2**31))
            func_name = spec
            func_count += 1
            f.write("\ndef get_{}_data():\n".format(func_name))
            f.write('    """Return {} entries of {} data."""\n'.format(entries, func_name.replace("_", " ")))
            f.write("    return [\n")
            for i in range(entries):
                name = "{}_{}_{}".format(
                    frng.choice(PREFIXES), frng.randint(100, 9999), frng.choice(SUFFIXES))
                val1 = round(frng.uniform(0.01, 9999.99), 2)
                val2 = frng.randint(1, 10000)
                val3 = frng.choice(LEVELS)
                val4 = round(frng.uniform(0.0, 100.0), 1)
                val5 = frng.choice(STATUSES)
                f.write('        ("{}", {}, {}, "{}", {}, "{}")'.format(name, val1, val2, val3, val4, val5))
                f.write(",\n" if i < entries - 1 else ",\n")
            f.write("    ]\n")
    total = os.path.getsize(filename)
    lines = (entries + 3) * func_count
    print("{}: {} functions, ~{} lines, {:.1f} KB".format(filename, func_count, lines, total/1024))

generate_bulk("../datab/data_bulk29.py", TOPICS29)
generate_bulk("../datab/data_bulk30.py", TOPICS30)
