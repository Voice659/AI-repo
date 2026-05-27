"""Generate data_bulk25.py and data_bulk26.py: 500K+ lines total."""
import random, os

SEED = 2526
random.seed(SEED)

TOPICS25 = [
    "solar_energy", "wind_energy", "hydroelectric_power", "geothermal_energy", "nuclear_power",
    "tidal_energy", "biomass_energy", "hydrogen_fuel", "battery_storage", "smart_grid",
    "carbon_capture", "emissions_trading", "recycling_plant", "water_treatment", "air_purifier",
    "plastic_waste", "composting_system", "electric_vehicle", "solar_panel", "wind_turbine",
    "energy_audit", "green_building", "sustainable_farming", "organic_farming", "permaculture",
    "reforestation", "ocean_cleanup", "biofuel_plant", "methane_capture", "landfill_gas",
    "waste_to_energy", "desalination", "rainwater_harvest", "green_roof", "vertical_farm",
    "energy_star", "led_lighting", "smart_meter", "demand_response", "distributed_generation",
    "microgrid", "peak_shaving", "load_balancing", "power_factor", "harmonic_filter",
    "transformer_efficiency", "motor_efficiency", "cogeneration", "heat_pump", "solar_thermal",
    "concentrated_solar", "offshore_wind", "run_of_river", "pumped_storage", "compressed_air",
    "flywheel_storage", "thermal_storage", "superconductor_cable", "hvdc_transmission", "substation",
    "distribution_line", "feeder_protection", "relay_coordination", "arc_flash", "lightning_protection",
    "grounding_system", "surge_protector", "ups_system", "generator_set", "switchgear",
    "circuit_breaker", "fuse_type", "contactor", "starter_motor", "variable_freq_drive",
    "soft_starter", "servo_drive", "plc_controller", "scada_system", "remote_terminal",
    "intelligent_elec", "energy_management", "building_automation", "hvac_control", "lighting_control",
    "access_control", "fire_alarm", "elevator_control", "escalator_drive", "parking_system",
    "ev_charger", "battery_management", "fuel_cell_stack", "electrolyzer", "power_electronics",
    "inverter_type", "converter_type", "rectifier", "chopper_circuit", "cycloconverter",
    "dc_dc_converter", "multilevel_inverter", "matrix_converter", "resonant_converter", "snubber_circuit",
    "gate_driver", "igbt_module", "mosfet_power", "thyristor", "triac",
    "diode_power", "sic_device", "gan_transistor", "magnetic_core", "inductor_design",
    "capacitor_bank", "resistor_network", "filter_design", "emc_filter", "pcb_layout_power",
    "thermal_management", "heat_sink", "liquid_cooling", "phase_change", "thermoelectric_cooler",
    "pyranometer", "anemometer", "flow_meter", "gas_analyzer", "particle_counter",
    "noise_meter", "lux_meter", "multimeter", "clamp_meter", "megger",
    "power_analyzer", "oscilloscope", "data_logger", "chart_recorder", "thermography",
    "vibration_analysis", "oil_analysis", "ultrasonic_test", "insulation_test", "hi_pot_test",
    "earth_tester", "phase_sequence", "frequency_counter", "spectrum_analyzer", "signal_generator",
    "function_generator", "arbitrary_gen", "waveform_monitor", "transient_recorder", "event_recorder",
    "sequence_recorder", "alarm_management", "event_management", "trip_logic", "interlock_logic",
    "permissive_logic", "safety_integrity", "sil_rating", "fail_safe", "redundancy_config",
    "voting_logic", "diagnostic_coverage", "proof_test", "mission_time", "failure_rate",
    "availability_calc", "reliability_block", "fault_tree", "event_tree", "lopa_analysis",
    "hazop_study", "risk_matrix", "layer_protection", "safety_instr", "emergency_shutdown",
    "fire_gas_system", "burner_management", "turbine_control", "compressor_control", "pump_control",
    "valve_actuator", "positioner", "flow_control", "level_control", "pressure_control",
    "temp_control", "ph_control", "conductivity", "turbidity", "dissolved_oxygen",
    "chemical_dosing", "catalyst_regeneration", "reactor_control", "distillation_column", "heat_exchanger_control",
    "boiler_control", "steam_turbine", "gas_turbine", "recip_engine", "centrifugal_compressor",
    "axial_compressor", "screw_compressor", "fan_performance", "pump_performance", "valve_sizing",
]

