from aipy_ansi import *
from data_bulk import *
from data_bulk2 import *
from data_bulk3 import *
from data_bulk4 import *
from data_bulk5 import *
from data_bulk6 import *
from data_bulk7 import *
from data_bulk8 import *
from data_bulk9 import *
from data_bulk10 import *
from data_bulk11 import *
from data_bulk12 import *
from data_bulk13 import *
from data_bulk14 import *
from data_bulk15 import *
from data_bulk16 import *
from data_bulk17 import *
from data_bulk18 import *
from data_bulk19 import *
from data_bulk20 import *
from data_bulk21 import *
from data_bulk22 import *
from data_bulk23 import *
from data_bulk24 import *
from data_bulk25 import *
from data_bulk26 import *
from data_bulk27 import *
from data_bulk28 import *
from data_bulk29 import *
from data_bulk30 import *
from data_bulk31 import *
from data_bulk32 import *
from data_bulk33 import *
from data_bulk34 import *
from data_bulk35 import *
from data_bulk36 import *
from data_bulk37 import *
from data_bulk38 import *
import aiscript
import random, os, json, textwrap
__version__ = "6.1.0"

def show_help(role=None):
    print("15 - ASCII house            16 - ASCII flower")
    print("17 - ASCII smiley           18 - Fibonacci")
    print("19 - Prime check            20 - Factorial")
    print("21 - GCD                    22 - LCM")
    print("23 - Prime factors          24 - Text analyzer")
    print("25 - Binary                 26 - Hex")
    print("27 - Octal                  28 - Roman numerals")
    print("29 - Temperature conv       30 - Distance conv")
    print("31 - Weight conv            32 - Random password")
    print("33 - Password strength      34 - Pig Latin")
    print("35 - Guess number           36 - Hangman")
    print("37 - Word scramble          38 - Riddle game")
    print("39 - Trivia quiz            40 - Magic 8 ball")
    print("41 - Caesar cipher          42 - Palindrome")
    print("43 - Anagram                44 - BMI calculator")
    print("45 - Zodiac                 46 - Morse code")
    print("47 - Day of week            48 - Leap year")
    print("49 - Multiplication table   50 - Progress bar")
    print("51 - Countdown              52 - Random name")
    print("53 - Coin flip              54 - Dice roll")
    print("55 - Card draw              56 - High/Low game")
    print("57 - Rock paper scissors    58 - Todo manager")
    print("59 - Calendar               60 - Calculator")
    print("61 - Mean/Med/Mode          62 - Std deviation")
    print("63 - Quadratic              64 - Bubble sort")
    print("65 - Binary search          66 - Typing test")
    print("67 - Quote                  68 - More quotes")
    print("69 - Random animal          70 - Random color")
    print("71 - Random fruit           72 - Random vegetable")
    print("73 - Random element         74 - Random number")
    print("75 - Random UUID            76 - ASCII pyramid")
    print("77 - ASCII triangle         78 - ASCII rev triangle")
    print("79 - ASCII hourglass        80 - ASCII circle")
    print("81 - ASCII pineapple        82 - ASCII ghost")
    print("83 - ASCII alien            84 - ASCII bird")
    print("85 - ASCII turtle           86 - ASCII unicorn")
    print("87 - ASCII robot            88 - ASCII spaceship")
    print("89 - ASCII dragon           90 - ASCII crown")
    print("91 - ASCII castle           92 - ASCII mountain")
    print("93 - ASCII wave             94 - ASCII sun")
    print("95 - ASCII moon             96 - ASCII star shape")
    print("97 - ASCII arrow up         98 - ASCII arrow down")
    print("99 - ASCII arrow left       100 - ASCII arrow right")
    print("101 - ASCII DNA             102 - ASCII pacman")
    print("103 - ASCII bowtie          104 - ASCII flag")
    print("105 - ASCII stairs          106 - ASCII table")
    print("107 - ASCII candle          108 - ASCII lamp")
    print("109 - ASCII key             110 - ASCII lock")
    print("111 - ASCII phone           112 - ASCII TV")
    print("113 - ASCII envelope        114 - ASCII coffee")
    print("115 - ASCII burger          116 - ASCII pizza")
    print("117 - ASCII ice cream       118 - ASCII cake")
    print("119 - ASCII house+sun       120 - Convert seconds")
    print("121 - Random data           122 - Shuffle list")
    print("123 - Flatten list          124 - Chunk list")
    print("125 - Unique elements       126 - List intersect")
    print("127 - List union            128 - List difference")
    print("129 - List sym diff         130 - Rotate list")
    print("131 - Find indexes          132 - Split evens/odds")
    print("133 - Sum digits            134 - Reverse number")
    print("135 - Armstrong             136 - Perfect number")
    print("137 - Happy number          138 - Collatz seq")
    print("139 - Sieve of Eratosth     140 - Nth prime")
    print("141 - Goldbach              142 - Euler totient")
    print("143 - Ext GCD               144 - Mod inverse")
    print("145 - Matrix multiply       146 - Transpose")
    print("147 - Matrix det            148 - Dot product")
    print("149 - Cross product         150 - Vector magnitude")
    print("151 - Euclid distance       152 - Manhattan dist")
    print("153 - Hamming dist          154 - Levenshtein")
    print("155 - Base converter        156 - SHA256 hash")
    print("157 - MD5 hash              158 - Base64 encode")
    print("159 - Base64 decode         160 - ROT13")
    print("161 - Text to ASCII         162 - ASCII to text")
    print("163 - Count words           164 - Count sentences")
    print("165 - Count paragraphs      166 - Remove dup words")
    print("167 - Reverse words         168 - Sort words")
    print("169 - Shuffle words         170 - Acronym")
    print("171 - Capitalize title      172 - Detect language")
    print("173 - Spell check           174 - Word frequency")
    print("175 - Longest word          176 - Shortest word")
    print("177 - Common letter         178 - Has URL")
    print("179 - Has email             180 - Extract numbers")
    print("181 - Extract emails        182 - Extract URLs")
    print("183 - Remove HTML tags      184 - Censor words")
    print("185 - Suggest emoji         186 - Format JSON")
    print("187 - Count JSON elements   188 - CSV to list")
    print("189 - Dice roll sim         190 - Coin flip sim")
    print("191 - Lottery sim           192 - Birthday paradox")
    print("193 - Monty Hall sim        194 - Morse to text")
    print("195 - Atbash cipher         196 - Vigenere cipher")
    print("197 - XOR cipher            198 - Substitution cipher")
    print("199 - Nerd dice             200 - Poker hand")
    print("201 - Goldbach format       202 - Number facts")
    print("203 - Temp summary          204 - Days til birthday")
    print("205 - Days since birth      206 - Age in seconds")
    print("207 - Current time info     208 - Week number")
    print("209 - Day of year           210 - Next full moon")
    print("211 - Moon phase            212 - Horoscope")
    print("213 - Numerology            214 - Chinese zodiac")
    print("215 - Tarot                 216 - Crystal ball")
    print("217 - Coffee grounds        218 - Magic spell")
    print("219 - Country info          220 - World clock")
    print("221 - Countdown to NY       222 - Countdown Xmas")
    print("223 - Random movie          224 - Random book")
    print("225 - Random song           226 - Random recipe")
    print("227 - Random hobby          228 - Workout")
    print("229 - Meditation guide      230 - BMI calc")
    print("231 - Tip calculator        232 - Loan calculator")
    print("233 - Savings calculator    234 - Unit converter")
    print("235 - Discount calculator   236 - Currency converter")
    print("237 - Planet info           238 - Astronomy fact")
    print("239 - Weather fact          240 - Ocean fact")
    print("241 - Space mission fact     242 - Number guessing 2")
    print("243 - Color quiz            244 - Fruit quiz")
    print("245 - Animal quiz           246 - Country quiz")
    print("247 - Random emoji          248 - Random planet")
    print("249 - Random galaxy         250 - Random star")
    print("251 - Random asteroid       252 - Random comet")
    print("253 - Random nebula         254 - Random quasar")
    print("255 - Random black hole")
    print("256 - Capital city quiz     257 - Flag quiz")
    print("258 - Math quiz             259 - Science quiz")
    print("260 - History quiz          261 - Geography quiz")
    print("262 - Programming quiz      263 - Random emoji")
    print("264 - Random constellation  265 - Random dinosaur")
    print("266 - Random flower         267 - Random gemstone")
    print("268 - Mythical creature     269 - Planet type")
    print("270 - Chemical reaction     271 - Mathematician")
    print("272 - Biologist             273 - Physicist")
    print("274 - Inventor              275 - Planet weight")
    print("276 - Solar age             277 - Space distance")
    print("278 - Apollo missions       279 - Rocket facts")
    print("280 - Mars facts            281 - Jupiter facts")
    print("282 - Deep space fact       283 - Random moon")
    print("284 - Random exoplanet      285 - ISS crew")
    print("286 - Asteroid belt         287 - Tic Tac Toe")
    print("288 - Connect Four          289 - Word search")
    print("290 - Number puzzle         291 - Memory game")
    print("292 - Reaction game         293 - Binary search game")
    print("294 - Word association      295 - Rapid math")
    print("296 - Movie trivia          297 - Music trivia")
    print("298 - Sports trivia         299 - Art trivia")
    print("300 - Food trivia           301 - Animal trivia")
    print("302 - Tech trivia           303 - Nature trivia")
    print("304 - Random trivia         305 - Random sentence")
    print("306 - Random poem           307 - Haiku")
    print("308 - Tongue twister        309 - Proverb")
    print("310 - Idiom                 311 - Simile")
    print("312 - Metaphor              313 - Oxymoron")
    print("314 - Palindrome word       315 - Anagra")
    print("316 - Chessboard            317 - Sierpinski")
    print("318 - Radial star           319 - Spiral")
    print("320 - Maze                  321 - Target")
    print("322 - Snowflake             323 - Fractal tree")
    print("324 - Flower garden         325 - Cross")
    print("326 - Fence                 327 - Railroad")
    print("328 - Tunnel                329 - Lighthouse")
    print("330 - Rocket                331 - Submarine")
    print("332 - Helicopter            333 - Airplane")
    print("334 - Bicycle               335 - Umbrella")
    print("336 - Compass               337 - Web")
    print("338 - Bridge                339 - Castle tower")
    print("340 - Sword                 341 - Shield")
    print("342 - Anchor                343 - Crown king")
    print("344 - Throne")
    print("345 - HubBasePE (launch PE)")
    print("346 - Random country        347 - Country continent")
    print("348 - World population       349 - Largest cities")
    print("350 - World rivers           351 - World mountains")
    print("352 - World deserts          353 - World islands")
    print("354 - World lakes            355 - World wonders")
    print("356 - World currencies       357 - Flag description")
    print("358 - Random story           359 - Programming joke")
    print("360 - Animal joke            361 - Food joke")
    print("362 - Science joke           363 - Sports joke")
    print("364 - Music joke             365 - Math joke")
    print("366 - History joke           367 - Dad joke")
    print("368 - Conversation starter   369 - Philosophy question")
    print("370 - Nobel Prize            371 - Historic event")
    print("372 - Philosopher            373 - Scientific law")
    print("374 - Programming language   375 - Algorithm")
    print("376 - Data structure         377 - Tech company")
    print("378 - Historical figure      379 - World record")
    print("380 - Math fact              381 - Chemistry fact")
    print("382 - Biology fact           383 - Physics fact")
    print("384 - Geography fact         385 - Astronomy fact")
    print("386 - Psychology fact        387 - Technology fact")
    print("388 - Geology fact           389 - Sports fact")
    print("390 - Music fact             391 - Art fact")
    print("392 - Medicine fact          393 - Economics fact")
    print("394 - Literature fact        395 - Random movie")
    print("396 - Random song            397 - Random book")
    print("398 - Cocktail recipe        399 - Board game")
    print("400 - Video game             401 - TV show")
    print("402 - Space mission          403 - Country fact")
    print("404 - Language fact          405 - Food fact")
    print("406 - Animal fact            407 - Ocean fact")
    print("408 - Moon fact              409 - Weather fact")
    print("410 - Invention              411 - Random quote")
    print("412 - Holiday                413 - Random joke")
    print("414 - Puzzle                 415 - AI fact")
    print("416 - Quantum fact           417 - Space object")
    print("418 - Human body fact        419 - Architecture")
    print("420 - Energy fact            421 - Mythology fact")
    print("422 - Ocean life fact        423 - Mountain fact")
    print("424 - River fact             425 - Desert fact")
    print("426 - Forest fact            427 - Volcano fact")
    print("428 - City fact              429 - Flag fact")
    print("430 - Number fact            431 - History fact")
    print("432 - Lake fact              433 - Island fact")
    print("434 - Planet fact            435 - Ocean fact II")
    print("436 - Culture fact           437 - Famous landmark")
    print("438 - Weather phenomenon     439 - Science experiment")
    print("440 - Engineering fact       441 - Medicine fact II")
    print("442 - Bridge fact            443 - Tunnel fact")
    print("444 - Animal speed fact      445 - Unusual ability")
    print("446 - Dinosaur fact")
    print("447 - Space mission deep     448 - Natural disaster")
    print("449 - Climate fact            450 - Chemical element")
    print("451 - Programming term        452 - Festival")
    print("453 - Renewable energy fact")
    print("454 - City data            455 - Country details")
    print("456 - Occupation data      457 - Recipe data")
    print("458 - Animal data          459 - Planet data")
    print("460 - Mountain data        461 - River data")
    print("462 - Lake data            463 - Island data")
    print("464 - Ocean features       465 - Star data")
    print("466 - Galaxy data          467 - Dinosaur data")
    print("468 - Mineral data         469 - Tree data")
    print("470 - Flower data          471 - Butterfly data")
    print("472 - Bird data            473 - Shark data")
    print("474 - Whale data           475 - Snake data")
    print("476 - Fish data            477 - Dog breed data")
    print("478 - Cat breed data       479 - Horse breed data")
    print("480 - Herb data            481 - Spice data")
    print("482 - Wine data            483 - Cheese data")
    print("484 - Cocktail data        485 - Dessert data")
    print("486 - Programming terms    487 - Math theorems")
    print("488 - Physics concepts     489 - Chemical elements")
    print("490 - Medical terms        491 - Musical terms")
    print("492 - Instrument data      493 - Sport data")
    print("494 - Gemstone data        495 - Architecture data")
    print("496 - Mythology data       497 - Philosopher data")
    print("498 - Historical events    499 - Artist data")
    print("500 - Movie data           501 - Book data")
    print("502 - Song data            503 - Painting data")
    print("504 - Invention data       505 - Airport data")
    print("506 - Hotel data           507 - Restaurant data")
    print("508 - University data      509 - Museum data")
    print("510 - Park data            511 - Library data")
    print("512 - Bridge data          513 - Tunnel data")
    print("514 - Dam data             515 - Canal data")
    print("516 - Lighthouse data      517 - Castle data")
    print("518 - Temple data          519 - Church data")
    print("520 - Mosque data          521 - Synagogue data")
    print("522 - Observatory data     523 - Research station data")
    print("524 - Power plant data     525 - Hospital data")
    print("526 - School data          527 - Stadium data")
    print("528 - Conference center    529 - Shopping mall data")
    print("530 - Train station data   531 - Subway station data")
    print("532 - Port data            533 - Railway line data")
    print("534 - Highway data         535 - Cuisine data")
    print("536 - Heritage site data   537 - National symbol data")
    print("538 - Corporation data     539 - Nonprofit data")
    print("540 - Journal data         541 - Award data")
    print("542 - Festival data        543 - Battle data")
    print("801 - PyLevel test")
    print()
    if role:
        print("=== {} COMMANDS ===".format(role))
        if role == "Admin":
            print("system_info   - System information")
            print("list_users    - List online users")
            print("clear_logs    - Clear system logs")
            print("toggle_debug  - Toggle debug mode")
            print("hbpe_start    - Start HubBasePE")
            print("hbpe_advance  - Advance HubBasePE")
            print("hbpe_restart  - Restart HubBasePE")
            print("hbpe_stop     - Stop HubBasePE")
            print("hbpe_program1-20 - Run programs 1-20")
            print("hbpe_programp1-5 - Run programs P1-P5")
            print("hbpe_dev_console - HubBasePE dev console")
            print("hbpe_compat   - Show HBPE version info")
            print("aiscript_run  - Run AiScript code inline")
            print("aiscript_file - Run an AiScript .ais file")
            print("docs          - Open HTML documentation")
            print("dashboard     - Open HTML dashboard")
        elif role == "Mod":
            print("featured_joke - Show featured joke")
            print("mute_user     - Mute a user")
            print("warn_user     - Warn a user")
            print("hbpe_start    - Start HubBasePE")
            print("hbpe_advance  - Advance HubBasePE")
            print("hbpe_stop     - Stop HubBasePE")
            print("hbpe_program1-20 - Run programs 1-20")
            print("hbpe_dev_console - HubBasePE dev console")
            print("hbpe_compat   - Show HBPE version info")
            print("aiscript_run  - Run AiScript code inline")
            print("aiscript_file - Run an AiScript .ais file")
            print("docs          - Open HTML documentation")
            print("dashboard     - Open HTML dashboard")
        elif role == "Vip":
            print("vip_fact  - VIP exclusive fact")
            print("vip_quote - VIP exclusive quote")
            print("hbpe_start    - Start HubBasePE")
            print("hbpe_program1-20 - Run programs 1-20")
            print("hbpe_dev_console - HubBasePE dev console")
            print("hbpe_compat   - Show HBPE version info")
            print("aiscript_run  - Run AiScript code inline")
            print("aiscript_file - Run an AiScript .ais file")
            print("docs          - Open HTML documentation")
            print("dashboard     - Open HTML dashboard")
        print()
    if debug_mode:
        print("=== DEBUG COMMANDS ===")
        print("debug_functions  - List all available functions")
        print("debug_vars       - Show global state")
        print("debug_cmd_count  - Show command total")
        print("debug_exec       - Interactive Python console (type stop to exit)")
        print()
    print("=== ALL-USER COMMANDS ===")
    print("docs          - Open HTML documentation in browser")
    print("dashboard     - Open HTML dashboard in browser")
    print("gen_html      - Regenerate HTML files from current data")
    print("notes         - Note taking (add/list/remove/clear)")
    print("todo          - Todo list (add/list/done/remove/clear)")
    print("remind <s> <m> - Set a timer reminder")
    print("explain <cmd> - Detailed help for a specific command")
    print("hbpe_start    - Start HubBasePE (turtle graphics)")
    print("hbpe_program1-20 - Run HBPE programs 1-20")
    print("hbpe_programp1-5 - Run HBPE programs P1-P5")
    print("hbpe_dev_console - HBPE developer console")
    print("hb_util/hbu   - HubBase Utility showcase")
    print("pylevel/lvl   - PyLevel interactive learning module")
    print("aiscript_run  - Run AiScript code inline")
    print("aiscript_file - Run an AiScript .ais file")
    print("quiz          - Interactive data quiz")
    print("chart         - ASCII bar chart generator")
    print("flashcard     - Flashcard learner")
    print("ask/ai/query  - Natural-language data query")
    print("timer         - Countdown timer")
    print("stopwatch     - Stopwatch with laps")
    print("calc          - Calculator REPL")
    print("categories    - Categorized command listing")
    print("save/export   - Export data table to file")
    print("345           - Launch HubBasePE Code system")
    print()
    print("h  - Show this help")
    print("q  - Quit")
    print()

