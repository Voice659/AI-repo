"""Generate data_bulk6.py: 100 data functions, 1000 entries each, ~100K lines."""
import random

random.seed(456)

NAMES = "Aria,Bodhi,Cora,Dax,Elio,Faye,Gael,Hana,Iris,Jiro,Kai,Lena,Milo,Nava,Oren,Pia,Rio,Suki,Taro,Uma,Vida,Wren,Xia,Yuki,Zion,Aiko,Bencio,Cielo,Dario,Enya".split(",")
SURNAMES = "Stone,Woods,Cross,Bridge,Ford,Frost,Glen,Hart,Kent,Lake,Moore,Parks,Reef,Ridge,Shore,Vale,Wells,Wolfe,Yard,Zorn,Ash,Blake,Chase,Drake,Elm,Fox,Gale,Hale,Ivy,Jade".split(",")

ADJ = "Bright,Crystal,Deep,Elastic,Frozen,Gleaming,Hidden,Icy,Jade,Keen,Lunar,Misty,Noble,Opal,Pearly,Quiet,Rich,Silent,Tender,Urban,Vivid,Warm,Xeric,Yellow,Zesty,Amber,Blush,Crisp,Dusky,Ember".split(",")
NOUN = "Arch,Beam,Bell,Cliff,Dawn,Edge,Flame,Gate,Heath,Isle,Jade,Knoll,Light,Meadow,Node,Oasis,Peak,Quay,Reach,Spire,Thorn,Urn,Vale,Wave,Yard,Zone,Arbor,Brook,Cove,Dune".split(",")

def rand_name():
    return random.choice(NAMES) + " " + random.choice(SURNAMES)

def rand_title():
    return "The " + random.choice(ADJ) + " " + random.choice(NOUN)

