"""Generate data_bulk7.py: 100 data functions, 1000 entries each, ~100K lines."""
import random

random.seed(789)

NAMES = "Asha,Beno,Calla,Dario,Enzo,Fia,Gino,Hana,Ilia,Javi,Kiana,Lino,Mira,Nila,Omar,Pia,Rina,Seno,Tino,Ula,Vita,Wilo,Xena,Yara,Zalo,Ami,Brio,Ciel,Dune,Elio".split(",")
SURNAMES = "Apex,Blake,Cove,Dune,Elm,Fern,Glen,Holm,Isle,Jade,Kelp,Linn,Moor,Nook,Orm,Pike,Quay,Reef,Shore,Tarn,Urn,Vale,Wold,Xen,Yard,Zion,Atoll,Bight,Chine,Dale".split(",")

ADJ = "Amber,Beryl,Coral,Dewy,Ebony,Frosty,Gleam,Hazel,Indigo,Jade,Khaki,Lilac,Mauve,Navy,Olive,Peridot,Quartz,Rose,Sepia,Taupe,Umber,Violet,Wheat,Xanthic,Yellow,Zaffre,Azure,Blush,Crimson,Dun".split(",")
NOUN = "Arch,Bank,Cove,Dell,Edge,Firth,Gate,Heath,Inlet,Jamb,Knoll,Lea,Moor,Ness,Ore,Pike,Quay,Ree,Shaw,Tarn,Urn,Vale,Wick,Yard,Zone,Abbey,Brook,Croft,Dune,Erne".split(",")

def rand_name():
    return random.choice(NAMES) + " " + random.choice(SURNAMES)

def rand_title():
    return "The " + random.choice(ADJ) + " " + random.choice(NOUN)

