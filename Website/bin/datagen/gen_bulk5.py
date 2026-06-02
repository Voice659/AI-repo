"""Generate data_bulk5.py: 100 data functions, 1000 entries each, ~100K lines."""
import random

random.seed(123)

NAMES = "Aiden,Bella,Chloe,Dylan,Elijah,Freya,Gideon,Harper,Isaiah,Jade,Kai,Leila,Maya,Nico,Olive,Phoenix,Quinn,River,Sage,Thea,Uri,Violet,Winter,Xander,Yara,Zane,Aria,Bodhi,Cora,Dax,Elara,Finn,Gia,Hugo,Isla,Jax,Kira,Liam,Mira,Nyx,Owen,Pia,Rex,Shay,Troy,Una,Vera,Wren,Xia,Zuri".split(",")
SURNAMES = "Adams,Baker,Chen,Davis,Edwards,Foster,Garcia,Hall,Irvine,Jones,Kim,Lee,Miller,Nguyen,Owen,Patel,Quinn,Reyes,Smith,Taylor,Umber,Vega,Wang,Xu,Yang,Zhao,Black,White,Green,Brown".split(",")

ADJ = "Ancient,Mighty,Golden,Crimson,Frozen,Silent,Brave,Grand,Noble,Subtle,Fierce,Cosmic,Stellar,Lunar,Solar,Mystic,Shadow,Radiant,Thunder,Silver,Crystal,Ember,Frost,Storm,Wild,Sacred,Quiet,Bright,Deep,Hidden".split(",")
NOUN = "Summit,River,Forest,Valley,Horizon,Crystal,Thunder,Shadow,Ember,Frost,Star,Storm,Sage,Phoenix,Dragon,Tiger,Wolf,Eagle,Hawk,Lynx,Reef,Dune,Peak,Glade,Grove,Heath,Moor,Hill,Cove,Bay".split(",")

def rand_name():
    return random.choice(NAMES) + " " + random.choice(SURNAMES)

def rand_title():
    return "The " + random.choice(ADJ) + " " + random.choice(NOUN)

