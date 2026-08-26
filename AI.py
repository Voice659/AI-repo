import random, datetime, os, math, string, json, re, hashlib, base64, uuid, time, statistics, sys, textwrap
__version__ = "6.2.0"  # AI training system
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_SCRIPT_DIR, 'AiScript'))
sys.path.insert(0, os.path.join(_SCRIPT_DIR, 'AiModel'))
sys.path.insert(0, os.path.join(_SCRIPT_DIR, 'bin', 'datae'))
sys.path.insert(0, os.path.join(_SCRIPT_DIR, 'bin', 'datab'))
sys.path.insert(0, os.path.join(_SCRIPT_DIR, 'HBPE'))
sys.path.insert(0, os.path.join(_SCRIPT_DIR, 'HBUtil'))
os.makedirs(os.path.join(_SCRIPT_DIR, 'Json'), exist_ok=True)
import space_data, mini_games, trivia_pack, word_play, art_extra, world_data, story_data
import hbpe_compat as HB
import aiscript
import lvl_test
from lvl_test import *
import data_bulk
from data_bulk import *
import data_bulk2
from data_bulk2 import *
import data_bulk3
from data_bulk3 import *
import data_bulk4
from data_bulk4 import *
import data_bulk5
from data_bulk5 import *
import data_bulk6
from data_bulk6 import *
import data_bulk7
from data_bulk7 import *
import data_bulk8
from data_bulk8 import *
import data_bulk9
from data_bulk9 import *
import data_bulk10
from data_bulk10 import *
import data_bulk11
from data_bulk11 import *
import data_bulk12
from data_bulk12 import *
import data_bulk13
from data_bulk13 import *
import data_bulk14
from data_bulk14 import *
import data_bulk15
from data_bulk15 import *
import data_bulk16
from data_bulk16 import *
import data_bulk17
from data_bulk17 import *
import data_bulk18
from data_bulk18 import *
import data_bulk19
from data_bulk19 import *
import data_bulk20
from data_bulk20 import *
import data_bulk21
from data_bulk21 import *
import data_bulk22
from data_bulk22 import *
import data_bulk23
from data_bulk23 import *
import data_bulk24
from data_bulk24 import *
import data_bulk25
from data_bulk25 import *
import data_bulk26
from data_bulk26 import *
import data_bulk27
from data_bulk27 import *
import data_bulk28
from data_bulk28 import *
import data_bulk29
from data_bulk29 import *
import data_bulk30
from data_bulk30 import *
import data_bulk31
from data_bulk31 import *
import data_bulk32
from data_bulk32 import *
import data_bulk33
from data_bulk33 import *
import data_bulk34
from data_bulk34 import *
import data_bulk35
from data_bulk35 import *
import data_bulk36
from data_bulk36 import *
import data_bulk37
from data_bulk37 import *
import data_bulk38
from data_bulk38 import *


from aipy_ansi import *
from aipy_data import *

from aipy_help import *
import aipy_ai
import commands as _commands

_cmd_registry = {}

def _commands_dispatch(cmd, role, name, badge, ns):
    """Dispatch auto-eligible commands via commands.py registry."""
    return _commands.dispatch_auto(cmd, ns)

def cmd(*names, **kwargs):
    """Decorator: registers a function as a command handler.
    Usage: @cmd('name1','name2', role='Admin')
    Handler signature: def handler(name, role, badge): ...
    """
    role_req = kwargs.get('role')
    def decorator(func):
        for n in names:
            key = (n, role_req) if role_req else n
            _cmd_registry[key] = func
        return func
    return decorator

