import os, json, random, math

OUT = os.path.dirname(os.path.abspath(__file__))
random.seed(42)

# ── Word pools (for name variety, not descriptions) ──────────────
NOUNS = "value data item element entry record field property key index count total sum product difference quotient remainder modulus power root base exponent coefficient factor term operand result output input argument parameter variable constant flag option setting mode type kind category group set collection sequence series range interval limit boundary edge case scenario situation context scope domain namespace identifier label tag name title header footer body content container wrapper holder".split()
ADJS = "basic advanced simple complex nested flat deep shallow wide narrow long short big small large tiny huge massive minimal primary secondary tertiary final initial previous next current active passive static dynamic constant variable temporary permanent local global internal external public private protected".split()
VERBS = "calculate compute evaluate solve process handle parse validate check verify test run execute perform generate create build construct form produce return yield emit send receive fetch load save store cache buffer flush clear reset init setup configure adjust tune calibrate convert transform map reduce filter sort search find locate match compare merge split join flatten expand compress encode decode encrypt decrypt hash sign".split()

# ── Python patterns ──────────────────────────────────────────────
# Each: (cat, nargs, template_str, keywords, desc_fmt)
# desc_fmt is a template string describing what the function does, using {desc_words}

PY_PATTERNS = []

def py(template, kw, cat="math", nargs=2, desc_fmt=None):
    if desc_fmt is None:
        desc_fmt = f"{kw[0].capitalize()} {{a}} {kw[1] if len(kw) > 1 else 'data'}" if len(kw) >= 2 else f"{kw[0].capitalize()} {{a}}"
    PY_PATTERNS.append((cat, nargs, template, kw, desc_fmt))

def _name(kw, n):
    base = kw[0] if len(kw[0]) > 3 else (kw[1] if len(kw) > 1 else "process")
    suffix = random.choice([''] + ['_'+v for v in ['by','via','using','as','in']]) if random.random() < 0.15 else ''
    return f"{base}_{random.choice(NOUNS)}{suffix}_{n}"

# math
py("def {name}({a}, {b}):\n    \"\"\"{desc}\"\"\"\n    return {a} + {b}\n", ["add","plus","sum"], desc_fmt="Adds {a} and {b} together and returns the result")
py("def {name}({a}, {b}):\n    \"\"\"{desc}\"\"\"\n    return {a} - {b}\n", ["subtract","minus","diff"], desc_fmt="Subtracts {b} from {a} and returns the difference")
py("def {name}({a}, {b}):\n    \"\"\"{desc}\"\"\"\n    return {a} * {b}\n", ["multiply","product","times"], desc_fmt="Multiplies {a} by {b} and returns the product")
py("def {name}({a}, {b}):\n    \"\"\"{desc}\"\"\"\n    return {a} / {b}\n", ["divide","quotient","division"], desc_fmt="Divides {a} by {b} and returns the quotient")
py("def {name}({a}, {b}):\n    \"\"\"{desc}\"\"\"\n    return {a} ** {b}\n", ["power","exponent"], desc_fmt="Raises {a} to the power of {b}")
py("def {name}({a}, {b}):\n    \"\"\"{desc}\"\"\"\n    return {a} % {b}\n", ["modulo","remainder"], desc_fmt="Returns the remainder of {a} divided by {b}")
py("def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return abs(n)\n", ["absolute","abs","magnitude"], nargs=1, desc_fmt="Returns the absolute value of n")
py("def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return n * n\n", ["square","squared"], nargs=1, desc_fmt="Returns the square of n")
py("def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return n ** 3\n", ["cube","cubed"], nargs=1, desc_fmt="Returns the cube of n")
py("def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return math.sqrt(n)\n", ["square","root","sqrt"], nargs=1, desc_fmt="Returns the square root of n")
py("def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return math.floor(n)\n", ["floor","round","down"], nargs=1, desc_fmt="Rounds n down to the nearest integer")
py("def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return math.ceil(n)\n", ["ceil","ceiling","round","up"], nargs=1, desc_fmt="Rounds n up to the nearest integer")
py("def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return round(n, 2)\n", ["round","decimal","precision"], nargs=1, desc_fmt="Rounds n to 2 decimal places")
py("def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return n % 2 == 0\n", ["even","check","parity"], nargs=1, desc_fmt="Returns True if n is an even number")
py("def {name}({a}, {b}):\n    \"\"\"{desc}\"\"\"\n    return math.gcd({a}, {b})\n", ["gcd","greatest","common","divisor"], desc_fmt="Returns the greatest common divisor of {a} and {b}")
py("def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return 1 if n <= 1 else n * {name}(n - 1)\n", ["factorial","recursion"], nargs=1, desc_fmt="Calculates the factorial of n recursively")

