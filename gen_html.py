import AI, data_bulk, json, html, os

# ---- Collect all data tables ----
funcs = sorted([f for f in dir(AI) if f.startswith('get_') and f.endswith('_data')])
curated_names = {
    'get_chemistry_element_data','get_planet_data','get_city_data','get_mountain_data',
    'get_country_detail_data','get_river_data','get_lake_data','get_language_data',
    'get_invention_data','get_dinosaur_data','get_ocean_data','get_volcano_data',
    'get_earthquake_data','get_hurricane_data',
    'get_constellation_data','get_galaxy_data','get_gemstone_data','get_mineral_data',
    'get_ocean_current_data','get_geological_formation_data','get_soil_type_data'
}

data_index = []   # (name, display_name, count, is_curated)
curated_data = {} # name -> list of rows
for name in funcs:
    try:
        data = getattr(AI, name)()
        cnt = len(data) if isinstance(data, (list, tuple)) else 0
        disp = name.replace('get_','').replace('_data','').replace('_',' ').title()
        is_cur = name in curated_names
        data_index.append((name, disp, cnt, is_cur))
        if is_cur and cnt > 0:
            curated_data[name] = list(data[:30]) if cnt > 30 else list(data)
    except:
        data_index.append((name, name.replace('get_','').replace('_data',''), 0, False))

VERSION = AI.__version__
YEAR = "2025"

# ---- HTML Escaping helpers ----
def esc(s):
    return html.escape(str(s))

def esc_json(obj):
    return json.dumps(obj, ensure_ascii=False)

# ---- Build command categories ----
cat_drawing = [(1,"Diamond"),(2,"Tree"),(3,"Heart"),(4,"Star"),(5,"Cat"),(6,"Dog"),
    (7,"Fish"),(8,"Butterfly"),(9,"Rabbit"),(10,"Owl"),(11,"Snake"),(12,"House"),
    (13,"Flower"),(14,"Smiley"),(15,"ASCII House"),(16,"ASCII Flower"),(17,"ASCII Smiley"),
    (76,"Pyramid"),(77,"Triangle"),(78,"Hourglass"),(79,"Circle"),(80,"Pineapple"),
    (81,"Ghost"),(82,"Alien"),(83,"Bird"),(84,"Turtle"),(85,"Unicorn"),(86,"Robot"),
    (87,"Spaceship"),(88,"Dragon"),(89,"Crown"),(90,"Castle"),(91,"Mountain"),
    (92,"Wave"),(93,"Sun"),(94,"Moon"),(95,"Arrows"),(96,"DNA"),(97,"Pacman"),
    (98,"Bowtie"),(99,"Flag"),(100,"Stairs"),(101,"Table"),(102,"Candle"),(103,"Lamp"),
    (104,"Key"),(105,"Lock"),(106,"Phone"),(107,"TV"),(108,"Envelope"),(109,"Coffee"),
    (110,"Burger"),(111,"Pizza"),(112,"Ice Cream"),(113,"Cake")]
cat_math = [(18,"Fibonacci"),(19,"Prime Check"),(20,"Factorial"),(21,"GCD"),(22,"LCM"),
    (23,"Prime Factors"),
    (61,"Mean/Avg"),(62,"Median"),(63,"Mode"),(64,"Std Dev"),(65,"Quadratic Solver"),
    (66,"Sort"),(67,"Search"),
    (133,"Sum Digits"),(134,"Reverse Number"),(135,"Armstrong"),(136,"Perfect Number"),
    (137,"Happy Number"),(138,"Collatz"),(139,"Sieve"),(140,"Prime Count"),
    (141,"Goldbach"),(142,"Euler"),(143,"Matrix Ops"),(144,"Vector Ops"),
    (145,"Determinant"),(146,"Dot Product"),(147,"Cross Product"),
    (148,"Matrix Transpose"),(149,"Matrix Multiply"),(150,"Factorial (big)"),
    (151,"Combination"),(152,"Permutation"),(153,"Catalan"),(154,"Bell"),
    (155,"Stirling")]
cat_utils = [(24,"Binary"),(25,"Hex"),(26,"Octal"),(27,"Roman Numerals"),
    (28,"Temp Convert"),(29,"Distance Convert"),(30,"Weight Convert"),
    (31,"Password Gen"),(32,"Password Strength"),
    (33,"Pig Latin"),(34,"Caesar Cipher"),(41,"Palindrome"),(42,"Anagram"),
    (43,"BMI Calc"),(44,"Zodiac Sign"),(45,"Morse Code"),(46,"Day of Week"),
    (47,"Leap Year"),(48,"Base Convert"),(49,"Hash"),(50,"Encode/Decode"),
    (51,"ROT13"),
    (155,"Word Count"),(156,"Text Sort"),(157,"Reverse Words"),(158,"Acronym"),
    (159,"UUID Gen"),(160,"Shuffle List"),(161,"Flatten List"),(162,"Chunk List"),
    (163,"Unique List"),(164,"Intersect Lists"),(165,"Union Lists"),
    (166,"Diff Lists"),(167,"Sym Diff"),(168,"Zip Lists"),
    (169,"Rotate List"),(170,"Partition List"),(171,"Split List"),
    (172,"Random Item")]
cat_games = [(35,"Guess Number"),(36,"Hangman"),(37,"Word Scramble"),(38,"Riddle"),
    (39,"Trivia"),(40,"Magic 8 Ball"),(52,"Coin Flip"),(53,"Dice Roll"),
    (54,"Card Draw"),(55,"High/Low"),(56,"RPS"),(57,"Wordle")]