FUNCTION_SPECS = [
    ("famous_landmark", ["Name", "Location", "Year", "Type"]),
    ("world_festival", ["Name", "Country", "Month", "Category"]),
    ("famous_painting", ["Title", "Artist", "Year", "Movement"]),
    ("scientific_theory", ["Name", "Proposer", "Year", "Field"]),
    ("ancient_civilization", ["Name", "Region", "Period", "Achievement"]),
    ("famous_inventor", ["Name", "Birth", "Invention", "Field"]),
    ("national_park", ["Name", "Country", "Area", "Established"]),
    ("famous_bridge", ["Name", "Location", "Length", "Type"]),
    ("world_religion", ["Name", "Followers", "Origin", "Founded"]),
    ("famous_philosopher", ["Name", "Era", "School", "KeyIdea"]),
    ("astronomical_event", ["Name", "Date", "Type", "Visibility"]),
    ("natural_disaster", ["Name", "Location", "Year", "Type"]),
    ("famous_exploration", ["Name", "Explorer", "Year", "Region"]),
    ("medical_advancement", ["Name", "Discoverer", "Year", "Field"]),
    ("famous_architect", ["Name", "Birth", "Style", "FamousWork"]),
    ("world_university", ["Name", "Location", "Founded", "Students"]),
    ("literary_award", ["Name", "Category", "FirstAwarded", "Prize"]),
    ("famous_statue", ["Name", "Location", "Year", "Material"]),
    ("historical_period", ["Name", "Start", "End", "Region"]),
    ("famous_library", ["Name", "City", "Volumes", "Type"]),
    ("world_market", ["Name", "Location", "Type", "Founded"]),
    ("famous_garden", ["Name", "Location", "Area", "Style"]),
    ("royal_dynasty", ["Name", "Country", "Period", "Founder"]),
    ("famous_battlefield", ["Name", "Location", "Year", "Conflict"]),
    ("archaeological_find", ["Name", "Site", "Year", "Period"]),
    ("famous_mountain_pass", ["Name", "Range", "Elevation", "Location"]),
    ("world_lighthouse", ["Name", "Location", "Height", "Built"]),
    ("famous_fountain", ["Name", "City", "Year", "Style"]),
    ("world_stadium", ["Name", "City", "Capacity", "Sport"]),
    ("famous_marketplace", ["Name", "City", "Type", "Historic"]),
    ("ancient_wonder", ["Name", "Location", "Built", "Civilization"]),
    ("famous_observatory", ["Name", "Location", "Altitude", "Telescope"]),
    ("world_harbor", ["Name", "City", "Traffic", "Depth"]),
    ("famous_waterfall_detail", ["Name", "Height", "Location", "River"]),
    ("world_canyon", ["Name", "Location", "Depth", "Length"]),
    ("famous_peninsula", ["Name", "Location", "Area", "Countries"]),
    ("world_plateau", ["Name", "Location", "Elevation", "Area"]),
    ("famous_delta", ["Name", "River", "Location", "Area"]),
    ("world_glacier", ["Name", "Range", "Length", "Status"]),
    ("famous_reef", ["Name", "Location", "Area", "Type"]),
    ("world_volcano_range", ["Name", "Location", "Peaks", "Active"]),
    ("famous_geyser", ["Name", "Location", "Height", "Interval"]),
    ("world_thermal_spring", ["Name", "Location", "Temp", "Mineral"]),
    ("famous_cave_system", ["Name", "Location", "Length", "Depth"]),
    ("world_archipelago", ["Name", "Location", "Islands", "Area"]),
    ("famous_strait", ["Name", "Connects", "Width", "Depth"]),
    ("world_channel", ["Name", "Location", "Length", "Type"]),
    ("famous_isthmus", ["Name", "Connects", "Width", "Countries"]),
    ("world_mountain_system", ["Name", "Continent", "Length", "Highest"]),
    ("famous_bay", ["Name", "Location", "Area", "Depth"]),
    ("world_cape", ["Name", "Location", "Country", "Prominence"]),
    ("famous_aboriginal_culture", ["Name", "Region", "Population", "Language"]),
    ("world_migration_route", ["Name", "Species", "Distance", "Season"]),
    ("famous_research_station", ["Name", "Location", "Country", "Purpose"]),
    ("world_biosphere_reserve", ["Name", "Country", "Area", "Year"]),
    ("famous_plant_collection", ["Name", "Location", "Species", "Type"]),
    ("world_butterfly", ["Name", "Region", "Wingspan", "Status"]),
    ("famous_bird_sanctuary", ["Name", "Location", "Species", "Area"]),
    ("world_wildlife_corridor", ["Name", "Countries", "Length", "Purpose"]),
    ("famous_nature_reserve", ["Name", "Country", "Area", "Habitat"]),
    ("world_marine_park", ["Name", "Location", "Area", "Established"]),
    ("famous_rock_formation", ["Name", "Location", "Height", "Type"]),
    ("world_fossil_site", ["Name", "Location", "Period", "Finds"]),
    ("famous_impact_crater", ["Name", "Location", "Diameter", "Age"]),
    ("world_coral_reef_system", ["Name", "Location", "Area", "Species"]),
    ("famous_mangrove_forest", ["Name", "Location", "Area", "Type"]),
    ("world_wetland", ["Name", "Country", "Area", "Type"]),
    ("famous_grassland", ["Name", "Location", "Area", "Climate"]),
    ("world_tundra", ["Name", "Location", "Area", "Type"]),
    ("famous_bamboo_forest", ["Name", "Location", "Area", "Species"]),
    ("world_tea_region", ["Name", "Country", "Type", "Established"]),
    ("famous_coffee_region", ["Name", "Country", "Altitude", "Variety"]),
    ("world_wine_region", ["Name", "Country", "Grape", "Classification"]),
    ("famous_cheese_variety", ["Name", "Country", "Milk", "Type"]),
    ("world_chocolate_origin", ["Name", "Country", "Type", "Flavor"]),
    ("famous_spice_route", ["Name", "Trade", "Origin", "Destination"]),
    ("world_silk_road_site", ["Name", "Country", "Period", "Significance"]),
    ("famous_trade_route", ["Name", "Start", "End", "Goods"]),
    ("world_pilgrimage_route", ["Name", "Religion", "Destination", "Distance"]),
    ("famous_ancient_road", ["Name", "Civilization", "Length", "Built"]),
    ("world_historic_canal", ["Name", "Country", "Length", "Built"]),
    ("famous_aqueduct", ["Name", "Location", "Length", "Year"]),
    ("world_historic_fort", ["Name", "Location", "Built", "Battles"]),
    ("famous_castle_detail", ["Name", "Country", "Built", "Style"]),
    ("world_palace", ["Name", "Location", "Year", "Architect"]),
    ("famous_temple_complex", ["Name", "Religion", "Location", "Built"]),
    ("world_historic_square", ["Name", "City", "Area", "Built"]),
    ("famous_historic_district", ["Name", "City", "Period", "Style"]),
    ("world_open_air_museum", ["Name", "Location", "Type", "Founded"]),
    ("famous_sculpture_garden", ["Name", "Location", "Works", "Founded"]),
    ("world_historical_archive", ["Name", "City", "Documents", "Founded"]),
    ("famous_manuscript", ["Name", "Culture", "Date", "Language"]),
    ("world_epic_poem", ["Name", "Culture", "Date", "Language"]),
    ("famous_myth_collection", ["Name", "Culture", "Period", "Stories"]),
    ("world_folklore_tradition", ["Name", "Country", "Type", "Period"]),
    ("famous_fairy_tale", ["Name", "Collector", "Country", "Published"]),
    ("world_legendary_creature", ["Name", "Culture", "Type", "Habitat"]),
    ("famous_urban_legend", ["Name", "Country", "Type", "Period"]),
    ("world_ghost_story", ["Name", "Location", "Period", "Type"]),
    ("famous_superstition", ["Name", "Origin", "Type", "Belief"]),
    ("world_taboo", ["Name", "Culture", "Type", "Description"]),
    ("famous_ritual", ["Name", "Culture", "Purpose", "Frequency"]),
]

