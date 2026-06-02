"""Generate data_bulk9.py: 100 data functions, 1000 entries each, ~100K lines."""
import random

random.seed(2025)

NAMES = "Aero,Brio,Comet,Dune,Edge,Frost,Gale,Haze,Iris,Jolt,Kite,Luxe,Mira,Nova,Onyx,Pulse,Quest,Raze,Star,Thorn,Umbra,Virtue,Whisper,Xero,Yonder,Zeal,Atlas,Bliss,Crest,Drift".split(",")
SURNAMES = "Aegis,Blade,Crest,Drake,Ember,Frost,Gleam,Haven,Isle,Jade,Keen,Leaf,Muse,Nyx,Oracle,Pinnacle,Quill,Ridge,Shield,Tide,Umber,Valor,Veil,Will,Xenith,Yield,Zephyr,Arbor,Basin,Canyon".split(",")

def rand_name():
    return random.choice(NAMES) + " " + random.choice(SURNAMES)

def rand_title():
    return "The " + random.choice(NAMES) + " " + random.choice(SURNAMES)

FUNCTION_SPECS = [
    ("ancient_rune", ["Symbol", "Culture", "Meaning", "Date"]),
    ("medieval_manuscript", ["Title", "Scribe", "Year", "Script"]),
    ("folklore_creature", ["Name", "Region", "Type", "Feature"]),
    ("mythical_artifact", ["Name", "Origin", "Power", "Culture"]),
    ("legendary_sword", ["Name", "Forged", "Culture", "Property"]),
    ("magic_spell", ["Name", "School", "Effect", "Difficulty"]),
    ("astrology_sign", ["Sign", "Element", "Quality", "Ruler"]),
    ("tarot_card", ["Name", "Arcana", "Number", "Fortune"]),
    ("divination_method", ["Name", "Origin", "Type", "Tool"]),
    ("alchemy_symbol", ["Symbol", "Element", "Property", "Planet"]),
    ("ancient_deity", ["Name", "Pantheon", "Domain", "Symbol"]),
    ("sacred_mountain", ["Name", "Range", "Height", "Religion"]),
    ("holy_well", ["Name", "Location", "Tradition", "Healing"]),
    ("pilgrimage_route", ["Name", "Destination", "Length", "Religion"]),
    ("monastic_order", ["Name", "Founded", "Founder", "Rule"]),
    ("religious_festival_month", ["Name", "Religion", "Month", "Duration"]),
    ("sacred_dance", ["Name", "Culture", "Purpose", "Occasion"]),
    ("ritual_music", ["Name", "Tradition", "Instruments", "Purpose"]),
    ("traditional_garb", ["Name", "Culture", "Material", "Occasion"]),
    ("ceremonial_mask", ["Name", "Culture", "Material", "Purpose"]),
    ("ancient_currency", ["Name", "Civilization", "Material", "Value"]),
    ("trade_route", ["Name", "From", "To", "Goods"]),
    ("marketplace_type", ["Name", "Culture", "Goods", "Frequency"]),
    ("merchant_guild", ["Name", "City", "Founded", "Trade"]),
    ("banking_dynasty", ["Name", "Country", "Founded", "Fortune"]),
    ("economic_zone", ["Name", "Region", "Type", "Members"]),
    ("trade_agreement", ["Name", "Parties", "Year", "Scope"]),
    ("colonial_commodity", ["Name", "Origin", "Destination", "Era"]),
    ("industrial_innovation_textile", ["Name", "Inventor", "Year", "Impact"]),
    ("manufacturing_center", ["City", "Country", "Industry", "Output"]),
    ("famous_workshop", ["Name", "City", "Craft", "Era"]),
    ("artisan_collective", ["Name", "City", "Medium", "Founded"]),
    ("design_movement", ["Name", "Period", "Origin", "Principle"]),
    ("famous_atelier", ["Name", "City", "Founded", "Specialty"]),
    ("pottery_tradition", ["Name", "Culture", "Type", "Period"]),
    ("glassblowing_center", ["City", "Country", "Technique", "Period"]),
    ("jewelry_period", ["Name", "Era", "Style", "Gems"]),
    ("watchmaking_brand", ["Name", "Country", "Founded", "Type"]),
    ("automotive_heritage", ["Brand", "Country", "Founded", "Classic"]),
    ("motorcycle_culture", ["Brand", "Country", "Type", "Era"]),
    ("bicycle_innovation", ["Name", "Inventor", "Year", "Feature"]),
    ("shipbuilding_tradition", ["City", "Country", "Type", "Period"]),
    ("aviation_milestone_era", ["Event", "Pilot", "Year", "Achievement"]),
    ("railway_history", ["Line", "Country", "Opened", "Length"]),
    ("canal_system", ["Name", "Country", "Opened", "Length"]),
    ("bridge_engineering", ["Name", "Country", "Opened", "Span"]),
    ("tunnel_project", ["Name", "Country", "Opened", "Length"]),
    ("road_network", ["Name", "Country", "Length", "Type"]),
    ("urban_planning_movement", ["Name", "Era", "Origin", "Concept"]),
    ("garden_design", ["Name", "Country", "Style", "Period"]),
    ("landscape_architect", ["Name", "Era", "Country", "Work"]),
    ("public_park", ["Name", "City", "Opened", "Area"]),
    ("city_square", ["Name", "City", "Opened", "Size"]),
    ("famous_market", ["Name", "City", "Type", "Founded"]),
    ("carnival_tradition", ["Name", "City", "Duration", "Founded"]),
    ("street_festival", ["Name", "City", "Month", "Theme"]),
    ("night_market", ["Name", "City", "Cuisine", "Frequency"]),
    ("food_court_concept", ["Name", "City", "Counters", "Founded"]),
    ("coffee_house_history", ["Name", "City", "Founded", "Specialty"]),
    ("tea_house_tradition", ["Name", "Culture", "Ceremony", "Origin"]),
    ("bakery_chain", ["Name", "Country", "Founded", "Shops"]),
    ("confectionery_brand", ["Name", "Country", "Founded", "Specialty"]),
    ("brewery_tradition", ["Name", "Country", "Founded", "Type"]),
    ("winemaking_region", ["Name", "Country", "Varieties", "Terroir"]),
    ("spice_blend", ["Name", "Origin", "Ingredients", "Use"]),
    ("sauce_invention", ["Name", "Chef", "Year", "Cuisine"]),
    ("cheese_variety", ["Name", "Country", "Milk", "Texture"]),
    ("fermented_food", ["Name", "Country", "Base", "Process"]),
    ("preservation_method", ["Name", "Origin", "Technique", "Period"]),
    ("cooking_technique", ["Name", "Origin", "Method", "Dish"]),
    ("kitchen_tool", ["Name", "Inventor", "Year", "Function"]),
    ("table_setting_style", ["Name", "Culture", "Era", "Elements"]),
    ("dining_etiquette", ["Rule", "Culture", "Occasion", "Origin"]),
    ("royal_court_cuisine", ["Dish", "Court", "Era", "Chef"]),
    ("military_ration", ["Name", "Country", "Era", "Contents"]),
    ("explorer_food", ["Dish", "Expedition", "Era", "Preserved"]),
    ("space_food", ["Name", "Agency", "Year", "Packaging"]),
    ("survival_skill", ["Skill", "Region", "Category", "Difficulty"]),
    ("navigation_technique", ["Method", "Culture", "Era", "Tool"]),
    ("knot_tying", ["Name", "Type", "Use", "Difficulty"]),
    ("shelter_type", ["Name", "Region", "Material", "Season"]),
    ("fire_making_method", ["Name", "Technique", "Difficulty", "Era"]),
    ("water_purification", ["Method", "Origin", "Type", "Efficiency"]),
    ("foraging_guide", ["Plant", "Region", "Edible", "Season"]),
    ("hunting_tool", ["Name", "Culture", "Type", "Target"]),
    ("fishing_technique", ["Name", "Type", "Region", "Target"]),
    ("trap_design", ["Name", "Target", "Type", "Culture"]),
    ("weapon_system", ["Name", "Era", "Type", "Origin"]),
    ("armor_design", ["Name", "Era", "Material", "Culture"]),
    ("fortification_style", ["Name", "Era", "Material", "Region"]),
    ("siege_weapon", ["Name", "Era", "Range", "Civilization"]),
    ("naval_vessel_type", ["Name", "Era", "Displacement", "Origin"]),
    ("cavalry_unit", ["Name", "Era", "Type", "Origin"]),
    ("infantry_formation", ["Name", "Era", "Origin", "Tactic"]),
    ("military_rank_history", ["Rank", "Service", "Era", "Country"]),
    ("battle_standard", ["Name", "Era", "Battle", "Country"]),
    ("war_flag", ["Name", "Country", "Era", "Design"]),
    ("medal_of_honor", ["Name", "Country", "Era", "Criteria"]),
    ("military_memorial", ["Name", "Location", "Conflict", "Year"]),
    ("war_cemetery", ["Name", "Location", "Country", "Fallen"]),
    ("peace_monument", ["Name", "City", "Artist", "Year"]),
    ("diplomatic_gift", ["Object", "From", "To", "Year"]),
    ("state_visit", ["Leader", "Country", "Year", "Purpose"]),
]