cat_data = [(67,"Quote"),(68,"Animals"),(69,"Colors"),(70,"Fruits"),(71,"Vegetables"),
    (72,"Elements"),(73,"Planets"),(74,"Countries"),(75,"Cities"),
    (121,"Weather"),(122,"Oceans"),(123,"Volcanoes"),(124,"Earthquakes"),
    (125,"Tsunamis"),(126,"Hurricanes"),(127,"Tornadoes"),(128,"Climate"),
    (129,"Geology"),(130,"Fossils"),(131,"Minerals"),(132,"Gemstones"),
    (173,"Stars"),(174,"Galaxies"),(175,"Space Missions"),
    (176,"Constellations"),(177,"Observatories"),(178,"Satellites"),
    (179,"Astronauts"),(180,"Telescopes"),
    (181,"Animals"),(182,"Birds"),(183,"Fish"),(184,"Insects"),(185,"Reptiles"),
    (186,"Mammals"),(187,"Dog Breeds"),(188,"Cat Breeds"),(189,"Horse Breeds"),
    (190,"Sharks"),(191,"Whales"),(192,"Snakes"),(193,"Butterflies"),
    (194,"Tree Species"),(195,"Flowers"),(196,"Fruits"),(197,"Vegetables"),
    (198,"Grains"),(199,"Herbs"),(200,"Spices"),
    (201,"Cuisines"),(202,"Cheeses"),(203,"Wines"),(204,"Cocktails"),
    (205,"Desserts"),(206,"Breads"),(207,"Pastas"),(208,"Soups"),(209,"Salads"),
    (210,"Sauces"),(211,"Recipes"),
    (212,"Languages"),(213,"Currencies"),(214,"Flags"),(215,"Capitals"),
    (216,"Continents"),(217,"Islands"),(218,"Deserts"),(219,"Forests"),
    (220,"Mountains"),(221,"Lakes"),(222,"Rivers"),
    (223,"Heritage Sites"),(224,"National Parks"),(225,"Natural Wonders"),
    (226,"Volcanoes"),(227,"Earthquakes"),(228,"Oceans"),
    (229,"Bridges"),(230,"Dams"),(231,"Tunnels"),(232,"Canals"),
    (233,"Lighthouses"),(234,"Ports"),(235,"Railways"),(236,"Highways"),
    (237,"Subways"),(238,"Airports"),
    (239,"Diseases"),(240,"Medicines"),(241,"Human Anatomy"),(242,"Vitamins"),
    (243,"Hormones"),(244,"Cell Types"),(245,"Medical Terms"),
    (246,"Artists"),(247,"Paintings"),(248,"Sculptures"),(249,"Museums"),
    (250,"Theaters"),(251,"Opera Houses"),(252,"Concert Halls"),
    (253,"Composers"),(254,"Musical Terms"),(255,"Dance Styles"),
    (256,"Music Genres"),(257,"Instruments"),
    (258,"Writers"),(259,"Poets"),(260,"Books"),(261,"Magazines"),
    (262,"Newspapers"),(263,"Publishers"),(264,"Awards"),(265,"Award Shows"),
    (266,"Film Festivals"),(267,"Film Genres"),(268,"Movies"),
    (269,"Directors"),(270,"Actors"),(271,"TV Channels"),
    (272,"TV Shows"),(273,"Radio Stations"),(274,"Record Labels"),
    (275,"Songs"),(276,"Music Festivals"),
    (277,"Directors"),(278,"Writers"),(279,"Scientists"),
    (280,"Mathematicians"),(281,"Physicists"),(282,"Chemists"),
    (283,"Biologists"),(284,"Astronomers"),(285,"Explorers"),
    (286,"Philosophers"),(287,"Presidents"),(288,"Prime Ministers"),
    (289,"Leaders"),(290,"Pharaohs"),(291,"Emperors"),
    (292,"Sports"),(293,"Olympic Games"),(294,"Olympic Sports"),
    (295,"Stadiums"),(296,"Sports Teams"),(297,"Marathons"),
    (298,"Martial Arts"),(299,"Board Games"),(300,"Card Games"),
    (301,"Video Games"),
    (302,"Elements"),(303,"Minerals"),(304,"Rocks"),(305,"Fossils"),
    (306,"Gemstones"),(307,"Particles"),
    (308,"Cloud Types"),(309,"Wind Patterns"),(310,"Soil Types"),
    (311,"Biomes"),(312,"Ecosystems"),(313,"Rock Types")]
cat_admin = [
    ("system_info","System info (any role)"),("list_users","List users (any role)"),
    ("toggle_debug","Toggle debug mode (Admin)"),("featured_joke","Joke (Mod+)"),
    ("vip_fact","VIP fact"),("vip_quote","VIP quote"),
    ("debug_functions","Debug functions list"),("debug_vars","Debug vars"),
    ("debug_cmd_count","Debug cmd count"),("debug_exec","Debug console")]
cat_hbpe = [
    ("hbpe_start","Start HBPE"),("hbpe_advance","Advance HBPE"),
    ("hbpe_restart","Restart HBPE"),("hbpe_stop","Stop HBPE"),
    ("hbpe_program1","Run HBPE P1"),("hbpe_program2","Run HBPE P2"),
    ("hbpe_program3","Run HBPE P3"),("hbpe_dev_console","HBPE dev console"),
    ("hbpe_socket_server","Start socket server"),("hbpe_socket_connect","Connect to server"),
    ("hbpe_socket_send","Send message"),("hbpe_socket_recv","Receive message"),
    ("hbpe_socket_close","Close socket")]
cat_new = [
    ("quiz / data_quiz","Interactive quiz on 16 data tables"),
    ("chart / barchart","ASCII bar chart from numbers"),
    ("suggest / find","Search commands by keyword"),
    ("ask / ai / query","Query all data tables by keyword"),
    ("flashcard / learn","Flashcard learner with score"),
    ("help2 / categories","Categorized command listing"),
    ("save / export","Export data table to file"),
    ("timer / countdown","Countdown timer"),
    ("stopwatch","Stopwatch with laps"),
    ("calc / calculator","Calculator REPL with history"),
    ("colors / badge","Color settings, badge display"),
    ("pager_test","Test pager output"),
    ("cls / clear","Clear screen"),
    ("version / ver","Show version")]

def render_cat_table(cat_name, items):
    rows = []
    for item in items:
        if isinstance(item, tuple) and len(item) == 2:
            cmd, desc = item
            rows.append('<tr><td class="cmd-num">{}</td><td>{}</td></tr>'.format(esc(str(cmd)), esc(desc)))
        else:
            num, name = item
            rows.append('<tr><td class="cmd-num">{}</td><td>{}</td></tr>'.format(esc(str(num)), esc(name)))
    return '<table class="cmd-table"><tr><th>#</th><th>Command</th></tr>{}</table>'.format('\n'.join(rows))

