"""Generate data_bulk8.py: 100 data functions, 1000 entries each, ~100K lines."""
import random

random.seed(2024)

NAMES = "Arlo,Bina,Cade,Dory,Elan,Faye,Gael,Hera,Ivo,Jyn,Kael,Lura,Mace,Nyx,Oona,Pace,Qira,Rune,Sage,Thor,Ula,Veda,Wren,Xion,Yuki,Ziva,Asha,Bram,Cora,Dax".split(",")
SURNAMES = "Aster,Brick,Crest,Drake,Ember,Frost,Grove,Haven,Isle,Jasper,Kelp,Leaf,Mist,Nyx,Onyx,Peak,Quill,Ridge,Slate,Tide,Umber,Veil,Wave,Yarn,Zion,Ash,Birch,Cove,Dune,Elm".split(",")
ADJ = "Azure,Beryl,Coral,Dew,Ember,Frost,Gleam,Haze,Ivory,Jet,Khaki,Lime,Mauve,Navy,Onyx,Plum,Quartz,Rust,Silver,Taupe,Ultra,Teal,Wine,Xenon,Yellow,Zinc,Amber,Blush,Cream,Dusk".split(",")
NOUN = "Arch,Beak,Cove,Dell,Edge,Fjord,Glen,Hill,Inlet,Jamb,Knoll,Lea,Moor,Nook,Ore,Pike,Quay,Reef,Shaw,Tarn,Urn,Vale,Wick,Yard,Zone,Abbey,Brook,Crest,Dune,Erne".split(",")

def rand_name():
    return random.choice(NAMES) + " " + random.choice(SURNAMES)

def rand_title():
    return "The " + random.choice(ADJ) + " " + random.choice(NOUN)

