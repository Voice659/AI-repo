import time, shutil, json, re, hashlib, base64, os, math, string
from pathlib import Path

def _confirm(msg):
    return input(msg + " (y/n) -- ").lower() == "y"

def _int_input(prompt, default=0, mini=None, maxi=None):
    raw = input(prompt).strip()
    if not raw:
        return default
    try:
        v = int(raw)
        if mini is not None and v < mini:
            print("Value too small, using", mini)
            return mini
        if maxi is not None and v > maxi:
            print("Value too large, using", maxi)
            return maxi
        return v
    except ValueError:
        print("Invalid number, using", default)
        return default

def pylevel_main():
    MaxNumber = 45
    while True:
        time.sleep(0.5)
        print("--- PyLevel v2.0 — Select an action: ---")
        print(" 1. Count occurrences            2. Find first occurrence")
        print(" 3. Find all occurrence positions 4. Check int/float/string")
        print(" 5. Create & write file           6. Read file contents")
        print(" 7. Append to file                8. Check file exists")
        print(" 9. Check directory exists       10. Delete a file")
        print("11. Create directory             12. Delete a directory")
        print("13. Rename file/dir              14. Copy a file")
        print("15. Get full path                16. Get file name from path")
        print("17. Get file extension           18. Get parent directory")
        print("19. List files in directory      20. Generate random password")
        print("21. Caesar cipher                22. Count words in file")
        print("23. Read/format JSON             24. Write JSON")
        print("25. Regex search in file         26. Validate URL")
        print("27. Validate email               28. Text statistics")
        print("29. File size report             30. File hash (MD5/SHA256)")
        print("31. Unix timestamp converter     32. Base64 encode/decode")
        print("33. Directory tree               34. Grep text in files")
        print("35. Simple calculator            36. Random number gen")
        print("37. Palindrome checker           38. System info")
        print("39. HubBase Utility launcher     45. Undo last file operation")
        print("exit or 0. Exit")

        choice = input("Which? -- ").strip().lower()
        if choice in ("exit", "0"):
            print("Exiting PyLevel.")
            time.sleep(0.2)
            break

        # --- helpers for ops 1-3 ---
        if choice in ("1", "2", "3"):
            ms = input("Main String -- ")
            ss = input("Sub String -- ")

        if choice == "1":
            print(ms.count(ss))
        elif choice == "2":
            p = ms.find(ss)
            print(p + 1 if p != -1 else -1)
        elif choice == "3":
            poses, start = [], 0
            while True:
                p = ms.find(ss, start)
                if p == -1:
                    break
                poses.append(p + 1)
                start = p + len(ss)
            print("Positions:", poses)
        elif choice == "4":
            v = input("Enter a word or number -- ")
            try:
                float(v)
                print("Decimal" if "." in v or "e" in v.lower() else "Integer")
            except ValueError:
                print("String")

        # --- file ops ---
        elif choice == "5":
            Path("task5tt7.txt").write_text("Written by task 5.", encoding="utf-8")
            print("File written.")
        elif choice == "6":
            p = Path("task5tt7.txt")
            if not p.exists():
                p.write_text("Created by task 6.", encoding="utf-8")
            print(p.read_text(encoding="utf-8"))
        elif choice == "7":
            with open("task5tt7.txt", "a", encoding="utf-8") as f:
                f.write("Appended by task 7.\n")
            print("Appended.")
        elif choice == "8":
            p = Path(input("File path [task5tt7.txt]: ") or "task5tt7.txt")
            print("Exists" if p.is_file() else "Not found")
        elif choice == "9":
            p = Path(input("Directory path [.]: ") or ".")
            print("Exists" if p.is_dir() else "Not found")
        elif choice == "10":
            p = Path(input("File to delete [task5tt7.txt]: ") or "task5tt7.txt")
            if p.is_file() and _confirm("Delete " + str(p) + "?"):
                p.unlink()
                print("Deleted.")
            else:
                print("Cancelled or not found.")
        elif choice == "11":
            p = Path(input("Dir name [pylevel_dir]: ") or "pylevel_dir")
            p.mkdir(exist_ok=True)
            print("Ready.")
        elif choice == "12":
            p = Path(input("Dir to delete [pylevel_dir]: ") or "pylevel_dir")
            if p.is_dir() and _confirm("Delete " + str(p) + "?"):
                try:
                    p.rmdir()
                    print("Deleted.")
                except OSError:
                    if _confirm("Not empty. Remove all?"):
                        shutil.rmtree(p)
                        print("Deleted recursively.")
            else:
                print("Cancelled.")
        elif choice == "13":
            src = Path(input("Source path [task5tt7.txt]: ") or "task5tt7.txt")
            if not src.exists():
                print("Not found.")
                continue
            dst = Path(input("New name: "))
            if dst.exists() and not _confirm("Overwrite?"):
                print("Cancelled.")
                continue
            src.rename(dst)
            print("Renamed.")
        elif choice == "14":
            src = Path(input("Source file [task5tt7.txt]: ") or "task5tt7.txt")
            if not src.is_file():
                print("Not found.")
                continue
            dst = Path(input("Destination: "))
            if dst.exists() and not _confirm("Overwrite?"):
                print("Cancelled.")
                continue
            shutil.copy(src, dst)
            print("Copied.")
        elif choice == "15":
            p = Path(input("Path [task5tt7.txt]: ") or "task5tt7.txt")
            print(p.resolve())
        elif choice == "16":
            p = Path(input("Path [task5tt7.txt]: ") or "task5tt7.txt")
            print(p.name)
        elif choice == "17":
            p = Path(input("Path [task5tt7.txt]: ") or "task5tt7.txt")
            print(p.suffix if p.suffix else "(no extension)")
        elif choice == "18":
            p = Path(input("Path [task5tt7.txt]: ") or "task5tt7.txt")
            print(p.parent)
        elif choice == "19":
            for item in Path.cwd().iterdir():
                if item.is_file():
                    print(item.name)

        # --- NEW OPS 20-40 ---
        elif choice == "20":
            length = _int_input("Password length [16]: ", 16, 1, 256)
            chars = string.ascii_letters + string.digits + "!@#$%^&*"
            pw = "".join(chars[hashlib.sha256(os.urandom(1) + str(i).encode()).digest()[0] % len(chars)] for i in range(length))
            print("Password:", pw)

        elif choice == "21":
            text = input("Text: ")
            shift = _int_input("Shift [3]: ", 3, 1, 25)
            result = "".join(chr((ord(c) - 97 + shift) % 26 + 97) if c.islower() else chr((ord(c) - 65 + shift) % 26 + 65) if c.isupper() else c for c in text)
            print("Result:", result)

        elif choice == "22":
            p = Path(input("File path [task5tt7.txt]: ") or "task5tt7.txt")
            if p.is_file():
                words = p.read_text(encoding="utf-8").split()
                print("Word count:", len(words))
            else:
                print("File not found.")

        elif choice == "23":
            p = Path(input("JSON file path: "))
            if p.is_file():
                try:
                    data = json.loads(p.read_text(encoding="utf-8"))
                    print(json.dumps(data, indent=2, ensure_ascii=False))
                except Exception as e:
                    print("JSON error:", e)
            else:
                print("File not found.")

        elif choice == "24":
            p = Path(input("Output JSON file path [output.json]: ") or "output.json")
            try:
                raw = input("Python object (dict/list literal): ")
                data = eval(raw, {"__builtins__": {}}, {})
                p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
                print("Written to", p)
            except Exception as e:
                print("Error:", e)

        elif choice == "25":
            p = Path(input("File path: "))
            pat = input("Regex pattern: ")
            if p.is_file():
                try:
                    for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
                        if re.search(pat, line):
                            print("{:4d}: {}".format(i, line))
                except Exception as e:
                    print("Error:", e)
            else:
                print("File not found.")

        elif choice == "26":
            url = input("URL: ")
            pat = r"^https?://[^\s/$.?#].[^\s]*$"
            print("Valid" if re.match(pat, url) else "Invalid")

        elif choice == "27":
            email = input("Email: ")
            pat = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            print("Valid" if re.match(pat, email) else "Invalid")

        elif choice == "28":
            text = input("Text: ")
            print("Chars:", len(text))
            print("Words:", len(text.split()))
            print("Lines:", text.count("\n") + 1)
            print("Paragraphs:", max(1, text.count("\n\n") + 1))

        elif choice == "29":
            p = Path(input("File path [task5tt7.txt]: ") or "task5tt7.txt")
            if p.is_file():
                size = p.stat().st_size
                if size < 1024:
                    print("Size:", size, "B")
                elif size < 1024**2:
                    print("Size:", round(size / 1024, 1), "KB")
                else:
                    print("Size:", round(size / 1024**2, 1), "MB")
            else:
                print("Not found.")

        elif choice == "30":
            p = Path(input("File path [task5tt7.txt]: ") or "task5tt7.txt")
            if p.is_file():
                algo = input("Hash (md5/sha256) [md5]: ").strip().lower() or "md5"
                data = p.read_bytes()
                if algo == "sha256":
                    h = hashlib.sha256(data).hexdigest()
                else:
                    h = hashlib.md5(data).hexdigest()
                print(algo.upper() + ":", h)
            else:
                print("Not found.")

        elif choice == "31":
            raw = input("Unix timestamp (or press Enter for now): ").strip()
            ts = int(raw) if raw else int(time.time())
            print("Timestamp:", ts)
            print("UTC time:", time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime(ts)))
            print("Local:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts)))

        elif choice == "32":
            mode = input("Encode (e) or Decode (d)? [e]: ").strip().lower() or "e"
            data = input("Data: ")
            if mode == "d":
                try:
                    print("Decoded:", base64.b64decode(data).decode("utf-8"))
                except Exception as e:
                    print("Error:", e)
            else:
                print("Encoded:", base64.b64encode(data.encode()).decode())

        elif choice == "33":
            p = Path(input("Directory path [.]: ") or ".")
            prefix = input("Prefix string: ")
            def _walk(d, depth=0):
                for item in sorted(d.iterdir()):
                    print(prefix + "  " * depth + ("[DIR] " if item.is_dir() else "[FILE] ") + item.name)
                    if item.is_dir():
                        _walk(item, depth + 1)
            _walk(p)

        elif choice == "34":
            p = Path(input("Directory to search [.]: ") or ".")
            pat = input("Text/regex to find: ")
            ext = input("File extension filter (optional, e.g. .py): ").strip()
            found = 0
            for item in p.rglob("*"):
                if item.is_file() and (not ext or item.suffix == ext):
                    try:
                        for i, line in enumerate(item.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
                            if re.search(pat, line):
                                print("{}:{}: {}".format(item, i, line.strip()))
                                found += 1
                    except Exception:
                        pass
            print("--- {} matches ---".format(found))

        elif choice == "35":
            print("Simple calculator. Type expressions like 2+2, or 'q' to quit.")
            while True:
                expr = input("calc> ").strip()
                if expr.lower() == "q":
                    break
                try:
                    safe = re.sub(r"[^0-9+\-*/().% ]", "", expr)
                    print("=", eval(safe, {"__builtins__": {}}, {"math": math}))
                except Exception as e:
                    print("Error:", e)

        elif choice == "36":
            lo = _int_input("Min [1]: ", 1)
            hi = _int_input("Max [100]: ", 100)
            n = _int_input("How many [1]: ", 1, 1, 1000)
            import random
            nums = [random.randint(lo, hi) for _ in range(n)]
            print("Numbers:", nums if len(nums) <= 20 else str(nums[:20]) + " ... ({} total)".format(n))

        elif choice == "37":
            text = input("Text: ").lower()
            clean = re.sub(r"[^a-z0-9]", "", text)
            print("Palindrome!" if clean == clean[::-1] else "Not a palindrome.")

        elif choice == "38":
            import platform
            print("System:", platform.system(), platform.release())
            print("Python:", platform.python_version())
            print("Machine:", platform.machine())
            print("Node:", platform.node())
            print("CWD:", os.getcwd())

        elif choice == "39":
            try:
                import HubBaseUtility.Main as HBU
                print("HubBase Utility v{} loaded.".format(getattr(HBU, "__version__", "?")))
                HBU.Showcase()
            except ImportError:
                print("HubBaseUtility not installed. Install with: pip install HubBaseUtility")

        elif choice == "45":
            print("Undo feature not yet implemented in this session.")

        else:
            print("Invalid choice. Enter 1-45 or 'exit'.")