def handle_cmd(cmd, role, name, badge):
    # Check command registry first
    handler = _cmd_registry.get(cmd)
    if handler:
        return handler(name, role, badge)
    handler = _cmd_registry.get((cmd, role))
    if handler:
        return handler(name, role, badge)
    if cmd == "h":
        show_help(role)
    # Auto-eligible commands (from commands.py registry)
    if _commands_dispatch(cmd, role, name, badge, globals()):
        return True

    elif cmd == "Voice659" or cmd == "Voice659()":
        print("Voice659, The great /bin/je lord")
    elif cmd == "system_info" and role == "Admin":
        print(admin_system_info())
    elif cmd == "list_users" and role == "Admin":
        print(admin_list_users())
    elif cmd == "toggle_debug" and role == "Admin":
        print(toggle_debug())
    elif cmd == "featured_joke" and role == "Mod":
        print(mod_featured_joke())
    elif cmd == "vip_fact" and role == "Vip":
        print(vip_extra_fact())
    elif cmd == "vip_quote" and role == "Vip":
        print(vip_extra_quote())
    elif cmd == "hbpe_start":
        print("Starting HubBasePE...")
        HB.Start()
    elif cmd == "hbpe_advance":
        print("Advancing HubBasePE...")
        HB.Advance()
    elif cmd == "hbpe_restart" and role == "Admin":
        print("Restarting HubBasePE...")
        HB.Restart()
    elif cmd == "hbpe_stop":
        HB.PStop()
        print("HubBasePE stopped.")
    elif cmd.startswith("hbpe_program") or cmd.startswith("hbpe_prog"):
        _prog_id = cmd.replace("hbpe_program", "").replace("hbpe_prog", "")
        _plist = getattr(HB, "_prList", {}) or {}
        _ppr = getattr(HB, "_pprList", {}) or {}
        _key = None
        if _prog_id.isdigit():
            _key = int(_prog_id)
        elif _prog_id.upper().startswith("P") and _prog_id[1:].isdigit():
            _pk = int(_prog_id[1:])
            if _pk in _ppr:
                print("Running HubBasePE Program P{}...".format(_pk))
                try:
                    _ppr[_pk]()
                except SystemExit:
                    pass
                _key = None
            else:
                print("Program P{} not available.".format(_pk))
                _key = -1
        if _key is not None and _key >= 0:
            if _key in _plist:
                print("Running HubBasePE Program {}...".format(_prog_id))
                try:
                    _plist[_key]()
                except SystemExit:
                    pass
            else:
                print("Program {} not available in HBPE v{}.".format(_prog_id, HB.HBPE_VERSION))
    elif cmd == "hbpe_dev_console":
        if HB.HBPE_HAS_DEV_CONSOLE:
            print("Opening HubBasePE developer console...")
            HB.dev_console()
        else:
            print("Dev console not available in this HBPE version (v{}).".format(HB.HBPE_VERSION))
    elif cmd == "hbpe_compat":
        print("HBPE version: v{}".format(HB.HBPE_VERSION))
        print("Programm20: {}".format(HB.HBPE_HAS_PROGRAM20))
        print("Programm21: {}".format(getattr(HB, "HBPE_HAS_PROGRAM21", False)))
        print("Dev console: {}".format(HB.HBPE_HAS_DEV_CONSOLE))
        print("API: {}".format(HB.HBPE_API))
        _vip_user = HB.current_user() if hasattr(HB, "current_user") else None
        print("VIP: {}".format(bool(getattr(_vip_user, "VipAccess", False)) if _vip_user else False))
    elif cmd == "hbpe_vip" or cmd == "hbpe_vip off":
        if cmd.endswith("off"):
            if hasattr(HB, "set_vip"):
                HB.set_vip(False)
                print("VIP mode off.")
            else:
                print("VIP control not available in this HBPE version.")
        else:
            _vip_pw = input("VIP password -- ")
            if _vip_pw == "5280":
                if hasattr(HB, "set_vip"):
                    HB.set_vip(True)
                    print("Correct.")
                    print("VIP mode enabled.")
                else:
                    print("VIP control not available in this HBPE version.")
            else:
                print("Incorrect.")
    elif cmd.startswith("hbpe_run"):
        _run_arg = cmd[8:].strip()
        _plist = getattr(HB, "_prList", {}) or {}
        _key = None
        if _run_arg:
            if _run_arg[:1].upper() == "P" and _run_arg[1:].isdigit():
                _key = int(_run_arg[1:]) + int(getattr(HB._raw_hb, "progs", 20) or 20)
            elif _run_arg.isdigit():
                _key = int(_run_arg)
        if _key is None or _key not in _plist:
            print("Usage: hbpe_run <1-21 | P1-P5>  - run a single HubBasePE program")
        else:
            print("Running HubBasePE program {}...".format(_run_arg.upper()))
            try:
                _plist[_key]()
            except SystemExit:
                pass
    elif cmd in ("3608", "pylevel", "lvl"):
        print("--- PyLevel Module ---")
        pylevel_main()
    elif cmd.split(" ", 1)[0] in ("hb_util", "hb_utility", "hbut", "hbu"):
        _hbu_arg = cmd.split(" ", 1)[1].strip() if " " in cmd else ""
        try:
            import HubBaseUtility.Main as _HBU
            if not hasattr(_HBU, "ProgrammCycle"):
                _HBU.ProgrammCycle = _HBU.ProgramCycle
            print("--- HubBase Utility v{} ---".format(getattr(_HBU, '__version__', '?')))
            if _hbu_arg in ("0", "1", "2"):
                getattr(_HBU, "ProgrammU" + _hbu_arg)()
            elif not _hbu_arg:
                _HBU.Showcase()
            else:
                print("Usage: hbut [0|1|2]  (0 hello, 1 type detector, 2 calculator)")
        except ImportError:
            print("HubBaseUtility not installed.")
        except Exception as _hbu_e:
            print("HubBaseUtility error:", _hbu_e)
    elif cmd.startswith("ais ") or cmd.startswith("aiscript_run "):
        code = cmd[cmd.index(" ")+1:] if " " in cmd else ""
        if not code:
            print("Usage: ais <code>  — run AiScript one-liner")
        else:
            try:
                tokens = aiscript._Lexer(code).tokenize()
                ast = aiscript._Parser(tokens, code).parse()
                e = aiscript._Eval()
                _register_ai_module(e)
                e.eval(ast)
            except Exception as ex:
                print("AiScript error:", ex)
    elif cmd in ("ais","aiscript_run"):
        print("Usage: ais <code>  — run AiScript one-liner")
    elif cmd.startswith("run ") or cmd.startswith("aiscript_file "):
        path = cmd[cmd.index(" ")+1:] if " " in cmd else ""
        if not path:
            print("Usage: run <path>  — run AiScript file")
        else:
            try:
                _run_aiscript_file(path)
            except Exception as ex:
                print("AiScript error:", ex)
    elif cmd in ("run","aiscript_file"):
        print("Usage: run <path>  — run AiScript file")
    elif cmd in ("docs","html_docs"):
        if os.path.exists("AI.py-docs.html"):
            os.startfile("AI.py-docs.html")
        else:
            print("AI.py-docs.html not found. Run gen_html.py to generate it.")
    elif cmd in ("dashboard","html_dash"):
        if os.path.exists("dashboard.html"):
            os.startfile("dashboard.html")
        else:
            print("dashboard.html not found. Run gen_html.py to generate it.")
    elif cmd in ("2672","gen_html","regenerate"):
        print("Regenerating HTML documentation...")
        os.system(".venv\\Scripts\\python gen_html.py")
        print("Done. Type 'docs' or 'dashboard' to open.")
    elif cmd.startswith("notes") or cmd.startswith("todo") or cmd.startswith("remind"):
        cmd_lower = cmd.strip()
        if cmd_lower.startswith("notes "):
            print(cmd_notes(cmd_lower[6:]))
        elif cmd_lower == "notes":
            print("Usage: notes add|list|remove N|clear")
        elif cmd_lower.startswith("todo "):
            print(cmd_todo(cmd_lower[5:]))
        elif cmd_lower == "todo":
            print("Usage: todo add|list|done N|remove N|clear")
        elif cmd_lower.startswith("remind "):
            print(cmd_remind(cmd_lower[7:]))
        elif cmd_lower == "remind":
            print("Usage: remind <seconds> <message>")
    elif cmd.startswith("help_") or cmd.startswith("explain") or cmd.startswith("whatis"):
        topic = cmd.split(None, 1)[1] if " " in cmd else ""
        print(cmd_help_detail(topic))
    elif cmd in ("system_info","list_users","toggle_debug","featured_joke","vip_fact","vip_quote"):
        if debug_mode:
            print("Access denied. Debug mode active but role insufficient.")
        else:
            print("Access denied. You need a higher role.")
    elif cmd == "debug_functions" and debug_mode:
        funcs = [k for k in dir() if not k.startswith('_')]
        print("Functions in scope: {}".format(len(funcs)))
        for f in sorted(funcs)[:50]:
            print("  ", f)
        if len(funcs) > 50:
            print("  ... and {} more".format(len(funcs)-50))
    elif cmd == "debug_vars" and debug_mode:
        print("debug_mode:", debug_mode)
        print("role:", role if 'role' in locals() else 'N/A')
    elif cmd == "debug_cmd_count" and debug_mode:
        print("Total command bindings: 2665+")
    elif cmd == "debug_exec" and debug_mode:
        _plist = getattr(HB, "_prList", {}) or {}
        _ppr = getattr(HB, "_pprList", {}) or {}
        _hbpe_progs = {}
        for _k in _plist:
            if isinstance(_k, int):
                _hbpe_progs[str(_k)] = _k
        for _k in _ppr:
            _hbpe_progs["p{}".format(_k)] = ("p", _k)
        print("Debug/Dev console. Type 'h' for commands, 'stop' to exit.")
        while True:
            try:
                _line = input(">>> ")
                _lower = _line.strip().lower()
                if _lower == "stop":
                    print("Exiting debug console.")
                    break
                if _lower in ("h","help","commands"):
                    print("=== DEBUG CONSOLE COMMANDS ===")
                    print("Python code      - Any expression or statement")
                    print("1-{}, P1-P{}    - Run HBPE program".format(
                        max((k for k in _plist if isinstance(k, int)), default=0),
                        max(_ppr.keys(), default=0)))
                    print("AI.py commands  - Any AI.py command number or name")
                    print("stop             - Exit console")
                    print("h, help, commands - This screen")
                elif _lower in _hbpe_progs:
                    _prog = _hbpe_progs[_lower]
                    if isinstance(_prog, tuple) and _prog[0] == "p":
                        if _prog[1] in _ppr:
                            _ppr[_prog[1]]()
                        else:
                            print("HBPE program P{} not available.".format(_prog[1]))
                    elif isinstance(_prog, int) and _prog in _plist:
                        _plist[_prog]()
                    else:
                        print("HBPE program {} not available.".format(_lower))
                elif _lower != "debug_exec" and handle_cmd(_lower, role, name, badge):
                    pass
                else:
                    try:
                        _result = eval(_line)
                        if _result is not None:
                            print(_result)
                    except SyntaxError:
                        exec(_line)
            except Exception as _ex:
                print("Error:", _ex)
    elif cmd in ("debug_functions","debug_vars","debug_cmd_count","debug_exec"):
        print("Debug commands require debug mode. Use 'toggle_debug' as Admin first.")
    elif cmd == "1":
        print("{} {}!".format(get_time_greeting(), name))
    elif cmd == "4":
        print(draw_diamond(7))
    elif cmd == "5":
        print(draw_tree(7))
    elif cmd == "7":
        print(draw_star(5))
    elif cmd == "18":
        seq = fibonacci(100)
        print("Fibonacci: {}".format(", ".join(str(x) for x in seq)))
    elif cmd == "19":
        try:
            n = int(input("Number: "))
            print("{} is {}prime.".format(n, "" if is_prime(n) else "not "))
        except:
            print("Not valid.")
    elif cmd == "20":
        try:
            n = int(input("Number: "))
            f = factorial(n)
            print("{}! = {}".format(n, f) if f else "Undefined.")
        except:
            print("Not valid.")
    elif cmd == "21":
        try:
            a, b = int(input("A: ")), int(input("B: "))
            print("GCD({},{}) = {}".format(a, b, gcd(a, b)))
        except:
            print("Not valid.")
    elif cmd == "22":
        try:
            a, b = int(input("A: ")), int(input("B: "))
            print("LCM({},{}) = {}".format(a, b, lcm(a, b)))
        except:
            print("Not valid.")
    elif cmd == "23":
        try:
            n = int(input("Number: "))
            print("Prime factors: {}".format(prime_factors(n)))
        except:
            print("Not valid.")
    elif cmd == "24":
        text = input("Text: ")
        w, v, c, d, s, sp, rev = analyze(text)
        print("Words:{} Vowels:{} Consonants:{} Digits:{} Spaces:{} Special:{}".format(w,v,c,d,s,sp))
        print("Reversed: {}".format(rev))
    elif cmd == "25":
        try:
            n = int(input("Number: "))
            print("Binary: {}".format(to_binary(n)))
        except:
            print("Not valid.")
    elif cmd == "26":
        try:
            n = int(input("Number: "))
            print("Hex: {}".format(to_hex(n)))
        except:
            print("Not valid.")
    elif cmd == "27":
        try:
            n = int(input("Number: "))
            print("Octal: {}".format(to_octal(n)))
        except:
            print("Not valid.")
    elif cmd == "28":
        try:
            n = int(input("Number (1-3999): "))
            print("Roman: {}".format(to_roman(n)))
        except:
            print("Not valid.")
    elif cmd == "29":
        try:
            v = float(input("Value: "))
            t = input("C to F or F to C? ").lower()
            if t == "c to f":
                print("{} F".format(celsius_to_fahrenheit(v)))
            elif t == "f to c":
                print("{} C".format(fahrenheit_to_celsius(v)))
            else:
                print("Say 'C to F' or 'F to C'")
        except:
            print("Not valid.")
    elif cmd == "30":
        try:
            v = float(input("Value: "))
            t = input("km to miles or miles to km? ").lower()
            if "km" in t:
                print("{:.3f} miles".format(km_to_miles(v)))
            else:
                print("{:.3f} km".format(miles_to_km(v)))
        except:
            print("Not valid.")
    elif cmd == "31":
        try:
            v = float(input("Value: "))
            t = input("kg to lbs or lbs to kg? ").lower()
            if "kg" in t:
                print("{:.3f} lbs".format(kg_to_pounds(v)))
            else:
                print("{:.3f} kg".format(pounds_to_kg(v)))
        except:
            print("Not valid.")
    elif cmd == "32":
        try:
            n = int(input("Length (default 16): ") or 16)
            print("Password: {}".format(generate_password(n)))
        except:
            print("Not valid.")
    elif cmd == "33":
        pw = input("Enter a password: ")
        print("Strength: {}".format(password_strength(pw)))
    elif cmd == "34":
        text = input("Text: ")
        print("Pig Latin: {}".format(pig_latin(text)))
    elif cmd == "35":
        guess_number()
    elif cmd == "36":
        hangman()
    elif cmd == "37":
        scramble_word()
    elif cmd == "38":
        riddle_game()
    elif cmd == "39":
        trivia_quiz()
    elif cmd == "40":
        q = input("Ask the Magic 8 Ball: ")
        print(magic_8_ball())
    elif cmd == "41":
        text = input("Text: ")
        try:
            s = int(input("Shift: "))
            print("Encoded: {}".format(caesar_cipher(text, s)))
            print("Decoded: {}".format(caesar_cipher(text, -s)))
        except:
            print("Not valid.")
    elif cmd == "42":
        text = input("Text: ")
        print("Palindrome: {}".format("Yes" if is_palindrome(text) else "No"))
    elif cmd == "43":
        a = input("First: ")
        b = input("Second: ")
        print("Anagram: {}".format("Yes" if is_anagram(a, b) else "No"))
    elif cmd == "44":
        try:
            h = float(input("Height (m): "))
            w = float(input("Weight (kg): "))
            bmi = w / (h * h)
            print("BMI: {:.2f} - {}".format(bmi, bmi_category(bmi)))
        except:
            print("Not valid.")
    elif cmd == "45":
        try:
            m = int(input("Month (1-12): "))
            d = int(input("Day: "))
            print("Zodiac: {}".format(zodiac_sign(m, d)))
        except:
            print("Not valid.")
    elif cmd == "46":
        text = input("Text: ")
        print(to_morse(text))
    elif cmd == "47":
        try:
            y = int(input("Year: "))
            m = int(input("Month: "))
            d = int(input("Day: "))
            print(day_of_week(y, m, d))
        except:
            print("Not valid.")
    elif cmd == "48":
        try:
            y = int(input("Year: "))
            print("Leap year: {}".format("Yes" if is_leap_year(y) else "No"))
        except:
            print("Not valid.")
    elif cmd == "49":
        try:
            n = int(input("Number: "))
            print(multiplication_table(n))
        except:
            print("Not valid.")
    elif cmd == "50":
        for i in range(0, 101, 10):
            print(progress_bar(i, 100))
            import time
            time.sleep(0.1)
    elif cmd == "51":
        try:
            s = int(input("Seconds: "))
            countdown(s)
        except:
            print("Not valid.")
    elif cmd == "54":
        try:
            n = int(input("How many dice? "))
            s = int(input("Sides (6): ") or 6)
            rolls = roll_multiple(n, s)
            print("Rolls: {}".format(rolls))
            print("Sum: {}".format(sum(rolls)))
        except:
            print("Not valid.")
    elif cmd == "56":
        high_low()
    elif cmd == "57":
        rock_paper_scissors()
    elif cmd == "58":
        todo_manager()
    elif cmd == "59":
        show_calendar()
    elif cmd == "60":
        simple_calculator()
    elif cmd == "61":
        try:
            nums = [float(x) for x in input("Enter numbers separated by space: ").split()]
            print("Mean: {:.4f}".format(mean(nums)))
            print("Median: {:.4f}".format(median(nums)))
            print("Mode: {}".format(mode(nums)))
        except:
            print("Not valid.")
    elif cmd == "62":
        try:
            nums = [float(x) for x in input("Numbers: ").split()]
            print("Std Dev: {:.4f}".format(standard_deviation(nums)))
        except:
            print("Not valid.")
    elif cmd == "63":
        try:
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            print(solve_quadratic(a, b, c))
        except:
            print("Not valid.")
    elif cmd == "64":
        bubble_sort_demo()
    elif cmd == "65":
        binary_search_demo()
    elif cmd == "66":
        typing_speed()
    elif cmd == "73":
        name, sym, num = random_element()
        print("{} ({}) - Atomic #{}".format(name, sym, num))
    elif cmd == "76":
        print(draw_pyramid(7))
    elif cmd == "77":
        print(draw_triangle(7))
    elif cmd == "78":
        print(draw_reverse_triangle(7))
    elif cmd == "79":
        print(draw_hourglass(5))
    elif cmd == "80":
        print(draw_circle(5))
    elif cmd == "97":
        print(draw_arrow_up(7))
    elif cmd == "98":
        print(draw_arrow_down(7))
    elif cmd == "99":
        print(draw_arrow_left(5))
    elif cmd == "100":
        print(draw_arrow_right(5))
    elif cmd == "103":
        print(draw_bowtie(5))
    elif cmd == "104":
        print(draw_flag(5))
    elif cmd == "105":
        print(draw_stairs(5))
    elif cmd == "106":
        print(draw_table(3))
    elif cmd == "120":
        try:
            s = int(input("Seconds: "))
            print(convert_seconds(s))
        except:
            print("Not valid.")
    elif cmd == "121":
        try:
            n = int(input("Size: ") or 10)
            print(generate_random_data(n))
        except:
            print("Not valid.")
    elif cmd == "122":
        items = input("Items (space separated): ").split()
        print("Shuffled: {}".format(random_shuffle_list(items)))
    elif cmd == "123":
        try:
            lst = eval(input("Nested list: "))
            print(flatten_list(lst))
        except:
            print("Not valid.")
    elif cmd == "124":
        try:
            lst = input("Items: ").split()
            size = int(input("Chunk size: "))
            print(chunk_list(lst, size))
        except:
            print("Not valid.")
    elif cmd == "125":
        items = input("Items: ").split()
        print(unique_elements(items))
    elif cmd == "126":
        a = input("List A: ").split()
        b = input("List B: ").split()
        print(list_intersection(a, b))
    elif cmd == "127":
        a = input("List A: ").split()
        b = input("List B: ").split()
        print(list_union(a, b))
    elif cmd == "128":
        a = input("List A: ").split()
        b = input("List B: ").split()
        print(list_difference(a, b))
    elif cmd == "129":
        a = input("List A: ").split()
        b = input("List B: ").split()
        print(list_symmetric_difference(a, b))
    elif cmd == "130":
        try:
            lst = input("List: ").split()
            n = int(input("Rotate by: "))
            print(rotate_list(lst, n))
        except:
            print("Not valid.")
    elif cmd == "131":
        try:
            lst = input("List: ").split()
            val = input("Value: ")
            print(find_all_indexes(lst, val))
        except:
            print("Not valid.")
    elif cmd == "132":
        try:
            nums = [int(x) for x in input("Numbers: ").split()]
            e, o = split_evens_odds(nums)
            print("Evens: {} Odds: {}".format(e, o))
        except:
            print("Not valid.")
    elif cmd == "133":
        try:
            n = int(input("Number: "))
            print("Sum digits: {}".format(sum_digits(n)))
        except:
            print("Not valid.")
    elif cmd == "134":
        try:
            n = int(input("Number: "))
            print("Reversed: {}".format(reverse_number(n)))
        except:
            print("Not valid.")
    elif cmd == "135":
        try:
            n = int(input("Number: "))
            print("Armstrong: {}".format("Yes" if is_armstrong(n) else "No"))
        except:
            print("Not valid.")
    elif cmd == "136":
        try:
            n = int(input("Number: "))
            print("Perfect: {}".format("Yes" if is_perfect_number(n) else "No"))
        except:
            print("Not valid.")
    elif cmd == "137":
        try:
            n = int(input("Number: "))
            print("Happy: {}".format("Yes" if is_happy_number(n) else "No"))
        except:
            print("Not valid.")
    elif cmd == "138":
        try:
            n = int(input("Number: "))
            print(collatz_sequence(n))
        except:
            print("Not valid.")
    elif cmd == "139":
        try:
            n = int(input("Up to: "))
            primes = sieve_of_eratosthenes(n)
            print("Primes up to {}: {}".format(n, primes))
        except:
            print("Not valid.")
    elif cmd == "140":
        try:
            n = int(input("Which prime (nth): "))
            print("Prime #{}: {}".format(n, nth_prime(n)))
        except:
            print("Not valid.")
    elif cmd == "141":
        try:
            n = int(input("Even number > 2: "))
            print(goldbach_conjecture(n))
        except:
            print("Not valid.")
    elif cmd == "142":
        try:
            n = int(input("Number: "))
            print("Euler totient: {}".format(euler_totient(n)))
        except:
            print("Not valid.")
    elif cmd == "143":
        try:
            a, b = int(input("A: ")), int(input("B: "))
            g, x, y = extended_gcd(a, b)
            print("GCD = {} ({}*{} + {}*{})".format(g, a, x, b, y))
        except:
            print("Not valid.")
    elif cmd == "144":
        try:
            a = int(input("Number: "))
            m = int(input("Modulus: "))
            inv = modular_inverse(a, m)
            if inv:
                print("Inverse: {}".format(inv))
            else:
                print("No inverse exists.")
        except:
            print("Not valid.")
    elif cmd == "145":
        try:
            a = eval(input("Matrix A: "))
            b = eval(input("Matrix B: "))
            print(matrix_multiply(a, b))
        except:
            print("Not valid.")
    elif cmd == "146":
        try:
            m = eval(input("Matrix: "))
            print(matrix_transpose(m))
        except:
            print("Not valid.")
    elif cmd == "147":
        try:
            m = eval(input("Matrix: "))
            print("Determinant: {}".format(matrix_determinant(m)))
        except:
            print("Not valid.")
    elif cmd == "148":
        try:
            a = [float(x) for x in input("Vector A: ").split()]
            b = [float(x) for x in input("Vector B: ").split()]
            print("Dot product: {}".format(dot_product(a, b)))
        except:
            print("Not valid.")
    elif cmd == "149":
        try:
            a = [float(x) for x in input("Vector A (3D): ").split()]
            b = [float(x) for x in input("Vector B (3D): ").split()]
            print("Cross product: {}".format(cross_product(a, b)))
        except:
            print("Not valid.")
    elif cmd == "150":
        try:
            v = [float(x) for x in input("Vector: ").split()]
            print("Magnitude: {:.4f}".format(vector_magnitude(v)))
        except:
            print("Not valid.")
    elif cmd == "151":
        try:
            p1 = [float(x) for x in input("Point 1: ").split()]
            p2 = [float(x) for x in input("Point 2: ").split()]
            print("Euclidean dist: {:.4f}".format(euclidean_distance(p1, p2)))
        except:
            print("Not valid.")
    elif cmd == "152":
        try:
            p1 = [float(x) for x in input("Point 1: ").split()]
            p2 = [float(x) for x in input("Point 2: ").split()]
            print("Manhattan dist: {:.4f}".format(manhattan_distance(p1, p2)))
        except:
            print("Not valid.")
    elif cmd == "153":
        s1 = input("String 1: ")
        s2 = input("String 2: ")
        d = hamming_distance(s1, s2)
        if d == -1:
            print("Strings must be equal length.")
        else:
            print("Hamming dist: {}".format(d))
    elif cmd == "154":
        s1 = input("String 1: ")
        s2 = input("String 2: ")
        print("Levenshtein dist: {}".format(levenshtein_distance(s1, s2)))
    elif cmd == "155":
        try:
            n = int(input("Number: "))
            b = int(input("Base (2-36): "))
            print("Result: {}".format(to_base(n, b)))
        except:
            print("Not valid.")
    elif cmd == "156":
        text = input("Text: ")
        print(sha256_hash(text))
    elif cmd == "157":
        text = input("Text: ")
        print(md5_hash(text))
    elif cmd == "158":
        text = input("Text: ")
        print(base64_encode(text))
    elif cmd == "159":
        text = input("Base64: ")
        print(base64_decode(text))
    elif cmd == "160":
        text = input("Text: ")
        print("ROT13: {}".format(rot13(text)))
    elif cmd == "161":
        text = input("Text: ")
        print(text_to_ascii(text))
    elif cmd == "162":
        try:
            codes = [int(x) for x in input("ASCII codes: ").split()]
            print(ascii_to_text(codes))
        except:
            print("Not valid.")
    elif cmd == "163":
        text = input("Text: ")
        print("Words: {}".format(count_words(text)))
    elif cmd == "164":
        text = input("Text: ")
        print("Sentences: {}".format(count_sentences(text)))
    elif cmd == "165":
        text = input("Text: ")
        print("Paragraphs: {}".format(count_paragraphs(text)))
    elif cmd == "166":
        text = input("Text: ")
        print("Result: {}".format(remove_duplicate_words(text)))
    elif cmd == "167":
        text = input("Text: ")
        print("Reversed: {}".format(reverse_words(text)))
    elif cmd == "168":
        text = input("Text: ")
        print("Sorted: {}".format(sort_words(text)))
    elif cmd == "169":
        text = input("Text: ")
        print("Shuffled: {}".format(shuffle_words(text)))
    elif cmd == "170":
        text = input("Text: ")
        print("Acronym: {}".format(acronym(text)))
    elif cmd == "171":
        text = input("Text: ")
        print("Title: {}".format(capitalize_title(text)))
    elif cmd == "172":
        text = input("Text: ")
        print("Language: {}".format(detect_language(text)))
    elif cmd == "173":
        text = input("Text: ")
        bad = spell_check(text)
        if bad:
            print("Possible errors: {}".format(bad[:10]))
        else:
            print("All words look correct.")
    elif cmd == "174":
        text = input("Text: ")
        freq = word_frequency(text)
        for w, c in list(freq.items())[:15]:
            print("  {}: {}".format(w, c))
    elif cmd == "175":
        text = input("Text: ")
        print("Longest: {}".format(longest_word(text)))
    elif cmd == "176":
        text = input("Text: ")
        print("Shortest: {}".format(shortest_word(text)))
    elif cmd == "177":
        text = input("Text: ")
        letter, count = most_common_letter(text)
        print("Most common: '{}' ({} times)".format(letter, count))
    elif cmd == "178":
        text = input("Text: ")
        print("Has URL: {}".format("Yes" if has_url(text) else "No"))
    elif cmd == "179":
        text = input("Text: ")
        print("Has email: {}".format("Yes" if has_email(text) else "No"))
    elif cmd == "180":
        text = input("Text: ")
        print("Numbers: {}".format(extract_numbers(text)))
    elif cmd == "181":
        text = input("Text: ")
        print("Emails: {}".format(extract_emails(text)))
    elif cmd == "182":
        text = input("Text: ")
        print("URLs: {}".format(extract_urls(text)))
    elif cmd == "183":
        text = input("HTML: ")
        print("Text: {}".format(remove_html_tags(text)))
    elif cmd == "184":
        text = input("Text: ")
        print("Censored: {}".format(censor_bad_words(text)))
    elif cmd == "185":
        text = input("Text: ")
        print(suggest_emoji(text))
    elif cmd == "186":
        data = input("JSON: ")
        print(format_json(data))
    elif cmd == "187":
        data = input("JSON: ")
        print("Elements: {}".format(count_json_elements(data)))
    elif cmd == "188":
        csv_text = input("CSV: ")
        result = csv_to_list(csv_text)
        for row in result[:5]:
            print(row)
    elif cmd == "189":
        try:
            n = int(input("Rolls: ") or 1000)
            s = int(input("Sides: ") or 6)
            counts = simulate_dice_rolls(n, s)
            print(counts)
        except:
            print("Not valid.")
    elif cmd == "190":
        try:
            n = int(input("Flips: ") or 1000)
            heads, tails = simulate_coin_flips(n)
            print("Heads: {} Tails: {}".format(heads, tails))
        except:
            print("Not valid.")
    elif cmd == "191":
        print("Lottery numbers: {}".format(simulate_lottery()))
    elif cmd == "192":
        try:
            n = int(input("People: ") or 23)
            t = int(input("Trials: ") or 10000)
            pct = birthday_paradox(n, t)
            print("Probability of shared birthday: {:.1f}%".format(pct))
        except:
            print("Not valid.")
    elif cmd == "193":
        try:
            t = int(input("Trials: ") or 10000)
            stick, switch = monty_hall_simulation(t)
            print("Stick win: {:.1f}% Switch win: {:.1f}%".format(stick, switch))
        except:
            print("Not valid.")
    elif cmd == "194":
        code = input("Morse: ")
        print(morse_to_text(code))
    elif cmd == "195":
        text = input("Text: ")
        print("Atbash: {}".format(atbash_cipher(text)))
    elif cmd == "196":
        text = input("Text: ")
        key = input("Key: ")
        print("Vigenere: {}".format(vigenere_cipher(text, key)))
    elif cmd == "197":
        text = input("Text: ")
        key = input("Key: ")
        print("XOR: {}".format(xor_cipher(text, key)))
    elif cmd == "198":
        text = input("Text: ")
        print("Substitution with sample key...")
        print("(Try later)")
    elif cmd == "199":
        print("Nerd dice: {}".format(generate_nerd_dice()))
    elif cmd == "200":
        hand = poker_hand()
        print("Poker hand: {}".format(["{} of {}".format(r, s) for r, s in hand]))
    elif cmd == "201":
        try:
            n = int(input("Limit: ") or 50)
            print(format_goldbach(n))
        except:
            print("Not valid.")
    elif cmd == "202":
        try:
            n = int(input("Number: "))
            print(show_number_facts(n))
        except:
            print("Not valid.")
    elif cmd == "203":
        try:
            c = float(input("Celsius: "))
            print(temperature_summary(c))
        except:
            print("Not valid.")
    elif cmd == "204":
        try:
            m = int(input("Birth month: "))
            d = int(input("Birth day: "))
            print(time_until_birthday(m, d))
        except:
            print("Not valid.")
    elif cmd == "205":
        try:
            y = int(input("Birth year: "))
            m = int(input("Birth month: "))
            d = int(input("Birth day: "))
            print(days_since_birth(y, m, d))
        except:
            print("Not valid.")
    elif cmd == "206":
        try:
            y = int(input("Birth year: "))
            m = int(input("Birth month: "))
            d = int(input("Birth day: "))
            print(age_in_seconds(y, m, d))
        except:
            print("Not valid.")
    elif cmd == "212":
        sign = input("Your zodiac sign: ")
        print(astrology_horoscope(sign))
    elif cmd == "213":
        try:
            n = int(input("Your birth number: "))
            print(numerology(n))
        except:
            print("Not valid.")
    elif cmd == "214":
        try:
            y = int(input("Birth year: "))
            print(chinese_zodiac(y))
        except:
            print("Not valid.")
    elif cmd == "230":
        bmi_calculator()
    elif cmd == "231":
        tip_calculator()
    elif cmd == "232":
        loan_calculator()
    elif cmd == "233":
        savings_calculator()
    elif cmd == "234":
        unit_converter()
    elif cmd == "235":
        discount_calculator()
    elif cmd == "236":
        currency_converter()
    elif cmd == "242":
        number2 = random.randint(1, 50)
        print("Guess a number between 1 and 50.")
        for _ in range(5):
            try:
                g = int(input("Guess: "))
                if g == number2:
                    print("Correct!"); break
                print("Too high!" if g > number2 else "Too low!")
            except:
                print("Invalid.")
        print("Number was: {}".format(number2))
    elif cmd == "243":
        print("Guess the color: {}".format(random_color()))
    elif cmd == "244":
        print("Guess the fruit: {}".format(random_fruit()))
    elif cmd == "245":
        print("Guess the animal: {}".format(random_animal()))
    elif cmd == "246":
        print("Guess the country: {}".format(show_country_info()))
    elif cmd == "247":
        print("Random emoji: {}".format(random.choice(["😊","😂","❤️","🔥","👍","🎉","✨","💪","🐱","🐶","🌺","🍕","🚀","⭐","🌙","☀️","🌈","🎵","💻","🍀"])))
    elif cmd == "248":
        planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
        print("Random planet: {}".format(random.choice(planets)))
    elif cmd == "249":
        galaxies = ["Milky Way","Andromeda","Triangulum","Whirlpool","Sombrero","Pinwheel","Cartwheel","Black Eye","Cigar","Tadpole"]
        print("Random galaxy: {}".format(random.choice(galaxies)))
    elif cmd == "250":
        stars = ["Sun","Sirius","Betelgeuse","Rigel","Vega","Polaris","Alpha Centauri","Proxima","Antares","Aldebaran","Capella","Deneb"]
        print("Random star: {}".format(random.choice(stars)))
    elif cmd == "251":
        asteroids = ["Ceres","Vesta","Pallas","Hygiea","Eros","Itokawa","Bennu","Ryugu","Davida","Interamnia"]
        print("Random asteroid: {}".format(random.choice(asteroids)))
    elif cmd == "252":
        comets = ["Halley","Hale-Bopp","Shoemaker-Levy 9","Hyakutake","Neowise","Lovejoy","ISON","Encke","Tempel 1","Wild 2"]
        print("Random comet: {}".format(random.choice(comets)))
    elif cmd == "253":
        nebulaes = ["Orion","Eagle","Crab","Ring","Horsehead","Cat's Eye","Helix","Tarantula","Carina","Veil"]
        print("Random nebula: {}".format(random.choice(nebulaes)))
    elif cmd == "254":
        quasars = ["3C 273","3C 48","QSO J0313-1806","PKS 1302-102","APM 08279+5255","BR 1202-0725","SDSS J0100+2802","ULAS J1120+0641","PC 1247+3406","TON 618"]
        print("Random quasar: {}".format(random.choice(quasars)))
    elif cmd == "255":
        black_holes = ["Sagittarius A*","M87*","Cygnus X-1","TON 618","Holmberg 15A","IC 1101","Phoenix A","SDSS J140821","HLX-1","LB-1"]
        print("Random black hole: {}".format(random.choice(black_holes)))
    elif cmd == "256":
        quiz_capital_cities()
    elif cmd == "257":
        quiz_flags()
    elif cmd == "258":
        quiz_math()
    elif cmd == "259":
        quiz_science()
    elif cmd == "260":
        quiz_history()
    elif cmd == "261":
        quiz_geography()
    elif cmd == "262":
        quiz_programming()
    elif cmd == "264":
        print("Constellation: {}".format(random_constellation()))
    elif cmd == "265":
        print("Dinosaur: {}".format(random_dinosaur()))
    elif cmd == "266":
        print("Flower: {}".format(random_flower()))
    elif cmd == "267":
        print("Gemstone: {}".format(random_gemstone()))
    elif cmd == "268":
        print("Mythical creature: {}".format(random_mythical_creature()))
    elif cmd == "269":
        print("Planet type: {}".format(random_planet_type()))
    elif cmd == "270":
        print("Reaction: {}".format(random_chemical_reaction()))
    elif cmd == "275":
        try:
            w = float(input("Your weight in kg: "))
            print(space_data.planet_weight(w))
        except: print("Invalid.")
    elif cmd == "276":
        try:
            a = float(input("Your age in years: "))
            print(space_data.solar_system_age(a))
        except: print("Invalid.")
    elif cmd == "277":
        print(space_data.space_distance_scale())
    elif cmd == "278":
        print(space_data.apollo_missions())
    elif cmd == "279":
        print(space_data.rocket_facts())
    elif cmd == "280":
        print(space_data.mars_facts())
    elif cmd == "281":
        print(space_data.jupiter_facts())
    elif cmd == "282":
        print(space_data.deep_space_fact())
    elif cmd == "283":
        print("Moon: {}".format(space_data.random_moon()))
    elif cmd == "284":
        print("Exoplanet: {}".format(space_data.random_exoplanet()))
    elif cmd == "285":
        print(space_data.astronauts_on_iss())
    elif cmd == "286":
        print(space_data.asteroid_belt_fact())
    elif cmd == "287":
        mini_games.tic_tac_toe()
    elif cmd == "288":
        mini_games.connect_four()
    elif cmd == "289":
        mini_games.word_search_puzzle()
    elif cmd == "290":
        mini_games.number_puzzle()
    elif cmd == "291":
        mini_games.memory_challenge()
    elif cmd == "292":
        mini_games.reaction_game()
    elif cmd == "293":
        mini_games.guess_the_number_advanced()
    elif cmd == "294":
        mini_games.word_association()
    elif cmd == "295":
        mini_games.rapid_math()
    elif cmd == "296":
        trivia_pack.movie_trivia()
    elif cmd == "297":
        trivia_pack.music_trivia()
    elif cmd == "298":
        trivia_pack.sports_trivia()
    elif cmd == "299":
        trivia_pack.art_trivia()
    elif cmd == "300":
        trivia_pack.food_trivia()
    elif cmd == "301":
        trivia_pack.animal_trivia()
    elif cmd == "302":
        trivia_pack.tech_trivia()
    elif cmd == "303":
        trivia_pack.nature_trivia()
    elif cmd == "304":
        print(trivia_pack.random_trivia_fact())
    elif cmd == "305":
        print(word_play.random_sentence())
    elif cmd == "306":
        print(word_play.random_poem())
    elif cmd == "307":
        print(word_play.random_haiku())
    elif cmd == "308":
        print(word_play.random_tongue_twister())
    elif cmd == "309":
        print(word_play.random_proverb())
    elif cmd == "310":
        print(word_play.random_idiom())
    elif cmd == "311":
        print(word_play.random_simile())
    elif cmd == "312":
        print(word_play.random_metaphor())
    elif cmd == "313":
        print(word_play.random_oxymoron())
    elif cmd == "314":
        print("Palindrome word: {}".format(word_play.random_palindrome_word()))
    elif cmd == "315":
        w = input("Enter a word: ")
        print("Anagram: {}".format(word_play.anagram_generator(w)))
    elif cmd == "316":
        try:
            n = int(input("Size (4-12): ") or 8)
            print(art_extra.draw_chessboard(min(n, 12)))
        except: print("Invalid.")
    elif cmd == "317":
        print(art_extra.draw_sierpinski(4))
    elif cmd == "318":
        print(art_extra.draw_radial_star(5))
    elif cmd == "319":
        print(art_extra.draw_spiral(12))
    elif cmd == "320":
        print(art_extra.draw_maze())
    elif cmd == "321":
        print(art_extra.draw_target(5))
    elif cmd == "322":
        print(art_extra.draw_snowflake(5))
    elif cmd == "323":
        print(art_extra.draw_fractal_tree(3))
    elif cmd == "324":
        print(art_extra.draw_flower_garden())
    elif cmd == "325":
        print(art_extra.draw_cross())
    elif cmd == "326":
        print(art_extra.draw_fence(4))
    elif cmd == "327":
        print(art_extra.draw_railroad())
    elif cmd == "328":
        print(art_extra.draw_tunnel())
    elif cmd == "329":
        print(art_extra.draw_lighthouse())
    elif cmd == "330":
        print(art_extra.draw_rocket())
    elif cmd == "331":
        print(art_extra.draw_submarine())
    elif cmd == "332":
        print(art_extra.draw_helicopter())
    elif cmd == "333":
        print(art_extra.draw_airplane())
    elif cmd == "334":
        print(art_extra.draw_bicycle())
    elif cmd == "335":
        print(art_extra.draw_umbrella())
    elif cmd == "336":
        print(art_extra.draw_compass())
    elif cmd == "337":
        print(art_extra.draw_web())
    elif cmd == "338":
        print(art_extra.draw_bridge())
    elif cmd == "339":
        print(art_extra.draw_castle_tower())
    elif cmd == "340":
        print(art_extra.draw_sword())
    elif cmd == "341":
        print(art_extra.draw_shield())
    elif cmd == "342":
        print(art_extra.draw_anchor())
    elif cmd == "343":
        print(art_extra.draw_crown_king())
    elif cmd == "344":
        print(art_extra.draw_throne())
    elif cmd == "345":
        if role:
            ra_level = {"Admin": 3, "Mod": 2, "Vip": 1}.get(role, 0)
            print("--- HubBasePE v{} (AI.py integrated) ---".format(HB.HBPE_VERSION))
            print("Auto-login as {} (RA={})...".format(role, ra_level))
            global RA
            RA = ra_level
        HB.VipAccess = "T"
        HB.PassGuess = "5280"
        HB.Login = role if role else "user"
        print("Launching HubBasePE...")
        HB.Code()
    elif cmd == "346":
        print(world_data.random_country())
    elif cmd == "347":
        print(world_data.country_by_continent())
    elif cmd == "348":
        print(world_data.world_population())
    elif cmd == "349":
        print(world_data.largest_cities())
    elif cmd == "350":
        print(world_data.world_rivers())
    elif cmd == "351":
        print(world_data.world_mountains())
    elif cmd == "352":
        print(world_data.world_deserts())
    elif cmd == "353":
        print(world_data.world_islands())
    elif cmd == "354":
        print(world_data.world_lakes())
    elif cmd == "355":
        print(world_data.world_wonders())
    elif cmd == "356":
        print(world_data.world_currencies())
    elif cmd == "357":
        print(world_data.random_flag_description())
    elif cmd == "358":
        print(story_data.generate_story())
    elif cmd == "359":
        print(story_data.random_joke_theme("programming"))
    elif cmd == "360":
        print(story_data.random_joke_theme("animal"))
    elif cmd == "361":
        print(story_data.random_joke_theme("food"))
    elif cmd == "362":
        print(story_data.random_joke_theme("science"))
    elif cmd == "363":
        print(story_data.random_joke_theme("sports"))
    elif cmd == "364":
        print(story_data.random_joke_theme("music"))
    elif cmd == "365":
        print(story_data.random_joke_theme("math"))
    elif cmd == "366":
        print(story_data.random_joke_theme("history"))
    elif cmd == "367":
        print(story_data.random_dad_joke())
    elif cmd == "368":
        print(story_data.random_conversation_starter())
    elif cmd == "369":
        print(story_data.random_philosophical_question())
    elif cmd == "544":
        try:
            _val = input("Circle radius: ") or "0"
            print(calculate_circle_area(float(_val)))
        except Exception as _e:
            print(_e)
    elif cmd == "545":
        try:
            _val = input("Circle radius: ") or "0"
            print(calculate_circle_volume(float(_val)))
        except Exception as _e:
            print(_e)
    elif cmd == "546":
        try:
            _val = input("Circle radius: ") or "0"
            print(calculate_circle_perimeter(float(_val)))
        except Exception as _e:
            print(_e)
    elif cmd == "547":
        try:
            _val = input("Circle radius: ") or "0"
            print(calculate_circle_surface_area(float(_val)))
        except Exception as _e:
            print(_e)
    elif cmd == "548":
        try:
            _val = input("Square side: ") or "0"
            print(calculate_square_area(float(_val)))
        except Exception as _e:
            print(_e)
    elif cmd == "549":
        try:
            _val = input("Square side: ") or "0"
            print(calculate_square_volume(float(_val)))
        except Exception as _e:
            print(_e)
    elif cmd == "550":
        try:
            _val = input("Square side: ") or "0"
            print(calculate_square_perimeter(float(_val)))
        except Exception as _e:
            print(_e)
    elif cmd == "551":
        try:
            _val = input("Square side: ") or "0"
            print(calculate_square_surface_area(float(_val)))
        except Exception as _e:
            print(_e)
    elif cmd == "552":
        try:
            _val = input("Rectangle value: ") or "0"
            print(calculate_rectangle_area(float(_val)))
        except Exception as _e:
            print(_e)
    elif cmd == "553":
        try:
            _val = input("Rectangle value: ") or "0"
            print(calculate_rectangle_volume(float(_val)))
        except Exception as _e:
            print(_e)
    elif cmd == "554":
        try:
            _val = input("Rectangle value: ") or "0"
            print(calculate_rectangle_perimeter(float(_val)))
        except Exception as _e:
            print(_e)
    elif cmd == "555":
        try:
            _val = input("Rectangle value: ") or "0"
            print(calculate_rectangle_surface_area(float(_val)))
        except Exception as _e:
            print(_e)
    elif cmd in ("2658","chart","barchart"):
        try:
            n_str = input("Numbers (comma separated): ")
            nums = [float(x.strip()) for x in n_str.split(",") if x.strip()]
            lab_str = input("Labels (comma separated, optional): ").strip()
            labs = [x.strip() for x in lab_str.split(",")] if lab_str else None
            t = input("Title (optional): ").strip()
            print(ascii_chart(nums, labs, title=t))
        except:
            print("Usage: enter numbers separated by commas.")
    elif cmd in ("2659","suggest","find"):
        p = input("Search term: ").strip()
        print(cmd_suggest(p))
    elif cmd in ("2660","version","ver"):
        print(__version__)
    elif cmd in ("2661","pager_test"):
        pager("\n".join("Line {}".format(i) for i in range(1, 101)))
    elif cmd in ("2662","cls","clear"):
        clear()
    elif cmd in ("2663","colors","color_test"):
        print(C_RED + "RED" + C_RESET, C_GREEN + "GREEN" + C_RESET, C_BLUE + "BLUE" + C_RESET)
        print(C_YELLOW + "YELLOW" + C_RESET, C_MAGENTA + "MAGENTA" + C_RESET, C_CYAN + "CYAN" + C_RESET)
    elif cmd in ("2664","badge","colorbadge"):
        print("Your badge: " + role_badge(role))
    elif cmd in ("2667","help2","categories"):
        help_cat()
    elif cmd in ("2669","timer","countdown"):
        cmd_timer()
    elif cmd in ("2670","stopwatch"):
        cmd_stopwatch()
    elif cmd in ("2671","calc","calculator"):
        cmd_calc()
    elif cmd.startswith('ai '):
        print(aipy_ai.ask(cmd[3:]))
    elif cmd.startswith('ask '):
        print(aipy_ai.ask(cmd[4:]))
    elif cmd == 'ai_train':
        ok = aipy_ai.reload()
        print("AI training {}.".format('loaded' if ok else 'failed - no data'))
    else:
        print("Unknown. Type 'h' for help.")