# string
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text[::-1]\n", ["reverse","string","text"], nargs=1, desc_fmt="Reverses the characters in a string")
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.upper()\n", ["uppercase","capitalize"], nargs=1, desc_fmt="Converts a string to uppercase")
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.lower()\n", ["lowercase","casefold"], nargs=1, desc_fmt="Converts a string to lowercase")
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.strip()\n", ["strip","trim","whitespace"], nargs=1, desc_fmt="Removes leading and trailing whitespace from a string")
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.replace(' ', '_')\n", ["replace","space","underscore"], nargs=1, desc_fmt="Replaces spaces with underscores in a string")
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    words = text.split()\n    return len(words)\n", ["word","count","tokenize"], nargs=1, desc_fmt="Counts the number of words in a string")
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return len(text)\n", ["length","string","length"], nargs=1, desc_fmt="Returns the length of a string")
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.capitalize()\n", ["capitalize","title"], nargs=1, desc_fmt="Capitalizes the first character of a string")
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.title()\n", ["title","case"], nargs=1, desc_fmt="Converts a string to title case")
py("def {name}(text, ch):\n    \"\"\"{desc}\"\"\"\n    return text.count(ch)\n", ["count","character","occurrence"], nargs=2, desc_fmt="Counts occurrences of ch in text")
py("def {name}(text, old, new):\n    \"\"\"{desc}\"\"\"\n    return text.replace(old, new)\n", ["replace","substring","swap"], nargs=3, desc_fmt="Replaces old substring with new in text")
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return ''.join(sorted(text))\n", ["sort","alphabetical","order"], nargs=1, desc_fmt="Sorts the characters in a string alphabetically")
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return all(c.isdigit() for c in text)\n", ["digit","numeric","check"], nargs=1, desc_fmt="Returns True if all characters in text are digits")

# list
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return len(items)\n", ["list","length","count","size"], nargs=1, desc_fmt="Returns the number of items in a list")
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return sum(items)\n", ["sum","total","list"], nargs=1, desc_fmt="Returns the sum of all items in a list")
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return sum(items) / len(items) if items else 0\n", ["average","mean","list"], nargs=1, desc_fmt="Returns the average value of items in a list")
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return max(items)\n", ["maximum","max","largest"], nargs=1, desc_fmt="Returns the maximum value from a list")
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return min(items)\n", ["minimum","min","smallest"], nargs=1, desc_fmt="Returns the minimum value from a list")
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return sorted(items)\n", ["sort","sorted","ascending"], nargs=1, desc_fmt="Returns a sorted copy of a list")
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return list(set(items))\n", ["unique","distinct","deduplicate"], nargs=1, desc_fmt="Removes duplicate items from a list")
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return items[::-1]\n", ["reverse","order","list"], nargs=1, desc_fmt="Reverses the order of items in a list")
py("def {name}(items, value):\n    \"\"\"{desc}\"\"\"\n    return [x for x in items if x == value]\n", ["filter","find","match"], nargs=2, desc_fmt="Filters a list for items matching a value")
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return [x * 2 for x in items]\n", ["double","multiply","scale"], nargs=1, desc_fmt="Doubles each item in a list")
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return [x for x in items if x > 0]\n", ["positive","filter","negative"], nargs=1, desc_fmt="Filters a list to keep only positive numbers")
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return [x for x in items if x % 2 == 0]\n", ["even","filter","list"], nargs=1, desc_fmt="Filters a list to keep only even numbers")

# dict
py("def {name}(data):\n    \"\"\"{desc}\"\"\"\n    return len(data)\n", ["dict","dictionary","size"], nargs=1, desc_fmt="Returns the number of entries in a dictionary")
py("def {name}(data):\n    \"\"\"{desc}\"\"\"\n    return list(data.keys())\n", ["dict","keys","dictionary"], nargs=1, desc_fmt="Returns all keys from a dictionary")
py("def {name}(data):\n    \"\"\"{desc}\"\"\"\n    return list(data.values())\n", ["dict","values","dictionary"], nargs=1, desc_fmt="Returns all values from a dictionary")
py("def {name}(data, key):\n    \"\"\"{desc}\"\"\"\n    return data.get(key, None)\n", ["dict","get","lookup"], nargs=2, desc_fmt="Looks up a key in a dictionary safely")

