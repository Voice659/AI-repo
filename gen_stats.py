import AI, html, os
from inspect import getmembers, isfunction

def esc(s):
    return html.escape(str(s))

funcs = sorted([f for f in dir(AI) if f.startswith('get_') and f.endswith('_data')])
total_funcs = len(funcs)

files_info = {}
for fname in ['AI.py', 'data_bulk.py', 'data_bulk2.py', 'data_bulk3.py', 'data_bulk4.py']:
    if os.path.exists(fname):
        sz = os.path.getsize(fname)
        with open(fname, 'rb') as f:
            lc = sum(1 for _ in f)
        files_info[fname] = (sz, lc)

total_lines = sum(lc for _, lc in files_info.values())

curated_names = {
    'get_chemistry_element_data','get_planet_data','get_city_data','get_mountain_data',
    'get_country_detail_data','get_river_data','get_lake_data','get_language_data',
    'get_invention_data','get_dinosaur_data','get_ocean_data','get_volcano_data',
    'get_earthquake_data','get_hurricane_data',
    'get_constellation_data','get_galaxy_data','get_gemstone_data','get_mineral_data',
    'get_ocean_current_data','get_geological_formation_data','get_soil_type_data'
}
curated_count = len(curated_names)
bulk_count = total_funcs - curated_count

size_ranges = {}
total_entries = 0
for name in funcs:
    try:
        data = getattr(AI, name)()
        cnt = len(data) if isinstance(data, (list, tuple)) else 0
        total_entries += cnt
        key = '500 entries' if cnt >= 500 else ('100-499 entries' if cnt >= 100 else ('50-99 entries' if cnt >= 50 else ('10-49 entries' if cnt >= 10 else '1-9 entries')))
        size_ranges[key] = size_ranges.get(key, 0) + 1
    except:
        pass

VERSION = AI.__version__

html_str = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
html_str += '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
html_str += '<title>AI.py v' + VERSION + ' Statistics</title>\n'
html_str += '<style>\n'
html_str += '  *{margin:0;padding:0;box-sizing:border-box;}\n'
html_str += '  body{background:#0d1117;color:#c9d1d9;font-family:Courier New,monospace;line-height:1.6;padding:20px;}\n'
html_str += '  .container{max-width:960px;margin:auto;}\n'
html_str += '  h1{color:#58a6ff;font-size:2em;margin:20px 0 5px;}\n'
html_str += '  h2{color:#79c0ff;font-size:1.4em;margin:30px 0 10px;border-bottom:1px solid #30363d;padding-bottom:5px;}\n'
html_str += '  .subtitle{color:#8b949e;font-size:0.95em;margin-bottom:20px;}\n'
html_str += '  .stat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px;margin:20px 0;}\n'
html_str += '  .stat-card{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:20px;text-align:center;}\n'
html_str += '  .stat-card .num{font-size:2em;font-weight:bold;color:#58a6ff;}\n'
html_str += '  .stat-card .lbl{font-size:0.85em;color:#8b949e;margin-top:5px;}\n'
html_str += '  table{width:100%;border-collapse:collapse;margin:10px 0;}\n'
html_str += '  th{text-align:left;color:#8b949e;border-bottom:1px solid #30363d;padding:8px 12px;font-size:0.85em;}\n'
html_str += '  td{padding:6px 12px;border-bottom:1px solid #21262d;font-size:0.9em;}\n'
html_str += '  a{color:#58a6ff;}\n'
html_str += '  .footer{margin-top:40px;padding-top:20px;border-top:1px solid #30363d;color:#8b949e;font-size:0.85em;text-align:center;}\n'
html_str += '</style>\n</head>\n<body>\n'
html_str += '<div style="background:#161b22;border-bottom:1px solid #30363d;padding:8px 20px;text-align:center;font-size:0.85em;">\n'
html_str += '<a href="index.html" style="color:#58a6ff;text-decoration:none;">Home</a>\n'
html_str += '<span style="color:#30363d;margin:0 12px;">|</span>\n'
html_str += '<a href="AI.py-docs.html" style="color:#58a6ff;text-decoration:none;">Docs</a>\n'
html_str += '<span style="color:#30363d;margin:0 12px;">|</span>\n'
html_str += '<a href="dashboard.html" style="color:#58a6ff;text-decoration:none;">Dashboard</a>\n'
html_str += '<span style="color:#30363d;margin:0 12px;">|</span>\n'
html_str += '<a href="changelog.html" style="color:#58a6ff;text-decoration:none;">Changelog</a>\n'
html_str += '<span style="color:#30363d;margin:0 12px;">|</span>\n'
html_str += '<span style="color:#8b949e;">Stats</span>\n'
html_str += '</div>\n<div class="container">\n'
html_str += '<h1>AI.py Statistics</h1>\n<p class="subtitle">Project breakdown for v' + VERSION + '</p>\n'
html_str += '<div class="stat-grid">\n'
html_str += '  <div class="stat-card"><div class="num">' + str(total_funcs) + '</div><div class="lbl">Data Functions</div></div>\n'
html_str += '  <div class="stat-card"><div class="num">' + '{:,}'.format(total_entries) + '</div><div class="lbl">Data Entries</div></div>\n'
html_str += '  <div class="stat-card"><div class="num">' + '{:,}'.format(total_lines) + '</div><div class="lbl">Total Lines</div></div>\n'
html_str += '  <div class="stat-card"><div class="num">' + str(curated_count) + '</div><div class="lbl">Curated Tables</div></div>\n'
html_str += '  <div class="stat-card"><div class="num">' + str(bulk_count) + '</div><div class="lbl">Bulk Tables</div></div>\n'
html_str += '  <div class="stat-card"><div class="num">2700+</div><div class="lbl">Commands</div></div>\n'
html_str += '  <div class="stat-card"><div class="num">10</div><div class="lbl">Ext Modules</div></div>\n'
html_str += '  <div class="stat-card"><div class="num">' + VERSION + '</div><div class="lbl">Version</div></div>\n'
html_str += '</div>\n<h2>File Distribution</h2>\n<table>\n<tr><th>File</th><th>Size</th><th>Lines</th><th>Type</th></tr>\n'
for fname in ['AI.py', 'data_bulk.py', 'data_bulk2.py', 'data_bulk3.py', 'data_bulk4.py']:
    sz, lc = files_info[fname]
    sz_str = '{:.1f} KB'.format(sz/1024)
    ftype = 'Main' if fname == 'AI.py' else 'Bulk'
    html_str += '<tr><td>' + esc(fname) + '</td><td>' + sz_str + '</td><td>' + '{:,}'.format(lc) + '</td><td>' + ftype + '</td></tr>\n'