# ============ BUILD DOCS HTML ============
def build_docs():
    # Version history
    versions = [
        ("3.0.2","Initial large expansion, external modules"),
        ("3.0.3","HBPE integration, role system"),
        ("3.1.0","debug_exec merged console"),
        ("3.2.0","Utility functions, handle_cmd refactor"),
        ("3.3.0","Data functions, 239K lines"),
        ("3.4.0","CLI colors, badges, pager, chart, quiz"),
        ("3.5.0","Bulk data (424 tables), module split"),
        ("3.6.0","Curated data, flashcard, AI query, timer, calc, docs"),
        ("3.7.0","133 new data functions (data_bulk2.py), 67K lines"),
        ("3.8.0","103 new data functions (data_bulk3.py), 50K lines, 465 total data tables, stats/changelog pages"),
        ("3.9.0","data-index.html page, updated welcome message, rebuilt updater"),
        ("4.0.0","Major: 200 new data functions (data_bulk4.py), ~201K lines, 665 total tables, visual installer (AIInstaller.exe), download/features site pages, 800K+ total lines"),
        ("4.1.0","Major: 100 new data functions (data_bulk5.py), ~100K lines, 750+ total tables, dual HBPE (v0.0.1.2.01 + v0.0.2.0.00b1), hbpe_compat.py compat layer, Programm20 support, dev_console detection, 900K+ total lines"),
        ("4.2.0","Major: 100 new data functions (data_bulk6.py), ~100K lines, 850+ total tables, 1M+ total lines, installer/updater rebuilt with version history, AIInstaller v4.2.0, AIUpdater v4.2.0"),
        ("4.4.0","Major: 935 new utility functions via gen_code4.py, 3600+ commands, 1.3M+ total lines"),
    ]
    curated_sample_map = {}
    for name in curated_names:
        disp = name.replace('get_','').replace('_data','').replace('_',' ').title()
        if name in curated_data:
            rows = curated_data[name]
            sample_html = '<table class="sample-table"><tr>'
            if rows:
                keys = list(rows[0]) if isinstance(rows[0], (list, tuple)) else []
                gen = (esc(k) for k in keys)
                sample_html += ''.join('<th>{}</th>'.format(k) for k in gen)
                sample_html += '</tr>'
                for row in rows[:5]:
                    sample_html += '<tr>' + ''.join('<td>{}</td>'.format(esc(c)) for c in row) + '</tr>'
                sample_html += '</table>'
            curated_sample_map[disp] = sample_html

    bulk_count = sum(1 for n,d,c,cu in data_index if not cu and c > 0)

    html_str = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI.py v''' + VERSION + r''' Documentation</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: #0d1117; color: #c9d1d9; font-family: 'Courier New', monospace; line-height: 1.6; padding: 20px; }
  .container { max-width: 960px; margin: auto; }
  h1 { color: #58a6ff; font-size: 2em; margin: 20px 0 5px; }
  h2 { color: #79c0ff; font-size: 1.4em; margin: 30px 0 10px; border-bottom: 1px solid #30363d; padding-bottom: 5px; }
  h3 { color: #a5d6ff; font-size: 1.1em; margin: 20px 0 8px; }
  .subtitle { color: #8b949e; font-size: 0.95em; margin-bottom: 20px; }
  .badge { display: inline-block; padding: 2px 10px; border-radius: 4px; font-weight: bold; font-size: 0.8em; margin: 2px; }
  .badge-admin { background: #d73a49; color: #fff; }
  .badge-mod { background: #0366d6; color: #fff; }
  .badge-vip { background: #28a745; color: #fff; }
  .badge-user { background: #30363d; color: #c9d1d9; }
  .stat-box { display: inline-block; background: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 15px 25px; margin: 5px; text-align: center; }
  .stat-box .num { font-size: 1.8em; font-weight: bold; color: #58a6ff; }
  .stat-box .label { font-size: 0.8em; color: #8b949e; }
  .cmd-table { width: 100%; border-collapse: collapse; margin: 10px 0; }
  .cmd-table th { text-align: left; color: #8b949e; border-bottom: 1px solid #30363d; padding: 6px 10px; font-size: 0.85em; }
  .cmd-table td { padding: 4px 10px; border-bottom: 1px solid #21262d; font-size: 0.9em; }
  .cmd-table .cmd-num { color: #58a6ff; font-weight: bold; width: 60px; }
  .cmd-table tr:hover { background: #161b22; }
  .sample-table { width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 0.85em; overflow-x: auto; display: block; }
  .sample-table th { text-align: left; background: #161b22; border: 1px solid #30363d; padding: 5px 8px; color: #79c0ff; }
  .sample-table td { border: 1px solid #21262d; padding: 4px 8px; }
  .tag-curated { display: inline-block; background: #1f6feb; color: #fff; font-size: 0.7em; padding: 1px 6px; border-radius: 3px; }
  .tag-bulk { display: inline-block; background: #21262d; color: #8b949e; font-size: 0.7em; padding: 1px 6px; border-radius: 3px; }
  .data-list { columns: 3; column-gap: 20px; }
  .data-list li { list-style: none; font-size: 0.85em; padding: 3px 0; color: #8b949e; break-inside: avoid; }
  .data-list li.curated { color: #79c0ff; }
  pre { background: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 15px; overflow-x: auto; font-size: 0.9em; margin: 10px 0; }
  code { background: #161b22; padding: 1px 5px; border-radius: 3px; font-size: 0.9em; }
  a { color: #58a6ff; }
  .footer { margin-top: 40px; padding-top: 20px; border-top: 1px solid #30363d; color: #8b949e; font-size: 0.85em; text-align: center; }
  @media (max-width: 600px) { .data-list { columns: 2; } }
</style>
</head>
<body>
<div style="background:#161b22;border-bottom:1px solid #30363d;padding:8px 20px;text-align:center;font-size:0.85em;">
  <a href="index.html" style="color:#58a6ff;text-decoration:none;">&#x2190; Home</a>
  <span style="color:#30363d;margin:0 12px;">|</span>
  <a href="dashboard.html" style="color:#58a6ff;text-decoration:none;">Dashboard</a>
  <span style="color:#30363d;margin:0 12px;">|</span>
  <a href="data-index.html" style="color:#58a6ff;text-decoration:none;">Data Index</a>
  <span style="color:#30363d;margin:0 12px;">|</span>
  <a href="features.html" style="color:#58a6ff;text-decoration:none;">Features</a>
  <span style="color:#30363d;margin:0 12px;">|</span>
  <a href="download.html" style="color:#58a6ff;text-decoration:none;">Downloads</a>
  <span style="color:#30363d;margin:0 12px;">|</span>
  <a href="stats.html" style="color:#58a6ff;text-decoration:none;">Statistics</a>
  <span style="color:#30363d;margin:0 12px;">|</span>
  <a href="changelog.html" style="color:#58a6ff;text-decoration:none;">Changelog</a>
  <span style="color:#30363d;margin:0 12px;">|</span>
  <span style="color:#8b949e;">AI.py v''' + VERSION + r''' Docs</span>
</div>
<div class="container">

<h1>AI.py v''' + VERSION + r'''</h1>
<p class="subtitle">A massive Python CLI assistant — 3600+ commands, 1.3M+ lines, 950+ data tables</p>

<p>
  <span class="badge badge-admin">ADMIN</span>
  <span class="badge badge-mod">MOD</span>
  <span class="badge badge-vip">VIP</span>
  <span class="badge badge-user">User</span>
</p>

<h2>Statistics</h2>
<p>
  <span class="stat-box"><span class="num">3600+</span><br><span class="label">Commands</span></span>
  <span class="stat-box"><span class="num">''' + "{:,}".format(total_entries) + r'''</span><br><span class="label">Data Entries</span></span>
  <span class="stat-box"><span class="num">''' + str(len(data_index)) + r'''</span><br><span class="label">Data Tables</span></span>
  <span class="stat-box"><span class="num">''' + str(len(curated_names)) + r'''</span><br><span class="label">Curated Tables</span></span>
</p>

<h2>Commands by Category</h2>

<h3>Drawing (1–17, 76–113)</h3>
''' + render_cat_table("Drawing", cat_drawing) + r'''

<h3>Math (18–23, 61–67, 133–155)</h3>
''' + render_cat_table("Math", cat_math) + r'''

<h3>Utilities (24–34, 41–51, 155–172)</h3>
''' + render_cat_table("Utilities", cat_utils) + r'''

<h3>Games (35–40, 52–57)</h3>
''' + render_cat_table("Games", cat_games) + r'''

<h3>Data / Reference (67–75, 121–132, 173–313)</h3>
''' + render_cat_table("Data", cat_data) + r'''

<h3>Admin / Mod / VIP</h3>
''' + render_cat_table("Admin", cat_admin) + r'''

<h3>HBPE Integration</h3>
''' + render_cat_table("HBPE", cat_hbpe) + r'''

<h3>New in v3.6</h3>
''' + render_cat_table("New", cat_new) + r'''

<h2>Data Tables Index</h2>
<p>All ''' + str(len(data_index)) + r''' data tables. <span class="tag-curated">Curated</span> = real verified data. <span class="tag-bulk">Bulk</span> = generated procedural data.</p>
<ul class="data-list">
'''

    for name, disp, cnt, is_cur in data_index:
        tag = '<span class="tag-curated">C</span>' if is_cur else '<span class="tag-bulk">B</span>'
        cls = 'class="curated"' if is_cur else ''
        html_str += '  <li {}>{} {} ({:,})</li>\n'.format(cls, tag, esc(disp), cnt)

    html_str += r'''</ul>

<h2>Curated Data Samples</h2>
<p>Displaying first 5 entries from each curated table.</p>
'''

    for name in sorted(curated_names):
        disp = name.replace('get_','').replace('_data','').replace('_',' ').title()
        html_str += '<h3>{}</h3>\n'.format(esc(disp))
        if name in curated_data and curated_data[name]:
            rows = curated_data[name]
            html_str += '<table class="sample-table"><tr>'
            keys = list(rows[0]) if isinstance(rows[0], (list, tuple)) else []
            html_str += ''.join('<th>{}</th>'.format(esc(str(k))) for k in keys)
            html_str += '</tr>'
            for row in rows[:5]:
                html_str += '<tr>' + ''.join('<td>{}</td>'.format(esc(str(c))) for c in row) + '</tr>'
            html_str += '</table>\n'
        else:
            html_str += '<p>No data</p>\n'

    html_str += r'''

<h2>Version History</h2>
<table class="cmd-table">
<tr><th>Version</th><th>Changes</th></tr>
'''
    for v, desc in versions:
        html_str += '<tr><td class="cmd-num">{}</td><td>{}</td></tr>\n'.format(esc(v), esc(desc))

    html_str += r'''
</table>

<h2>Role System</h2>
<table class="sample-table">
<tr><th>Role</th><th>Password</th><th>Badge Color</th><th>Access</th></tr>
<tr><td>User</td><td>—</td><td>Gray</td><td>Basic commands</td></tr>
<tr><td>VIP</td><td>5280</td><td>Green</td><td>VIP commands + basic</td></tr>
<tr><td>Mod</td><td>M-5280-M</td><td>Blue</td><td>Mod commands + VIP + basic</td></tr>
<tr><td>Admin</td><td>A-52-80-A</td><td>Red</td><td>All commands</td></tr>
</table>

<h2>Quick Start</h2>
<pre>
python AI.py
# Enter role password at prompt, or just press Enter for User
# Type 'h' for help, 'q' to quit
# Type 'categories' for categorized help
# Type 'quiz' for interactive quiz
# Type 'timer' for countdown timer
# Type 'calc' for calculator REPL
</pre>

<h2>Built With</h2>
<ul>
  <li>Python 3.x</li>
  <li>HubBasePE v0.0.1.2.01 / v0.0.2.0.00b1 (dual)</li>
  <li>15 external modules: space_data, mini_games, trivia_pack, word_play, art_extra, world_data, story_data, data_bulk, data_bulk2, data_bulk3, data_bulk4, data_bulk5, data_bulk6, data_bulk7, hbpe_compat</li>
  <li>gen_code4.py, installer.py, updater.py</li>
</ul>

<div class="footer">
  <p>AI.py v''' + VERSION + r''' &mdash; ''' + str(YEAR) + r'''</p>
</div>

</div>
</body>
</html>'''

    with open("AI.py-docs.html", "w", encoding="utf-8") as f:
        f.write(html_str)
    print("Written AI.py-docs.html ({:,} chars)".format(len(html_str)))

# ============ BUILD DASHBOARD HTML ============
def build_dashboard():
    # Prepare curated data as JSON for embedding
    curated_json = {}
    for name in sorted(curated_names):
        if name in curated_data:
            rows = curated_data[name]
            # Convert tuples to lists for JSON
            curated_json[name] = [list(r) for r in rows]
        else:
            curated_json[name] = []

    # Build data index JSON (for data browser)
    data_json = [{"name": n, "disp": d, "count": c, "curated": cu} for n, d, c, cu in data_index]

    curated_js = esc_json(curated_json)
    data_index_js = esc_json(data_json)

    # Build command list for searchable command browser
    all_cmds = []
    for num, name in cat_drawing: all_cmds.append({"num": str(num), "name": name, "cat": "Drawing"})
    for num, name in cat_math: all_cmds.append({"num": str(num), "name": name, "cat": "Math"})
    for num, name in cat_utils: all_cmds.append({"num": str(num), "name": name, "cat": "Utilities"})
    for num, name in cat_games: all_cmds.append({"num": str(num), "name": name, "cat": "Games"})
    for num, name in cat_data: all_cmds.append({"num": str(num), "name": name, "cat": "Data"})
    for cmd, desc in cat_admin: all_cmds.append({"num": cmd, "name": desc, "cat": "Admin"})
    for cmd, desc in cat_hbpe: all_cmds.append({"num": cmd, "name": desc, "cat": "HBPE"})
    for name, desc in cat_new: all_cmds.append({"num": name.split(" / ")[0], "name": desc, "cat": "v3.6"})
    cmds_js = esc_json(all_cmds)

    html_str = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI.py v''' + VERSION + r''' Dashboard</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  :root { --bg: #0d1117; --bg2: #161b22; --bg3: #21262d; --fg: #c9d1d9; --fg2: #8b949e; --accent: #58a6ff; --accent2: #79c0ff; --border: #30363d; --green: #28a745; --red: #d73a49; }
  body { background: var(--bg); color: var(--fg); font-family: 'Segoe UI', Arial, sans-serif; }
  .navbar { background: var(--bg2); border-bottom: 1px solid var(--border); padding: 10px 20px; display: flex; align-items: center; gap: 20px; position: sticky; top: 0; z-index: 100; }
  .navbar .title { font-weight: bold; color: var(--accent); font-size: 1.2em; }
  .navbar .tabs { display: flex; gap: 5px; }
  .navbar .tabs button { background: transparent; border: 1px solid var(--border); color: var(--fg2); padding: 6px 14px; border-radius: 4px; cursor: pointer; font-size: 0.85em; }
  .navbar .tabs button.active { background: var(--accent); color: #fff; border-color: var(--accent); }
  .navbar .tabs button:hover { background: var(--bg3); color: var(--fg); }
  .theme-btn { margin-left: auto; background: transparent; border: 1px solid var(--border); color: var(--fg2); padding: 6px 12px; border-radius: 4px; cursor: pointer; font-size: 0.85em; }
  .container { max-width: 1000px; margin: auto; padding: 20px; }
  .tab-content { display: none; }
  .tab-content.active { display: block; }
  h2 { color: var(--accent2); margin-bottom: 15px; }
  .stats { display: flex; gap: 10px; flex-wrap: wrap; margin: 20px 0; }
  .stat-card { background: var(--bg2); border: 1px solid var(--border); border-radius: 8px; padding: 20px 30px; text-align: center; flex: 1; min-width: 120px; }
  .stat-card .num { font-size: 2em; font-weight: bold; color: var(--accent); }
  .stat-card .lbl { font-size: 0.85em; color: var(--fg2); margin-top: 5px; }
  input, select { background: var(--bg2); border: 1px solid var(--border); color: var(--fg); padding: 8px 12px; border-radius: 4px; font-size: 0.9em; width: 100%; margin: 5px 0; }
  input:focus, select:focus { outline: none; border-color: var(--accent); }
  table { width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 0.85em; }
  th { text-align: left; background: var(--bg2); border: 1px solid var(--border); padding: 8px; color: var(--accent2); position: sticky; top: 0; cursor: pointer; }
  th:hover { background: var(--bg3); }
  td { border: 1px solid var(--border); padding: 6px 8px; }
  tr:hover { background: var(--bg2); }
  .data-browser { display: flex; gap: 10px; margin: 10px 0; }
  .data-browser select { flex: 1; }
  .data-browser .info { background: var(--bg2); border: 1px solid var(--border); border-radius: 4px; padding: 8px 15px; white-space: nowrap; display: flex; align-items: center; color: var(--fg2); font-size: 0.85em; }
  #chart-input { width: 100%; min-height: 100px; font-family: monospace; background: var(--bg2); border: 1px solid var(--border); color: var(--fg); padding: 10px; border-radius: 4px; resize: vertical; }
  #chart-output { background: var(--bg2); border: 1px solid var(--border); border-radius: 4px; padding: 15px; margin-top: 10px; font-family: monospace; white-space: pre; overflow-x: auto; }
  .badge { display: inline-block; padding: 1px 8px; border-radius: 3px; font-size: 0.75em; font-weight: bold; }
  .badge-c { background: #1f6feb; color: #fff; }
  .badge-b { background: var(--bg3); color: var(--fg2); }
  .quiz-question { background: var(--bg2); border: 1px solid var(--border); border-radius: 8px; padding: 20px; margin: 15px 0; }
  .quiz-question p { font-size: 1.1em; margin-bottom: 10px; }
  .quiz-option { display: block; background: var(--bg3); border: 1px solid var(--border); border-radius: 4px; padding: 10px 15px; margin: 5px 0; cursor: pointer; }
  .quiz-option:hover { background: var(--accent); color: #fff; }
  .quiz-option.correct { background: var(--green); color: #fff; }
  .quiz-option.wrong { background: var(--red); color: #fff; }
  .quiz-score { font-size: 1.2em; color: var(--accent); margin: 10px 0; }
  #quiz-result { font-size: 1.1em; margin: 10px 0; }
  .scroll-table { max-height: 500px; overflow-y: auto; border: 1px solid var(--border); border-radius: 4px; }
  .tag { display: inline-block; background: var(--bg3); color: var(--fg2); padding: 2px 8px; border-radius: 3px; font-size: 0.75em; margin: 1px; }
  .version-badge { color: var(--accent); font-weight: bold; }
  .footer { margin-top: 40px; padding: 20px; text-align: center; color: var(--fg2); font-size: 0.85em; border-top: 1px solid var(--border); }

  /* Light theme */
  .light { --bg: #f6f8fa; --bg2: #fff; --bg3: #e1e4e8; --fg: #24292e; --fg2: #586069; --border: #d1d5da; }
</style>
</head>
<body>
<div style="background:var(--bg2);border-bottom:1px solid var(--border);padding:8px 20px;text-align:center;font-size:0.85em;display:flex;align-items:center;justify-content:center;gap:12px;">
  <a href="index.html" style="color:var(--accent);text-decoration:none;">&#x2190; Home</a>
  <span style="color:var(--border);">|</span>
  <a href="AI.py-docs.html" style="color:var(--accent);text-decoration:none;">Documentation</a>
  <span style="color:var(--border);">|</span>
  <a href="data-index.html" style="color:var(--accent);text-decoration:none;">Data Index</a>
  <span style="color:var(--border);">|</span>
  <a href="features.html" style="color:var(--accent);text-decoration:none;">Features</a>
  <span style="color:var(--border);">|</span>
  <a href="download.html" style="color:var(--accent);text-decoration:none;">Downloads</a>
  <span style="color:var(--border);">|</span>
  <a href="stats.html" style="color:var(--accent);text-decoration:none;">Statistics</a>
  <span style="color:var(--border);">|</span>
  <a href="changelog.html" style="color:var(--accent);text-decoration:none;">Changelog</a>
  <span style="color:var(--border);">|</span>
  <span style="color:var(--fg2);">Dashboard</span>
</div>

<div class="navbar">
  <span class="title">AI.py v''' + VERSION + r'''</span>
  <div class="tabs">
    <button class="active" data-tab="home">Home</button>
    <button data-tab="commands">Commands</button>
    <button data-tab="data">Data Browser</button>
    <button data-tab="quiz">Quiz</button>
    <button data-tab="chart">Chart</button>
  </div>
  <button class="theme-btn" onclick="toggleTheme()">Toggle Theme</button>
</div>

<div class="container">

<!-- HOME TAB -->
<div id="tab-home" class="tab-content active">
  <h2>AI.py Dashboard</h2>
  <p style="color:var(--fg2);margin-bottom:20px;">A massive Python CLI assistant — interactive web companion.</p>
  <div class="stats">
    <div class="stat-card"><div class="num">2,700+</div><div class="lbl">Commands</div></div>
    <div class="stat-card"><div class="num">''' + "{:,}".format(len(data_index)) + r'''</div><div class="lbl">Data Tables</div></div>
    <div class="stat-card"><div class="num">''' + "{:,}".format(total_entries) + r'''</div><div class="lbl">Data Entries</div></div>
    <div class="stat-card"><div class="num">''' + str(len(curated_names)) + r'''</div><div class="lbl">Curated Tables</div></div>
    <div class="stat-card"><div class="num">4.3.0</div><div class="lbl">Version</div></div>
  </div>
  <h3>Quick Features</h3>
  <p style="color:var(--fg2);line-height:1.8;">
    <span class="tag">quiz</span> Interactive knowledge quiz
    <span class="tag">flashcard</span> Flashcard learner with scoring
    <span class="tag">chart</span> ASCII bar charts
    <span class="tag">ask/ai</span> Natural-language data query
    <span class="tag">timer</span> Countdown timer
    <span class="tag">stopwatch</span> Lap-capable stopwatch
    <span class="tag">calc</span> REPL calculator with history
    <span class="tag">categories</span> Categorized command help
    <span class="tag">save/export</span> Export tables to file
  </p>
  <h3>Data Categories</h3>
  <p style="color:var(--fg2);">
    Elements, Planets, Cities, Mountains, Countries, Rivers, Lakes, Languages,
    Inventions, Dinosaurs, Oceans, Volcanoes, Earthquakes, Hurricanes (curated)
    + 215+ generated data tables with 500–1500 entries each.
  </p>
  <h3>Role System</h3>
  <p style="color:var(--fg2);">
    <span class="badge badge-c">ADMIN</span> A-52-80-A &nbsp;
    <span class="badge" style="background:#0366d6;color:#fff;">MOD</span> M-5280-M &nbsp;
    <span class="badge" style="background:#28a745;color:#fff;">VIP</span> 5280 &nbsp;
    <span class="badge" style="background:var(--bg3);color:var(--fg2);">User</span> (no password)
  </p>
</div>

<!-- COMMANDS TAB -->
<div id="tab-commands" class="tab-content">
  <div style="display:flex;gap:10px;">
    <input id="cmd-search" placeholder="Search commands..." oninput="filterCommands()">
    <select id="cmd-cat-filter" onchange="filterCommands()" style="width:200px;">
      <option value="">All Categories</option>
      <option>Drawing</option><option>Math</option><option>Utilities</option><option>Games</option>
      <option>Data</option><option>Admin</option><option>HBPE</option><option>v3.6</option>
    </select>
  </div>
  <div class="scroll-table">
    <table id="cmd-table">
      <tr><th onclick="sortCmdTable(0)">#</th><th onclick="sortCmdTable(1)">Name</th><th onclick="sortCmdTable(2)">Category</th></tr>
    </table>
  </div>
</div>

<!-- DATA BROWSER TAB -->
<div id="tab-data" class="tab-content">
  <div class="data-browser">
    <select id="data-select" onchange="loadDataTable()">
      <option value="">Select a table...</option>
    </select>
    <div class="info" id="data-info">No table selected</div>
  </div>
  <div class="scroll-table">
    <table id="data-table"><tr><td style="color:var(--fg2);text-align:center;padding:40px;">Select a table above</td></tr></table>
  </div>
</div>

<!-- QUIZ TAB -->
<div id="tab-quiz" class="tab-content">
  <div style="display:flex;gap:10px;margin-bottom:15px;">
    <select id="quiz-topic" style="width:200px;">
      <option value="elements">Elements</option>
      <option value="planets">Planets</option>
      <option value="cities">Cities</option>
      <option value="languages">Languages</option>
      <option value="inventions">Inventions</option>
      <option value="dinosaurs">Dinosaurs</option>
      <option value="mountains">Mountains</option>
      <option value="volcanoes">Volcanoes</option>
    </select>
    <button style="background:var(--accent);color:#fff;border:none;padding:8px 20px;border-radius:4px;cursor:pointer;" onclick="startQuiz()">New Quiz</button>
    <span id="quiz-score" class="quiz-score"></span>
  </div>
  <div id="quiz-area">
    <p style="color:var(--fg2);">Select a topic and click "New Quiz" to start.</p>
  </div>
  <div id="quiz-result"></div>
</div>

<!-- CHART TAB -->
<div id="tab-chart" class="tab-content">
  <p style="color:var(--fg2);margin-bottom:10px;">Enter comma-separated numbers (e.g. 5,12,8,3,15). Optionally add labels: "Apples,5,Oranges,12,Bananas,8".</p>
  <textarea id="chart-input" placeholder="5,12,8,3,15">5,12,8,3,15</textarea>
  <div style="margin:10px 0;">
    <input id="chart-title" placeholder="Chart title (optional)" style="width:300px;">
    <button style="background:var(--accent);color:#fff;border:none;padding:8px 20px;border-radius:4px;cursor:pointer;margin-left:10px;" onclick="drawChart()">Draw Chart</button>
  </div>
  <div id="chart-output"></div>
</div>

</div>

<div class="footer">
  AI.py v''' + VERSION + r''' Dashboard &mdash; Generated companion
</div>

<script>
// === DATA (embedded from Python) ===
var CURATED = ''' + curated_js + r''';
var DATA_INDEX = ''' + data_index_js + r''';
var COMMANDS = ''' + cmds_js + r''';

// === THEME ===
function toggleTheme() {
  document.body.classList.toggle('light');
  localStorage.setItem('ai-py-theme', document.body.classList.contains('light') ? 'light' : 'dark');
}
if (localStorage.getItem('ai-py-theme') === 'light') document.body.classList.add('light');

// === TABS ===
document.querySelectorAll('.navbar .tabs button').forEach(function(btn) {
  btn.addEventListener('click', function() {
    document.querySelectorAll('.navbar .tabs button').forEach(function(b) { b.classList.remove('active'); });
    document.querySelectorAll('.tab-content').forEach(function(t) { t.classList.remove('active'); });
    btn.classList.add('active');
    document.getElementById('tab-' + btn.getAttribute('data-tab')).classList.add('active');
  });
});

// === COMMANDS TAB ===
function filterCommands() {
  var q = document.getElementById('cmd-search').value.toLowerCase();
  var cat = document.getElementById('cmd-cat-filter').value;
  var tbody = document.getElementById('cmd-table');
  tbody.innerHTML = '<tr><th onclick="sortCmdTable(0)">#</th><th onclick="sortCmdTable(1)">Name</th><th onclick="sortCmdTable(2)">Category</th></tr>';
  COMMANDS.forEach(function(c) {
    if (cat && c.cat !== cat) return;
    if (q && !c.name.toLowerCase().includes(q) && !c.num.toLowerCase().includes(q)) return;
    var tr = tbody.insertRow();
    tr.insertCell().textContent = c.num;
    tr.insertCell().textContent = c.name;
    tr.insertCell().textContent = c.cat;
  });
}
var cmdSortDir = [1,1,1];
function sortCmdTable(col) {
  cmdSortDir[col] *= -1;
  var tbody = document.getElementById('cmd-table');
  var rows = Array.from(tbody.rows).slice(1);
  rows.sort(function(a, b) {
    var va = a.cells[col].textContent.toLowerCase();
    var vb = b.cells[col].textContent.toLowerCase();
    if (va < vb) return -1 * cmdSortDir[col];
    if (va > vb) return 1 * cmdSortDir[col];
    return 0;
  });
  for (var i = 1; i < tbody.rows.length; i++) tbody.deleteRow(i);
  for (var i = 0; i < rows.length; i++) tbody.appendChild(rows[i]);
}
filterCommands();

// === DATA BROWSER ===
(function() {
  var sel = document.getElementById('data-select');
  DATA_INDEX.forEach(function(d) {
    var opt = document.createElement('option');
    opt.value = d.name;
    var tag = d.curated ? ' [C]' : ' [B]';
    opt.textContent = d.disp + tag + ' (' + d.count.toLocaleString() + ')';
    sel.appendChild(opt);
  });
})();

function loadDataTable() {
  var name = document.getElementById('data-select').value;
  if (!name) {
    document.getElementById('data-table').innerHTML = '<tr><td style="color:var(--fg2);text-align:center;padding:40px;">Select a table above</td></tr>';
    document.getElementById('data-info').textContent = 'No table selected';
    return;
  }
  var data = CURATED[name];
  var info = DATA_INDEX.find(function(d) { return d.name === name; });
  document.getElementById('data-info').textContent = (info ? info.disp : name) + ' - ' + (data ? data.length : 0) + ' entries';
  if (!data || data.length === 0) {
    document.getElementById('data-table').innerHTML = '<tr><td style="color:var(--fg2);text-align:center;padding:40px;">Bulk data not embedded. Run AI.py to view this table.</td></tr>';
    return;
  }
  var html = '<tr>';
  var keys = Object.keys(data[0]);
  keys.forEach(function(k) { html += '<th>' + k + '</th>'; });
  html += '</tr>';
  data.forEach(function(row) {
    html += '<tr>';
    row.forEach(function(cell) {
      html += '<td>' + String(cell) + '</td>';
    });
    html += '</tr>';
  });
  document.getElementById('data-table').innerHTML = html;
}

// === QUIZ ===
var quizState = { topic: '', questions: [], index: 0, correct: 0, total: 0 };

function startQuiz() {
  var topic = document.getElementById('quiz-topic').value;
  var map = { elements: 'get_chemistry_element_data', planets: 'get_planet_data', cities: 'get_city_data',
              languages: 'get_language_data', inventions: 'get_invention_data', dinosaurs: 'get_dinosaur_data',
              mountains: 'get_mountain_data', volcanoes: 'get_volcano_data' };
  var data = CURATED[map[topic]];
  if (!data || data.length < 4) {
    document.getElementById('quiz-area').innerHTML = '<p style="color:var(--red);">Not enough data for this topic.</p>';
    return;
  }
  var questions = [];
  var used = {};
  var maxQ = Math.min(10, data.length);
  while (questions.length < maxQ) {
    var idx = Math.floor(Math.random() * data.length);
    if (used[idx]) continue;
    used[idx] = true;
    var row = data[idx];
    var q, answer, choices;
    // Generate question based on topic
    if (topic === 'elements') {
      answer = row[0];
      var wrong = getWrong(data, idx, 3);
      q = 'What is the name of element ' + row[2] + ' (symbol: ' + row[1] + ')?';
      choices = shuffle([answer].concat(wrong));
    } else if (topic === 'planets') {
      answer = row[0];
      var wrong = getWrong(data, idx, 3);
      q = 'Which planet is ' + row[2] + ' AU from the Sun?';
      choices = shuffle([answer].concat(wrong));
    } else if (topic === 'cities') {
      answer = row[0];
      var wrong = getWrong(data, idx, 3);
      q = 'Which city has a population of ' + row[2].toLocaleString() + '?';
      choices = shuffle([answer].concat(wrong));
    } else if (topic === 'languages') {
      answer = row[0];
      var wrong = getWrong(data, idx, 3);
      q = 'Which language has ' + row[2] + ' million speakers?';
      choices = shuffle([answer].concat(wrong));
    } else if (topic === 'inventions') {
      answer = row[0];
      var wrong = getWrong(data, idx, 3);
      q = 'What invention was created in ' + row[2] + ' by ' + row[3] + '?';
      choices = shuffle([answer].concat(wrong));
    } else if (topic === 'dinosaurs') {
      answer = row[0];
      var wrong = getWrong(data, idx, 3);
      q = 'Which dinosaur lived in the ' + row[1] + ' period?';
      choices = shuffle([answer].concat(wrong));
    } else if (topic === 'mountains') {
      answer = row[0];
      var wrong = getWrong(data, idx, 3);
      q = 'Which mountain is ' + row[1] + 'm tall?';
      choices = shuffle([answer].concat(wrong));
    } else if (topic === 'volcanoes') {
      answer = row[0];
      var wrong = getWrong(data, idx, 3);
      q = 'Which volcano is ' + row[1] + 'm tall?';
      choices = shuffle([answer].concat(wrong));
    }
    questions.push({ q: q, answer: answer, choices: choices });
  }
  quizState = { topic: topic, questions: questions, index: 0, correct: 0, total: questions.length };
  document.getElementById('quiz-score').textContent = '0/' + questions.length;
  showQuizQuestion();
}

function getWrong(data, idx, count) {
  var wrong = [];
  var used = {};
  while (wrong.length < count) {
    var r = Math.floor(Math.random() * data.length);
    if (r === idx || used[r]) continue;
    used[r] = true;
    wrong.push(data[r][0]);
  }
  return wrong;
}

function shuffle(arr) {
  for (var i = arr.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
  }
  return arr;
}

function showQuizQuestion() {
  var state = quizState;
  if (state.index >= state.questions.length) {
    document.getElementById('quiz-area').innerHTML = '<div class="quiz-question"><p style="font-size:1.3em;">Quiz Complete!</p></div>';
    document.getElementById('quiz-result').innerHTML = '<p style="font-size:1.2em;color:var(--accent);">Score: ' + state.correct + '/' + state.total + ' (' + Math.round(state.correct/state.total*100) + '%)</p>';
    return;
  }
  var q = state.questions[state.index];
  var html = '<div class="quiz-question"><p>' + q.q + '</p>';
  q.choices.forEach(function(c) {
    html += '<div class="quiz-option" onclick="answerQuiz(this, \'' + q.answer.replace(/'/g, "\\'") + '\', \'' + c.replace(/'/g, "\\'") + '\')">' + c + '</div>';
  });
  html += '</div>';
  document.getElementById('quiz-area').innerHTML = html;
  document.getElementById('quiz-result').innerHTML = 'Question ' + (state.index + 1) + ' of ' + state.total;
}

function answerQuiz(el, answer, choice) {
  if (el.classList.contains('correct') || el.classList.contains('wrong')) return;
  var all = el.parentElement.querySelectorAll('.quiz-option');
  all.forEach(function(o) { o.style.pointerEvents = 'none'; });
  if (choice === answer) {
    el.classList.add('correct');
    quizState.correct++;
  } else {
    el.classList.add('wrong');
    all.forEach(function(o) { if (o.textContent === answer) o.classList.add('correct'); });
  }
  document.getElementById('quiz-score').textContent = quizState.correct + '/' + quizState.total;
  setTimeout(function() {
    quizState.index++;
    showQuizQuestion();
  }, 1000);
}

// === CHART ===
function drawChart() {
  var text = document.getElementById('chart-input').value.trim();
  var title = document.getElementById('chart-title').value.trim();
  if (!text) { document.getElementById('chart-output').textContent = 'Enter numbers.'; return; }
  var parts = text.split(',').map(function(s) { return s.trim(); });
  var nums = [];
  var labels = [];
  var i = 0;
  // Try to parse as label,value pairs
  while (i < parts.length) {
    var val = parseFloat(parts[i]);
    if (isNaN(val) && i + 1 < parts.length) {
      labels.push(parts[i]);
      i++;
      val = parseFloat(parts[i]);
      if (!isNaN(val)) nums.push(val);
      i++;
    } else if (!isNaN(val)) {
      labels.push('');
      nums.push(val);
      i++;
    } else {
      i++;
    }
  }
  if (nums.length === 0) { document.getElementById('chart-output').textContent = 'No valid numbers found.'; return; }
  var maxVal = Math.max.apply(null, nums);
  var barChar = '\u2588';
  var lines = [];
  if (title) lines.push(title);
  lines.push('');
  var maxLabelLen = 0;
  labels.forEach(function(l) { if (l.length > maxLabelLen) maxLabelLen = l.length; });
  for (var j = 0; j < nums.length; j++) {
    var barLen = maxVal > 0 ? Math.round((nums[j] / maxVal) * 50) : 1;
    var label = labels[j] || '';
    while (label.length < maxLabelLen + 1) label += ' ';
    var bar = '';
    for (var k = 0; k < barLen; k++) bar += barChar;
    lines.push(label + ' ' + bar + ' ' + nums[j]);
  }
  document.getElementById('chart-output').textContent = lines.join('\n');
}

// Draw initial chart
drawChart();
</script>
</body>
</html>'''

    with open("dashboard.html", "w", encoding="utf-8") as f:
        f.write(html_str)
    print("Written dashboard.html ({:,} chars)".format(len(html_str)))

# ============ BUILD DATA INDEX HTML ============
def build_data_index():
    html_str = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI.py v''' + VERSION + r''' — Data Tables Index</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: #0d1117; color: #c9d1d9; font-family: 'Segoe UI', Arial, sans-serif; }
  .container { max-width: 1000px; margin: auto; padding: 20px; }
  h1 { color: #58a6ff; font-size: 2em; margin: 20px 0 5px; }
  .subtitle { color: #8b949e; font-size: 0.95em; margin-bottom: 20px; }
  .controls { display: flex; gap: 10px; margin: 20px 0; flex-wrap: wrap; }
  .controls input, .controls select { background: #161b22; border: 1px solid #30363d; color: #c9d1d9; padding: 8px 12px; border-radius: 4px; font-size: 0.9em; }
  .controls input { flex: 1; min-width: 200px; }
  .controls select { width: 160px; }
  .controls input:focus, .controls select:focus { outline: none; border-color: #58a6ff; }
  .stats-row { color: #8b949e; font-size: 0.85em; margin: 10px 0; }
  table { width: 100%; border-collapse: collapse; }
  th { text-align: left; color: #8b949e; border-bottom: 1px solid #30363d; padding: 8px 12px; font-size: 0.85em; cursor: pointer; position: sticky; top: 0; background: #0d1117; }
  th:hover { color: #58a6ff; }
  td { padding: 6px 12px; border-bottom: 1px solid #21262d; font-size: 0.9em; }
  tr:hover { background: #161b22; }
  .tag-curated { display: inline-block; background: #1f6feb; color: #fff; font-size: 0.7em; padding: 1px 6px; border-radius: 3px; }
  .tag-bulk { display: inline-block; background: #21262d; color: #8b949e; font-size: 0.7em; padding: 1px 6px; border-radius: 3px; }
  .num { color: #58a6ff; font-family: monospace; }
  .footer { margin-top: 40px; padding-top: 20px; border-top: 1px solid #30363d; color: #8b949e; font-size: 0.85em; text-align: center; }
  a { color: #58a6ff; }
  .nav { background: #161b22; border-bottom: 1px solid #30363d; padding: 8px 20px; text-align: center; font-size: 0.85em; }
</style>
</head>
<body>
<div class="nav">
  <a href="index.html" style="color:#58a6ff;text-decoration:none;">&#x2190; Home</a>
  <span style="color:#30363d;margin:0 12px;">|</span>
  <a href="AI.py-docs.html" style="color:#58a6ff;text-decoration:none;">Documentation</a>
  <span style="color:#30363d;margin:0 12px;">|</span>
  <a href="dashboard.html" style="color:#58a6ff;text-decoration:none;">Dashboard</a>
  <span style="color:#30363d;margin:0 12px;">|</span>
  <a href="features.html" style="color:#58a6ff;text-decoration:none;">Features</a>
  <span style="color:#30363d;margin:0 12px;">|</span>
  <a href="download.html" style="color:#58a6ff;text-decoration:none;">Downloads</a>
  <span style="color:#30363d;margin:0 12px;">|</span>
  <a href="stats.html" style="color:#58a6ff;text-decoration:none;">Statistics</a>
  <span style="color:#30363d;margin:0 12px;">|</span>
  <a href="changelog.html" style="color:#58a6ff;text-decoration:none;">Changelog</a>
  <span style="color:#30363d;margin:0 12px;">|</span>
  <span style="color:#8b949e;">Data Index</span>
</div>
<div class="container">
<h1>AI.py Data Tables Index</h1>
<p class="subtitle">All ''' + str(len(data_index)) + r''' data tables — searchable, sortable, filterable</p>

<div class="controls">
  <input id="search" placeholder="Search tables..." oninput="filterTable()">
  <select id="filter" onchange="filterTable()">
    <option value="all">All Types</option>
    <option value="curated">Curated Only</option>
    <option value="bulk">Bulk Only</option>
  </select>
  <select id="sort" onchange="filterTable()">
    <option value="name">Sort by Name</option>
    <option value="count">Sort by Count</option>
  </select>
</div>
<div class="stats-row" id="stats">''' + str(len(data_index)) + r''' tables — ''' + '{:,}'.format(total_entries) + r''' total entries</div>
<table id="table">
<tr><th onclick="sortTable(0)">#</th><th onclick="sortTable(1)">Table Name</th><th onclick="sortTable(2)">Entries</th><th onclick="sortTable(3)">Type</th></tr>
</table>
</div>
<div class="footer">
  AI.py v''' + VERSION + r''' Data Index
</div>
<script>
var DATA = [
'''
    for i, (name, disp, cnt, is_cur) in enumerate(data_index, 1):
        typ = 'curated' if is_cur else 'bulk'
        tag = 'C' if is_cur else 'B'
        html_str += '  {{"n":"{}","d":"{}","c":{},"t":"{}","tag":"{}"}},\n'.format(
            esc(name.replace('"','\\"')), esc(disp.replace('"','\\"')), cnt, typ, tag)
    html_str += r"""];
var sortDir = [1,1,-1,1];
var sortCol = 1;

function filterTable() {
  var q = document.getElementById('search').value.toLowerCase();
  var f = document.getElementById('filter').value;
  var s = document.getElementById('sort').value;
  var filtered = DATA.filter(function(d) {
    if (f === 'curated' && d.t !== 'curated') return false;
    if (f === 'bulk' && d.t !== 'bulk') return false;
    return d.d.toLowerCase().includes(q) || d.n.toLowerCase().includes(q);
  });
  var sorted = filtered.slice().sort(function(a, b) {
    var va, vb;
    if (s === 'name') { va = a.d.toLowerCase(); vb = b.d.toLowerCase(); }
    else { va = a.c; vb = b.c; }
    if (va < vb) return -1;
    if (va > vb) return 1;
    return 0;
  });
  var tbody = document.getElementById('table');
  tbody.innerHTML = '<tr><th onclick="sortTable(0)">#</th><th onclick="sortTable(1)">Table Name</th><th onclick="sortTable(2)">Entries</th><th onclick="sortTable(3)">Type</th></tr>';
  sorted.forEach(function(d, i) {
    var tr = tbody.insertRow();
    tr.insertCell().textContent = i + 1;
    tr.insertCell().innerHTML = d.d;
    var cCell = tr.insertCell();
    cCell.textContent = d.c.toLocaleString();
    cCell.className = 'num';
    tr.insertCell().innerHTML = d.t === 'curated' ? '<span class="tag-curated">C</span>' : '<span class="tag-bulk">B</span>';
  });
  document.getElementById('stats').textContent = sorted.length + ' tables shown';
}

function sortTable(col) {
  sortDir[col] *= -1;
  document.getElementById('sort').value = 'name';
  var tbody = document.getElementById('table');
  var rows = Array.from(tbody.rows).slice(1);
  rows.sort(function(a, b) {
    var va = a.cells[col].textContent.toLowerCase();
    var vb = b.cells[col].textContent.toLowerCase();
    if (col === 2) { va = parseInt(a.cells[col].textContent.replace(/,/g,'')); vb = parseInt(b.cells[col].textContent.replace(/,/g,'')); }
    if (va < vb) return -1 * sortDir[col];
    if (va > vb) return 1 * sortDir[col];
    return 0;
  });
  for (var i = tbody.rows.length - 1; i > 0; i--) tbody.deleteRow(i);
  for (var i = 0; i < rows.length; i++) tbody.appendChild(rows[i]);
}

filterTable();
</script>
</body>
</html>"""

    with open("data-index.html", "w", encoding="utf-8") as f:
        f.write(html_str)
    print("Written data-index.html ({:,} chars)".format(len(html_str)))

# === MAIN ===
total_entries = sum(c for n,d,c,cu in data_index)
build_docs()
build_data_index()
build_dashboard()
print("Done!")