FUNCTION_SPECS = [
    ("ocean_trench", ["Name", "Ocean", "Depth", "Length"]),
    ("famous_volcano_eruption", ["Name", "Location", "Year", "VEI"]),
    ("underwater_volcano", ["Name", "Ocean", "Height", "Status"]),
    ("famous_earthquake_zone", ["Name", "Region", "LastMajor", "Risk"]),
    ("tidal_wave_event", ["Name", "Location", "Year", "Height"]),
    ("world_weather_phenomenon", ["Name", "Type", "Location", "Season"]),
    ("famous_cloud_type", ["Name", "Altitude", "Precipitation", "Symbol"]),
    ("wind_pattern", ["Name", "Region", "Speed", "Direction"]),
    ("famous_climate_zone", ["Name", "Latitude", "Temp", "Precipitation"]),
    ("world_biome", ["Name", "Climate", "Flora", "Fauna"]),
    ("famous_ecoregion", ["Name", "Continent", "Area", "Status"]),
    ("endemic_species", ["Name", "Location", "Type", "Status"]),
    ("world_migratory_bird", ["Name", "Route", "Distance", "Season"]),
    ("famous_marine_mammal", ["Name", "Ocean", "Population", "Status"]),
    ("deep_sea_creature", ["Name", "Depth", "Size", "Feature"]),
    ("famous_coral_species", ["Name", "Ocean", "Depth", "Color"]),
    ("world_seagrass_meadow", ["Name", "Location", "Area", "Species"]),
    ("famous_kelp_forest", ["Name", "Location", "Depth", "Species"]),
    ("world_mangrove_species", ["Name", "Region", "Height", "Type"]),
    ("famous_estuary", ["Name", "River", "Location", "Area"]),
    ("world_lagoon", ["Name", "Location", "Area", "Depth"]),
    ("famous_salt_flat", ["Name", "Country", "Area", "Elevation"]),
    ("world_desert_dune", ["Name", "Desert", "Height", "Type"]),
    ("famous_oasis", ["Name", "Desert", "Area", "Water"]),
    ("world_badland", ["Name", "Location", "Area", "Formation"]),
    ("famous_mesa", ["Name", "Location", "Height", "Area"]),
    ("world_butte", ["Name", "Location", "Height", "Type"]),
    ("famous_monolith", ["Name", "Location", "Height", "Material"]),
    ("world_natural_arch", ["Name", "Location", "Span", "Height"]),
    ("famous_blowhole", ["Name", "Location", "Height", "Frequency"]),
    ("world_sea_stack", ["Name", "Location", "Height", "Type"]),
    ("famous_cave_painting", ["Name", "Cave", "Year", "Culture"]),
    ("world_underground_river", ["Name", "Location", "Length", "Depth"]),
    ("famous_sinkhole", ["Name", "Location", "Depth", "Diameter"]),
    ("world_hot_spring_pool", ["Name", "Location", "Temp", "Mineral"]),
    ("famous_mud_volcano", ["Name", "Location", "Height", "Activity"]),
    ("world_ice_cave", ["Name", "Location", "Length", "IceAge"]),
    ("famous_lava_tube", ["Name", "Location", "Length", "Age"]),
    ("world_geothermal_field", ["Name", "Location", "Area", "Capacity"]),
    ("famous_petrified_forest", ["Name", "Location", "Area", "Age"]),
    ("world_fossil_reef", ["Name", "Location", "Age", "Type"]),
    ("famous_amber_deposit", ["Name", "Location", "Age", "Finds"]),
    ("world_trace_fossil_site", ["Name", "Location", "Period", "Type"]),
    ("famous_lagerstatte", ["Name", "Location", "Period", "Preservation"]),
    ("world_dinosaur_trackway", ["Name", "Location", "Period", "Length"]),
    ("famous_paleo_lake", ["Name", "Location", "Period", "Area"]),
    ("world_ancient_reef", ["Name", "Location", "Period", "Type"]),
    ("famous_coal_forest", ["Name", "Location", "Period", "Area"]),
    ("world_impact_crater_lake", ["Name", "Location", "Diameter", "Age"]),
    ("famous_meteorite_find", ["Name", "Location", "Mass", "Type"]),
    ("world_tektite_field", ["Name", "Location", "Age", "Type"]),
    ("famous_asteroid_belt_object", ["Name", "Diameter", "Type", "Discovery"]),
    ("world_comet", ["Name", "Period", "Discoverer", "LastSeen"]),
    ("famous_dwarf_planet", ["Name", "Orbit", "Diameter", "Discovered"]),
    ("world_moon_feature", ["Name", "Body", "Type", "Diameter"]),
    ("famous_lunar_sea", ["Name", "Location", "Diameter", "Type"]),
    ("world_martian_feature", ["Name", "Region", "Type", "Size"]),
    ("famous_venusian_feature", ["Name", "Region", "Type", "Size"]),
    ("world_jovian_moon", ["Name", "Planet", "Diameter", "Discovery"]),
    ("famous_saturnian_moon", ["Name", "Diameter", "Discovery", "Feature"]),
    ("world_space_mission", ["Name", "Agency", "Year", "Target"]),
    ("famous_telescope", ["Name", "Type", "Location", "Aperture"]),
    ("world_observatory_detail", ["Name", "Altitude", "Instruments", "Founded"]),
    ("famous_astronomer", ["Name", "Era", "Nationality", "Discovery"]),
    ("world_constellation_star", ["Name", "Magnitude", "Distance", "Type"]),
    ("famous_binary_star", ["Name", "Distance", "Period", "Type"]),
    ("world_nebula_detail", ["Name", "Distance", "Type", "Constellation"]),
    ("famous_galaxy_cluster", ["Name", "Distance", "Galaxies", "Constellation"]),
    ("world_quasar", ["Name", "Distance", "Luminosity", "Redshift"]),
    ("famous_pulsar", ["Name", "Distance", "Period", "Type"]),
    ("world_black_hole", ["Name", "Mass", "Distance", "Type"]),
    ("famous_exoplanet", ["Name", "Star", "Mass", "Distance"]),
    ("world_habitable_zone_planet", ["Name", "Star", "Radius", "ESI"]),
    ("famous_rogue_planet", ["Name", "Mass", "Distance", "Discovery"]),
    ("world_brown_dwarf", ["Name", "Mass", "Temp", "Discovery"]),
    ("famous_white_dwarf", ["Name", "Mass", "Temp", "Constellation"]),
    ("world_globular_cluster", ["Name", "Constellation", "Distance", "Stars"]),
    ("famous_open_cluster", ["Name", "Constellation", "Distance", "Stars"]),
    ("world_stellar_association", ["Name", "Constellation", "Distance", "Stars"]),
    ("famous_molecular_cloud", ["Name", "Constellation", "Mass", "Size"]),
    ("world_hii_region", ["Name", "Constellation", "Distance", "Size"]),
    ("famous_supernova_remnant", ["Name", "Constellation", "Age", "Size"]),
    ("world_gamma_ray_burst", ["Name", "Distance", "Duration", "Energy"]),
    ("famous_cosmic_ray_source", ["Name", "Type", "Energy", "Distance"]),
    ("world_neutrino_source", ["Name", "Type", "Energy", "Distance"]),
    ("famous_gravitational_wave", ["Name", "Distance", "Merger", "Year"]),
    ("world_dark_matter_halo", ["Name", "Galaxy", "Mass", "Radius"]),
    ("famous_cosmic_filament", ["Name", "Length", "Galaxies", "Constellation"]),
    ("world_void", ["Name", "Constellation", "Diameter", "Galaxies"]),
    ("famous_galaxy_supercluster", ["Name", "Distance", "Galaxies", "Diameter"]),
    ("world_archaeological_site", ["Name", "Country", "Period", "Type"]),
    ("famous_megalith", ["Name", "Location", "Mass", "Period"]),
    ("world_rock_art_site", ["Name", "Country", "Period", "Style"]),
    ("famous_burial_mound", ["Name", "Location", "Period", "Culture"]),
    ("world_ancient_temple", ["Name", "Civilization", "Year", "Deity"]),
    ("famous_ziggurat", ["Name", "Civilization", "Year", "City"]),
    ("world_amphitheater", ["Name", "Location", "Capacity", "Year"]),
    ("famous_ancient_theater", ["Name", "Location", "Capacity", "Year"]),
    ("world_hanging_garden_site", ["Name", "Location", "Period", "Type"]),
    ("famous_lighthouse_detail", ["Name", "Location", "Height", "Built"]),
    ("world_colossus", ["Name", "Location", "Height", "Material"]),
    ("famous_mausoleum", ["Name", "Location", "Year", "Architect"]),
]