FUNCTION_SPECS = [
    ("quantum_computer", ["Name", "Developer", "Year", "Qubits"]),
    ("particle_accelerator", ["Name", "Location", "Energy", "Type"]),
    ("fusion_reactor", ["Name", "Country", "Year", "Method"]),
    ("solar_farm", ["Name", "Country", "Capacity", "Area"]),
    ("wind_farm", ["Name", "Country", "Capacity", "Turbines"]),
    ("hydroelectric_dam", ["Name", "Country", "Capacity", "River"]),
    ("nuclear_power_plant", ["Name", "Country", "Reactors", "Output"]),
    ("geothermal_plant", ["Name", "Country", "Capacity", "Depth"]),
    ("wave_energy_device", ["Name", "Country", "Capacity", "Type"]),
    ("battery_factory", ["Name", "Country", "Capacity", "Year"]),
    ("desalination_plant", ["Name", "Country", "Capacity", "Method"]),
    ("water_treatment_facility", ["Name", "City", "Capacity", "Method"]),
    ("recycling_center", ["Name", "City", "Capacity", "Materials"]),
    ("waste_to_energy", ["Name", "City", "Capacity", "Year"]),
    ("green_hydrogen_plant", ["Name", "Country", "Capacity", "Year"]),
    ("carbon_capture_facility", ["Name", "Country", "Capacity", "Method"]),
    ("smart_city_project", ["Name", "Country", "Population", "Features"]),
    ("vertical_farm", ["Name", "City", "Area", "Crops"]),
    ("aquaponics_system", ["Name", "Country", "Area", "Fish"]),
    ("lab_grown_meat_company", ["Name", "Country", "Founded", "Product"]),
    ("plant_based_brand", ["Name", "Country", "Founded", "Product"]),
    ("precision_agriculture", ["Name", "Country", "Crop", "Technology"]),
    ("autonomous_tractor", ["Name", "Manufacturer", "Year", "Power"]),
    ("drone_delivery_service", ["Name", "Country", "Founded", "Range"]),
    ("electric_aircraft", ["Name", "Manufacturer", "Year", "Range"]),
    ("hyperloop_project", ["Name", "Country", "Speed", "Status"]),
    ("maglev_train", ["Name", "Country", "Speed", "Opened"]),
    ("autonomous_bus", ["Name", "Manufacturer", "Year", "Capacity"]),
    ("electric_ferry", ["Name", "Country", "Year", "Capacity"]),
    ("cargo_drone", ["Name", "Manufacturer", "Payload", "Range"]),
    ("space_tourism_company", ["Name", "Country", "Founded", "Price"]),
    ("orbital_hotel", ["Name", "Company", "Capacity", "Target"]),
    ("mars_habitat_design", ["Name", "Agency", "Capacity", "Year"]),
    ("lunar_base_plan", ["Name", "Agency", "Crew", "Year"]),
    ("asteroid_mining_venture", ["Name", "Company", "Target", "Year"]),
    ("space_elevator_concept", ["Name", "Designer", "Length", "Material"]),
    ("solar_sail_mission", ["Name", "Agency", "Year", "Size"]),
    ("quantum_satellite", ["Name", "Agency", "Year", "Purpose"]),
    ("internet_satellite_constellation", ["Name", "Company", "Satellites", "Year"]),
    ("ai_chip", ["Name", "Manufacturer", "Year", "Performance"]),
    ("quantum_processor", ["Name", "Developer", "Qubits", "Year"]),
    ("neuromorphic_chip", ["Name", "Developer", "Neurons", "Year"]),
    ("dna_computer", ["Name", "Developer", "Year", "Application"]),
    ("optical_computer", ["Name", "Developer", "Year", "Speed"]),
    ("brain_computer_interface", ["Name", "Company", "Year", "Type"]),
    ("neural_implant", ["Name", "Company", "Year", "Application"]),
    ("bionic_limb", ["Name", "Company", "Year", "Type"]),
    ("artificial_organ", ["Name", "Developer", "Year", "Organ"]),
    ("gene_therapy", ["Name", "Company", "Year", "Target"]),
    ("crispr_application", ["Name", "Researcher", "Year", "Target"]),
    ("mrna_vaccine", ["Name", "Developer", "Year", "Target"]),
    ("cancer_treatment", ["Name", "Company", "Year", "Type"]),
    ("personalized_medicine", ["Name", "Company", "Year", "Approach"]),
    ("digital_twin_platform", ["Name", "Developer", "Year", "Industry"]),
    ("blockchain_protocol", ["Name", "Developer", "Year", "Consensus"]),
    ("defi_platform", ["Name", "Developer", "Year", "Type"]),
    ("nft_marketplace", ["Name", "Platform", "Year", "Category"]),
    ("metaverse_platform", ["Name", "Developer", "Year", "Type"]),
    ("vr_headset", ["Name", "Manufacturer", "Year", "Resolution"]),
    ("ar_glasses", ["Name", "Manufacturer", "Year", "Field"]),
    ("haptic_suit", ["Name", "Developer", "Year", "Actuators"]),
    ("exoskeleton", ["Name", "Developer", "Year", "Application"]),
    ("robotic_surgical_system", ["Name", "Company", "Year", "Specialty"]),
    ("nanorobot_platform", ["Name", "Developer", "Year", "Application"]),
    ("autonomous_warehouse", ["Name", "Company", "Year", "Capacity"]),
    ("delivery_robot", ["Name", "Manufacturer", "Year", "Payload"]),
    ("humanoid_robot", ["Name", "Developer", "Year", "Height"]),
    ("social_robot", ["Name", "Developer", "Year", "Capability"]),
    ("swarm_robot_system", ["Name", "Developer", "Year", "SwarmSize"]),
    ("underwater_drone", ["Name", "Manufacturer", "Depth", "Year"]),
    ("agricultural_robot", ["Name", "Manufacturer", "Year", "Task"]),
    ("construction_robot", ["Name", "Manufacturer", "Year", "Task"]),
    ("lab_automation_robot", ["Name", "Developer", "Year", "Throughput"]),
    ("quantum_sensor", ["Name", "Developer", "Year", "Sensitivity"]),
    ("lidar_system", ["Name", "Manufacturer", "Year", "Range"]),
    ("hyperspectral_imager", ["Name", "Developer", "Year", "Bands"]),
    ("gravity_telescope", ["Name", "Agency", "Year", "Sensitivity"]),
    ("neutrino_detector", ["Name", "Collaboration", "Location", "Year"]),
    ("dark_matter_experiment", ["Name", "Collaboration", "Location", "Year"]),
    ("quantum_network", ["Name", "Developer", "Year", "Nodes"]),
    ("quantum_repeater", ["Name", "Developer", "Year", "Distance"]),
    ("photonic_chip", ["Name", "Developer", "Year", "Speed"]),
    ("topological_insulator", ["Name", "Lab", "Year", "Material"]),
    ("superconducting_material", ["Name", "Lab", "Year", "Tc"]),
    ("metamaterial", ["Name", "Lab", "Year", "Property"]),
    ("aerogel_production", ["Name", "Company", "Year", "Density"]),
    ("graphene_application", ["Name", "Developer", "Year", "Application"]),
    ("self_healing_material", ["Name", "Developer", "Year", "Application"]),
    ("shape_memory_alloy", ["Name", "Developer", "Year", "Application"]),
    ("4d_printing_technology", ["Name", "Developer", "Year", "Material"]),
    ("bioprinting_platform", ["Name", "Company", "Year", "Tissue"]),
    ("organoid_technology", ["Name", "Lab", "Year", "Type"]),
    ("synthetic_biology", ["Name", "Company", "Year", "Application"]),
    ("algae_biofuel", ["Name", "Company", "Year", "Yield"]),
    ("microbial_fuel_cell", ["Name", "Lab", "Year", "Output"]),
    ("smart_window_technology", ["Name", "Company", "Year", "Type"]),
    ("thermoelectric_material", ["Name", "Lab", "Year", "Efficiency"]),
    ("perovskite_solar_cell", ["Name", "Lab", "Year", "Efficiency"]),
    ("quantum_dot_display", ["Name", "Company", "Year", "Size"]),
    ("micro_led_display", ["Name", "Company", "Year", "Pitch"]),
    ("flexible_screen", ["Name", "Company", "Year", "Type"]),
    ("e_ink_technology", ["Name", "Company", "Year", "Color"]),
    ("holographic_display", ["Name", "Company", "Year", "Resolution"]),
    ("laser_projector", ["Name", "Company", "Year", "Brightness"]),
    ("light_field_camera", ["Name", "Company", "Year", "Megapixels"]),
    ("computational_photography", ["Name", "Company", "Year", "Feature"]),
]