# validate
py("def {name}(value):\n    \"\"\"{desc}\"\"\"\n    return '@' in value and '.' in value.split('@')[-1]\n", ["email","validate","check"], nargs=1, desc_fmt="Validates whether a string is a valid email address")
py("def {name}(value):\n    \"\"\"{desc}\"\"\"\n    return isinstance(value, int) and value > 0\n", ["positive","integer","validate"], nargs=1, desc_fmt="Checks if a value is a positive integer")
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    import re\n    return bool(re.match(r'^[a-zA-Z0-9_]+$', text))\n", ["alphanumeric","regex","validate"], nargs=1, desc_fmt="Validates if text contains only letters, numbers, and underscores")
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.isalnum()\n", ["alnum","alphanumeric","check"], nargs=1, desc_fmt="Checks if text is alphanumeric")
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.isalpha()\n", ["alpha","letters","check"], nargs=1, desc_fmt="Checks if text contains only letters")

# convert
py("def {name}(value):\n    \"\"\"{desc}\"\"\"\n    return int(value)\n", ["convert","integer","parse"], nargs=1, desc_fmt="Converts a value to an integer")
py("def {name}(value):\n    \"\"\"{desc}\"\"\"\n    return float(value)\n", ["convert","float","parse"], nargs=1, desc_fmt="Converts a value to a float")
py("def {name}(value):\n    \"\"\"{desc}\"\"\"\n    return str(value)\n", ["convert","string","stringify"], nargs=1, desc_fmt="Converts a value to a string")
py("def {name}(value):\n    \"\"\"{desc}\"\"\"\n    return list(value)\n", ["convert","list","sequence"], nargs=1, desc_fmt="Converts a value to a list")
py("def {name}(c):\n    \"\"\"{desc}\"\"\"\n    return c * 9 / 5 + 32\n", ["celsius","fahrenheit","convert"], nargs=1, desc_fmt="Converts Celsius to Fahrenheit")
py("def {name}(f):\n    \"\"\"{desc}\"\"\"\n    return (f - 32) * 5 / 9\n", ["fahrenheit","celsius","convert"], nargs=1, desc_fmt="Converts Fahrenheit to Celsius")

# ── AiScript patterns ────────────────────────────────────────────
AIS_PATTERNS = []

def ais(template, kw, nargs=2, desc_fmt=None):
    if desc_fmt is None:
        desc_fmt = f"Demonstrates {kw[0]} in AiScript"
    AIS_PATTERNS.append((nargs, template, kw, desc_fmt))

ais("def {name}(a, b):\n    //{desc}\n    print(a + b)\n", ["add","aiscript"], desc_fmt="Adds two numbers in AiScript")
ais("def {name}(a, b):\n    //{desc}\n    print(a - b)\n", ["subtract","aiscript"], desc_fmt="Subtracts two numbers in AiScript")
ais("def {name}(a, b):\n    //{desc}\n    print(a * b)\n", ["multiply","aiscript"], desc_fmt="Multiplies two numbers in AiScript")
ais("def {name}(a, b):\n    //{desc}\n    print(a / b)\n", ["divide","aiscript"], desc_fmt="Divides two numbers in AiScript")
ais("def {name}(a, b):\n    //{desc}\n    print(a // b)\n", ["floor","divide"], desc_fmt="Performs floor division in AiScript")
ais("def {name}(a, b):\n    //{desc}\n    print(a % b)\n", ["modulo","remainder"], desc_fmt="Returns the remainder of division in AiScript")
ais("def {name}(n):\n    //{desc}\n    if n > 0:\n        print(\"positive\")\n    elif n == 0:\n        print(\"zero\")\n    else:\n        print(\"negative\")\n", ["if","elif","else","conditional"], nargs=1, desc_fmt="Checks if a number is positive, negative, or zero in AiScript")
ais("def {name}(n):\n    //{desc}\n    for i in range(n):\n        print(i)\n", ["for","loop","range"], nargs=1, desc_fmt="Iterates from 0 to n-1 using a for loop in AiScript")
ais("def {name}(n):\n    //{desc}\n    while n > 0:\n        print(n)\n        n = n - 1\n", ["while","loop","countdown"], nargs=1, desc_fmt="Counts down using a while loop in AiScript")
ais("def {name}(items):\n    //{desc}\n    print(len(items))\n    print(items[0])\n", ["list","length","first"], nargs=1, desc_fmt="Prints the length and first element of a list in AiScript")
ais("def {name}(items, x):\n    //{desc}\n    append(items, x)\n    print(len(items))\n", ["list","append","add"], desc_fmt="Appends an item to a list in AiScript")
ais("def {name}(d, key):\n    //{desc}\n    print(d[key])\n", ["dict","key","lookup"], desc_fmt="Looks up a value by key in a dictionary in AiScript")
ais("def {name}(a, b):\n    //{desc}\n    return a + b\n", ["return","function"], desc_fmt="Returns the sum of two numbers in AiScript")
ais("def {name}(msg):\n    //{desc}\n    print(\"Message: \" + msg)\n", ["print","string","message"], nargs=1, desc_fmt="Prints a message with a label in AiScript")
ais("def {name}(name):\n    //{desc}\n    result = \"Hello \" + name\n    print(result)\n", ["hello","concat","string"], nargs=1, desc_fmt="Concatenates strings to greet someone in AiScript")
ais("def {name}(x, y):\n    //{desc}\n    if x > y:\n        print(x)\n    else:\n        print(y)\n", ["maximum","compare","conditional"], desc_fmt="Prints the larger of two numbers in AiScript")