random.shuffle(FUNCTION_SPECS)
specs = FUNCTION_SPECS[:100]

ENTRIES = 1000
lines = 0

with open("../datab/data_bulk9.py", "w", encoding="utf-8") as f:
    f.write('"""data_bulk9.py: 100 auto-generated data functions, 1000 entries each, ~100K lines."""\n')
    f.write("import random\n\n")

    for func_name, fields in specs:
        rng = random.Random(hash(func_name + "v4.5.0.9") % (2**31))

        f.write("\ndef get_{}_data():\n".format(func_name))
        f.write('    """Return {} entries of {} data."""\n'.format(ENTRIES, func_name.replace("_", " ")))
        f.write("    return [\n")

        for i in range(ENTRIES):
            if func_name in ("ancient_deity",):
                vals = (rand_title(), random.choice(["Greek","Norse","Egyptian","Hindu","Chinese","Roman","Aztec","Mayan","Celtic","Slavic"]), random.choice(["Sky","War","Love","Wisdom","Death","Sun","Moon","Sea","Fire","Earth"]), random.choice(["Thunderbolt","Trident","Sword","Bow","Ankh","Wheel","Scepter","Spear","Shield","Crown"]))
            elif func_name in ("sacred_mountain", "holy_well"):
                vals = (rand_title(), random.choice(["Himalayas","Andes","Alps","Rockies","Urals","Atlas","Caucasus","Hindu Kush","Tian Shan","Karakoram"]), str(rng.randint(1000, 8849)) + "m", random.choice(["Hinduism","Buddhism","Islam","Shinto","Animism","Christianity","Taoism","Jainism","Sikhism","Zoroastrianism"]))
            elif func_name in ("pilgrimage_route",):
                vals = (rand_title(), random.choice(["Jerusalem","Mecca","Santiago","Varanasi","Lourdes","Fatima","Rome","Medjugorje","Mount Kailash","Shikoku"]), str(rng.randint(100, 5000)) + " km", random.choice(["Christianity","Islam","Hinduism","Buddhism","Judaism","Sikhism","Shinto","Taoism"]))
            elif func_name in ("traditional_garb", "ceremonial_mask"):
                vals = (rand_title(), random.choice(["Japanese","Nigerian","Peruvian","Indian","Scottish","Mexican","Indonesian","Mongolian","Berber","Sami"]), random.choice(["Silk","Cotton","Wool","Leather","Bark","Feathers","Gold","Beads","Linen","Hemp"]), random.choice(["Wedding","Funeral","Festival","Warrior","Daily","Ritual","Ceremonial","Harvest","Initiation","Royal"]))
            elif func_name in ("ancient_currency",):
                vals = (rand_title(), random.choice(["Roman","Greek","Persian","Chinese","Indian","Egyptian","Mesoamerican","Carthaginian","Phoenician","Byzantine"]), random.choice(["Gold","Silver","Bronze","Copper","Iron","Shells","Leather","Stone","Salt","Cloth"]), str(rng.randint(1, 1000)) + " units")
            elif func_name in ("automotive_heritage",):
                vals = (rand_title(), random.choice(["USA","Germany","Italy","UK","Japan","France","Sweden","South Korea","Spain","India"]), str(rng.randint(1885, 1950)), random.choice(["Sedan","Roadster","Coupe","Convertible","Luxury","Sports","Utility","Touring","Limousine","Race"]))
            elif func_name in ("military_rank_history",):
                vals = (random.choice(["General","Colonel","Major","Captain","Lieutenant","Sergeant","Corporal","Private","Admiral","Commander"]), random.choice(["Army","Navy","Marines","Air Force","Coast Guard","Space Force","Legion","Guard","Militia","Janissary"]), str(rng.randint(-500, 2020)), random.choice(["Rome","China","France","UK","USA","Russia","Japan","Ottoman","Mongol","Byzantine"]))
            elif func_name in ("battle_standard", "war_flag"):
                vals = (rand_title(), str(rng.randint(-500, 2020)), rand_title(), random.choice(["Rome","Persia","China","Mongol","Ottoman","France","UK","Spain","Russia","USA"]))
            elif func_name in ("state_visit",):
                vals = (rand_name(), random.choice(["USA","China","Russia","UK","France","Germany","Japan","India","Brazil","South Korea"]), str(rng.randint(1900, 2024)), random.choice(["Trade","Diplomacy","Summit","State Dinner","Treaty","Cultural","Humanitarian","Military","Climate","Technology"]))
            elif func_name in ("medieval_manuscript",):
                vals = (rand_title(), rand_name(), str(rng.randint(400, 1500)), random.choice(["Uncial","Insular","Carolingian","Gothic","Humanist","Beneventan","Visigothic","Merovingian","Anglicana","Fraktur"]))
            else:
                vals = (rand_title(), random.choice(["Global","Eastern","Western","Northern","Southern","Central","Tropical","Arctic","Coastal","Inland"]), str(rng.randint(-3000, 2025)), random.choice(["Type I","Type II","Type III","Standard","Premium","Ancient","Classic","Modern","Traditional","Contemporary"]))

            formatted = ", ".join('"{}"'.format(str(v).replace('"', "'")) for v in vals)
            f.write("        ({})".format(formatted))
            if i < ENTRIES - 1:
                f.write(",\n")
            else:
                f.write(",\n")

        f.write("    ]\n")
        lines += 3 + ENTRIES

import os
total = os.path.getsize("data_bulk9.py") if os.path.exists("data_bulk9.py") else 0
print("Generated data_bulk9.py: {} functions, ~{} lines, {:.1f} KB".format(len(specs), lines, total/1024))