# Shuffle and take 100
random.shuffle(FUNCTION_SPECS)
specs = FUNCTION_SPECS[:100]

ENTRIES = 1000
lines = 0

with open("../datab/data_bulk5.py", "w", encoding="utf-8") as f:
    f.write('"""data_bulk5.py: 100 auto-generated data functions, 1000 entries each, ~100K lines."""\n')
    f.write("import random\n\n")

    for func_name, fields in specs:
        suffix = "_data"
        rng = random.Random(hash(func_name + "v4.1.0") % (2**31))

        f.write("\ndef get_{}{}():\n".format(func_name, suffix))
        f.write('    """Return {} entries of {} data."""\n'.format(ENTRIES, func_name.replace("_", " ")))
        f.write("    return [\n")

        for i in range(ENTRIES):
            if func_name == "famous_landmark":
                vals = (rand_title(), random.choice(["Egypt","China","India","Italy","France","USA","UK","Mexico","Peru","Greece"]), str(rng.randint(-3000, 2025)), random.choice(["Temple","Pyramid","Palace","Monument","Castle","Cathedral","Fortress","Bridge","Tower","Gate"]))
            elif func_name == "world_festival":
                vals = (rand_title() + " Festival", random.choice(["India","Brazil","Spain","Japan","USA","Italy","Thailand","Mexico","China","Germany"]), random.choice(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]), random.choice(["Cultural","Religious","Music","Food","Harvest","New Year","Dance","Fire","Water","Flower"]))
            elif func_name == "famous_painting":
                vals = (rand_title(), rand_name(), str(rng.randint(1300, 2025)), random.choice(["Renaissance","Baroque","Impressionism","Expressionism","Cubism","Surrealism","Pop Art","Realism","Romanticism","Modern"]))
            elif func_name == "scientific_theory":
                vals = (rand_title() + " Theory", rand_name(), str(rng.randint(1500, 2025)), random.choice(["Physics","Biology","Chemistry","Astronomy","Mathematics","Geology","Medicine","Psychology","Ecology","Cosmology"]))
            elif func_name == "ancient_civilization":
                vals = (rand_name() + " Civilization", random.choice(["Mesopotamia","Andes","Indus Valley","Central America","Mediterranean","China","West Africa","North America","Southeast Asia","Eastern Europe"]), random.choice(["3000 BCE","2500 BCE","2000 BCE","1500 BCE","1000 BCE","500 BCE"]), random.choice(["Writing","Architecture","Agriculture","Astronomy","Mathematics","Metallurgy","Navigation","Medicine","Law","Trade"]))
            elif func_name == "famous_inventor":
                vals = (rand_name(), str(rng.randint(1400, 2000)), rand_title(), random.choice(["Communication","Transportation","Medicine","Computing","Energy","Agriculture","Manufacturing","Textile","Military","Domestic"]))
            elif func_name == "national_park":
                vals = (rand_title() + " Park", random.choice(["USA","Canada","Australia","Brazil","China","India","South Africa","New Zealand","Norway","Costa Rica"]), str(rng.randint(100, 50000)) + " km2", str(rng.randint(1872, 2020)))
            elif func_name == "famous_bridge":
                vals = (rand_title() + " Bridge", random.choice(["San Francisco","London","Sydney","New York","Paris","Tokyo","Istanbul","Venice","Prague","Shanghai"]), str(rng.randint(100, 5000)) + " m", random.choice(["Suspension","Arch","Cable-stayed","Truss","Beam","Cantilever","Tied-arch","Floating","Drawbridge","Viaduct"]))
            elif func_name == "world_religion":
                vals = (rand_name() + " Faith", str(rng.randint(100000, 2500000000)) + " followers", random.choice(["Middle East","India","China","Japan","Europe","Africa","Americas","SE Asia"]), str(rng.randint(-2000, 2000)))
            elif func_name == "famous_philosopher":
                vals = (rand_name(), random.choice(["Ancient","Medieval","Renaissance","Enlightenment","19th C","20th C","Modern"]), random.choice(["Stoicism","Existentialism","Empiricism","Rationalism","Idealism","Materialism","Pragmatism","Utilitarianism","Nihilism","Phenomenology"]), rand_title())
            elif func_name == "astronomical_event":
                vals = (rand_title(), str(rng.randint(1000, 2100)), random.choice(["Eclipse","Comet","Supernova","Meteor Shower","Transit","Conjunction","Opposition","Aurora","Nova","Occultation"]), random.choice(["Total","Partial","Annual","Visible","Rare","Bright"]))
            elif func_name == "natural_disaster":
                vals = (rand_title() + " Disaster", random.choice(["Japan","Indonesia","USA","Philippines","India","China","Mexico","Italy","Turkey","Haiti"]), str(rng.randint(1000, 2024)), random.choice(["Earthquake","Volcano","Hurricane","Tsunami","Flood","Wildfire","Tornado","Landslide","Blizzard","Drought"]))
            elif func_name in ("famous_exploration","famous_exploration"):
                vals = (rand_title() + " Expedition", rand_name(), str(rng.randint(1400, 2020)), random.choice(["Arctic","Antarctic","Mariana Trench","Everest","Amazon","Sahara","Space","Deep Sea","Cave","Desert"]))
            elif func_name == "medical_advancement":
                vals = (rand_title(), rand_name(), str(rng.randint(1500, 2025)), random.choice(["Surgery","Pharmacology","Genetics","Immunology","Diagnostics","Virology","Neurology","Cardiology","Oncology","Epidemiology"]))
            elif func_name in ("famous_architect","famous_architect"):
                vals = (rand_name(), str(rng.randint(1400, 2000)), random.choice(["Gothic","Renaissance","Baroque","Neoclassical","Art Deco","Modernist","Brutalist","Postmodern","Contemporary","Vernacular"]), rand_title())
            elif func_name == "world_university":
                vals = (rand_title() + " University", random.choice(["Cambridge","Oxford","Harvard","Stanford","Paris","Berlin","Tokyo","Beijing","Sydney","Toronto"]), str(rng.randint(1000, 2020)), str(rng.randint(500, 50000)))
            elif func_name == "literary_award":
                vals = (rand_title() + " Prize", random.choice(["Fiction","Poetry","Drama","Non-fiction","Science","History","Translation","Children's","Biography","Mystery"]), str(rng.randint(1800, 2020)), random.choice(["$10000","$50000","$100000","Medal","Golden","Crystal","Silver","Bronze","Honor","Grant"]))
            elif func_name == "famous_statue":
                vals = (rand_title(), random.choice(["Rome","Paris","New York","Rio","Moscow","Beijing","Cairo","Athens","Bangkok","London"]), str(rng.randint(-500, 2020)), random.choice(["Marble","Bronze","Granite","Limestone","Steel","Wood","Copper","Gold","Iron","Concrete"]))
            elif func_name == "historical_period":
                vals = (rand_title() + " Period", str(rng.randint(-3000, 1000)), str(rng.randint(500, 2020)), random.choice(["Europe","Asia","Africa","Americas","Middle East","Oceania","Global","Mediterranean","Central Asia","Scandinavia"]))
            else:
                vals = (rand_title(), rand_name() if rng.random() > 0.5 else random.choice(["Europe","Asia","Africa","Americas","Oceania"]), str(rng.randint(0, 2025)), random.choice(["Cultural","Natural","Historical","Scientific","Artistic","Religious","Political","Social","Technological","Economic"]))

            formatted = ", ".join('"{}"'.format(str(v).replace('"', "'")) for v in vals)
            f.write("        ({})".format(formatted))
            if i < ENTRIES - 1:
                f.write(",\n")
            else:
                f.write(",\n")

        f.write("    ]\n")
        lines += 3 + ENTRIES

import os
total = os.path.getsize("data_bulk5.py") if os.path.exists("data_bulk5.py") else 0
print("Generated data_bulk5.py: {} functions, ~{} lines, {:.1f} KB".format(len(specs), lines, total/1024))