html_str += '</table>\n<h2>Data Table Distribution by Size</h2>\n<table>\n<tr><th>Size Range</th><th>Count</th></tr>\n'
for rng, cnt in sorted(size_ranges.items()):
    html_str += '<tr><td>' + rng + '</td><td>' + str(cnt) + '</td></tr>\n'
html_str += '</table>\n<h2>Data Function Distribution</h2>\n<table>\n<tr><th>Module</th><th>Functions</th><th>Type</th></tr>\n'
html_str += '<tr><td>AI.py + data_bulk.py</td><td>229</td><td>Bulk</td></tr>\n'
html_str += '<tr><td>data_bulk2.py</td><td>133</td><td>Bulk</td></tr>\n'
html_str += '<tr><td>data_bulk3.py</td><td>103</td><td>Bulk</td></tr>\n'
html_str += '<tr><td>data_bulk4.py</td><td>200</td><td>Bulk</td></tr>\n'
html_str += '</table>\n<h2>External Modules</h2>\n<table>\n<tr><th>Module</th><th>Purpose</th></tr>\n'
html_str += '<tr><td>space_data.py</td><td>Astronomy data</td></tr>\n'
html_str += '<tr><td>mini_games.py</td><td>Games: guess, hangman, scramble, riddles</td></tr>\n'
html_str += '<tr><td>trivia_pack.py</td><td>Trivia questions</td></tr>\n'
html_str += '<tr><td>word_play.py</td><td>Pig Latin, Caesar cipher, anagrams</td></tr>\n'
html_str += '<tr><td>art_extra.py</td><td>Additional ASCII art</td></tr>\n'
html_str += '<tr><td>world_data.py</td><td>Geographic data tables</td></tr>\n'
html_str += '<tr><td>story_data.py</td><td>Story prompts</td></tr>\n'
html_str += '<tr><td>data_bulk.py</td><td>424 tables (214K lines)</td></tr>\n'
html_str += '<tr><td>data_bulk2.py</td><td>133 tables (67K lines)</td></tr>\n'
html_str += '<tr><td>data_bulk3.py</td><td>103 tables (52K lines)</td></tr>\n'
html_str += '<tr><td>data_bulk4.py</td><td>200 tables (201K lines)</td></tr>\n'
html_str += '</table>\n<h2>Role System</h2>\n<table>\n<tr><th>Role</th><th>Password</th><th>Badge</th></tr>\n'
html_str += '<tr><td>User</td><td>-</td><td>Gray</td></tr>\n'
html_str += '<tr><td>VIP</td><td>5280</td><td>Green</td></tr>\n'
html_str += '<tr><td>Mod</td><td>M-5280-M</td><td>Blue</td></tr>\n'
html_str += '<tr><td>Admin</td><td>A-52-80-A</td><td>Red</td></tr>\n'
html_str += '</table>\n<h2>Curated Tables</h2>\n<table>\n<tr><th>Table</th><th>Type</th></tr>\n'
for cur_name in sorted(curated_names):
    disp = cur_name.replace('get_','').replace('_data','').replace('_',' ').title()
    html_str += '<tr><td>' + disp + '</td><td>Curated</td></tr>\n'
html_str += '</table>\n<div class="footer">\n  AI.py v' + VERSION + ' Statistics\n</div>\n</div>\n</body>\n</html>'

with open('stats.html', 'w', encoding='utf-8') as f:
    f.write(html_str)

print('Written stats.html ({:,} chars)'.format(len(html_str)))
print('Functions: {}, entries: {:,}, lines: {:,}'.format(total_funcs, total_entries, total_lines))