TOPICS26 = [
    "stock_market", "bond_market", "commodity_trading", "forex_trading", "derivatives_market",
    "options_trading", "futures_contract", "swap_agreement", "credit_default", "etf_trading",
    "mutual_fund", "hedge_fund", "private_equity", "venture_capital", "angel_investing",
    "ipo_offering", "secondary_offering", "dividend_policy", "share_buyback", "merger_acquisition",
    "corporate_finance", "project_finance", "trade_finance", "supply_chain_finance", "invoice_factoring",
    "working_capital", "cash_flow", "financial_statement", "balance_sheet", "income_statement",
    "cash_flow_statement", "ratio_analysis", "liquidity_ratio", "solvency_ratio", "profitability_ratio",
    "efficiency_ratio", "valuation_method", "dcf_valuation", "comparable_analysis", "precedent_transaction",
    "lbo_model", "mna_model", "budget_forecast", "financial_model", "scenario_analysis",
    "sensitivity_analysis", "monte_carlo_sim", "var_calculation", "stress_testing", "backtesting",
    "algorithmic_trading", "high_freq_trading", "quant_strategy", "arbitrage_strategy", "market_making",
    "pair_trading", "momentum_strategy", "mean_reversion", "stat_arb", "volatility_arb",
    "risk_management", "market_risk", "credit_risk", "operational_risk", "liquidity_risk",
    "counterparty_risk", "systemic_risk", "risk_metric", "risk_weighted_asset", "capital_adequacy",
    "basel_accord", "solvency_ii", "ifrs_standard", "gaap_accounting", "tax_accounting",
    "transfer_pricing", "consolidation", "audit_procedure", "internal_control", "compliance_program",
    "aml_procedure", "kyc_process", "sanctions_screening", "fraud_detection", "forensic_accounting",
    "central_bank", "monetary_policy", "fiscal_policy", "interest_rate", "inflation_target",
    "quantitative_easing", "open_market_op", "reserve_requirement", "discount_window", "currency_peg",
    "digital_currency", "cryptocurrency", "blockchain_finance", "defi_protocol", "smart_contract_finance",
    "stablecoin", "tokenization", "nft_finance", "dao_governance", "yield_farming",
    "liquidity_pool", "automated_market", "lending_protocol", "borrowing_protocol", "staking_mechanism",
    "insurance_underwriting", "life_insurance", "health_insurance", "property_insurance", "liability_insurance",
    "reinsurance", "actuarial_science", "premium_calculation", "loss_reserving", "claims_management",
    "catastrophe_model", "longevity_risk", "mortality_table", "policy_valuation", "surplus_management",
    "real_estate_finance", "mortgage_type", "commercial_loan", "residential_loan", "construction_loan",
    "reit_analysis", "property_valuation", "cap_rate", "cash_on_cash", "equity_multiple",
    "lease_analysis", "tenant_credit", "occupancy_cost", "development_appraisal", "land_valuation",
    "personal_finance", "retirement_plan", "estate_planning", "tax_planning", "budget_management",
    "debt_management", "credit_score", "mortgage_broker", "financial_advisor", "wealth_management",
    "robo_advisor", "portfolio_optimization", "asset_allocation", "rebalancing_strategy", "tax_loss_harvest",
    "behavioral_finance", "prospect_theory", "herd_behavior", "market_anomaly", "calendar_effect",
    "momentum_effect", "value_effect", "size_effect", "low_beta_anomaly", "quality_factor",
    "factor_investing", "smart_beta", "style_premium", "carry_trade", "volatility_risk_premium",
    "economic_indicator", "gdp_forecast", "cpi_index", "ppi_index", "unemployment_rate",
    "consumer_confidence", "business_confidence", "pmi_index", "industrial_production", "capacity_utilization",
    "housing_start", "building_permit", "retail_sales", "durable_goods", "trade_balance",
    "current_account", "capital_account", "foreign_reserve", "sovereign_wealth", "development_bank",
    "microfinance", "sustainable_finance", "green_bond", "social_bond", "impact_investing",
    "esg_score", "carbon_footprint_finance", "climate_risk_finance", "transition_finance", "blue_finance",
    "payment_system", "mobile_payment", "digital_wallet", "remittance_service", "cross_border_payment",
    "open_banking", "payment_gateway", "merchant_account", "pos_system", "billing_system",
]

random.shuffle(TOPICS25)
random.shuffle(TOPICS26)

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
            frng = random.Random(hash(spec + "v5.2.0") % (2**31))
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

generate_bulk("data_bulk25.py", TOPICS25)
generate_bulk("data_bulk26.py", TOPICS26)
