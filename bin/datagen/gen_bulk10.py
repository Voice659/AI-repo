"""Generate data_bulk10.py: 100 data functions, 1000 entries each, ~100K lines."""
import random

random.seed(3030)

NAMES = "Arden,Blake,Corin,Dara,Elric,Fenn,Galen,Hale,Irvin,Jace,Kael,Lira,Myra,Nick,Orin,Phae,Quinn,Reed,Shae,Torin,Urien,Vance,Wynn,Xanthe,Yates,Zane,Asher,Brynn,Clive,Dante".split(",")
SURNAMES = "Ashford,Blackwood,Castlewood,Dunwich,Eastwick,Fellwood,Greyhawk,Holloway,Ironwood,Jaywick,Knightly,Langley,Moorcroft,Netherby,Olney,Pemberly,Quimby,Ravenscroft,Stanhope,Tilbury,Underwood,Valebrook,Westwick,Ashby,Brackley,Cromwell,Danbury,Eldridge,Farnham,Glendower".split(",")

def rand_name():
    return random.choice(NAMES) + " " + random.choice(SURNAMES)

def rand_title():
    return "The " + random.choice(NAMES) + " " + random.choice(SURNAMES)

FUNCTION_SPECS = [
    ("arctic_expedition", ["Name", "Leader", "Year", "Result"]),
    ("antarctic_station", ["Name", "Country", "Opened", "Capacity"]),
    ("deep_sea_mission", ["Name", "Depth", "Year", "Vehicle"]),
    ("cave_exploration", ["Name", "Depth", "Location", "Length"]),
    ("desert_crossing", ["Name", "Explorer", "Year", "Desert"]),
    ("jungle_expedition", ["Name", "Leader", "Year", "Region"]),
    ("mountain_ascent", ["Peak", "Height", "FirstAscent", "Range"]),
    ("volcano_expedition", ["Name", "Height", "LastEruption", "Type"]),
    ("river_source_discovery", ["River", "Source", "Length", "Country"]),
    ("underwater_cave", ["Name", "Location", "Length", "Depth"]),
    ("space_observatory", ["Name", "Location", "Altitude", "Telescope"]),
    ("radio_observatory", ["Name", "Location", "Dishes", "Year"]),
    ("neutrino_observatory", ["Name", "Location", "Depth", "Year"]),
    ("gravitational_wave_detector", ["Name", "Location", "Year", "Type"]),
    ("cosmic_ray_station", ["Name", "Altitude", "Country", "Year"]),
    ("weather_station", ["Name", "Location", "Elevation", "Year"]),
    ("climate_research_station", ["Name", "Location", "Year", "Focus"]),
    ("ice_core_drill_site", ["Name", "Location", "Depth", "Year"]),
    ("ocean_buoy_network", ["Name", "Region", "Buoys", "Year"]),
    ("seismic_station", ["Name", "Location", "Sensors", "Network"]),
    ("tide_gauge_station", ["Name", "Location", "Year", "DataSince"]),
    ("air_quality_monitor", ["City", "Country", "Year", "Pollutants"]),
    ("wildlife_tracking_project", ["Name", "Species", "Region", "Year"]),
    ("bird_migration_study", ["Species", "Route", "Distance", "Year"]),
    ("marine_biology_station", ["Name", "Location", "Year", "Focus"]),
    ("coral_reef_monitoring", ["Name", "Reef", "Country", "Year"]),
    ("forest_ecology_plot", ["Name", "Location", "Area", "Year"]),
    ("soil_sampling_project", ["Name", "Region", "Samples", "Year"]),
    ("archaeological_dig", ["Name", "Location", "Period", "Year"]),
    ("paleontological_site", ["Name", "Location", "Era", "Fossils"]),
    ("underwater_archaeology", ["Site", "Location", "Period", "Artifacts"]),
    ("space_archaeology", ["Site", "Location", "Method", "Findings"]),
    ("cultural_heritage_survey", ["Name", "Country", "Year", "Sites"]),
    ("oral_history_project", ["Name", "Community", "Year", "Stories"]),
    ("language_documentation", ["Language", "Country", "Speakers", "Status"]),
    ("dialect_survey", ["Dialect", "Region", "Speakers", "Year"]),
    ("folk_music_archive", ["Name", "Country", "Recordings", "Year"]),
    ("traditional_craft_study", ["Craft", "Region", "Practitioners", "Status"]),
    ("indigenous_knowledge_project", ["Name", "Community", "Year", "Focus"]),
    ("ethnobotanical_study", ["Plant", "Culture", "Use", "Region"]),
    ("ethnomedicine_research", ["Name", "Culture", "Ailment", "Remedy"]),
    ("food_anthropology_study", ["Dish", "Culture", "Year", "Significance"]),
    ("ritual_study", ["Ritual", "Culture", "Type", "Frequency"]),
    ("kinship_system_study", ["System", "Culture", "Type", "Region"]),
    ("mythology_comparison", ["Myth", "FirstCulture", "SecondCulture", "Theme"]),
    ("symbolism_study", ["Symbol", "Culture", "Meaning", "Context"]),
    ("pilgrimage_study", ["Destination", "Religion", "Annual", "Significance"]),
    ("festival_documentation", ["Name", "Country", "Month", "Observances"]),
    ("performance_study", ["Form", "Culture", "Type", "Practitioners"]),
    ("storytelling_tradition", ["Name", "Culture", "Format", "Themes"]),
    ("nursery_rhyme_history", ["Name", "Origin", "FirstRecorded", "Meaning"]),
    ("fairy_tale_variant", ["Title", "Culture", "Collector", "Year"]),
    ("epic_poem", ["Title", "Culture", "Verses", "Era"]),
    ("fable_collection", ["Title", "Author", "Year", "Themes"]),
    ("proverb_study", ["Proverb", "Culture", "Meaning", "Equivalent"]),
    ("riddle_tradition", ["Name", "Culture", "Type", "Examples"]),
    ("tongue_twister", ["Name", "Language", "Difficulty", "Origin"]),
    ("word_game", ["Name", "Culture", "Type", "Players"]),
    ("board_game_history", ["Name", "Origin", "Year", "Players"]),
    ("card_game", ["Name", "Origin", "Players", "Deck"]),
    ("dice_game", ["Name", "Culture", "Dice", "Players"]),
    ("sport_ancient", ["Name", "Origin", "Equipment", "Objective"]),
    ("martial_art", ["Name", "Origin", "Founder", "Style"]),
    ("traditional_dance_martial", ["Name", "Origin", "Type", "Purpose"]),
    ("acrobatic_tradition", ["Name", "Culture", "Type", "Skills"]),
    ("circus_act", ["Name", "Type", "Year", "Company"]),
    ("puppetry_tradition", ["Name", "Culture", "Type", "Material"]),
    ("theater_form", ["Name", "Origin", "Type", "Elements"]),
    ("opera_style", ["Name", "Origin", "Era", "Composers"]),
    ("musical_instrument_woodwind", ["Name", "Origin", "Material", "Range"]),
    ("musical_instrument_string", ["Name", "Origin", "Strings", "Technique"]),
    ("musical_instrument_percussion", ["Name", "Origin", "Material", "Technique"]),
    ("musical_instrument_brass", ["Name", "Origin", "Material", "Range"]),
    ("musical_instrument_keyboard", ["Name", "Origin", "Mechanism", "Range"]),
    ("musical_instrument_electronic", ["Name", "Inventor", "Year", "Sound"]),
    ("music_notation_system", ["Name", "Origin", "Era", "Elements"]),
    ("scale_type", ["Name", "Intervals", "Origin", "Mood"]),
    ("rhythm_pattern", ["Name", "Origin", "TimeSig", "Dance"]),
    ("harmony_concept", ["Name", "Era", "Theory", "Composers"]),
    ("counterpoint_style", ["Name", "Era", "Rules", "Composers"]),
    ("improvisation_style", ["Name", "Genre", "Origin", "Technique"]),
    ("singing_technique", ["Name", "Culture", "Type", "Range"]),
    ("vocal_style", ["Name", "Genre", "Origin", "Characteristics"]),
    ("choir_type", ["Name", "Voices", "Repertoire", "Setting"]),
    ("recording_format", ["Name", "Inventor", "Year", "Capacity"]),
    ("audio_compression", ["Name", "Year", "Bitrate", "Quality"]),
    ("sound_synthesis", ["Name", "Inventor", "Year", "Method"]),
    ("music_player", ["Name", "Manufacturer", "Year", "Storage"]),
    ("headphone_design", ["Name", "Manufacturer", "Year", "Type"]),
    ("speaker_technology", ["Name", "Inventor", "Year", "Principle"]),
    ("microphone_type", ["Name", "Inventor", "Year", "PolarPattern"]),
    ("amplifier_design", ["Name", "Inventor", "Year", "Type"]),
    ("equalizer_type", ["Name", "Inventor", "Year", "Bands"]),
    ("effect_pedal", ["Name", "Inventor", "Year", "Effect"]),
    ("studio_monitor", ["Name", "Manufacturer", "Year", "Size"]),
    ("mixing_console", ["Name", "Manufacturer", "Year", "Channels"]),
    ("digital_audio_workstation", ["Name", "Developer", "Year", "Platform"]),
    ("music_copyright", ["Name", "Year", "Territory", "Duration"]),
    ("performance_rights", ["Organization", "Country", "Founded", "Members"]),
    ("music_award", ["Name", "Country", "Category", "Prize"]),
    ("music_venue", ["Name", "City", "Capacity", "Opened"]),
    ("record_label_type", ["Name", "Country", "Founded", "Genre"]),
    ("music_streaming_service", ["Name", "Country", "Year", "Subscribers"]),
]

