"""Generate data_bulk4.py: 200 data functions, 1000 entries each, ~200K lines."""
import random, os, textwrap

random.seed(42)

# ---- Name pools for variety ----
NAMES = "Aarav,Aria,Bodhi,Chen,Dao,Elena,Finn,Grace,Hiro,Iris,Jiro,Kai,Lei,Ming,Nora,Omar,Park,Quinn,Ravi,Sato,Tao,Uma,Viktor,Wei,Xia,Yuki,Zara,Amara,Bao,Cielo,Dante,Elara,Fen,Hana,Idris,Juno,Kiran,Lila,Milo,Nia,Ori,Paz,Rio,Suki,Taro,Una,Vera,Wren,Xena,Yara,Zion,Anya,Bran,Cora,Dax,Enzo,Faye,Gia,Hugo,Isla,Jax,Koa,Lux,Mae,Nyx,Otto,Pia,Rex,Sage,Thea,Ugo,Vida,Wade,Xia,Yara,Zeke".split(",")
SURNAMES = "Acharya,Bhattacharya,Chakraborty,Dasgupta,Ganguly,Iyer,Joshi,Kulkarni,Mehta,Nair,Patel,Rao,Sharma,Singh,Trivedi,Verma,Yadav,Aoki,Fujimoto,Goto,Hasegawa,Ito,Kaneko,Matsuda,Nakamura,Ohno,Saito,Tanaka,Ueda,Watanabe,Yamamoto,Zhang,Wang,Li,Chen,Liu,Yang,Zhao,Huang,Wu,Zhou,Xu,Sun,Ma,Zhu,Hu,Lin,Guo,He,Gao".split(",")
ADJ = "Ancient,Mighty,Golden,Crimson,Silver,Shadow,Bright,Deep,Swift,Hidden,Noble,Quiet,Wild,Sacred,Broken,Eternal,Restless,Frozen,Burning,Fading,Shining,Dark,Pale,Fierce,Gentle,Brave,Subtle,Grand,Royal,Humble,Proud,Stern,Bright,Stormy,Calm,Silent,Blazing,Icy,Misty,Thunder".split(",")
NOUN = "Mountain,River,Forest,Valley,Desert,Island,Ocean,Peak,Cave,Glacier,Canyon,Reef,Dune,Falls,Lake,Storm,Wave,Flame,Stone,Wind,Rain,Star,Moon,Sun,Cloud,Shadow,Light,Dawn,Dusk,Tide,Frost,Ember,Crystal,Thorn,Root,Wing,Fang,Claw,Horn,Shield".split(",")
YEARS = [str(random.randint(1400, 2025)) for _ in range(200)]
COUNTRIES = "USA,China,India,Russia,Brazil,Japan,Germany,UK,France,Italy,Canada,Australia,Spain,Mexico,Indonesia,Netherlands,South Korea,Sweden,Switzerland,Turkey,Norway,Poland,Argentina,Denmark,South Africa,Finland,Greece,Portugal,Egypt,Ireland,Chile,Colombia,Vietnam,Thailand,Malaysia,Philippines,New Zealand,Peru,Nigeria,Kenya".split(",")
CITIES = "New York,London,Tokyo,Paris,Beijing,Sydney,Rome,Moscow,Berlin,Mumbai,Shanghai,Seoul,Istanbul,Delhi,Cairo,Jakarta,Lagos,Manila,Mexico City,Dubai,Singapore,Bangkok,Los Angeles,Chicago,Toronto,San Francisco,Amsterdam,Barcelona,Madrid,Vienna,Prague,Budapest,Warsaw,Dublin,Oslo,Helsinki,Stockholm,Copenhagen,Lisbon,Athens".split(",")
FIELDS = "Medicine,Physics,Chemistry,Biology,Astronomy,Mathematics,Engineering,Geology,Oceanography,Meteorology,Paleontology,Archaeology,Psychology,Sociology,Economics,Linguistics,Philosophy,Art,Music,Literature,History,Politics,Law,Education,Agriculture".split(",")
ANIMALS = "Elephant,Tiger,Panda,Kangaroo,Penguin,Dolphin,Octopus,Eagle,Falcon,Cheetah,Leopard,Gorilla,Orangutan,Chimpanzee,Zebra,Giraffe,Rhino,Hippo,Crocodile,Python,Anaconda,Sloth,Koala,Platypus,Wolf,Fox,Bear,Deer,Elk,Bison".split(",")
COLORS = "Red,Blue,Green,Yellow,Purple,Orange,Black,White,Gray,Brown,Pink,Gold,Silver,Bronze,Ivory,Crimson,Azure,Emerald,Amber,Sapphire".split(",")
NUMBERS = [str(random.randint(100, 9999)) for _ in range(500)]