# Shuffle and take 100
random.shuffle(FUNCTION_SPECS)
specs = FUNCTION_SPECS[:100]

ENTRIES = 1000
lines = 0

with open("data_bulk6.py", "w", encoding="utf-8") as f:
    f.write('"""data_bulk6.py: 100 auto-generated data functions, 1000 entries each, ~100K lines."""\n')
    f.write("import random\n\n")

    for func_name, fields in specs:
        suffix = "_data"
        rng = random.Random(hash(func_name + "v4.2.0") % (2**31))

        f.write("\ndef get_{}{}():\n".format(func_name, suffix))
        f.write('    """Return {} entries of {} data."""\n'.format(ENTRIES, func_name.replace("_", " ")))
        f.write("    return [\n")

        for i in range(ENTRIES):
            if func_name == "ocean_trench":
                vals = (rand_title() + " Trench", random.choice(["Pacific","Atlantic","Indian","Arctic","Southern"]), str(rng.randint(5000, 11000)) + " m", str(rng.randint(500, 5000)) + " km")
            elif func_name == "famous_volcano_eruption":
                vals = (rand_title(), random.choice(["Krakatoa","Vesuvius","Pinatubo","St Helens","Tambora","Etna","Eyjafjallajokull","Kilauea","Unzen","Pelée"]), str(rng.randint(79, 2024)), str(rng.randint(2, 8)))
            elif func_name == "underwater_volcano":
                vals = (rand_title(), random.choice(["Pacific","Atlantic","Indian","Mediterranean","Caribbean"]), str(rng.randint(500, 5000)) + " m", random.choice(["Active","Dormant","Extinct"]))
            elif func_name == "famous_earthquake_zone":
                vals = (rand_title() + " Zone", random.choice(["Ring of Fire","Alpine-Himalayan","Mid-Atlantic","East African","San Andreas"]), str(rng.randint(1900, 2024)), random.choice(["High","Moderate","Low","Extreme"]))
            elif func_name == "tidal_wave_event":
                vals = (rand_title(), random.choice(["Japan","Indonesia","Chile","Alaska","Portugal","India","Philippines","Peru","Mexico","Italy"]), str(rng.randint(1600, 2024)), str(rng.randint(1, 50)) + " m")
            elif func_name == "world_weather_phenomenon":
                vals = (rand_title(), random.choice(["El Niño","La Niña","Monsoon","Cyclone","Tornado","Derecho","Haboo","Polar Vortex","Heat Wave","Bomb Cyclone"]), random.choice(["Pacific","Atlantic","Asia","Americas","Africa"]), random.choice(["Winter","Spring","Summer","Fall","Year-round"]))
            else:
                vals = (rand_title(), random.choice(["Global","Pacific","Atlantic","Asia","Americas","Africa","Europe","Arctic","Antarctic","Indian"]), str(rng.randint(0, 2025)), random.choice(["Type A","Type B","Type C","Type D","Type E","Natural","Cultural","Historical","Scientific","Geological"]))

            formatted = ", ".join('"{}"'.format(str(v).replace('"', "'")) for v in vals)
            f.write("        ({})".format(formatted))
            if i < ENTRIES - 1:
                f.write(",\n")
            else:
                f.write(",\n")

        f.write("    ]\n")
        lines += 3 + ENTRIES

import os
total = os.path.getsize("data_bulk6.py") if os.path.exists("data_bulk6.py") else 0
print("Generated data_bulk6.py: {} functions, ~{} lines, {:.1f} KB".format(len(specs), lines, total/1024))