FUNCTION_SPECS = [
    ("ancient_scripture", ["Name", "Religion", "Date", "Language"]),
    ("medieval_codex", ["Name", "Scribe", "Year", "Monastery"]),
    ("famous_bestseller", ["Title", "Author", "Year", "Copies"]),
    ("world_newspaper", ["Name", "Country", "Founded", "Language"]),
    ("famous_magazine", ["Name", "Category", "Founded", "Country"]),
    ("literary_genre", ["Name", "Origin", "Period", "Style"]),
    ("world_poetry_form", ["Name", "Origin", "Structure", "Famous"]),
    ("famous_playwright", ["Name", "Era", "Country", "Works"]),
    ("film_director", ["Name", "Born", "Country", "Notable"]),
    ("world_film_festival", ["Name", "Location", "Founded", "Category"]),
    ("famous_movie_studio", ["Name", "Founded", "Country", "Famous"]),
    ("animation_studio", ["Name", "Founded", "Country", "Style"]),
    ("world_music_genre", ["Name", "Origin", "Decade", "Instrument"]),
    ("famous_composer", ["Name", "Era", "Country", "Famous"]),
    ("world_orchestra", ["Name", "City", "Founded", "Conductor"]),
    ("famous_opera_house", ["Name", "City", "Capacity", "Opened"]),
    ("music_festival", ["Name", "Location", "Genre", "Founded"]),
    ("world_band", ["Name", "Country", "Genre", "Years"]),
    ("famous_album", ["Title", "Artist", "Year", "Genre"]),
    ("world_symphony", ["Name", "Composer", "Key", "Movements"]),
    ("famous_ballet", ["Name", "Choreographer", "Year", "Music"]),
    ("world_dance_style", ["Name", "Origin", "Type", "Tempo"]),
    ("famous_sculptor", ["Name", "Era", "Country", "Medium"]),
    ("world_art_movement", ["Name", "Period", "Origin", "Key"]),
    ("famous_art_gallery", ["Name", "City", "Founded", "Works"]),
    ("world_museum", ["Name", "City", "Type", "Visitors"]),
    ("famous_photographer", ["Name", "Era", "Country", "Style"]),
    ("world_photo_award", ["Name", "Category", "Prize", "Founded"]),
    ("famous_fashion_designer", ["Name", "Born", "Country", "Brand"]),
    ("world_textile_pattern", ["Name", "Origin", "Type", "Period"]),
    ("famous_archaeologist", ["Name", "Era", "Country", "Discovery"]),
    ("world_linguist", ["Name", "Era", "Country", "Languages"]),
    ("famous_anthropologist", ["Name", "Era", "Country", "Theory"]),
    ("world_sociologist", ["Name", "Era", "Country", "Concept"]),
    ("famous_psychologist", ["Name", "Era", "Country", "School"]),
    ("world_economist", ["Name", "Era", "Country", "Theory"]),
    ("famous_political_theorist", ["Name", "Era", "Country", "Work"]),
    ("world_legal_system", ["Name", "Country", "Type", "Origin"]),
    ("famous_constitution", ["Name", "Country", "Year", "Articles"]),
    ("world_treaty", ["Name", "Signed", "Year", "Parties"]),
    ("famous_peace_accord", ["Name", "Location", "Year", "Conflict"]),
    ("world_alliance", ["Name", "Members", "Founded", "Purpose"]),
    ("famous_revolution", ["Name", "Country", "Year", "Leader"]),
    ("world_civil_rights_movement", ["Name", "Country", "Period", "Goal"]),
    ("famous_speech", ["Name", "Speaker", "Year", "Occasion"]),
    ("world_protest", ["Name", "Location", "Year", "Cause"]),
    ("famous_labor_movement", ["Name", "Country", "Year", "Achievement"]),
    ("world_womens_movement", ["Name", "Country", "Year", "Win"]),
    ("famous_environmental_campaign", ["Name", "Country", "Year", "Goal"]),
    ("world_humanitarian_award", ["Name", "Category", "Prize", "Founded"]),
    ("famous_ngo", ["Name", "Founded", "Headquarters", "Focus"]),
    ("world_think_tank", ["Name", "Country", "Founded", "Focus"]),
    ("famous_educational_reform", ["Name", "Country", "Year", "Change"]),
    ("world_university_program", ["Name", "University", "Field", "Level"]),
    ("famous_scholarship", ["Name", "Country", "Amount", "Field"]),
    ("world_research_institute", ["Name", "Country", "Founded", "Field"]),
    ("famous_science_journal", ["Name", "Field", "Founded", "Impact"]),
    ("world_mathematical_problem", ["Name", "Field", "Solved", "Prize"]),
    ("famous_experiment", ["Name", "Scientist", "Year", "Result"]),
    ("world_technology_patent", ["Name", "Inventor", "Year", "Field"]),
    ("famous_software", ["Name", "Developer", "Year", "Type"]),
    ("world_protocol", ["Name", "Purpose", "Year", "Standard"]),
    ("famous_cipher", ["Name", "Inventor", "Year", "Type"]),
    ("world_encryption_standard", ["Name", "Year", "KeySize", "Status"]),
    ("famous_hacker", ["Name", "Alias", "Year", "Action"]),
    ("world_cyber_attack", ["Name", "Target", "Year", "Damage"]),
    ("famous_ai_system", ["Name", "Developer", "Year", "Capability"]),
    ("world_robot", ["Name", "Developer", "Year", "Function"]),
    ("famous_satellite", ["Name", "Agency", "Year", "Purpose"]),
    ("world_space_probe", ["Name", "Agency", "Launch", "Target"]),
    ("famous_rocket", ["Name", "Agency", "FirstLaunch", "Payload"]),
    ("world_launch_site", ["Name", "Country", "Opened", "Launches"]),
    ("famous_astronaut", ["Name", "Nationality", "Mission", "Year"]),
    ("world_space_station", ["Name", "Agency", "Launched", "Crew"]),
    ("famous_mission_control", ["Name", "Agency", "Location", "Missions"]),
    ("world_planetarium", ["Name", "City", "Capacity", "Opened"]),
    ("famous_science_museum", ["Name", "City", "Opened", "Exhibits"]),
    ("world_aquarium", ["Name", "City", "Capacity", "Species"]),
    ("famous_zoo", ["Name", "City", "Animals", "Area"]),
    ("world_botanical_garden", ["Name", "City", "Species", "Area"]),
    ("famous_arboretum", ["Name", "Location", "Trees", "Area"]),
    ("world_nature_center", ["Name", "Location", "Opened", "Programs"]),
    ("famous_observatory_museum", ["Name", "Location", "Telescope", "Opened"]),
    ("world_heritage_site_country", ["Name", "Country", "Type", "Year"]),
    ("famous_historic_trail", ["Name", "Country", "Length", "Period"]),
    ("world_national_monument", ["Name", "Country", "Type", "Established"]),
    ("famous_protected_area", ["Name", "Country", "Category", "Area"]),
    ("world_wilderness_area", ["Name", "Country", "Area", "Designated"]),
    ("famous_scenic_byway", ["Name", "Country", "Length", "Highlights"]),
    ("world_natural_landmark_usa", ["Name", "State", "Type", "Designated"]),
    ("famous_national_forest", ["Name", "State", "Area", "Established"]),
    ("world_state_park", ["Name", "State", "Area", "Type"]),
    ("famous_county_park", ["Name", "County", "Area", "Features"]),
    ("world_urban_park", ["Name", "City", "Area", "Opened"]),
    ("famous_community_garden", ["Name", "City", "Plots", "Opened"]),
    ("world_green_roof", ["Name", "Building", "Area", "Type"]),
    ("famous_eco_building", ["Name", "City", "Rating", "Year"]),
    ("world_net_zero_building", ["Name", "City", "Energy", "Year"]),
    ("famous_sustainable_city", ["Name", "Country", "Population", "Initiatives"]),
    ("world_eco_village", ["Name", "Country", "Founded", "Residents"]),
    ("famous_renewable_project", ["Name", "Country", "Capacity", "Type"]),
    ("world_carbon_neutral_company", ["Name", "Industry", "Year", "Method"]),
    ("famous_climate_pledge", ["Name", "Entity", "Year", "Target"]),
]