def _load_config():
    p = os.path.join(_SCRIPT_DIR, "Json", "config.json")
    try:
        with open(p, encoding="utf-8") as f: return json.load(f)
    except: return {}

def _save_config(cfg):
    p = os.path.join(_SCRIPT_DIR, "Json", "config.json")
    try:
        with open(p, "w", encoding="utf-8") as f: json.dump(cfg, f, indent=2)
    except: pass

def main():
    clear()
    cfg = _load_config()
    print(C_CYAN + C_BOLD + "Welcome to AI.py v" + __version__ + "! 4,600+ commands, 5.9M+ lines, 5,300+ data tables, 38 bulk modules, 16 pages." + C_RESET)
    if cfg.get("name"):
        name = cfg["name"]
        print(C_YELLOW + "Welcome back, {}!".format(name) + C_RESET)
        role = cfg.get("role")
        if role:
            print("{} authenticated as {} (saved).".format(name, role))
    else:
        name = input(C_YELLOW + "What's your name? " + C_RESET).strip() or "Stranger"
        cfg["name"] = name
        pw = input("Role password (or press Enter for none): ").strip()
        role = check_role(pw) if pw else None
        if role:
            cfg["role"] = role
            print("{} authenticated as {}!".format(name, role))
            print("You now have access to special commands.")
            extra_cmds = get_role_commands(role)
            if extra_cmds:
                print("Your extra commands: {}".format(", ".join(extra_cmds)))
        _save_config(cfg)

    word, lang = random_greeting()
    badge = role_badge(role)
    print("{} {}, nice to meet you! {}".format(get_time_greeting(), name, badge))
    print("{} means hello in {}!".format(word, lang))
    print("Tip: type 'h' for commands, 'docs' for HTML docs, 'dashboard' for web UI, 'quiz' for knowledge test.\n")
    show_help(role)
    _cmd_history = []
    while True:
        prompt = (C_BOLD + badge + " " + C_CYAN + name + C_RESET + " >> ") if badge else (C_CYAN + name + C_RESET + " >> ")
        cmd = input(prompt).strip()
        lower = cmd.lower()
        if lower == "q":
            badge = role_badge(role)
            msg = "Goodbye {} {}!".format(badge, name) if badge else "Goodbye {}!".format(name)
            print(C_YELLOW + msg + C_RESET)
            break
        if not cmd: continue
        if lower == "history":
            for i, h in enumerate(_cmd_history, 1):
                print("{:4d}: {}".format(i, h))
            continue
        if lower.startswith("!"):
            try:
                n = int(cmd[1:])
                if 1 <= n <= len(_cmd_history):
                    cmd = _cmd_history[n - 1]
                    print("Repeating: {}".format(cmd))
                else:
                    print("No history entry {}.".format(n))
                    continue
            except ValueError:
                print("Usage: !N to repeat command N from history.")
                continue
        _cmd_history.append(cmd)
        handle_cmd(lower, role, name, badge)



from aipy_utils import *

if __name__ == "__main__":
    main()