random.shuffle(FUNCTION_SPECS)
specs = FUNCTION_SPECS[:100]

ENTRIES = 1000
lines = 0

with open("../datab/data_bulk10.py", "w", encoding="utf-8") as f:
    f.write('"""data_bulk10.py: 100 auto-generated data functions, 1000 entries each, ~100K lines."""\n')
    f.write("import random\n\n")

    for func_name, fields in specs:
        rng = random.Random(hash(func_name + "v4.5.0.10") % (2**31))

        f.write("\ndef get_{}_data():\n".format(func_name))
        f.write('    """Return {} entries of {} data."""\n'.format(ENTRIES, func_name.replace("_", " ")))
        f.write("    return [\n")

        for i in range(ENTRIES):
            if func_name in ("arctic_expedition", "antarctic_station"):
                vals = (rand_title(), random.choice(["UK","Norway","USA","Russia","Canada","Australia","Japan","Germany","France","Italy"]), str(rng.randint(1800, 2024)), random.choice(["Successful","Failed","Lost","Abandoned","Resupplied","First to Pole","Scientific","Mapping","Rescue","Wintering"]))
            elif func_name in ("deep_sea_mission", "underwater_cave"):
                vals = (rand_title(), str(rng.randint(1000, 11000)) + " m", str(rng.randint(1960, 2024)), random.choice(["Bathysphere","Submersible","ROV","AUV","Bathyscaphe","HOV","DSV","Atmospheric Suit","Rebreather","NOAA Ship"]))
            elif func_name in ("mountain_ascent",):
                vals = (rand_title(), str(rng.randint(4000, 8849)) + " m", str(rng.randint(1700, 2024)), random.choice(["Himalayas","Andes","Alps","Karakoram","Pamir","Tian Shan","Caucasus","Rockies","Ruwenzori","Ethiopian Highlands"]))
            elif func_name in ("ice_core_drill_site", "climate_research_station"):
                vals = (rand_title(), random.choice(["Greenland","Antarctica","Alps","Andes","Himalayas","Iceland","Svalbard","Siberia","Alaska","Patagonia"]), str(rng.randint(1950, 2024)), random.choice(["Temperature","CO2","Methane","Isotopes","Dust","Pollutants","Ash","Pollen","Accumulation","Dating"]))
            elif func_name in ("space_observatory", "radio_observatory"):
                vals = (rand_title(), random.choice(["Chile","Hawaii","Canary Islands","Arizona","South Africa","Australia","Tibet","India","Mexico","Spain"]), str(rng.randint(3000, 15000)) + " m", str(rng.randint(1, 100)) + "m " + random.choice(["Optical","Infrared","Radio","UV","Solar","Wide Field","Adaptive","Robotic","Interferometer","Survey"]))
            elif func_name in ("archaeological_dig",):
                vals = (rand_title(), random.choice(["Egypt","Peru","Greece","Italy","Turkey","China","Mexico","Iraq","Jordan","India"]), random.choice(["Neolithic","Bronze","Iron","Classical","Medieval","Pre-Columbian","Roman","Byzantine","Viking","Paleolithic"]), str(rng.randint(1800, 2024)))
            elif func_name in ("language_documentation",):
                vals = (random.choice(["Ainu","Basque","Nahuatl","Quechua","Sami","Welsh","Breton","Yoruba","Hausa","Zulu","Navajo","Cherokee","Inuit","Maori","Maya"]), random.choice(["Mexico","Peru","Canada","USA","Nigeria","South Africa","New Zealand","Japan","Spain","UK"]), str(rng.randint(100, 10000000)), random.choice(["Endangered","Vital","Developing","Extinct","Dormant","Revived","Stable","Threatened","Moribund","Relocated"]))
            elif func_name in ("musical_instrument_string", "musical_instrument_woodwind", "musical_instrument_percussion", "musical_instrument_brass", "musical_instrument_keyboard", "musical_instrument_electronic"):
                vals = (rand_title(), random.choice(["Africa","Asia","Europe","Americas","Middle East","Oceania"]), random.choice(["Wood","Metal","Bone","Skin","Synthetic","Bamboo","Gourd","Silk","Stone","Clay"]), str(rng.randint(2, 72)) + " " + random.choice(["notes","keys","strings","sensors","plates","bars","pads","holes","reeds","tubes"]))
            elif func_name in ("music_streaming_service",):
                vals = (rand_title(), random.choice(["USA","Sweden","UK","Germany","China","Japan","India","Brazil","France","Australia"]), str(rng.randint(2000, 2020)), str(rng.randint(1, 500)) + "M")
            elif func_name in ("board_game_history",):
                vals = (rand_title(), random.choice(["China","India","Egypt","Mesopotamia","Greece","Rome","Japan","Europe","Germany","USA"]), str(rng.randint(-3000, 2000)), str(rng.randint(2, 8)))
            else:
                vals = (rand_title(), random.choice(["Global","Western","Eastern","Northern","Southern","American","European","Asian","Pacific","African"]), str(rng.randint(-2000, 2025)), random.choice(["Category 1","Category 2","Category 3","Category 4","Classic","Modern","Traditional","Contemporary","Standard","Premium"]))

            formatted = ", ".join('"{}"'.format(str(v).replace('"', "'")) for v in vals)
            f.write("        ({})".format(formatted))
            if i < ENTRIES - 1:
                f.write(",\n")
            else:
                f.write(",\n")

        f.write("    ]\n")
        lines += 3 + ENTRIES

import os
total = os.path.getsize("data_bulk10.py") if os.path.exists("data_bulk10.py") else 0
print("Generated data_bulk10.py: {} functions, ~{} lines, {:.1f} KB".format(len(specs), lines, total/1024))