def rand_name():
    return random.choice(NAMES) + " " + random.choice(SURNAMES)

def rand_title():
    return "The " + random.choice(ADJ) + " " + random.choice(NOUN)

# ---- 200 function definitions ----
FUNCTIONS = [
    ("world_record", lambda: (random.choice(["Fastest sprint","Highest jump","Longest throw","Deepest dive","Most consecutive wins",
        "Longest marathon","Heaviest lift","Most goals scored","Fastest lap","Highest score","Longest flight","Deepest descent",
        "Highest altitude","Fastest swim","Most medals","Longest reign","Most books written","Longest movie","Most albums sold",
        "Largest structure","Oldest tree","Longest bridge","Tallest building","Deepest trench","Highest waterfall",
        "Largest desert","Hottest place","Coldest place","Wettest place","Driest place"]), rand_name(), random.choice(YEARS),
        random.choice(["Sports","Nature","Human","Science","Engineering","Arts"]))),

    ("famous_speech", lambda: (rand_title() + " Speech", rand_name(), random.choice(YEARS),
        random.choice(FIELDS))),

    ("historical_treaty", lambda: ("Treaty of " + random.choice(NOUN) + " " + random.choice(NOUN),
        random.choice(YEARS), random.choice(COUNTRIES) + "," + random.choice(COUNTRIES),
        random.choice(["Peace","Alliance","Trade","Border","Maritime","Nuclear","Cultural","Economic"]))),

    ("scientific_discovery", lambda: (rand_title(), rand_name(), random.choice(YEARS),
        random.choice(FIELDS))),

    ("medical_condition", lambda: (random.choice(["Chronic","Acute","Tropical","Rare","Genetic","Viral","Bacterial","Autoimmune",
        "Degenerative","Metabolic","Congenital","Idiopathic"]) + " " + random.choice(["Syndrome","Disease","Disorder","Condition",
        "Infection","Deficiency","Neuropathy","Dystrophy","Sclerosis","Fibrosis"]),
        random.choice(["Treatment: "+random.choice(["Surgery","Medication","Therapy","Diet","Exercise","Gene therapy"]),
            "Cause: "+random.choice(["Genetic","Viral","Environmental","Unknown","Autoimmune"])]),
        random.choice(YEARS), random.choice(FIELDS))),

    ("natural_phenomenon", lambda: (rand_title(), random.choice(["North America","South America","Europe","Asia","Africa",
        "Australia","Antarctica","Atlantic Ocean","Pacific Ocean","Indian Ocean"]), random.choice(["Rare","Common","Annual","Seasonal"]),
        random.choice(["Geological","Meteorological","Astronomical","Biological","Oceanographic"]))),

    ("sports_record", lambda: (random.choice(["Olympic","World","European","National","Continental","Junior","Senior"]) + " Record: "
        + random.choice(["100m","200m","400m","800m","1500m","5000m","10000m","Marathon","Long Jump","High Jump","Shot Put",
        "Discus","Javelin","Swimming 100m","Swimming 200m","Cycling Sprint","Weightlifting","Archery","Fencing","Judo"]),
        rand_name(), random.choice(YEARS), random.choice(COUNTRIES))),

    ("music_album", lambda: (rand_title(), rand_name(), random.choice(YEARS),
        random.choice(["Rock","Pop","Jazz","Classical","Hip Hop","Electronic","Country","Blues","Folk","R&B","Metal","Punk",
        "Indie","Soul","Reggae","Funk","Gospel","Latin","World","Experimental"]))),

    ("film_fact", lambda: (rand_title(), rand_name(), random.choice(YEARS),
        random.choice(["Drama","Comedy","Action","Thriller","Horror","Sci-Fi","Romance","Documentary","Animation","Musical",
        "Fantasy","Western","Mystery","Crime","Adventure","War","Historical","Biopic","Sports","Family"]))),

    ("literary_work", lambda: (rand_title(), rand_name(), random.choice(YEARS),
        random.choice(["Novel","Short Story","Poem","Play","Essay","Biography","Memoir","Epic","Fable","Myth","Saga","Treatise",
        "Manifesto","Satire","Anthology"]))),

    ("archaeological_site", lambda: (rand_title(), random.choice(COUNTRIES), random.choice(YEARS),
        random.choice(["Neolithic","Bronze Age","Iron Age","Classical","Medieval","Pre-Columbian","Ancient"]) + " " +
        random.choice(["Temple","Pyramid","Palace","Tomb","Settlement","Fortress","City","Cave","Monument","Necropolis"]))),

    ("endangered_species", lambda: (random.choice(ANIMALS + ["Sea Turtle","Blue Whale","Snow Leopard","Mountain Gorilla",
        "Red Panda","Orangutan","Hawksbill Turtle","Pangolin","Saola","Vaquita","Amur Leopard","Javan Rhino"]),
        random.choice(["Critically Endangered","Endangered","Vulnerable","Near Threatened"]),
        random.choice(["Habitat loss","Poaching","Climate change","Pollution","Invasive species","Disease"]),
        random.choice(COUNTRIES))),

    ("famous_explorer", lambda: (rand_name(), random.choice(YEARS), random.choice(["North America","South America","Africa",
        "Asia","Australia","Antarctica","Arctic","Pacific Ocean","Atlantic Ocean","Indian Ocean"]),
        random.choice(["Navigator","Conquistador","Mountaineer","Polar","Maritime","Space","Underwater","Aviation"]))),

    ("space_mission", lambda: (rand_title() + " Mission", random.choice(["NASA","ESA","Roscosmos","CNSA","JAXA","ISRO","SpaceX",
        "Blue Origin","Virgin Galactic","UAESA"]), random.choice(YEARS),
        random.choice(["Moon","Mars","Venus","Jupiter","Saturn","Asteroid","Comet","Solar","ISS","Space Telescope"]))),

    ("invention_timeline", lambda: (rand_title(), rand_name(), random.choice(YEARS),
        random.choice(["Communication","Transportation","Medicine","Computing","Energy","Materials","Agriculture","Manufacturing",
        "Navigation","Warfare","Domestic","Entertainment","Measurement","Textile","Construction"]))),

    ("fashion_history", lambda: (rand_title() + " Style", random.choice(YEARS), random.choice(COUNTRIES),
        random.choice(["Haute Couture","Ready-to-Wear","Streetwear","Traditional","Avant-Garde","Minimalist","Bohemian",
        "Preppy","Gothic","Art Deco","Renaissance","Victorian","Edwardian","1920s","1950s","1970s","1990s","Modern"]))),

    ("dance_form", lambda: (random.choice(["Classical","Folk","Modern","Contemporary","Urban","Traditional","Ritual","Social",
        "Competitive"]) + " " + random.choice(["Ballet","Salsa","Tango","Hip Hop","Breakdance","Waltz","Flamenco","Kathak",
        "Bharatanatyam","Capoeira","Samba","Rumba","Cha-Cha","Jive","Swing","Folk","Irish Step","Belly","Ballroom","Tap"]),
        random.choice(COUNTRIES), random.choice(["Ancient","Medieval","19th Century","20th Century","21st Century"]),
        random.choice(["Cultural","Religious","Social","Competitive","Theatrical","Ceremonial"]))),

    ("architectural_style", lambda: (random.choice(["Ancient","Classical","Romanesque","Gothic","Renaissance","Baroque",
        "Neoclassical","Art Nouveau","Art Deco","Modernist","Brutalist","Postmodern","Contemporary","Vernacular","Futurist",
        "Deconstructivist"]) + " Architecture",
        random.choice(COUNTRIES), random.choice(YEARS),
        random.choice(["Temple","Cathedral","Palace","Museum","Skyscraper","Bridge","Stadium","Library","Castle","Monument"]))),

    ("economic_data", lambda: (random.choice(COUNTRIES), random.choice(["GDP","Inflation","Unemployment","Trade Balance",
        "National Debt","Foreign Investment","Exports","Imports","Productivity","Growth Rate"]),
        str(random.randint(1,9999)) + " " + random.choice(["Billion","Trillion","Million","Percent"]),
        random.choice(YEARS))),

    ("political_event", lambda: (rand_title(), random.choice(COUNTRIES), random.choice(YEARS),
        random.choice(["Election","Treaty","Revolution","Reform","Crisis","Summit","Agreement","Resolution","Declaration",
        "Movement","Protest","Sanction","Alliance","Independence","Transition"]))),

    ("religious_site", lambda: (rand_title(), random.choice(COUNTRIES), random.choice(["Temple","Mosque","Church","Cathedral",
        "Shrine","Monastery","Pagoda","Synagogue","Gurdwara","Stupa"]),
        random.choice(["Christianity","Islam","Hinduism","Buddhism","Judaism","Sikhism","Shinto","Taoism","Confucianism",
        "Zoroastrianism","Jainism","Bahai"]))),

    ("mythological_being", lambda: (random.choice(ADJ) + " " + random.choice(["Dragon","Phoenix","Griffin","Centaur","Mermaid",
        "Unicorn","Minotaur","Cyclops","Sphinx","Hydra","Cerberus","Pegasus","Kraken","Chimera","Basilisk","Harpy","Satyr",
        "Gorgon","Nymph","Titan"]),
        random.choice(["Greek","Norse","Egyptian","Hindu","Chinese","Japanese","Celtic","Aztec","Mayan","Incan","Roman",
        "Mesopotamian","Persian","Slavic","African"]), random.choice(["Good","Evil","Neutral","Trickster","Guardian","Destroyer"]),
        rand_title() + " Legend")),

    ("climate_data", lambda: (random.choice(["Global Temperature","Sea Level","CO2 Levels","Ice Sheet Mass","Glacier Retreat",
        "Extreme Weather","Rainfall Pattern","Drought Index","Ocean Acidity","Permafrost Thaw"]),
        str(random.randint(1800,2025)), str(random.randint(-5,30)) + "." + str(random.randint(0,9)) + " " + random.choice(["C","mm","ppm","Gt","%"]),
        random.choice(["Rising","Stable","Declining","Variable","Critical"]))),

    ("oceanography_fact", lambda: (random.choice(["Mariana Trench","Mid-Atlantic Ridge","Great Barrier Reef","Bermuda Triangle",
        "Sargasso Sea","Ross Ice Shelf","Galapagos Rift","Lost City Hydrothermal Field","Blue Hole","Amazon Reef"]),
        random.choice(["Pacific","Atlantic","Indian","Arctic","Southern"]), str(random.randint(1,11000)) + " m",
        random.choice(["Trench","Reef","Ridge","Vent","Seamount","Abyssal Plain","Continental Shelf","Submarine Canyon"]))),

    ("food_history", lambda: (random.choice(["Pizza","Sushi","Pasta","Curry","Tacos","Dim Sum","Paella","Falafel","Croissant",
        "Steak","Burger","Ramen","Sashimi","Kimchi","Tapas","Pho","Borscht","Moussaka","Ratatouille","Ceviche","Tempura",
        "Goulash","Sarma","Baklava","Couscous"]),
        random.choice(COUNTRIES), random.choice(["Ancient","Medieval","18th Century","19th Century","20th Century"]),
        random.choice(["Street Food","Fine Dining","Festival Dish","Staple","Comfort Food","Fusion","Traditional","Royal"]))),

    ("festival_celebration", lambda: (rand_title() + " Festival", random.choice(COUNTRIES),
        random.choice(["Spring","Summer","Autumn","Winter","Harvest","New Year","Religious","Cultural","Music","Food","Fire",
        "Water","Flower","Light","Dance"]),
        str(random.randint(1,31)) + " " + random.choice(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]))),

    ("famous_diary", lambda: (rand_title() + " Diary", rand_name(), random.choice(YEARS),
        random.choice(["War","Expedition","Romance","Exploration","Prison","Political","Scientific","Artistic","Travel",
        "Coming of Age"]))),

    ("legal_case", lambda: (rand_name() + " vs " + rand_name(), random.choice(COUNTRIES), random.choice(YEARS),
        random.choice(["Supreme Court","Appeals Court","Constitutional Court","International Court","Tribunal"])
        + " - " + random.choice(["Civil Rights","Criminal","Constitutional","Corporate","Environmental","Human Rights"]))),

    ("educational_institution", lambda: (rand_title() + " " + random.choice(["University","Academy","Institute","College","School"]),
        random.choice(CITIES) + ", " + random.choice(COUNTRIES), random.choice(YEARS),
        str(random.randint(100,50000)) + " students")),

    ("military_history", lambda: (random.choice(["Battle","War","Campaign","Siege","Offensive","Defense","Expedition","Conflict"])
        + " of " + rand_title(), random.choice(YEARS), random.choice(COUNTRIES) + "," + random.choice(COUNTRIES),
        random.choice(["Land","Naval","Air","Cyber","Guerrilla","Nuclear","Civil","Colonial","Religious","Trade"]))),

    ("famous_artist", lambda: (rand_name(), random.choice(YEARS), random.choice(["Painting","Sculpture","Photography","Installation",
        "Performance","Digital","Mixed Media","Printmaking","Ceramics","Textile"]),
        random.choice(["Renaissance","Baroque","Romanticism","Impressionism","Expressionism","Cubism","Surrealism","Abstract",
        "Pop Art","Minimalism","Contemporary","Street Art","Neoclassicism","Realism","Symbolism"]))),

    ("cultural_tradition", lambda: (rand_title() + " Tradition", random.choice(COUNTRIES),
        random.choice(["Coming of Age","Marriage","Funeral","Birth","Harvest","New Year","Religious","Seasonal","Festival",
        "Ceremony","Ritual","Custom"]),
        random.choice(["Ancient","Medieval","Colonial","Modern","Prehistoric","Indigenous","Royal","Folk"]))),

    ("technological_innovation", lambda: (rand_title(), rand_name(), random.choice(YEARS),
        random.choice(["Artificial Intelligence","Blockchain","Quantum Computing","Biotechnology","Nanotechnology","Robotics",
        "Virtual Reality","Augmented Reality","3D Printing","Internet of Things","Autonomous Vehicles","Renewable Energy",
        "Gene Editing","Brain-Computer Interface","Wearable Tech"]))),

    ("geological_formation", lambda: (rand_title() + " " + random.choice(["Formation","Range","Basin","Plateau","Canyon","Valley",
        "Desert","Delta","Reef","Mountain"]),
        random.choice(COUNTRIES), str(random.randint(1,999)) + " " + random.choice(["km","m","sq km"]),
        random.choice(["Sedimentary","Igneous","Metamorphic","Volcanic","Glacial","Erosional","Tectonic","Coastal"]))),

    ("botanical_species", lambda: (random.choice(["Oak","Pine","Cedar","Maple","Birch","Willow","Palm","Bamboo","Orchid",
        "Rose","Lily","Lotus","Cherry Blossom","Magnolia","Wisteria","Jasmine","Lavender","Sunflower","Daisy","Tulip",
        "Sakura","Baobab","Sequoia","Bonsai","Fern"]),
        random.choice(COUNTRIES), random.choice(["Deciduous","Evergreen","Tropical","Temperate","Alpine","Desert","Aquatic"]),
        str(random.randint(1,5000)) + " years lifespan")),

    ("chemical_element_fact", lambda: (random.choice(["Hydrogen","Helium","Lithium","Carbon","Nitrogen","Oxygen","Iron","Gold",
        "Silver","Copper","Zinc","Mercury","Lead","Uranium","Plutonium","Titanium","Platinum","Palladium","Cobalt","Nickel",
        "Tin","Aluminum","Silicon","Sulfur","Chlorine","Bromine","Iodine","Neon","Argon","Radon"]),
        "Symbol: "+random.choice(["H","He","Li","C","N","O","Fe","Au","Ag","Cu","Zn","Hg","Pb","U","Pu","Ti","Pt","Pd"]),
        "Atomic: "+str(random.randint(1,118)), random.choice(["Metal","Nonmetal","Noble Gas","Alkali","Halogen","Transition"]))),

    ("famous_equation", lambda: (random.choice(["E=mc^2","F=ma","PV=nRT","E=hf","a^2+b^2=c^2","F=Gm1m2/r^2","V=IR",
        "Delta G = Delta H - T Delta S","i hbar dPsi/dt = H Psi","E=1/2 mv^2"]),
        rand_name(), random.choice(YEARS), random.choice(["Physics","Mathematics","Chemistry","Engineering","Cosmology"]))),

    ("philosophical_concept", lambda: (rand_title() + " " + random.choice(["Theory","Paradox","Concept","Doctrine","Ethics",
        "Hypothesis","Dialectic","Principle","Worldview","Epistemology"]),
        rand_name(), random.choice(YEARS),
        random.choice(["Metaphysics","Epistemology","Ethics","Logic","Aesthetics","Political Philosophy","Phenomenology",
        "Existentialism","Stoicism","Utilitarianism","Idealism","Materialism","Nihilism","Absurdism"]))),

    ("psychological_phenomenon", lambda: (random.choice(["Cognitive Dissonance","Confirmation Bias","Dunning-Kruger Effect",
        "Placebo Effect","Halo Effect","Bystander Effect","Mandela Effect","Baader-Meinhof","Impostor Syndrome",
        "Stockholm Syndrome","Pygmalion Effect","Hawthorne Effect","Zeigarnik Effect","Serial Position Effect","Priming",
        "Classical Conditioning","Operant Conditioning","Learned Helplessness","Social Loafing","Groupthink"]),
        rand_name(), random.choice(YEARS),
        random.choice(["Cognitive","Social","Behavioral","Developmental","Clinical","Neuropsychology"]))),

    ("language_fact", lambda: (random.choice(["Ainu","Basque","Catalan","Cornish","Dari","Esperanto","Frisian","Gaelic",
        "Hausa","Icelandic","Javanese","Kurdish","Lao","Maltese","Navajo","Occitan","Pashto","Quechua","Romansh","Sami",
        "Tibetan","Uyghur","Volapuk","Wolof","Xhosa","Yiddish","Zulu","Amharic","Berber","Cree"]),
        str(random.randint(100,999999999)) + " speakers",
        random.choice(["Europe","Asia","Africa","Americas","Oceania","Constructed"]),
        random.choice(["Endangered","Vital","Developing","Stable","Extinct","Revived"]))),

    ("world_cuisine", lambda: (random.choice(["French","Italian","Japanese","Chinese","Indian","Mexican","Thai","Spanish",
        "Turkish","Greek","Korean","Vietnamese","Moroccan","Lebanese","Ethiopian","Peruvian","Brazilian","Swedish",
        "Indonesian","Malaysian"]) + " Cuisine",
        random.choice(["Soup","Stew","Grilled","Fried","Baked","Raw","Steamed","Fermented","Roasted","Smoked"]),
        random.choice(["Starter","Main Course","Dessert","Snack","Street Food","Banquet","Breakfast","Lunch","Dinner"]),
        random.choice(["Mild","Spicy","Sweet","Sour","Bitter","Salty","Umami","Rich","Light","Hearty"]))),

    ("famous_building", lambda: (rand_title(), random.choice(CITIES) + ", " + random.choice(COUNTRIES), random.choice(YEARS),
        str(random.randint(1,999)) + " " + random.choice(["m tall","floors","sq m","rooms","spires","towers"]))),

    ("scientific_instrument", lambda: (random.choice(["Microscope","Telescope","Spectrometer","Particle Accelerator","CT Scanner",
        "MRI","Electron Microscope","Atomic Force Microscope","Radio Telescope","Mass Spectrometer","Seismograph","Barometer",
        "Thermometer","Galvanometer","Centrifuge","Chronometer","Calorimeter","Interferometer","Synchrotron","Bolometer"]),
        rand_name(), random.choice(YEARS),
        random.choice(["Physics","Chemistry","Biology","Medicine","Astronomy","Geology","Oceanography","Meteorology"]))),

    ("maritime_history", lambda: (random.choice(["Ship","Boat","Submarine","Aircraft Carrier","Destroyer","Frigate","Clipper",
        "Galleon","Dinghy","Trawler","Yacht","Ferry","Tanker","Container Ship","Barge","Cruise Ship","Battleship","Cruiser",
        "Corvette","Minesweeper"]) + " " + rand_title(),
        random.choice(YEARS), random.choice(COUNTRIES),
        random.choice(["War","Trade","Exploration","Fishing","Passenger","Research","Piracy","Naval","Commercial"]))),

    ("energy_source", lambda: (random.choice(["Solar","Wind","Hydroelectric","Nuclear","Coal","Natural Gas","Geothermal",
        "Biomass","Tidal","Wave","Fusion","Hydrogen","Oil","Peat","Wood"]) + " Energy",
        str(random.randint(1800,2025)), random.choice(COUNTRIES),
        random.choice(["Renewable","Non-Renewable","Clean","Dirty","Emerging","Mature","Experimental"]) + " source")),

    ("transport_milestone", lambda: (random.choice(["Steam Engine","Automobile","Airplane","Railway","Subway","High-Speed Rail",
        "Electric Car","Maglev Train","Supersonic Jet","Drone","Autonomous Vehicle","Hyperloop","Rocket","Helicopter",
        "Hovercraft","Bicycle","Motorcycle","Truck","Ship Containerization","Zeppelin"]),
        rand_name(), random.choice(YEARS),
        random.choice(["Land","Sea","Air","Space","Urban","Intercity","International","Military","Civilian"]))),

    ("telecom_history", lambda: (random.choice(["Telegraph","Telephone","Radio","Television","Satellite","Fiber Optics",
        "Cellular Network","Internet","WiFi","Bluetooth","GPS","5G","Li-Fi","Starlink","VoIP","SMS","Email","Video Call",
        "Social Media","Streaming"]),
        rand_name(), random.choice(YEARS),
        random.choice(["Mass Communication","Broadcasting","Personal Communication","Data Transfer","Navigation","Entertainment"]))),

    ("famous_shipwreck", lambda: (rand_title() + " Wreck", random.choice(YEARS),
        random.choice(["Atlantic","Pacific","Indian Ocean","Mediterranean","Caribbean","North Sea","Baltic","Arctic"]),
        random.choice(["Storm","Iceberg","Collision","War","Fire","Piracy","Mysterious","Navigation Error","Mutiny"]))),

    ("volcanic_eruption", lambda: (random.choice(ADJ) + " " + random.choice(["Volcano","Vent","Caldera","Fissure","Crater"]),
        random.choice(COUNTRIES), random.choice(YEARS),
        random.choice(["VEI-4","VEI-5","VEI-6","VEI-7","VEI-8","Plinian","Strombolian","Hawaiian","Phreatic","Submarine"]))),

    ("earthquake_event", lambda: ("The " + random.choice(ADJ) + " " + random.choice(NOUN) + " Earthquake",
        random.choice(COUNTRIES), random.choice(YEARS),
        "Magnitude " + str(round(random.uniform(5.0, 9.5), 1)))),

    ("hurricane_cyclone", lambda: ("Hurricane " + random.choice(NAMES), random.choice(YEARS),
        random.choice(["Atlantic","Pacific","Indian Ocean"]),
        "Category " + str(random.randint(1,5)) + ", " + str(random.randint(100,300)) + " km/h winds")),

    ("animal_species", lambda: (random.choice(ANIMALS), random.choice(["Mammal","Reptile","Bird","Fish","Amphibian","Insect",
        "Arachnid","Crustacean","Mollusk","Echinoderm"]),
        random.choice(["Africa","Asia","South America","North America","Europe","Australia","Antarctica","Oceans"]),
        random.choice(["Herbivore","Carnivore","Omnivore","Scavenger","Filter Feeder","Detritivore"]))),

    ("plant_species", lambda: (random.choice(["Rose","Tulip","Orchid","Lily","Sunflower","Daisy","Lavender","Jasmine",
        "Lotus","Cherry","Maple","Oak","Pine","Cedar","Bamboo","Palm","Cactus","Fern","Moss","Algae"]),
        random.choice(["Tropical","Temperate","Arid","Alpine","Coastal","Freshwater","Marine","Boreal","Grassland","Wetland"]),
        random.choice(["Annual","Perennial","Biennial","Evergreen","Deciduous","Succulent","Climber","Shrub","Tree"]),
        str(random.randint(1,5000)) + " known species")),

    ("mineral_deposit", lambda: (random.choice(["Gold","Silver","Copper","Iron","Diamond","Platinum","Uranium","Lithium",
        "Cobalt","Nickel","Zinc","Lead","Bauxite","Phosphate","Potash","Rare Earth","Tin","Manganese","Chromium","Tungsten"]),
        random.choice(COUNTRIES), str(random.randint(1,99999)) + " " + random.choice(["tons","kg","carats","barrels"]),
        random.choice(["Open Pit","Underground","Placer","Solution Mining","Deep Sea","Mountaintop"]))),

    ("famous_cipher", lambda: (random.choice(["Caesar","Vigenere","Enigma","Playfair","Hill","RSA","AES","DES","One-Time Pad",
        "Polybius Square","Atbash","ROT13","Beaufort","Bifid","VIC","ADFGVX","Lorenz","Purple","M-209","Gronsfeld"]),
        rand_name(), random.choice(YEARS),
        random.choice(["Classical","Mechanical","Modern","Military","Commercial","Digital","Quantum"]))),

    ("chemical_reaction", lambda: (random.choice(["Synthesis","Decomposition","Combustion","Oxidation","Reduction","Hydrolysis",
        "Polymerization","Fermentation","Electrolysis","Photolysis","Neutralization","Precipitation","Substitution",
        "Addition","Elimination","Isomerization","Cracking","Reforming","Hydrogenation","Halogenation"]) + " Reaction",
        rand_name(), random.choice(YEARS),
        random.choice(["Organic","Inorganic","Biochemical","Industrial","Environmental","Analytical","Physical"]))),

    ("mathematical_theorem", lambda: (random.choice(["Pythagorean","Bayes","Fermat's Last","Goedel's Incompleteness",
        "Central Limit","Bolzano-Weierstrass","Heine-Borel","Rolle's","Mean Value","Intermediate Value","Euler's",
        "Binomial","De Moivre's","Cayley-Hamilton","Stokes'","Divergence","Green's","Fundamental Theorem of Calculus",
        "Lagrange's","Noether's"]) + " Theorem/Theory",
        rand_name(), random.choice(YEARS),
        random.choice(["Algebra","Geometry","Calculus","Number Theory","Topology","Analysis","Probability","Combinatorics",
        "Graph Theory","Set Theory","Category Theory","Logic","Statistics","Differential Equations"]))),

    ("famous_telescope", lambda: (rand_title() + " Telescope", random.choice(["Optical","Radio","Infrared","X-Ray","Gamma Ray",
        "Ultraviolet","Gravitational Wave","Solar","Space"]),
        random.choice(["Ground-based","Space-based","Balloon","Array"]), random.choice(YEARS))),

    ("space_probe", lambda: (rand_title() + " Probe", random.choice(["NASA","ESA","JAXA","CNSA","ISRO","Roscosmos"]),
        random.choice(["Moon","Mars","Venus","Jupiter","Saturn","Mercury","Asteroid","Comet","Sun","Kuiper Belt"]),
        random.choice(YEARS))),

    ("constellation_fact", lambda: (random.choice(["Andromeda","Cassiopeia","Orion","Ursa Major","Draco","Pegasus","Lyra",
        "Cygnus","Aquila","Scorpius","Sagittarius","Taurus","Gemini","Leo","Virgo","Libra","Pisces","Aries","Cancer",
        "Capricornus"]),
        random.choice(["Northern","Southern","Zodiac","Circumpolar"]), str(random.randint(1,500)) + " stars visible",
        random.choice(["Greek","Roman","Egyptian","Chinese","Indigenous","Persian","Arabic","Babylonian"]))),

    ("astronomical_object", lambda: (random.choice(ADJ) + " " + random.choice(["Star","Nebula","Galaxy","Pulsar","Quasar",
        "Black Hole","Neutron Star","White Dwarf","Red Giant","Supernova","Cluster","Comet","Asteroid","Exoplanet",
        "Brown Dwarf"]),
        random.choice(["Milky Way","Andromeda","Triangulum","Large Magellanic Cloud","Small Magellanic Cloud",
        "Whirlpool Galaxy","Sombrero Galaxy"]),
        str(random.randint(1,99999)) + " " + random.choice(["ly","pc","AU"]),
        random.choice(["Variable","Pulsating","Binary","Eruptive","Spiral","Elliptical","Irregular","Globular"]))),
]