random.shuffle(FUNCTION_SPECS)
specs = FUNCTION_SPECS[:100]

ENTRIES = 1000
lines = 0

with open("data_bulk7.py", "w", encoding="utf-8") as f:
    f.write('"""data_bulk7.py: 100 auto-generated data functions, 1000 entries each, ~100K lines."""\n')
    f.write("import random\n\n")

    for func_name, fields in specs:
        suffix = "_data"
        rng = random.Random(hash(func_name + "v4.3.0") % (2**31))

        f.write("\ndef get_{}{}():\n".format(func_name, suffix))
        f.write('    """Return {} entries of {} data."""\n'.format(ENTRIES, func_name.replace("_", " ")))
        f.write("    return [\n")

        for i in range(ENTRIES):
            if func_name == "ancient_scripture":
                vals = (rand_title(), random.choice(["Christianity","Islam","Hinduism","Buddhism","Judaism","Taoism","Shinto","Zoroastrianism","Sikhism","Jainism"]), str(rng.randint(-2000, 1500)), random.choice(["Hebrew","Greek","Latin","Sanskrit","Arabic","Chinese","Aramaic","Pali","Ge'ez","Old Church Slavonic"]))
            elif func_name == "medieval_codex":
                vals = (rand_title(), rand_name(), str(rng.randint(500, 1500)), random.choice(["St. Gallen","Cluny","Monte Cassino","Durham","Skt. Peter","Bobbio","Reichenau","Fulda","Tours","Benediktbeuern"]))
            elif func_name == "famous_bestseller":
                vals = (rand_title(), rand_name(), str(rng.randint(1800, 2024)), str(rng.randint(1000000, 100000000)) + " copies")
            elif func_name == "world_newspaper":
                vals = (rand_title() + " Times", random.choice(["UK","USA","Japan","India","France","Germany","Brazil","China","Russia","Australia"]), str(rng.randint(1600, 2020)), random.choice(["English","Japanese","Hindi","French","German","Portuguese","Chinese","Russian","Spanish","Arabic"]))
            elif func_name == "famous_magazine":
                vals = (rand_title(), random.choice(["News","Science","Art","Fashion","Sports","Tech","Business","Nature","Travel","Food"]), str(rng.randint(1800, 2020)), random.choice(["USA","UK","France","Germany","Italy","Japan","Brazil","India","Australia","Canada"]))
            else:
                vals = (rand_title(), rand_name() if rng.random() > 0.5 else random.choice(["Global","Western","Eastern","Ancient","Medieval","Modern","Digital","Industrial","Agricultural","Information"]), str(rng.randint(-500, 2025)), random.choice(["Category A","Category B","Category C","Category D","Category E","Standard","Premium","Classic","Modern","Vintage"]))

            formatted = ", ".join('"{}"'.format(str(v).replace('"', "'")) for v in vals)
            f.write("        ({})".format(formatted))
            if i < ENTRIES - 1:
                f.write(",\n")
            else:
                f.write(",\n")

        f.write("    ]\n")
        lines += 3 + ENTRIES

import os
total = os.path.getsize("data_bulk7.py") if os.path.exists("data_bulk7.py") else 0
print("Generated data_bulk7.py: {} functions, ~{} lines, {:.1f} KB".format(len(specs), lines, total/1024))