def check_role(pw):

    if pw == "A-52-80-A":
        return "Admin"
    if pw == "M-5280-M":
        return "Mod"
    if pw == "5280":
        return "Vip"
    return None

debug_mode = False

def toggle_debug():
    global debug_mode
    debug_mode = not debug_mode
    return "Debug mode is now {}.".format("ON" if debug_mode else "OFF")

def get_role_commands(role):
    if role == "Admin":
        return ["system_info", "list_users", "clear_logs", "toggle_debug", "reload_config",
                "hbpe_start", "hbpe_advance", "hbpe_restart", "hbpe_stop",
                "hbpe_program1", "hbpe_program2", "hbpe_program3", "hbpe_compat",
                "aiscript_run", "aiscript_file"]
    if role == "Mod":
        return ["mute_user", "warn_user", "featured_joke", "pin_message",
                "hbpe_start", "hbpe_advance", "hbpe_stop", "hbpe_program1", "hbpe_compat",
                "aiscript_run", "aiscript_file"]
    if role == "Vip":
        return ["vip_joke", "vip_quote", "vip_fact", "skip_ad",
                "hbpe_start", "hbpe_program1", "hbpe_compat",
                "aiscript_run", "aiscript_file"]
    return []

def role_badge(role):
    badges = {"Admin": C_RED + "[ADMIN]" + C_RESET, "Mod": C_BLUE + "[MOD]" + C_RESET, "Vip": C_GREEN + "[VIP]" + C_RESET}
    badge = badges.get(role, "")
    if debug_mode and badge:
        badge += C_YELLOW + "[DEBUG]" + C_RESET
    return badge

def admin_system_info():
    import platform
    return "System: {}\nNode: {}\nPython: {}\nPlatform: {}".format(
        platform.system(), platform.node(), platform.python_version(), platform.platform())

def admin_list_users():
    return "Online users: you ({})".format("Admin")

def mod_featured_joke():
    return "FEATURED JOKE: Why did the Admin cross the road? To change permissions on the other side!"

def vip_extra_fact():
    return "VIP FACT: You are valued! Did you know? The first computer bug was a real moth."

def vip_extra_quote():
    return "VIP QUOTE: 'With great power comes great responsibility.' - Uncle Ben"