# ── JSON Q&A ─────────────────────────────────────────────────────
QA_TEMPLATES = []

def qa(q, a):
    qn = q.count("{}")
    an = a.count("{}")
    QA_TEMPLATES.append((q, a, qn, an))

qa("What is a {} in programming?", "A {} is a fundamental building block used to store, organize, and manipulate data during program execution.")
qa("How do I use {} in Python?", "To use {} in Python, learn its syntax and operations, then practice with simple examples before combining with other features.")
qa("What is the difference between {} and {}?", "{} and {} serve different purposes. {} handles one scenario while {} handles another. Choose based on your requirements.")
qa("Give an example of {} in code", "Example: declare a variable of type {}, assign it a value, then use it in an operation. Real projects apply {} in creative ways.")
qa("Why is {} important?", "{} is important because it helps organize code and enables complex functionality. It is a core concept in modern programming.")
qa("When should I use {}?", "Use {} when you need to handle specific requirements like data processing, validation, transformation, or state management.")
qa("How does {} improve code quality?", "{} improves code quality by making it more readable, maintainable, and efficient when following established patterns.")
qa("Common mistakes with {}?", "Common mistakes include forgetting edge cases, using incorrect syntax, and not considering performance implications. Always test thoroughly.")
qa("Benefits of {}?", "Benefits include cleaner code, better organization, reusable logic, and simplified debugging. Widely adopted across the industry.")
qa("How to optimize {} for performance?", "Avoid unnecessary operations, use efficient data structures, and profile before optimizing. Measure, then improve.")
qa("{} vs {} - which is better?", "{} and {} serve different use cases. {} excels in certain scenarios while {} is better for others. Evaluate based on your project needs.")
qa("Best practices for {}?", "Use consistent naming, write documentation, include unit tests, and follow language idioms. Study well-known codebases for examples.")
qa("How to debug {} issues?", "Reproduce the problem, check inputs, add logging, use a debugger, and isolate the failing component. Systematic debugging helps.")
qa("What tools work with {}?", "Tools include linters, formatters, debuggers, and profilers. Choose tools that integrate well with your development workflow.")
qa("{} in large projects?", "Organize {} with modular design, clear interfaces, consistent naming, and thorough documentation to manage complexity at scale.")
qa("How to test {} code?", "Write unit tests, integration tests, and edge case coverage. Use test-driven development for critical components.")
qa("{} alternatives?", "Alternatives depend on your tech stack. Evaluate each option based on team expertise, ecosystem, and maintainability.")
qa("Learning resources for {}?", "Start with official documentation, tutorials, and practice projects. Online courses and forum discussions also help.")
qa("{} security considerations?", "Validate inputs, handle errors gracefully, avoid injection attacks, and keep dependencies updated.")
qa("How does {} handle errors?", "Use proper error handling. Always validate inputs, raise meaningful exceptions, and provide user-friendly messages.")

# ── HTML/CSS sources ──────────────────────────────────────────────
HTML_TAGS = ["div","span","section","article","nav","header","footer","main","aside","form","table","ul","ol","figure","details","dialog"]
CSS_RULES = [
    (".container","display","flex"),(".grid","display","grid"),
    ("body","font-family","Arial, sans-serif"),("h1","font-size","2em"),
    ("a","color","#0066cc"),("button","padding","10px 20px"),
    (".hidden","display","none"),(".center","text-align","center"),
    (".bold","font-weight","bold"),(".italic","font-style","italic"),
    (".card","border","1px solid #ddd"),(".wrapper","max-width","1200px"),
    (".sidebar","width","250px"),(".modal","position","fixed"),
    (".tooltip","position","absolute"),
]