random.shuffle(FUNCTION_SPECS)
specs = FUNCTION_SPECS[:100]

ENTRIES = 1000
lines = 0

with open("../datab/data_bulk8.py", "w", encoding="utf-8") as f:
    f.write('"""data_bulk8.py: 100 auto-generated data functions, 1000 entries each, ~100K lines."""\n')
    f.write("import random\n\n")

    for func_name, fields in specs:
        rng = random.Random(hash(func_name + "v4.5.0.8") % (2**31))

        f.write("\ndef get_{}_data():\n".format(func_name))
        f.write('    """Return {} entries of {} data."""\n'.format(ENTRIES, func_name.replace("_", " ")))
        f.write("    return [\n")

        for i in range(ENTRIES):
            if func_name in ("quantum_computer", "quantum_processor"):
                vals = (rand_title(), random.choice(["IBM","Google","Microsoft","Rigetti","IonQ","D-Wave","Xanadu","Quantinuum","Intel","Honeywell"]), str(rng.randint(2010, 2026)), str(rng.randint(5, 5000)) + " qubits")
            elif func_name in ("fusion_reactor",):
                vals = (rand_title(), random.choice(["USA","China","UK","France","Germany","Japan","South Korea","Russia","Canada","Italy"]), str(rng.randint(2010, 2030)), random.choice(["Tokamak","Stellarator","Laser Inertial","Magnetized Target","Reverse Field"]))
            elif func_name in ("ai_chip",):
                vals = (rand_title(), random.choice(["NVIDIA","AMD","Intel","Google","Apple","Qualcomm","Samsung","Cerebras","Graphcore","Tesla"]), str(rng.randint(2015, 2026)), str(rng.randint(10, 2000)) + " TFLOPS")
            elif func_name in ("space_tourism_company",):
                vals = (rand_title(), random.choice(["USA","China","UK","Russia","India","Japan","UAE","Germany","France","Australia"]), str(rng.randint(1990, 2025)), "$" + str(rng.randint(10000, 50000000)))
            elif func_name in ("neural_implant", "brain_computer_interface"):
                vals = (rand_title(), random.choice(["Neuralink","Synchron","Blackrock Neurotech","Kernel","MindX","Paradromics","NeuroSky","Emotiv","NextMind","BrainCo"]), str(rng.randint(2015, 2026)), random.choice(["Invasive","Semi-invasive","Non-invasive","EEG","ECoG"]))
            elif func_name in ("crispr_application", "gene_therapy"):
                vals = (rand_title(), random.choice(["Editas","Intellia","CRISPR Therapeutics","Beam Therapeutics","Mammoth","Caribou","Synthego","Pairwise","Inari","Verve"]), str(rng.randint(2012, 2026)), random.choice(["Cancer","Sickle Cell","Blindness","Cystic Fibrosis","Muscular Dystrophy","HIV","Diabetes","Alzheimer's","Liver Disease","Blood Disorder"]))
            elif func_name in ("humanoid_robot",):
                vals = (rand_title(), random.choice(["Boston Dynamics","Tesla","Honda","SoftBank","Samsung","Xiaomi","Figure AI","1X Technologies","Agility Robotics","Fourier Intelligence"]), str(rng.randint(2010, 2026)), str(round(rng.uniform(1.2, 2.0), 2)) + " m")
            elif func_name in ("solar_farm", "wind_farm", "hydroelectric_dam", "nuclear_power_plant"):
                vals = (rand_title(), random.choice(["China","USA","India","Brazil","Canada","Germany","France","Australia","Spain","UK"]), str(rng.randint(1960, 2025)), str(rng.randint(50, 10000)) + " MW")
            elif func_name in ("quantum_satellite", "internet_satellite_constellation"):
                vals = (rand_title(), random.choice(["SpaceX","OneWeb","Amazon","Telesat","ESA","NASA","CNSA","ISRO","Northrop","Lockheed"]), str(rng.randint(100, 42000)), str(rng.randint(2015, 2026)))
            elif func_name in ("vr_headset", "ar_glasses", "haptic_suit"):
                vals = (rand_title(), random.choice(["Meta","Apple","HTC","Valve","Sony","Pico","Samsung","Microsoft","Magic Leap","Varjo"]), str(rng.randint(2014, 2026)), str(rng.randint(1024, 8192)) + "x" + str(rng.randint(1024, 8192)))
            else:
                vals = (rand_title(), random.choice(["Global","Western","Eastern","American","European","Asian","Pacific","African","Nordic","Southern"]), str(rng.randint(1990, 2026)), random.choice(["Alpha","Beta","Production","Concept","Prototype","Research","Commercial","Open Source","Patent","Standard"]))

            formatted = ", ".join('"{}"'.format(str(v).replace('"', "'")) for v in vals)
            f.write("        ({})".format(formatted))
            if i < ENTRIES - 1:
                f.write(",\n")
            else:
                f.write(",\n")

        f.write("    ]\n")
        lines += 3 + ENTRIES

import os
total = os.path.getsize("data_bulk8.py") if os.path.exists("data_bulk8.py") else 0
print("Generated data_bulk8.py: {} functions, ~{} lines, {:.1f} KB".format(len(specs), lines, total/1024))