def random_engineering_fact():
    facts = [
        ("Brooklyn Bridge", "1883, longest suspension bridge then, 486m span"),
        ("Golden Gate Bridge", "1937, 1,280m suspension, international orange"),
        ("Channel Tunnel", "1994, 50.5km undersea tunnel, UK-France"),
        ("Panama Canal", "1914, 82km, connects Atlantic and Pacific"),
        ("Suez Canal", "1869, 193km, connects Med and Red Sea"),
        ("Hoover Dam", "1936, 221m concrete arch-gravity, 2GW power"),
        ("Three Gorges Dam", "2012, 181m, 22.5GW, largest power station"),
        ("Itaipu Dam", "1984, Brazil/Paraguay, 14GW"),
        ("Millau Viaduct", "2004, France, 343m tallest bridge pillar"),
        ("Akashi Kaikyo Bridge", "1998, Japan, 1,991m longest suspension span"),
        ("Palm Islands", "Dubai, artificial archipelago, visible from space"),
        ("Burj Al Arab", "1999, Dubai, 321m sail-shaped hotel"),
        ("International Space Station", "1998, 109m x 73m, 16 countries"),
        ("Large Hadron Collider", "2008, CERN, 27km circumference tunnel"),
        ("ITTOPF", "Floating platform for oil drilling"),
        ("Falkirk Wheel", "2002, Scotland, rotating boat lift"),
        ("Pao de Acucar cable car", "Rio, 1912, first aerial cable car in Brazil"),
        ("Eiffel Tower", "1889, 300m, 18,038 iron parts, 2.5M rivets"),
        ("Sydney Harbour Bridge", "1932, 1,149m steel arch, coat hanger"),
        ("CN Tower", "1976, Toronto, 553m communications tower"),
        ("Empire State Building", "1931, NYC, 381m, art deco, 102 floors"),
        ("Transamerica Pyramid", "1972, San Francisco, 260m, 48 floors"),
        ("Petronas Towers", "1998, KL, 452m twin towers, skybridge"),
        ("Taipei 101", "2004, Taiwan, 509m, damper tuned mass"),
        ("Shanghai Tower", "2015, 632m, twisted 120 degrees"),
        ("Burj Khalifa", "2010, Dubai, 828m, 163 floors"),
        ("Singapore Changi Airport", "Jewel waterfall, 2019, stunning architecture"),
        ("Denver International Airport", "Largest US airport, 137 km\u00b2"),
        ("King's Cross Station", "London, 1852, Harry Potter platform 9 3/4"),
        ("Guggenheim Bilbao", "1997, titanium curves, Frank Gehry"),
        ("Sydney Opera House", "1973, 1M+ roof tiles, sail shells"),
        ("Taj Mahal", "1653, marble inlay, Mughal engineering marvel"),
        ("Hagia Sophia", "537 AD, Istanbul, massive dome, cathedral/mosque"),
        ("Pantheon", "125 AD, Rome, unreinforced concrete dome, 43m span"),
        ("Roman aqueducts", "~500km total, gravity-fed water system"),
        ("Great Wall of China", "21,196km, watchtowers and fortifications"),
        ("Machu Picchu", "1450, Inca, dry stone construction, earthquake-proof"),
        ("Sukkur barrage", "1932, Pakistan, 1.4km across River Indus"),
        ("James Webb Space Telescope", "2021, 6.5m mirror, origami sunshield"),
        ("Apollo Saturn V", "1967, 110m tall, 2.8M kg thrust, 13 moon missions"),
    ]
    name, year, desc = random.choice(facts)
    return "{} ({}): {}".format(name, year, desc)