# ── Generation ────────────────────────────────────────────────────

def gen_desc(desc_fmt, args, kw):
    d = desc_fmt.format(a=args[0] if len(args) > 0 else 'value', b=args[1] if len(args) > 1 else 'value', c=args[2] if len(args) > 2 else 'value')
    for w in sorted(set(kw), key=lambda x: -len(x)):
        if w not in d.lower():
            d = d + f" Related to {w}."
            break
    return d

def py_functions(count):
    lines = []
    needs_math = False
    for i in range(1, count + 1):
        cat, nargs, template, keywords, desc_fmt = random.choice(PY_PATTERNS)
        args = [random.choice(NOUNS) for _ in range(nargs)]
        name = _name(keywords, i)
        desc = gen_desc(desc_fmt, args, keywords)
        params = {chr(97 + j): args[j] for j in range(nargs)}
        body = template.format(name=name, desc=desc, **params)
        if "math." in body:
            needs_math = True
        lines.append(body)
    if needs_math:
        lines.insert(0, "import math\n")
    return lines

def ais_functions(count):
    lines = []
    for i in range(1, count + 1):
        nargs, template, keywords, desc_fmt = random.choice(AIS_PATTERNS)
        name = _name(keywords, i)
        desc = gen_desc(desc_fmt, ['value'] * nargs, keywords)
        body = template.format(name=name, desc=desc)
        lines.append(body)
    return lines

def json_qa(count):
    pairs = []
    words = NOUNS + ADJS + VERBS
    for _ in range(count):
        q_t, a_t, qn, an = random.choice(QA_TEMPLATES)
        picks = [random.choice(words) for _ in range(max(qn, an))]
        q = q_t.format(*picks[:qn])
        a = a_t.format(*picks[:an])
        pairs.append({"question": q, "answer": a, "keywords": [picks[0]]})
    return pairs

def html_snippets(count):
    snips = []
    for i in range(1, count + 1):
        tag = random.choice(HTML_TAGS)
        snips.append(f"<!-- Container example {i} -->\n<{tag} class=\"box-{i}\" id=\"id-{i}\">\n    <p>Sample content for {tag} #{i}</p>\n</{tag}>\n")
    return snips

def css_rules(count):
    rules = []
    for i in range(1, count + 1):
        sel, prop, val = random.choice(CSS_RULES)
        rules.append(f"/* Style rule {i} */\n{sel}-{i} {{\n    {prop}: {val};\n    margin: {random.choice(['0', '10px', 'auto'])};\n    padding: {random.choice(['5px', '10px', '20px'])};\n}}\n")
    return rules

def write_chunked(path, lines, chunk_size=5000):
    if len(lines) <= chunk_size:
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(l if l.endswith('\n') else l + '\n' for l in lines)
        return [path]
    paths = []
    base, ext = os.path.splitext(path)
    for chunk_idx in range(0, len(lines), chunk_size):
        chunk_path = f"{base}_{chunk_idx // chunk_size + 1}{ext}"
        with open(chunk_path, 'w', encoding='utf-8') as f:
            f.writelines(l if l.endswith('\n') else l + '\n' for l in lines[chunk_idx:chunk_idx + chunk_size])
        paths.append(chunk_path)
    return paths

def main():
    os.makedirs(OUT, exist_ok=True)

    print("Generating 10000+ .py functions...")
    py_lines = py_functions(10100)
    write_chunked(os.path.join(OUT, "coding_basics.py"), py_lines)
    print(f"  -> {len(py_lines)} functions")

    print("Generating 10000+ .ais functions...")
    ais_lines = ais_functions(10100)
    write_chunked(os.path.join(OUT, "python_coding.ais"), ais_lines)
    print(f"  -> {len(ais_lines)} functions")

    print("Generating 100000+ .json Q&A pairs...")
    qa = json_qa(100100)
    with open(os.path.join(OUT, "general_knowledge.json"), 'w', encoding='utf-8') as f:
        json.dump(qa, f, indent=2, ensure_ascii=False)
    print(f"  -> {len(qa)} pairs")

    print("Generating 1000+ .html snippets...")
    html_lines = html_snippets(1050)
    write_chunked(os.path.join(OUT, "html_basics.html"), html_lines)
    print(f"  -> {len(html_lines)} snippets")

    print("Generating 1000+ .css rules...")
    css_lines = css_rules(1050)
    write_chunked(os.path.join(OUT, "css_basics.css"), css_lines)
    print(f"  -> {len(css_lines)} rules")

    print("Done!")

if __name__ == "__main__":
    main()