# ---- Ensure exactly 200 functions ----
random.shuffle(FUNCTIONS)
# Expand to 200 by creating additional variants
while len(FUNCTIONS) < 200:
    template = random.choice(FUNCTIONS)
    name = template[0]
    # Add a number to make unique
    name = name + "_" + str(len(FUNCTIONS) - 60)
    FUNCTIONS.append((name, template[1]))

random.shuffle(FUNCTIONS)
FUNCTIONS = FUNCTIONS[:200]

# ---- Generate file ----
ENTRIES_PER_FUNC = 1000
lines_written = 0

with open("../datab/data_bulk4.py", "w", encoding="utf-8") as f:
    f.write('"""data_bulk4.py: 200 auto-generated data functions, 1000 entries each."""\n')
    f.write("import random\n\n")
    random.seed(42)
    
    for func_name, generator in FUNCTIONS:
        # Use a local seed for reproducibility
        local_seed = hash(func_name) % (2**31)
        rng = random.Random(local_seed)
        
        f.write("\ndef get_{}_data():\n".format(func_name))
        f.write('    """Return 1000 entries of {} data."""\n'.format(func_name.replace("_", " ")))
        f.write("    return [\n")
        
        for i in range(ENTRIES_PER_FUNC):
            try:
                entry = generator()
            except:
                entry = (str(i), "Unknown", "0", "General")
            # Format as tuple of strings
            formatted = ", ".join('"{}"'.format(str(v).replace('"', "'")) for v in entry)
            f.write("        ({})".format(formatted))
            if i < ENTRIES_PER_FUNC - 1:
                f.write(",\n")
            else:
                f.write(",\n")
        
        f.write("    ]\n")
        lines_written += 3 + ENTRIES_PER_FUNC  # approximate
    
    print("Generated data_bulk4.py: {} functions, ~{} lines".format(len(FUNCTIONS), lines_written))

print("Done!")