def random_medicine_fact_deep():
    facts = [
        ("Heart surgery", "First open heart 1953, bypass surgery 1960s"),
        ("Organ transplant", "First kidney 1954, heart 1967, liver 1967"),
        ("Stem cell therapy", "Bone marrow transplant 1968, first blood stem cells"),
        ("Gene therapy", "First approved 1990, ADA deficiency"),
        ("Immunotherapy", "Checkpoint inhibitors since 2011"),
        ("CAR-T cells", "Engineered immune cells attack cancer"),
        ("Antibiotics", "Penicillin 1928, golden age 1940-1960"),
        ("Vaccines", "Smallpox 1796, polio 1955, MMR 1971"),
        ("mRNA vaccines", "COVID-19 2020, revolutionary platform technology"),
        ("Insulin", "Discovered 1921, first protein sequenced"),
        ("Statins", "Cholesterol-lowering, 1987, Lipitor best-seller"),
        ("Aspirin", "1897, still widely used for pain and heart"),
        ("Anesthesia", "Ether 1846, revolutionized surgery"),
        ("X-rays", "1895 by Rontgen, first medical imaging"),
        ("CT scan", "1971, 3D X-ray, Hounsfield Nobel 1979"),
        ("MRI", "1973, Lauterbur, no radiation"),
        ("Ultrasound", "1950s, prenatal imaging"),
        ("PET scan", "1970s, metabolic imaging"),
        ("ECG", "1903, Einthoven, Nobel 1924"),
        ("Defibrillator", "1947, restores normal heart rhythm"),
        ("Pacemaker", "1958, implanted to regulate heartbeat"),
        ("Heart-lung machine", "1953, enabled open-heart surgery"),
        ("Dialysis", "1943, Kolff, kidney failure treatment"),
        ("Ventilator", "Iron lung 1928, modern ICU ventilators"),
        ("Prosthetics", "Ancient peg legs, modern bionic limbs"),
        ("Cochlear implant", "1972, restores hearing"),
        ("Retinal implant", "Argus II 2013, restores partial vision"),
        ("Vaccination schedule", "Childhood vaccines prevent 4M deaths/year"),
        ("Herd immunity", "Population protection through vaccination"),
        ("Antiseptic", "Lister 1867, carbolic acid, reduced infection"),
        ("Hygiene", "Semmelweis 1847, handwashing saves lives"),
        ("Sanitation", "Clean water prevents cholera and typhoid"),
        ("Eradication", "Smallpox eradicated 1980, polio nearly"),
        ("Tuberculosis", "1.5M deaths/year, drug-resistant strains"),
        ("Malaria", "619K deaths 2021, insecticide nets"),
        ("HIV/AIDS", "Peaked 2004, now manageable with ART"),
        ("Cancer", "Leading causes: lung, breast, colorectal"),
        ("Alzheimer's", "60-70% of dementia, no cure"),
        ("Diabetes", "537M adults, growing epidemic"),
        ("Obesity", "650M adults, BMI >30, global crisis"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_bridge_fact():
    facts = [
        ("Golden Gate Bridge", "San Francisco, 1,280m, 1937"),
        ("Brooklyn Bridge", "NYC, 486m, 1883, Gothic towers"),
        ("Tower Bridge", "London, 244m, 1894, bascule lift"),
        ("Millau Viaduct", "France, 2,460m, 2004, 343m tallest pillar"),
        ("Akashi Kaikyo", "Japan, 1,991m, 1998, longest suspension span"),
        ("Great Belt Bridge", "Denmark, 1,624m, 1998"),
        ("Runyang Bridge", "China, 1,490m, 2005"),
        ("Yi Sun-sin Bridge", "South Korea, 1,545m, 2012"),
        ("Xihoumen Bridge", "China, 1,650m, 2007"),
        ("Humber Bridge", "UK, 1,410m, 1981, longest in UK"),
        ("Verrazzano-Narrows", "NYC, 1,298m, 1964, connecting Brooklyn-Staten Isl"),
        ("Forth Bridge", "Scotland, 2,529m, 1890, cantilever rail"),
        ("Sydney Harbour Bridge", "1,149m, 1932, steel arch"),
        ("Harbor Bridge", "Bangkok, 1965"),
        ("Ponte Vecchio", "Florence, 1345, shops built on it"),
        ("Rialto Bridge", "Venice, 1591, stone arch across Grand Canal"),
        ("Charles Bridge", "Prague, 1402, 516m, 30 statues"),
        ("Stari Most", "Mostar, 1566, rebuilt 2004 after war"),
        ("Khaju Bridge", "Isfahan, 1650, bridge and dam"),
        ("Sidu River Bridge", "China, 1,222m, 496m highest deck"),
        ("Duge Bridge", "China, 565m high, 1340m span, 2016"),
        ("Baluarte Bridge", "Mexico, 1,124m, 403m high, 2012"),
        ("Royal Gorge Bridge", "USA, 384m, 291m above river, 1929"),
        ("Mackinac Bridge", "Michigan, 1,158m, 1957"),
        ("Sunshine Skyway", "Florida, 366m, 1987 cable-stayed"),
        ("Confederation Bridge", "Canada, 12.9km, 1997, fixed link PEI"),
        ("Oresund Bridge", "Denmark-Sweden, 7.8km, 2000, road and rail"),
        ("Tsing Ma Bridge", "Hong Kong, 1,377m, 1997, road and rail"),
        ("Lupu Bridge", "Shanghai, 550m, 2003, steel arch"),
        ("Chaotianmen Bridge", "Chongqing, 552m, 2009, longest steel arch"),
        ("Pont Alexandre III", "Paris, 107m, 1900, Beaux-Arts"),
        ("Mostar Bridge", "Bosnia, 1566, rebuilt symbol of unity"),
        ("Ponte 25 de Abril", "Lisbon, 2,277m, 1966, suspension"),
        ("Rio-Antirrio", "Greece, 2,252m, 2004, cable-stayed"),
        ("Vasco da Gama", "Lisbon, 17.2km, 1998, longest in Europe"),
        ("Padma Bridge", "Bangladesh, 6.15km, 2022"),
        ("Hong Kong-Zhuhai-Macao", "55km, 2018, longest sea crossing"),
        ("Danyang-Kunshan", "China, 164.8km, 2011, longest bridge of any kind"),
        ("Penang Bridge", "Malaysia, 13.5km, 1985"),
        ("Tengger-Skywalk", "China, glass-bottom bridge, 120m high"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_tunnel_fact():
    facts = [
        ("Channel Tunnel", "50.5km, 1994, UK-France, undersea"),
        ("Gotthard Base Tunnel", "57.1km, 2016, Swiss Alps, longest rail tunnel"),
        ("Seikan Tunnel", "53.9km, 1988, Japan, second longest, undersea"),
        ("Eurotunnel", "37.9km, undersea Channel Tunnel"),
        ("Lotschberg Base Tunnel", "34.6km, 2007, Switzerland"),
        ("New Guanjiao", "32.6km, 2014, China, highest altitude rail tunnel"),
        ("Yulhyeon Tunnel", "50.3km, 2016, South Korea"),
        ("Laerdal Tunnel", "24.5km, 2000, Norway, longest road tunnel"),
        ("Zhongnanshan", "18km, 2007, China, longest 2-lane"),
        ("Jinpingshan", "17.5km, 2012, China"),
        ("St. Gotthard Road Tunnel", "16.9km, 1980, Switzerland"),
        ("Mount Blanc Tunnel", "11.6km, 1965, France-Italy"),
        ("Fréjus Road Tunnel", "12.9km, 1980, France-Italy"),
        ("Mt. Baker Ridge", "1.3km, 1990, Seattle, largest diameter at 24m"),
        ("Eiksund Tunnel", "7.8km, 2008, Norway, -287m undersea deepest"),
        ("Ryfylke Tunnel", "14.5km, 2019, Norway, -292m deepest subsea"),
        ("Bømlafjord Tunnel", "7.9km, 2000, Norway"),
        ("Oslofjord Tunnel", "7.2km, 2000, Norway"),
        ("Hvalfjordur Tunnel", "5.8km, 1998, Iceland"),
        ("Eisenhower Tunnel", "2.7km, 1973, Colorado, 3,401m highest in US"),
        ("Holland Tunnel", "2.6km, 1927, NYC, first underwater vehicular"),
        ("Lincoln Tunnel", "2.4km, 1937, NYC"),
        ("Queens-Midtown Tunnel", "1.9km, 1940, NYC"),
        ("Brooklyn-Battery Tunnel", "2.8km, 1950, NYC, longest in US urban"),
        ("Antelope Hills", "1.7km, 1964, Arizona"),
        ("Ted Williams Tunnel", "1.2km, 1995, Boston"),
        ("Alameda Sains", "1.1km, 194o, Mexico City"),
        ("Tunnel of Eupalinos", "1km, 520 BC, Samos Greece, ancient engineering"),
        ("Appian Way", "Roman tunnels for roads, ~300 BC"),
        ("Fenghuoshan Tunnel", "1.3km, 2005, China, 4,905m highest railway"),
        ("Musha Tunnel", "20 km, 1998, Japan"),
        ("Oakland Bay Bridge", "tunnel portion, Yerba Buena Island"),
        ("Mersey Tunnel", "3.2km, 1971, Liverpool"),
        ("Dartford Crossing", "3.6km, 1963, London orbital"),
        ("Blackwall Tunnel", "2.5km, 1897, London"),
        ("Rotherhithe Tunnel", "1.5km, 1908, London"),
        ("Kanonersky Tunnel", "1.7km, 1986, St. Petersburg"),
        ("Santo Domingo Tunnel", "1.2km, Metro tunnel"),
        ("Crossrail", "21km, 2022, London Elizabeth Line"),
        ("Seoul Subway Tunnel", "deepest in Seoul metro"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_animal_speed_fact():
    facts = [
        ("Peregrine falcon", "389 km/h dive, fastest animal"),
        ("Golden eagle", "320 km/h dive"),
        ("White-throated needletail", "169 km/h horizontal flight"),
        ("Frigatebird", "153 km/h, highest speed-to-size ratio"),
        ("Spur-winged goose", "142 km/h, fastest bird in level flight"),
        ("Cheetah", "120 km/h land sprint, 0-100 in 3 sec"),
        ("Pronghorn antelope", "88 km/h, second fastest land"),
        ("Springbok", "88 km/h, leaps 4m high"),
        ("Wildebeest", "80 km/h, migration endurance"),
        ("Lion", "80 km/h, short burst hunter"),
        ("Blackbuck", "80 km/h, Indian antelope"),
        ("Brown hare", "72 km/h"),
        ("Horse", "72 km/h, thoroughbred"),
        ("Greyhound", "72 km/h, breed for racing"),
        ("Jackrabbit", "72 km/h"),
        ("Hyena", "60 km/h, pack hunter"),
        ("Zebra", "65 km/h, zigzag escape"),
        ("Grizzly bear", "56 km/h, surprisingly fast"),
        ("Elephant", "40 km/h despite 6 ton weight"),
        ("Black marlin", "129 km/h fastest fish"),
        ("Sailfish", "110 km/h, billfish family"),
        ("Swordfish", "97 km/h"),
        ("Yellowfin tuna", "76 km/h"),
        ("Porpoise", "56 km/h, fastest marine mammal"),
        ("Mako shark", "74 km/h, fastest shark"),
        ("Atlantic bluefin", "70 km/h"),
        ("Killer whale", "56 km/h, apex predator"),
        ("Dolphin", "60 km/h"),
        ("Giant tortoise", "0.3 km/h, slowest reptile"),
        ("Three-toed sloth", "0.24 km/h, slowest mammal"),
        ("Garden snail", "0.05 km/h, slowest animal"),
        ("Hummingbird", "385 body lengths/sec, fastest relative speed"),
        ("Gekko", "1m in 0.1 sec for tongue strike"),
        ("Mantis shrimp", "80 km/h punch acceleration"),
        ("Trap-jaw ant", "230 km/h jaw snap speed"),
        ("Boa constrictor", "Strikes at 2.7 m/s"),
        ("Cuttlefish", "Reacts in milliseconds, color change"),
        ("Archerfish", "Spits water at 2m/s at insects"),
        ("Chameleon", "Tongue at 5.8 m/s projectile"),
        ("Sea horse", "Slowest fish at 0.001 km/h"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_unusual_ability():
    abilities = [
        ("Echidna", "Lays eggs, but is a mammal (monotreme)"),
        ("Platypus", "Venomous spur, lays eggs, electroreception"),
        ("Tardigrade", "Survives -272C to 150C, radiation, vacuum, years without water"),
        ("Axolotl", "Regrows entire limbs, spinal cord, heart parts"),
        ("Immortal jellyfish", "Can revert to juvenile stage indefinitely"),
        ("Mimic octopus", "Imitates 15+ species including lionfish, flatfish, sea snakes"),
        ("Electric eel", "Generates 600V shocks, uses as radar"),
        ("Archerfish", "Shoots water jets up to 2m to knock insects into water"),
        ("Cheetah", "0 to 100 km/h in 3 seconds"),
        ("Chameleon", "Eyes move independently 360 degree, tongue at 5.8 m/s"),
        ("Trap-jaw ant", "Jaws snap at 230 km/h, fastest animal appendage"),
        ("Pistol shrimp", "Claw snaps at 4,400C for split second, creates cavitation"),
        ("Leaf-tailed gecko", "Perfect camouflage blending into tree bark"),
        ("Dragonfly", "Wings beat independently, hover, fly backward, 80% brain for vision"),
        ("Hummingbird", "Wings beat 80/s, only bird to fly backward"),
        ("Giraffe", "Neck 2.4m, 6 vertebrae like humans, 1.8m neck"),
        ("Giant panda", "False thumb for bamboo gripping"),
        ("Sloth", "Algae grows on fur for camouflage, metabolism extremely slow"),
        ("Ant", "Carries 50-100x body weight"),
        ("Dung beetle", "Strongest insect, pulls 1,141x body weight"),
        ("Bombardier beetle", "Sprays boiling chemicals at 100C from abdomen"),
        ("Pufferfish", "Inflates with water, deadly tetrodotoxin"),
        ("Poison dart frog", "One frog has enough toxin to kill 10 men"),
        ("Box jellyfish", "Most venomous, 24 eyes, active swimmer"),
        ("Star-nosed mole", "22 pink tentacles on nose, touches objects in 10ms"),
        ("Naked mole rat", "Feels no pain, cancer-resistant, lives 30+ years"),
        ("Planarian worm", "Splits into two, each regenerates full body"),
        ("Cicada", "17-year life cycle, spends most underground"),
        ("Spider silk", "Stronger than steel by weight, more elastic than nylon"),
        ("Baobab tree", "Stores 120K liters of water in trunk"),
        ("Venus flytrap", "Snap trap triggers in 100ms, counts touches"),
        ("Mimosa pudica", "Folds leaves instantly when touched"),
        ("Luna moth", "No mouth, lives only one week, just to mate"),
        ("Hatchetfish", "Bioluminescent underside, mimics sunlight to hide"),
        ("Eel", "Swims backwards, lives in freshwater but spawns in ocean"),
        ("Arctic tern", "Migrates 72,000 km annually, poles to poles"),
        ("Albatross", "Wingspan 3.5m, glides for hours without flapping"),
        ("Siberian tiger", "Weighs 300+ kg, survives -50C winters"),
        ("Camel", "Hump stores fat not water, goes weeks without water"),
        ("Koala", "Sleeps 20 hours/day, eats toxic eucalyptus"),
    ]
    name, ability = random.choice(abilities)
    return "{}: {}".format(name, ability)

def random_dinosaur_fact_deep():
    facts = [
        ("Tyrannosaurus Rex", "12m long, 8 tons, powerful jaws 12,000 lbs bite"),
        ("Triceratops", "9m, 12 tons, 3 horns, frill defense"),
        ("Stegosaurus", "9m, 5 tons, plates on back, tail spikes"),
        ("Brachiosaurus", "26m, 58 tons, long neck, tallest dinosaur"),
        ("Velociraptor", "2m, 15kg, feathered, intelligent pack hunter"),
        ("Spinosaurus", "18m, 20 tons, largest carnivorous, sail back"),
        ("Ankylosaurus", "9m, 6 tons, armored body, club tail"),
        ("Diplodocus", "27m, 15 tons, extremely long tail"),
        ("Parasaurolophus", "10m, 4 tons, head crest for communication"),
        ("Pterodactyl", "Wingspan 10m, not a dinosaur but pterosaur"),
        ("Mosasaurus", "18m, marine reptile, apex ocean predator"),
        ("Plesiosaurus", "15m, long neck, four flippers"),
        ("Allosaurus", "12m, 2.5 tons, dominant predator of late Jurassic"),
        ("Apatosaurus", "22m, 25 tons, former Brontosaurus"),
        ("Iguanodon", "10m, 5 tons, thumb spike defense"),
        ("Carnotaurus", "8m, 1.5 tons, two horns above eyes"),
        ("Giganotosaurus", "13m, 8 tons, larger than T-Rex"),
        ("Carcharodontosaurus", "12m, 7 tons, shark-toothed lizard"),
        ("Deinonychus", "3.4m, 80kg, sickle claw, raptor inspiration"),
        ("Gallimimus", "6m, 400kg, ostrich-like, fastest dinosaur"),
        ("Oviraptor", "2m, 35kg, beaked, brooded eggs"),
        ("Protoceratops", "2m, 200kg, early horned dinosaur"),
        ("Pachycephalosaurus", "4.5m, 500kg, dome-headed"),
        ("Therizinosaurus", "10m, 5 tons, 1m claws on arms"),
        ("Compsognathus", "1m, 3kg, one of smallest dinosaurs"),
        ("Microraptor", "0.8m, 1kg, four wings, gliding ability"),
        ("Dilophosaurus", "6m, 500kg, two head crests, spitter in movies"),
        ("Baryonyx", "9m, 2 tons, fish-eater, crocodile-like jaws"),
        ("Megalosaurus", "9m, 1.5 tons, first dinosaur named (1824)"),
        ("Coelophysis", "3m, 30kg, early dinosaur, Triassic"),
        ("Titanosaurus", "15-30m, 15-70 tons, massive sauropod"),
        ("Argentinosaurus", "35m, 90 tons, one of largest ever"),
        ("Mamenchisaurus", "26m, neck 11m, longest neck of any dinosaur"),
        ("Euoplocephalus", "5m, 2.5 tons, armored with tail club"),
        ("Corythosaurus", "9m, 4 tons, helmet-like head crest"),
        ("Velociraptor", "featured in Jurassic Park but much larger than real"),
        ("Troodon", "2.5m, 50kg, highest brain-to-body ratio"),
        ("K-T extinction", "66M years ago, asteroid caused mass extinction"),
        ("Dinosaur era", "Mesozoic Era: Triassic, Jurassic, Cretaceous"),
        ("Birds as dinosaurs", "Modern birds evolved from theropod dinosaurs"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_space_misson_deep():
    missions = [
        ("Apollo 8", "1968, first humans to orbit the Moon, iconic Earthrise photo"),
        ("Apollo 11", "1969, first Moon landing, Armstrong and Aldrin"),
        ("Apollo 13", "1970, 'Houston we have a problem', successful failure"),
        ("Apollo 17", "1972, last Moon landing, first geologist on Moon"),
        ("Skylab", "1973-1979, first US space station"),
        ("Space Shuttle", "1981-2011, reusable orbiter, 135 missions"),
        ("Challenger", "1986, disaster 73 sec after launch, 7 crew lost"),
        ("Columbia", "2003, disaster on re-entry, 7 crew lost"),
        ("Hubble repair", "1993-2009, 5 servicing missions, saved Hubble"),
        ("Mir space station", "1986-2001, Soviet/Russian, 15 years"),
        ("International Space Station", "1998-present, 16 countries, continuous habitation"),
        ("Mars Pathfinder", "1997, first Mars rover Sojourner"),
        ("Mars Exploration Rovers", "2004, Spirit and Opportunity, 15+ year mission"),
        ("Mars Science Laboratory", "2012, Curiosity rover, 1.5 billion cost"),
        ("Mars 2020", "2021, Perseverance rover and Ingenuity helicopter"),
        ("Viking 1 and 2", "1976, first US Mars landers"),
        ("Mars Reconnaissance Orbiter", "2006, high-resolution Mars imaging"),
        ("MAVEN", "2014, Mars atmosphere study"),
        ("Mars Express", "2003, European orbiter, found water ice"),
        ("ExoMars", "2016, ESA/Roscosmos, trace gas orbiter"),
        ("Venus Express", "2005, ESA, studied Venus atmosphere for 8 years"),
        ("Magellan", "1989, mapped Venus surface with radar"),
        ("MESSENGER", "2011, first Mercury orbiter, mapped whole surface"),
        ("BepiColombo", "2018, ESA/JAXA, en route to Mercury"),
        ("Cassini-Huygens", "1997-2017, Saturn system explorer"),
        ("Huygens probe", "2005, landed on Titan, Saturn's moon"),
        ("Galileo", "1989-2003, Jupiter orbiter, first asteroid flyby"),
        ("Juno", "2016-present, Jupiter polar orbiter"),
        ("JUICE", "2023, JUpiter ICy moons Explorer, ESA"),
        ("Europa Clipper", "2024, NASA, studying Europa ocean"),
        ("New Horizons", "2006-2015, Pluto flyby, now in Kuiper Belt"),
        ("Dawn", "2007-2018, Vesta and Ceres orbiter"),
        ("Rosetta", "2004-2016, comet 67P rendezvous and lander"),
        ("Philae lander", "2014, first comet landing, 60h battery"),
        ("Hayabusa", "2005, Japan, first asteroid sample return"),
        ("Hayabusa2", "2014-2020, Ryugu asteroid sample return"),
        ("OSIRIS-REx", "2016-2023, Bennu asteroid sample return"),
        ("Stardust", "1999-2006, comet Wild 2 sample return"),
        ("Genesis", "2001-2004, solar wind sample return"),
        ("WISE/NEOWISE", "2009, infrared sky survey, asteroid and comet discovery"),
        ("Kepler", "2009-2018, exoplanet discovery, 2,600+ confirmed"),
        ("TESS", "2018-present, exoplanet surveyor"),
        ("James Webb Space Telescope", "2021, infrared, successor to Hubble"),
        ("Chandra", "1999, X-ray observatory"),
        ("Spitzer", "2003-2020, infrared telescope"),
        ("Fermi", "2008, gamma-ray observatory"),
        ("Parker Solar Probe", "2018, touching the Sun at 692K km/h"),
        ("Solar Orbiter", "2020, ESA, studying Sun's poles"),
        ("STEREO", "2006, 3D views of Sun"),
        ("SOHO", "1995, solar observatory, discovered 3,000+ comets"),
        ("Voyager Golden Record", "Messages to space on Voyager 1 and 2"),
    ]
    name, year, desc = random.choice(missions)
    return "{} ({}): {}".format(name, year, desc)

def random_natural_disaster():
    disasters = [
        ("1900 Galveston hurricane", "8,000-12,000 dead, Category 4, US deadliest"),
        ("1970 Bhola cyclone", "300,000-500,000 dead, Bangladesh, deadliest tropical cyclone"),
        ("2004 Indian Ocean tsunami", "227,898 dead, 14 countries, 9.1 earthquake"),
        ("2010 Haiti earthquake", "160,000 dead, 7.0 Mw, Port-au-Prince"),
        ("2005 Kashmir earthquake", "87,000 dead, 7.6 Mw, Pakistan/India"),
        ("2011 Tohoku earthquake/tsunami", "19,759 dead, 9.0 Mw, Fukushima nuclear"),
        ("2008 Sichuan earthquake", "87,587 dead, 7.9 Mw, China"),
        ("1906 San Francisco earthquake", "3,000+ dead, 7.9 Mw, fire destroyed city"),
        ("1985 Mexico City earthquake", "10,000+ dead, 8.0 Mw"),
        ("1999 Izmit earthquake", "17,000+ dead, 7.6 Mw, Turkey"),
        ("1923 Great Kanto earthquake", "142,800 dead, 7.9 Mw, Tokyo/Yokohama"),
        ("2010 Eyjafjallajokull eruption", "Air travel halted 7 days, 20 countries closed"),
        ("1883 Krakatoa eruption", "36,417 dead, loudest sound in history"),
        ("1815 Mount Tambora eruption", "92,000 dead, Year Without Summer"),
        ("1980 Mount St. Helens", "57 dead, largest US volcanic eruption"),
        ("1986 Lake Nyos disaster", "1,746 dead, CO2 release from volcanic lake"),
        ("1931 China floods", "1-4 million dead, Yangtze River floods"),
        ("1887 Yellow River flood", "900,000-2M dead, worst flood in history"),
        ("1998 Yangtze floods", "3,704 dead, 223M affected"),
        ("2010 Pakistan floods", "2,000 dead, 20M affected, $43B damage"),
        ("1928 Okeechobee hurricane", "4,000+ dead, Florida, Category 5"),
        ("2005 Hurricane Katrina", "1,833 dead, $125B damage, New Orleans"),
        ("2013 Typhoon Haiyan", "6,300 dead, Philippines, 315 km/h winds"),
        ("2017 Hurricane Harvey", "107 dead, $125B, Houston catastrophic flooding"),
        ("2017 Hurricane Maria", "3,057 dead, Puerto Rico devastated"),
        ("1908 Tunguska event", "2,000 km\u00b2 forest flattened, airburst 3-10 MT"),
        ("2013 Chelyabinsk meteor", "1,500 injured, airburst 20km, 500 KT"),
        ("2018 Camp Fire", "85 dead, Butte County California, most destructive CA fire"),
        ("2019-2020 Australian bushfires", "34 dead, 18M ha, 1B animals killed"),
        ("2023 Maui wildfires", "100+ dead, Lahaina destroyed"),
        ("1930s Dust Bowl", "Severe drought/dust storms, US Great Plains"),
        ("2003 European heat wave", "70,000+ dead, worst in 500 years"),
        ("2010 Russian heat wave", "56,000 dead, wildfires"),
        ("2021 Pacific Northwest heat wave", "1,000+ dead, Lytton 49.6C Canada"),
        ("1918 Spanish flu", "50M dead, pandemic, 1/3 of world infected"),
        ("COVID-19 pandemic", "7M+ reported deaths, 2019-2023 global pandemic"),
        ("1347-1351 Black Death", "75-200M dead, 30-60% of Europe"),
        ("1984 Bhopal gas leak", "3,000-15,000 dead, worst industrial disaster"),
        ("2011 Deepwater Horizon", "11 dead, 4.9M barrels in Gulf of Mexico"),
        ("1986 Chernobyl", "~4,000 eventual deaths, nuclear disaster"),
        ("2011 Fukushima Daiichi", "Nuclear meltdown after tsunami"),
        ("1979 Three Mile Island", "Partial nuclear meltdown, no direct deaths"),
    ]
    name, detail = random.choice(disasters)
    return "{}: {}".format(name, detail)

def random_climate_fact():
    facts = [
        ("Global temperature rise", "1.2C above pre-industrial levels (2024)"),
        ("CO2 levels", "420+ ppm, highest in 4M years"),
        ("Sea level rise", "~3.7 mm/year, 20cm rise since 1901"),
        ("Arctic sea ice decline", "~13% per decade since 1979"),
        ("Greenland ice melt", "279 billion tons/year lost"),
        ("Antarctic ice melt", "148 billion tons/year lost"),
        ("Glacier retreat", "Almost all glaciers globally shrinking"),
        ("Ocean acidification", "~30% increase in acidity since industrial era"),
        ("Temperature record years", "2023 hottest year, 2016 second hottest"),
        ("Extreme weather increase", "Frequency and intensity rising globally"),
        ("Drought severity", "Increasing in Mediterranean, Africa, western US"),
        ("Wildfire season", "Lengthened, more severe globally"),
        ("Hurricane intensity", "Category 4-5 storms increasing"),
        ("Heavy rainfall", "More intense, increased flooding"),
        ("Heatwaves", "More frequent, longer, hotter"),
        ("Permafrost thaw", "Releasing methane, accelerating warming"),
        ("Methane emissions", "28x stronger greenhouse gas than CO2"),
        ("Nitrous oxide", "300x stronger than CO2, agriculture source"),
        ("Carbon budget", "Remaining ~500 GT CO2 for 1.5C target"),
        ("Paris Agreement", "2015, goal limit warming to 1.5-2C"),
        ("COP meetings", "Annual UN climate conferences since 1995"),
        ("Net zero targets", "Many countries target 2050 net zero emissions"),
        ("Renewable energy growth", "Solar and wind cheapest in many regions"),
        ("Electric vehicle adoption", "~18% of new car sales globally in 2023"),
        ("Deforestation", "10M ha/year lost, major carbon source"),
        ("Reforestation", "Nature-based carbon removal solution"),
        ("Carbon capture", "Direct air capture and CCS technologies"),
        ("Climate feedback loops", "Melting ice reduces albedo, amplifies warming"),
        ("Methane clathrate", "Frozen methane under ocean, risk of release"),
        ("Atlantic Meridional Overturning Circulation", "AMOC slowdown risk"),
        ("Gulf Stream stability", "At weakest in 1,000 years"),
        ("Tipping points", "Irreversible changes after certain thresholds"),
        ("Amazon dieback", "Risk of rainforest becoming savanna"),
        ("Coral reef loss", "90% of reefs may die at 1.5C warming"),
        ("Biodiversity loss", "1M species at risk of extinction"),
        ("Climate refugees", "Estimated 200M+ by 2050"),
        ("Climate adaptation", "Infrastructure, agriculture, coastal protection"),
        ("Green technology", "Falling costs making sustainable choices cheaper"),
        ("Youth climate movement", "Global activism led by young people"),
        ("IPCC reports", "UN scientific authority on climate change"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_chemical_element():
    elements = [
        ("Hydrogen", "H, 1, most abundant, 90% of atoms in universe"),
        ("Helium", "He, 2, inert gas, second most abundant"),
        ("Lithium", "Li, 3, lightest metal, batteries"),
        ("Beryllium", "Be, 4, light, strong, X-ray windows"),
        ("Boron", "B, 5, semiconductors, borosilicate glass"),
        ("Carbon", "C, 6, basis of all known life"),
        ("Nitrogen", "N, 7, 78% of air, essential for proteins"),
        ("Oxygen", "O, 8, 21% of air, essential for respiration"),
        ("Fluorine", "F, 9, most reactive element"),
        ("Neon", "Ne, 10, noble gas, red signs"),
        ("Sodium", "Na, 11, reactive metal, table salt NaCl"),
        ("Magnesium", "Mg, 12, lightweight, chlorophyll central atom"),
        ("Aluminum", "Al, 13, most abundant metal in crust"),
        ("Silicon", "Si, 14, semiconductor, computer chips"),
        ("Phosphorus", "P, 15, DNA backbone, ATP energy"),
        ("Sulfur", "S, 16, vulcanization, sulfuric acid production"),
        ("Chlorine", "Cl, 17, disinfectant, bleach"),
        ("Argon", "Ar, 18, inert gas, neon signs"),
        ("Potassium", "K, 19, essential for nerve function"),
        ("Calcium", "Ca, 20, bones, teeth, muscle function"),
        ("Scandium", "Sc, 21, aerospace alloys"),
        ("Titanium", "Ti, 22, strong, lightweight, biocompatible"),
        ("Vanadium", "V, 23, steel alloys"),
        ("Chromium", "Cr, 24, stainless steel, chrome plating"),
        ("Manganese", "Mn, 25, steel production"),
        ("Iron", "Fe, 26, most important industrial metal"),
        ("Cobalt", "Co, 27, battery cathodes, blue pigment"),
        ("Nickel", "Ni, 28, stainless steel, coinage"),
        ("Copper", "Cu, 29, electrical wiring, excellent conductor"),
        ("Zinc", "Zn, 30, galvanizing, battery anodes"),
        ("Gallium", "Ga, 31, melts in hand, semiconductors"),
        ("Germanium", "Ge, 32, semiconductor, fiber optics"),
        ("Arsenic", "As, 33, poison, semiconductor doping"),
        ("Selenium", "Se, 34, photocells, dandruff shampoo"),
        ("Bromine", "Br, 35, liquid nonmetal, flame retardants"),
        ("Krypton", "Kr, 36, noble gas, high-efficiency bulbs"),
        ("Rubidium", "Rb, 37, highly reactive, atomic clocks"),
        ("Strontium", "Sr, 38, red fireworks, bone-seeking"),
        ("Yttrium", "Y, 39, LED phosphors, superconductors"),
        ("Zirconium", "Zr, 40, nuclear fuel cladding"),
        ("Niobium", "Nb, 41, steel alloys, superconducting"),
        ("Molybdenum", "Mo, 42, steel alloys, enzyme cofactor"),
        ("Technetium", "Tc, 43, first man-made element"),
        ("Ruthenium", "Ru, 44, catalyst, hard alloys"),
        ("Rhodium", "Rh, 45, catalytic converters, expensive"),
        ("Palladium", "Pd, 46, catalytic converters, hydrogen storage"),
        ("Silver", "Ag, 47, best conductor, antimicrobial"),
        ("Cadmium", "Cd, 48, batteries, toxic"),
        ("Indium", "In, 49, touch screens, solar cells"),
        ("Tin", "Sn, 50, cans, solder"),
        ("Antimony", "Sb, 51, flame retardants"),
        ("Tellurium", "Te, 52, solar panels, thermoelectric"),
        ("Iodine", "I, 53, disinfectant, thyroid hormone"),
        ("Xenon", "Xe, 54, noble gas, high-intensity lamps"),
        ("Cesium", "Cs, 55, atomic clocks, most electropositive"),
        ("Barium", "Ba, 56, medical X-rays contrast"),
        ("Lanthanum", "La, 57, first lanthanide"),
        ("Cerium", "Ce, 58, catalytic converters, lighter flints"),
        ("Praseodymium", "Pr, 59, magnets, yellow pigment"),
        ("Neodymium", "Nd, 60, strongest permanent magnets"),
        ("Promethium", "Pm, 61, radioactive, glow paint"),
        ("Samarium", "Sm, 62, magnets, nuclear control rods"),
    ]
    name, detail = random.choice(elements)
    return "{}: {}".format(name, detail)

def random_programming_term():
    terms = [
        ("API", "Application Programming Interface - how components talk"),
        ("REST", "Representational State Transfer - web API architecture"),
        ("JSON", "JavaScript Object Notation - lightweight data format"),
        ("XML", "Extensible Markup Language - data format"),
        ("HTTP", "Hypertext Transfer Protocol - web communication"),
        ("HTTPS", "Secure HTTP with encryption (TLS/SSL)"),
        ("DNS", "Domain Name System - translates names to IPs"),
        ("TCP", "Transmission Control Protocol - reliable connection"),
        ("UDP", "User Datagram Protocol - fast, no guarantee"),
        ("IP", "Internet Protocol - addressing and routing"),
        ("SQL", "Structured Query Language - database queries"),
        ("NoSQL", "Non-tabular databases: MongoDB, DynamoDB"),
        ("ORM", "Object-Relational Mapping - bridges code and DB"),
        ("IDE", "Integrated Development Environment"),
        ("Git", "Distributed version control system"),
        ("CI/CD", "Continuous Integration/Continuous Deployment"),
        ("Docker", "Containerization platform"),
        ("Kubernetes", "Container orchestration system"),
        ("Microservices", "Architecture of small independent services"),
        ("Monolith", "Single application that handles all concerns"),
        ("Serverless", "Cloud functions without managing servers"),
        ("Edge computing", "Processing data near the source"),
        ("Cloud computing", "On-demand computing resources over internet"),
        ("SaaS", "Software as a Service - managed software"),
        ("PaaS", "Platform as a Service - managed deployment"),
        ("IaaS", "Infrastructure as a Service - virtual resources"),
        ("OOP", "Object-Oriented Programming paradigm"),
        ("FP", "Functional Programming paradigm"),
        ("AOP", "Aspect-Oriented Programming paradigm"),
        ("MVC", "Model-View-Controller pattern"),
        ("SOLID", "5 principles of object-oriented design"),
        ("DRY", "Don't Repeat Yourself - code reuse principle"),
        ("KISS", "Keep It Simple, Stupid - simplicity principle"),
        ("YAGNI", "You Aren't Gonna Need It - avoid overengineering"),
        ("Design patterns", "Singleton, Factory, Observer, Strategy, etc."),
        ("Algorithmic complexity", "Big O notation"),
        ("Time complexity", "How runtime scales with input size"),
        ("Space complexity", "How memory scales with input size"),
        ("Recursion", "Function calling itself"),
        ("Iteration", "Repeating with loops"),
        ("Memoization", "Caching function results for performance"),
        ("Lazy evaluation", "Compute only when needed"),
        ("Garbage collection", "Automatic memory management"),
        ("Multithreading", "Multiple threads in same process"),
        ("Concurrency", "Multiple tasks making progress simultaneously"),
        ("Parallelism", "Multiple tasks running at exact same time"),
        ("Synchronization", "Coordinating access to shared resources"),
        ("Deadlock", "Threads waiting for each other forever"),
        ("Race condition", "Unpredictable behavior from timing issues"),
    ]
    name, detail = random.choice(terms)
    return "{}: {}".format(name, detail)

def random_festival():
    festivals = [
        ("Diwali", "India, festival of lights, 5 days, lamps and fireworks"),
        ("Holi", "India, festival of colors, spring celebration"),
        ("Christmas", "Worldwide, December 25, gift-giving tradition"),
        ("Hanukkah", "Jewish, 8-day festival of lights"),
        ("Eid al-Fitr", "Islamic, breaking of Ramadan fast"),
        ("Chinese New Year", "China, 15 days, red envelopes and fireworks"),
        ("Songkran", "Thailand, water festival, Thai New Year"),
        ("Oktoberfest", "Germany, beer festival, 16 days"),
        ("Carnival", "Brazil, samba parades, before Lent"),
        ("Mardi Gras", "New Orleans, Fat Tuesday celebrations"),
        ("Day of the Dead", "Mexico, honoring ancestors, Nov 1-2"),
        ("La Tomatina", "Spain, tomato fight festival, August"),
        ("Running of the Bulls", "Spain, Pamplona, San Fermin"),
        ("Glastonbury", "UK, music festival, 5 days"),
        ("Coachella", "USA, music and arts festival, California"),
        ("Burning Man", "USA, Nevada, temporary community, art"),
        ("Edinburgh Fringe", "UK, largest arts festival, August"),
        ("Venice Carnival", "Italy, masks and costumes"),
        ("Rio Carnival", "Brazil, samba schools competition"),
        ("Notting Hill Carnival", "UK, London, Caribbean street festival"),
        ("Mardi Gras", "US, New Orleans, parades and beads"),
        ("Vivid Sydney", "Australia, light and music festival"),
        ("Cherry Blossom Festival", "Japan, hanami, April"),
        ("Gion Matsuri", "Japan, Kyoto, July, floats and parades"),
        ("Obon", "Japan, honoring ancestors, August"),
        ("Loy Krathong", "Thailand, floating lantern festival"),
        ("Yi Peng", "Thailand, lantern release festival"),
        ("That Luang Festival", "Laos, Buddhist temple festival"),
        ("Vesak", "Buddhist, Buddha birth/enlightenment/death"),
        ("Kumbh Mela", "India, world's largest religious gathering"),
        ("Durga Puja", "India, honoring goddess Durga, 10 days"),
        ("Ganesh Chaturthi", "India, elephant-headed god festival"),
        ("Paryushana", "Jain, 8-day fasting and reflection"),
        ("Okunchi", "Japan, Nagasaki, Chinese-influenced festival"),
        ("Seijin no Hi", "Japan, coming of age day"),
        ("Shichi-Go-San", "Japan, children celebration at 3-5-7"),
        ("Christmas markets", "Germany, mulled wine and crafts"),
        ("New Year's Eve", "Worldwide, fireworks and countdown"),
        ("Thanksgiving", "USA, family feast, November"),
        ("Halloween", "Worldwide, costumes, October 31"),
    ]
    name, loc, detail = random.choice(festivals)
    return "{} ({}): {}".format(name, loc, detail)

def random_renewable_fact():
    facts = [
        ("Solar power", "Cheapest electricity in history, $0.03/kWh"),
        ("Wind power", "Ongshore $0.03-0.05/kWh, offshore $0.05-0.08"),
        ("Hydropower", "16% of world electricity, 4,000 TWh/year"),
        ("Geothermal", "14 GW installed, Iceland gets 25% from geothermal"),
        ("Biomass", "Wood, crops, waste for heat and power"),
        ("Tidal power", "La Rance France 240MW, Sihwa South Korea 254MW"),
        ("Wave power", "Pelamis, Wave Hub, emerging technology"),
        ("Solar PV growth", "1 TW installed globally by 2022"),
        ("Solar thermal", "Concentrated solar power for heat storage"),
        ("Wind capacity", "900+ GW globally, China largest at 300 GW"),
        ("Offshore wind", "60 GW globally, UK and China leaders"),
        ("Hydrogen", "Green hydrogen from renewable electrolysis"),
        ("Battery storage", "Lithium-ion grid storage growing exponentially"),
        ("Pumped hydro", "95% of global energy storage capacity"),
        ("Smart grid", "Digital grid management for renewables"),
        ("Net metering", "Credits for solar sent to grid"),
        ("Community solar", "Shared solar installations for subscribers"),
        ("Microgrid", "Local independent grid with renewables"),
        ("Renewable target", "Many countries target 100% clean electricity"),
        ("100% renewable", "Costa Rica, Iceland, Norway near 100%"),
        ("Solar jobs", "4M+ jobs globally in solar industry"),
        ("Wind jobs", "1.4M jobs globally in wind industry"),
        ("Renewable investment", "$500B+ per year globally"),
        ("Levelized cost", "Solar and wind cheapest new electricity"),
        ("Grid parity", "Renewables cheaper than fossil fuels"),
        ("Peak sun hours", "Most useful solar resource measure"),
        ("Capacity factor", "Solar 15-25%, wind 30-50%, hydro 40-60%"),
        ("Intermittency", "Challenge: sun doesn't always shine"),
        ("Baseload", "Traditional coal/gas, renewables need storage"),
        ("Demand response", "Shifting electricity use to match supply"),
        ("Grid-scale batteries", "Tesla Megapack, Hornsdale 150MW"),
        ("Green certificates", "RECs, GOs for renewable attribution"),
        ("PPA", "Power Purchase Agreement for renewable energy"),
        ("Corporate renewable", "Google, Apple, Amazon 100% renewable"),
        ("RE100", "Corporate initiative for 100% renewable"),
        ("Renewable heat", "Solar thermal, heat pumps, biomass"),
        ("Renewable transport", "Electric vehicles, biofuels"),
        ("Green buildings", "LEED, Passive House, net zero energy"),
        ("Sustainable aviation", "Biofuels and hydrogen for airplanes"),
        ("COP28 target", "Triple renewable energy by 2030 agreed"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def pager(text, lines=20):
    chunks = text.split("\n")
    for i in range(0, len(chunks), lines):
        for line in chunks[i:i+lines]:
            print(line)
        if i + lines < len(chunks):
            input(C_DIM + "--- more (Enter) ---" + C_RESET)

def data_quiz():
    c = random.choice(["element", "city", "country", "animal", "planet", "language", "invention"])
    if c == "element":
        from functools import reduce
        data = get_chemistry_element_data()
        if not data: return "No element data."
        item = random.choice(data)
        name, sym, num, mass, cat = item[0], item[1], item[2], item[3], item[4]
        print("Element: {} (atomic number {})".format(name, num))
        a = input("Symbol? ").strip().capitalize()
        if a == sym.capitalize():
            print(C_GREEN + "Correct! " + name + " is " + sym + C_RESET)
        else:
            print(C_RED + "Wrong. The symbol for " + name + " is " + sym + C_RESET)
    elif c == "city":
        data = get_city_data()
        item = random.choice(data)
        print("City: {} (pop {})".format(item[0], item[2]))
        a = input("Region? ").strip().lower()
        if a in item[1].lower():
            print(C_GREEN + "Correct!" + C_RESET)
        else:
            print(C_RED + "Region: " + item[1] + C_RESET)
    elif c == "planet":
        data = get_planet_data()
        item = random.choice(data)
        print("Planet: {}".format(item[0]))
        a = input("Type? ").strip().lower()
        if a in item[2].lower():
            print(C_GREEN + "Correct!" + C_RESET)
        else:
            print(C_RED + "Type: " + item[2] + C_RESET)
    elif c == "animal":
        data = get_animal_extended_data()
        item = random.choice(data)
        print("Animal: {}".format(item[0]))
        a = input("Class? ").strip().lower()
        if a in item[2].lower():
            print(C_GREEN + "Correct!" + C_RESET)
        else:
            print(C_RED + "Class: " + item[2] + C_RESET)
    elif c == "language":
        data = get_language_data()
        item = random.choice(data)
        print("Code: {}".format(item[0]))
        a = input("Language name? ").strip().lower()
        if a in item[1].lower():
            print(C_GREEN + "Correct!" + C_RESET)
        else:
            print(C_RED + "Language: " + item[1] + C_RESET)
    elif c == "invention":
        data = get_invention_data()
        item = random.choice(data)
        print("Year: {}".format(item[2]))
        a = input("Invention? ").strip().lower()
        if a in item[0].lower() or a in item[1].lower():
            print(C_GREEN + "Correct!" + C_RESET)
        else:
            print(C_RED + "Invention: " + item[0] + " by " + item[1] + C_RESET)
    else:
        data = get_country_detail_data()
        item = random.choice(data)
        print("Country: {}".format(item[0]))
        a = input("Capital? ").strip().lower()
        if a in item[1].lower():
            print(C_GREEN + "Correct!" + C_RESET)
        else:
            print(C_RED + "Capital: " + item[1] + C_RESET)
    return ""

def ascii_chart(values, labels=None, width=40, title=""):
    if not values: return "No data."
    mx = max(values)
    if mx == 0: mx = 1
    res = C_BOLD + title + "\n" + C_RESET if title else ""
    for i, v in enumerate(values):
        bar_len = max(1, int(v / mx * width))
        bar = "#" * bar_len
        label = (labels[i] + " ").ljust(12) if labels and i < len(labels) else ""
        res += "{}{}| {} ({})\n".format(label, bar, str(v), C_DIM + str(round(v/mx*100,1)) + "%" + C_RESET)
    return res

def cmd_suggest(partial):
    names = []
    for i in range(1, 2676):
        names.append(str(i))
    names += ["h", "q", "system_info", "list_users", "toggle_debug", "featured_joke", "vip_fact", "vip_quote",
              "hbpe_start", "hbpe_advance", "hbpe_restart", "hbpe_stop", "hbpe_program1", "hbpe_program2",
               "hbpe_program3", "hbpe_dev_console", "hbpe_compat", "aiscript_run", "aiscript_file", "debug_functions", "debug_vars", "debug_cmd_count", "debug_exec",
              "quiz", "chart", "suggest", "cls", "clear", "pager_test", "version", "ask", "ai", "query",
              "flashcard", "learn", "help2", "categories", "save", "export", "color_test", "badge", "colorbadge",
              "data_quiz", "barchart", "find", "ver", "colors",               "timer", "countdown", "stopwatch", "calc", "calculator",
              "docs", "html_docs", "dashboard", "html_dash",
              "hbpe_program4", "hbpe_prog4", "hbpe_program5", "hbpe_prog5",
              "hbpe_program6", "hbpe_prog6", "hbpe_program7", "hbpe_prog7",
              "hbpe_program8", "hbpe_prog8", "hbpe_program9", "hbpe_prog9",
              "hbpe_program10", "hbpe_prog10", "hbpe_program11", "hbpe_prog11",
              "hbpe_program12", "hbpe_prog12", "hbpe_program13", "hbpe_prog13",
              "hbpe_program14", "hbpe_prog14", "hbpe_program15", "hbpe_prog15",
              "hbpe_program16", "hbpe_prog16", "hbpe_program17", "hbpe_prog17",
              "hbpe_program18", "hbpe_prog18", "hbpe_program19", "hbpe_prog19",
              "hbpe_programp1", "hbpe_progp1", "hbpe_programp2", "hbpe_progp2",
              "hbpe_programp3", "hbpe_progp3", "hbpe_programp4", "hbpe_progp4",
               "hbpe_programp5", "hbpe_progp5",
               "hbpe_program20", "hbpe_prog20",
               "gen_html", "regenerate", "html_docs", "html_dash",
              "notes", "todo", "remind", "help_", "explain", "whatis"]
    matches = [n for n in names if partial.lower() in n]
    if not matches: return "No matches for '" + partial + "'."
    return "Matches: " + ", ".join(matches[:30])

def cmd_timer():
    secs = input("Countdown seconds: ").strip()
    if not secs.isdigit(): return "Enter a number."
    secs = int(secs)
    import time as _tm
    for i in range(secs, 0, -1):
        mins, sec = divmod(i, 60)
        print("\r" + C_BOLD + C_YELLOW + "{:02d}:{:02d}".format(mins, sec) + C_RESET, end="")
        _tm.sleep(1)
    print("\r" + C_BOLD + C_RED + "00:00 - TIME'S UP!" + C_RESET)
    return ""

def cmd_stopwatch():
    import time as _tm
    print(C_BOLD + "Stopwatch started. Press Enter to lap, type 'stop' to end." + C_RESET)
    laps = []
    start = _tm.time()
    last = start
    while True:
        inp = input().strip().lower()
        now = _tm.time()
        if inp == "stop":
            elapsed = now - start
            laps.append(("Stop", elapsed))
            break
        lap_time = now - last
        total = now - start
        laps.append((inp or "Lap {}".format(len(laps)+1), total))
        last = now
        print("  {:.2f}s total, {:.2f}s lap".format(total, lap_time))
    print(C_CYAN + "--- STOPWATCH RESULTS ---" + C_RESET)
    for label, t in laps:
        print("  {}: {:.2f}s".format(label, t))
    return "Total: {:.2f}s".format(elapsed) if laps else ""

def cmd_calc():
    print(C_BOLD + "Calculator REPL (type 'h' for history, 'c' to clear, 'q' to quit)" + C_RESET)
    history = []
    while True:
        expr = input("calc> ").strip()
        if expr.lower() in ("q", "quit", "exit"): break
        if expr.lower() == "h":
            for h in history[-10:]: print("  " + h)
            continue
        if expr.lower() == "c": history.clear(); print("Cleared"); continue
        try:
            result = eval(expr, {"__builtins__":{}}, {"abs":abs,"min":min,"max":max,"pow":pow,"round":round,"int":int,"float":float,"str":str,"len":len,"sum":sum})
            line = "{} = {}".format(expr, result)
            print(line)
            history.append(line)
        except Exception as e:
            print("Error:", e)
    return ""

def ask_ai():
    q = input("Ask about data (e.g. 'capital of France', 'inventor of radio'): ").strip().lower()
    results = []
    # Search through known data tables
    searches = [
        ("country_detail", "get_country_detail_data", 0, [1]),
        ("city", "get_city_data", 0, [1]),
        ("invention", "get_invention_data", 0, [1]),
        ("element", "get_chemistry_element_data", 0, [1]),
        ("planet", "get_planet_data", 0, [1]),
        ("animal", "get_animal_extended_data", 0, [2]),
        ("language", "get_language_data", 1, [0]),
        ("crypto", "get_crypto_data", 0, [1]),
        ("programming_language", "get_programming_language_data", 0, [2]),
        ("scientist", "get_computer_scientist_data", 0, [2]),
        ("game_engine", "get_game_engine_data", 0, [1]),
        ("particle", "get_particle_data", 0, [1]),
        ("treaty", "get_treaty_data", 0, [2]),
        ("war", "get_war_data", 0, [2]),
        ("president", "get_president_data", 0, [2]),
        ("pharaoh", "get_pharaoh_data", 0, [2]),
        ("emperor", "get_emperor_data", 0, [2]),
        ("marathon", "get_marathon_data", 0, [2]),
        ("stadium", "get_stadium_data_new", 0, [2]),
        ("airline", "get_airline_data", 0, [2]),
        ("automaker", "get_automaker_data", 0, [2]),
        ("bank", "get_bank_data", 0, [2]),
        ("museum", "get_museum_data_new", 0, [2]),
    ]
    for label, func_name, name_idx, detail_idxs in searches:
        func = globals().get(func_name)
        if not func: continue
        try:
            data = func()
            for item in data:
                if len(item) > name_idx and q in str(item[name_idx]).lower():
                    parts = [str(item[name_idx])]
                    for di in detail_idxs:
                        if di < len(item):
                            parts.append(str(item[di]))
                    results.append("[" + label + "] " + " -> ".join(parts))
                    if len(results) >= 5: break
            if len(results) >= 5: break
        except: pass
    if not results:
        return "No data found for '" + q + "'. Try being more specific."
    return "\n".join(results[:10])

# === Notes System ===
NOTES_FILE = "Json/ai_notes.json"
TODOS_FILE = "Json/ai_todos.json"

def _load_notes():
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f: return json.load(f)
    except: return []

def _save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as f: json.dump(notes, f, indent=2)

def _load_todos():
    try:
        with open(TODOS_FILE, "r", encoding="utf-8") as f: return json.load(f)
    except: return []

def _save_todos(todos):
    with open(TODOS_FILE, "w", encoding="utf-8") as f: json.dump(todos, f, indent=2)

def cmd_notes(args):
    notes = _load_notes()
    parts = args.split(None, 1) if args else [""]
    action = parts[0].lower() if parts else ""
    if action == "add" and len(parts) > 1:
        notes.append(parts[1])
        _save_notes(notes)
        return "Note added ({} total).".format(len(notes))
    elif action == "list":
        if not notes: return "No notes."
        return "\n".join("  {}. {}".format(i+1, n) for i, n in enumerate(notes))
    elif action == "remove" and len(parts) > 1 and parts[1].isdigit():
        idx = int(parts[1]) - 1
        if 0 <= idx < len(notes):
            removed = notes.pop(idx)
            _save_notes(notes)
            return "Removed: " + removed
        return "Invalid index."
    elif action == "clear":
        _save_notes([])
        return "All notes cleared."
    return "Usage: notes add|list|remove N|clear"

def cmd_todo(args):
    todos = _load_todos()
    parts = args.split(None, 1) if args else [""]
    action = parts[0].lower() if parts else ""
    if action == "add" and len(parts) > 1:
        todos.append({"task": parts[1], "done": False})
        _save_todos(todos)
        return "Todo added ({} total).".format(len(todos))
    elif action == "list":
        if not todos: return "No todos."
        lines = []
        for i, t in enumerate(todos):
            status = C_GREEN + "[X]" + C_RESET if t["done"] else C_RED + "[ ]" + C_RESET
            lines.append("  {}. {} {}".format(i+1, status, t["task"]))
        return "\n".join(lines)
    elif action == "done" and len(parts) > 1 and parts[1].isdigit():
        idx = int(parts[1]) - 1
        if 0 <= idx < len(todos):
            todos[idx]["done"] = True
            _save_todos(todos)
            return "Marked done: " + todos[idx]["task"]
        return "Invalid index."
    elif action == "remove" and len(parts) > 1 and parts[1].isdigit():
        idx = int(parts[1]) - 1
        if 0 <= idx < len(todos):
            removed = todos.pop(idx)
            _save_todos(todos)
            return "Removed: " + removed["task"]
        return "Invalid index."
    elif action == "clear":
        _save_todos([])
        return "All todos cleared."
    return "Usage: todo add|list|done N|remove N|clear"

def cmd_remind(args):
    parts = args.split(None, 1)
    if len(parts) < 2 or not parts[0].isdigit():
        return "Usage: remind <seconds> <message>"
    secs = int(parts[0])
    msg = parts[1]
    import threading as _th
    def _notify():
        print("\n" + C_BOLD + C_YELLOW + "!!! REMINDER: " + msg + C_RESET)
    t = _th.Timer(secs, _notify)
    t.daemon = True
    t.start()
    return "Reminder set for {} seconds.".format(secs)

def cmd_help_detail(topic):
    help_map = {
        "quiz": "Interactive quiz on 16 data tables (elements, planets, cities, languages, inventions, dinosaurs, mountains, volcanoes). Type 'quiz' to start, then answer multiple choice questions.",
        "chart": "ASCII bar chart generator. Usage: chart <numbers> or barchart <numbers>. Numbers separated by commas. Optionally prefix with labels: 'Apples,5,Oranges,12'.",
        "timer": "Countdown timer. Usage: 'timer' then enter seconds. Shows live countdown MM:SS.",
        "stopwatch": "Stopwatch with lap support. Press Enter to record a lap, type 'stop' to end.",
        "calc": "Calculator REPL. Type expressions to evaluate. 'h' for history, 'c' to clear, 'q' to quit.",
        "flashcard": "Flashcard learner with score tracking. Tests knowledge on 16 data tables with multiple choice.",
        "ask": "Natural-language query across all data tables. Example: 'ask capital of France', 'ask inventor of radio'.",
        "save": "Export a data table to a file. Usage: 'save' then enter filename and table name.",
        "docs": "Opens AI.py-docs.html in your web browser (comprehensive documentation).",
        "dashboard": "Opens dashboard.html in your web browser (interactive web UI).",
        "hbpe_start": "Starts HubBasePE turtle graphics environment.",
        "hbpe_program1": "Runs HBPE Program 1 (turtle graphics demo). Programs 1-20 and P1-P5 available.",
        "hbpe_dev_console": "Opens HBPE developer console (requires HBPE >= 0.0.2.0.0).",
        "hbpe_compat": "Shows installed HubBasePE version and feature status.",
        "aiscript_run": "Run AiScript code inline. Usage: aiscript_run <code>",
        "aiscript_file": "Run an AiScript .ais file. Usage: aiscript_file <path>",
        "345": "Launches HubBasePE Code system with VIP authentication.",
        "debug_exec": "Interactive debug console. Type Python expressions, HBPE program numbers, or 'stop' to exit.",
        "notes": "Simple note taking. 'notes add <text>', 'notes list', 'notes remove N', 'notes clear'.",
        "todo": "Todo list manager. 'todo add <task>', 'todo list', 'todo done N', 'todo remove N', 'todo clear'.",
        "remind": "Set a timed reminder. Usage: 'remind <seconds> <message>'.",
        "hb_util": "Launch HubBaseUtility — built-in type/format checker with showcase demo. Aliases: hb_utility, hbu.",
        "hb_utility": "Launch HubBaseUtility — built-in type/format checker with showcase demo. Aliases: hb_util, hbu.",
        "hbu": "Launch HubBaseUtility — built-in type/format checker with showcase demo. Aliases: hb_util, hb_utility.",
        "pylevel": "PyLevel interactive learning module — 45 ops: file ops, crypto, regex, calculator, and more. Aliases: lvl, 3608.",
        "lvl": "PyLevel interactive learning module — 45 ops: file ops, crypto, regex, calculator, and more. Aliases: pylevel, 3608.",
        "3608": "PyLevel interactive learning module — 45 ops: file ops, crypto, regex, calculator, and more. Aliases: pylevel, lvl.",
        "pylevel / lvl / 3608": "PyLevel interactive learning module — file ops, crypto, regex, and more.",
    }
    if topic in help_map:
        return C_BOLD + topic + C_RESET + ": " + help_map[topic]
    # Try numeric
    if topic.isdigit():
        return "Command {}: try typing it to see what it does, or use 'categories' for grouped listing.".format(topic)
    return "No detailed help for '" + topic + "'. Try 'categories' for command listing."

def help_cat():
    print(C_BOLD + "=== COMMAND CATEGORIES ===" + C_RESET)
    cats = [
        ("Drawing", "1-17, 76-119 (diamond, tree, heart, star, cat, dog, fish, butterfly, rabbit, owl, snake, house, flower, smile, pyramid, triangle, hourglass, circle, pineapple, ghost, alien, bird, turtle, unicorn, robot, spaceship, dragon, crown, castle, mountain, wave, sun, moon, arrows, DNA, pacman, bowtie, flag, stairs, table, candle, lamp, key, lock, phone, TV, envelope, coffee, burger, pizza, ice cream, cake)"),
        ("Math", "18-23, 61-65 (fibonacci, prime, factorial, GCD, LCM, mean, median, mode, std dev, quad, sort, search), 133-155 (sum digits, reverse, armstrong, perfect, happy, collatz, sieve, prime, goldbach, euler, matrix, vector)"),
        ("Utilities", "24-31, 33-34, 41-50, 155-172 (binary, hex, octal, roman, temp, distance, weight, password, pig latin, caesar, palindrome, anagram, BMI, zodiac, morse, day of week, leap year, base, hash, encode, ROT13, word count, sort, reverse words, acronym)"),
        ("Games", "35-40, 52-57 (guess number, hangman, word scramble, riddle, trivia, magic 8 ball, coin flip, dice, card draw, high/low, RPS)"),
        ("Data", "67-75, 121-132 (quote, animals, colors, fruits, vegetables, elements, random number, UUID, shuffle, flatten, chunk, unique, intersect)"),
        ("Admin/Mod/VIP", "system_info, list_users, toggle_debug, featured_joke, vip_fact, vip_quote"),
        ("Debug", "debug_functions, debug_vars, debug_cmd_count, debug_exec"),
        ("HBPE / HB Util", "345, hbpe_start, hbpe_advance, hbpe_restart, hbpe_stop, hbpe_program1-20, hbpe_programp1-5, hbpe_dev_console, hbpe_compat, hb_util/hbu"),
        ("AiScript", "aiscript_run <code> (run inline code), aiscript_file <path> (run .ais file)"),
        ("PyLevel", "3608, pylevel, lvl — interactive file/string/crypto learning module"),
        ("New v3.6", "quiz, chart, suggest, ask/ai/query, flashcard/learn, colors, pager_test, cls, version, timer, stopwatch, calc, categories, save/export"),
        ("HTML Docs", "docs (open AI.py-docs.html), dashboard (open dashboard.html), gen_html/regenerate (rebuild HTML files)"),
        ("Notes/Todo", "notes (add/list/remove/clear), todo (add/list/done/remove/clear), remind <sec> <msg>"),
        ("Help", "help_<command> or explain <command> or whatis <command> for detailed command info"),
    ]
    for name, desc in cats:
        print(C_CYAN + name + C_RESET + ": " + desc)

def save_data():
    fname = input("Filename: ").strip() or "export.txt"
    table = input("Data table name (e.g. get_city_data): ").strip()
    func = globals().get(table)
    if not func: return "Table '" + table + "' not found."
    try:
        data = func()
        with open(fname, "w", encoding="utf-8") as f:
            for item in data:
                f.write(str(item) + "\n")
        return "Saved {} entries to {}".format(len(data), fname)
    except Exception as e:
        return "Error: " + str(e)

def flashcard():
    tables = [
        ("city", "get_city_data", 0, 1), ("country_detail", "get_country_detail_data", 0, 1),
        ("element", "get_chemistry_element_data", 0, 1), ("invention", "get_invention_data", 0, 1),
        ("planet", "get_planet_data", 0, 2), ("president", "get_president_data", 0, 2),
        ("pharaoh", "get_pharaoh_data", 0, 2), ("war", "get_war_data", 0, 2),
        ("treaty", "get_treaty_data", 0, 2), ("marathon", "get_marathon_data", 0, 2),
        ("bank", "get_bank_data", 0, 2), ("airline", "get_airline_data", 0, 2),
        ("automaker", "get_automaker_data", 0, 2), ("stadium", "get_stadium_data_new", 0, 2),
        ("museum", "get_museum_data_new", 0, 2), ("olympic", "get_olympic_games_data", 2, 1),
    ]
    print(C_BOLD + "=== FLASHCARD LEARNER ===" + C_RESET)
    print("Tables available:")
    for i, (label, _, _, _) in enumerate(tables):
        print("  {}. {}".format(i+1, label))
    try:
        choice = int(input("Pick table (1-{}): ".format(len(tables)))) - 1
        if choice < 0 or choice >= len(tables): return "Invalid choice."
        label, func_name, prompt_idx, answer_idx = tables[choice]
        func = globals().get(func_name)
        if not func: return "Table not loaded."
        data = func()
        correct = 0; total = 0
        print(C_CYAN + "Flashcards: {} (type 'q' to quit)".format(label) + C_RESET)
        random.shuffle(data)
        for entry in data:
            prompt = str(entry[prompt_idx]) if prompt_idx < len(entry) else "?"
            answer = str(entry[answer_idx]) if answer_idx < len(entry) else "?"
            resp = input("{}? ".format(prompt)).strip()
            if resp.lower() == "q": break
            total += 1
            if resp.lower() == answer.lower():
                print(C_GREEN + "Correct!" + C_RESET)
                correct += 1
            else:
                print(C_RED + "Wrong: {}".format(answer) + C_RESET)
        score = (correct/total*100) if total else 0
        return "Score: {}/{} = {:.1f}%".format(correct, total, score)
    except: return "Cancelled."

_AI_MODULE_FUNCS = None
def _register_ai_module(eval_):
    global _AI_MODULE_FUNCS
    if _AI_MODULE_FUNCS is None:
        _AI_MODULE_FUNCS = {}
        for _k, _v in list(globals().items()):
            if _k.startswith("_"): continue
            if not callable(_v): continue
            _c = getattr(_v, "__code__", None)
            if _c and getattr(_c, "co_filename", None) == __file__:
                _AI_MODULE_FUNCS[_k] = _v
    _AI_MODULE_FUNCS["__version__"] = __version__
    eval_.register_module("ai", _AI_MODULE_FUNCS)

def _run_aiscript_file(path):
    src = open(path, encoding="utf-8").read()
    tokens = aiscript._Lexer(src).tokenize()
    ast = aiscript._Parser(tokens, src).parse()
    e = aiscript._Eval()
    _register_ai_module(e)
    e.eval(ast)

