import os, json, random, math

OUT = os.path.dirname(os.path.abspath(__file__))
random.seed(42)

# ── Word pools ──────────────────────────────────────────────────
NOUNS = "value data item element entry record field property key index count total sum product difference quotient remainder modulus power root base exponent coefficient factor term operand result output input argument parameter variable constant flag option setting mode type kind category group set collection sequence series range interval limit boundary edge case scenario situation context scope domain range namespace identifier label tag name title header footer body content container wrapper holder".split()
ADJS = "basic advanced simple complex nested flat deep shallow wide narrow long short big small large tiny huge massive minimal primary secondary tertiary final initial previous next current active passive static dynamic constant variable temporary permanent local global internal external public private protected abstract concrete virtual real physical logical numerical textual binary decimal hex octal raw cooked processed raw refined pure mixed combined separated joined split merged".split()
VERBS = "calculate compute evaluate solve process handle parse validate check verify test run execute perform generate create build construct form produce return yield emit send receive fetch load save store cache buffer flush clear reset init setup configure adjust tune calibrate convert transform map reduce filter sort search find locate match compare merge split join flatten expand compress encode decode encrypt decrypt hash sign".split()
TOPICS = "math string list dict set tuple file io datetime network validation crypto random statistics sort search algorithm data structure recursion loop conditional function class module package library framework error exception handling input output format parse serialize deserialize config environment system process thread async concurrent parallel stream buffer cache memory disk network socket protocol format encode decode serialize".split()

# ── Python function patterns (real implementations) ─────────────
PY_PATTERNS = []

# Math patterns
for op, impl in [
    ("add", lambda a, b: f"    return {a} + {b}"),
    ("subtract", lambda a, b: f"    return {a} - {b}"),
    ("multiply", lambda a, b: f"    return {a} * {b}"),
    ("divide", lambda a, b: f"    return {a} / {b}"),
    ("power", lambda a, b: f"    return {a} ** {b}"),
    ("mod", lambda a, b: f"    return {a} % {b}"),
]:
    PY_PATTERNS.append(("math", "numbers", 2, f"def {{name}}({{a}}, {{b}}):\n    \"\"\"{{desc}}\"\"\"\n{impl('{a}', '{b}')}\n", ["number", "math", "arithmetic", op]))

PY_PATTERNS.append(("math", "number", 1, "def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return abs(n)\n", ["number", "math", "absolute", "value"]))
PY_PATTERNS.append(("math", "number", 1, "def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return n * n\n", ["number", "math", "square"]))
PY_PATTERNS.append(("math", "number", 1, "def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return n ** 3\n", ["number", "math", "cube"]))
PY_PATTERNS.append(("math", "number", 1, "def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return math.sqrt(n)\n", ["number", "math", "square", "root"]))
PY_PATTERNS.append(("math", "number", 1, "def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return math.floor(n)\n", ["number", "math", "floor", "round"]))
PY_PATTERNS.append(("math", "number", 1, "def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return math.ceil(n)\n", ["number", "math", "ceil", "round"]))
PY_PATTERNS.append(("math", "number", 1, "def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return round(n, 2)\n", ["number", "math", "round", "decimal"]))
PY_PATTERNS.append(("math", "number", 1, "def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return n % 2 == 0\n", ["number", "math", "even", "check"]))
PY_PATTERNS.append(("math", "numbers", 2, "def {name}({a}, {b}):\n    \"\"\"{desc}\"\"\"\n    return math.gcd({a}, {b})\n", ["number", "math", "gcd"]))
PY_PATTERNS.append(("math", "numbers", 2, "def {name}({a}, {b}):\n    \"\"\"{desc}\"\"\"\n    return a ** 2 + b ** 2\n", ["number", "math", "pythagorean"]))
PY_PATTERNS.append(("math", "number", 1, "def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return 1 if n <= 1 else n * factorial(n - 1)\n", ["number", "math", "factorial", "recursion"]))

# String patterns
PY_PATTERNS.append(("string", "text", 1, "def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text[::-1]\n", ["string", "reverse", "text"]))
PY_PATTERNS.append(("string", "text", 1, "def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.upper()\n", ["string", "uppercase", "text"]))
PY_PATTERNS.append(("string", "text", 1, "def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.lower()\n", ["string", "lowercase", "text"]))
PY_PATTERNS.append(("string", "text", 1, "def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.strip()\n", ["string", "strip", "trim", "text"]))
PY_PATTERNS.append(("string", "text", 1, "def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.replace(' ', '_')\n", ["string", "replace", "space"]))
PY_PATTERNS.append(("string", "text", 1, "def {name}(text):\n    \"\"\"{desc}\"\"\"\n    words = text.split()\n    return len(words)\n", ["string", "word", "count", "split"]))
PY_PATTERNS.append(("string", "text", 1, "def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return len(text)\n", ["string", "length", "text"]))
PY_PATTERNS.append(("string", "text", 1, "def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.capitalize()\n", ["string", "capitalize", "text"]))
PY_PATTERNS.append(("string", "text", 1, "def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.title()\n", ["string", "title", "case"]))
PY_PATTERNS.append(("string", "text_char", 2, "def {name}(text, ch):\n    \"\"\"{desc}\"\"\"\n    return text.count(ch)\n", ["string", "count", "character"]))
PY_PATTERNS.append(("string", "text_old_new", 3, "def {name}(text, old, new):\n    \"\"\"{desc}\"\"\"\n    return text.replace(old, new)\n", ["string", "replace", "substring"]))
PY_PATTERNS.append(("string", "text", 1, "def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return ''.join(sorted(text))\n", ["string", "sort", "characters"]))
PY_PATTERNS.append(("string", "text", 1, "def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return all(c.isdigit() for c in text)\n", ["string", "digit", "check"]))

# List patterns
PY_PATTERNS.append(("list", "items", 1, "def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return len(items)\n", ["list", "length", "count"]))
PY_PATTERNS.append(("list", "items", 1, "def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return sum(items)\n", ["list", "sum", "total"]))
PY_PATTERNS.append(("list", "items", 1, "def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return sum(items) / len(items) if items else 0\n", ["list", "average", "mean"]))
PY_PATTERNS.append(("list", "items", 1, "def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return max(items)\n", ["list", "maximum", "max"]))
PY_PATTERNS.append(("list", "items", 1, "def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return min(items)\n", ["list", "minimum", "min"]))
PY_PATTERNS.append(("list", "items", 1, "def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return sorted(items)\n", ["list", "sort", "sorted"]))
PY_PATTERNS.append(("list", "items", 1, "def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return list(set(items))\n", ["list", "unique", "distinct"]))
PY_PATTERNS.append(("list", "items", 1, "def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return items[::-1]\n", ["list", "reverse", "order"]))
PY_PATTERNS.append(("list", "items_value", 2, "def {name}(items, value):\n    \"\"\"{desc}\"\"\"\n    return [x for x in items if x == value]\n", ["list", "filter", "find"]))
PY_PATTERNS.append(("list", "items", 1, "def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return [x * 2 for x in items]\n", ["list", "double", "multiply"]))
PY_PATTERNS.append(("list", "items", 1, "def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return [x for x in items if x > 0]\n", ["list", "positive", "filter"]))
PY_PATTERNS.append(("list", "items", 1, "def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return [x for x in items if x % 2 == 0]\n", ["list", "even", "filter"]))

# Dict patterns
PY_PATTERNS.append(("dict", "data", 1, "def {name}(data):\n    \"\"\"{desc}\"\"\"\n    return len(data)\n", ["dict", "length", "size"]))
PY_PATTERNS.append(("dict", "data", 1, "def {name}(data):\n    \"\"\"{desc}\"\"\"\n    return list(data.keys())\n", ["dict", "keys", "list"]))
PY_PATTERNS.append(("dict", "data", 1, "def {name}(data):\n    \"\"\"{desc}\"\"\"\n    return list(data.values())\n", ["dict", "values", "list"]))
PY_PATTERNS.append(("dict", "data_key", 2, "def {name}(data, key):\n    \"\"\"{desc}\"\"\"\n    return data.get(key, None)\n", ["dict", "get", "lookup"]))

# Validation patterns
PY_PATTERNS.append(("validate", "email_str", 1, "def {name}(value):\n    \"\"\"{desc}\"\"\"\n    return '@' in value and '.' in value.split('@')[-1]\n", ["validate", "email", "check"]))
PY_PATTERNS.append(("validate", "value", 1, "def {name}(value):\n    \"\"\"{desc}\"\"\"\n    return isinstance(value, int) and value > 0\n", ["validate", "positive", "integer"]))
PY_PATTERNS.append(("validate", "text", 1, "def {name}(text):\n    \"\"\"{desc}\"\"\"\n    import re\n    return bool(re.match(r'^[a-zA-Z0-9_]+$', text))\n", ["validate", "alphanumeric", "regex"]))
PY_PATTERNS.append(("validate", "text", 1, "def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.isalnum()\n", ["validate", "alnum", "check"]))
PY_PATTERNS.append(("validate", "text", 1, "def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.isalpha()\n", ["validate", "alpha", "letter"]))

# Format / conversion patterns
PY_PATTERNS.append(("convert", "value", 1, "def {name}(value):\n    \"\"\"{desc}\"\"\"\n    return int(value)\n", ["convert", "to", "integer"]))
PY_PATTERNS.append(("convert", "value", 1, "def {name}(value):\n    \"\"\"{desc}\"\"\"\n    return float(value)\n", ["convert", "to", "float"]))
PY_PATTERNS.append(("convert", "value", 1, "def {name}(value):\n    \"\"\"{desc}\"\"\"\n    return str(value)\n", ["convert", "to", "string"]))
PY_PATTERNS.append(("convert", "value", 1, "def {name}(value):\n    \"\"\"{desc}\"\"\"\n    return list(value)\n", ["convert", "to", "list"]))
PY_PATTERNS.append(("convert", "celsius", 1, "def {name}(c):\n    \"\"\"{desc}\"\"\"\n    return c * 9 / 5 + 32\n", ["convert", "celsius", "fahrenheit"]))
PY_PATTERNS.append(("convert", "fahrenheit", 1, "def {name}(f):\n    \"\"\"{desc}\"\"\"\n    return (f - 32) * 5 / 9\n", ["convert", "fahrenheit", "celsius"]))

# ── AiScript function patterns (AiScript-compatible) ─────────────
AIS_PATTERNS = []

AIS_PATTERNS.append(("ais", "a_b", 2, "def {name}(a, b):\n    //{desc}\n    print(a + b)\n", ["aiscript", "add", "math"]))
AIS_PATTERNS.append(("ais", "a_b", 2, "def {name}(a, b):\n    //{desc}\n    print(a - b)\n", ["aiscript", "subtract", "math"]))
AIS_PATTERNS.append(("ais", "a_b", 2, "def {name}(a, b):\n    //{desc}\n    print(a * b)\n", ["aiscript", "multiply", "math"]))
AIS_PATTERNS.append(("ais", "a_b", 2, "def {name}(a, b):\n    //{desc}\n    print(a / b)\n", ["aiscript", "divide", "math"]))
AIS_PATTERNS.append(("ais", "a_b", 2, "def {name}(a, b):\n    //{desc}\n    print(a // b)\n", ["aiscript", "floor", "divide"]))
AIS_PATTERNS.append(("ais", "a_b", 2, "def {name}(a, b):\n    //{desc}\n    print(a % b)\n", ["aiscript", "modulo", "remainder"]))
AIS_PATTERNS.append(("ais", "n", 1, "def {name}(n):\n    //{desc}\n    if n > 0:\n        print(\"positive\")\n    elif n == 0:\n        print(\"zero\")\n    else:\n        print(\"negative\")\n", ["aiscript", "if", "elif", "else"]))
AIS_PATTERNS.append(("ais", "n", 1, "def {name}(n):\n    //{desc}\n    for i in range(n):\n        print(i)\n", ["aiscript", "for", "loop", "range"]))
AIS_PATTERNS.append(("ais", "n", 1, "def {name}(n):\n    //{desc}\n    while n > 0:\n        print(n)\n        n = n - 1\n", ["aiscript", "while", "loop"]))
AIS_PATTERNS.append(("ais", "items", 1, "def {name}(items):\n    //{desc}\n    print(len(items))\n    print(items[0])\n", ["aiscript", "list", "length"]))
AIS_PATTERNS.append(("ais", "items_x", 2, "def {name}(items, x):\n    //{desc}\n    append(items, x)\n    print(len(items))\n", ["aiscript", "list", "append"]))
AIS_PATTERNS.append(("ais", "d_key", 2, "def {name}(d, key):\n    //{desc}\n    print(d[key])\n", ["aiscript", "dict", "key"]))
AIS_PATTERNS.append(("ais", "a_b", 2, "def {name}(a, b):\n    //{desc}\n    return a + b\n", ["aiscript", "function", "return"]))
AIS_PATTERNS.append(("ais", "msg", 1, "def {name}(msg):\n    //{desc}\n    print(\"Message: \" + msg)\n", ["aiscript", "print", "string"]))
AIS_PATTERNS.append(("ais", "name", 1, "def {name}(name):\n    //{desc}\n    result = \"Hello \" + name\n    print(result)\n", ["aiscript", "string", "concat"]))
AIS_PATTERNS.append(("ais", "x_y", 2, "def {name}(x, y):\n    //{desc}\n    if x > y:\n        print(x)\n    else:\n        print(y)\n", ["aiscript", "max", "compare"]))

# ── JSON Q&A templates ──────────────────────────────────────────
QA_TEMPLATES = [
    ("What is {} in programming?", "{} is a fundamental concept that stores and manages data during program execution. It is used extensively in all programming languages."),
    ("How do I use {} in Python?", "To use {} in Python, you need to understand its basic syntax and operations. Practice with simple examples first, then combine with other concepts."),
    ("What is the difference between {} and {}?", "{} and {} are different concepts. {} is used for specific scenarios, while {} handles other situations. Choose based on your requirements."),
    ("Give an example of {} in code", "An example of {} in code: create a variable, assign it a value, then use it in an operation. Real projects use {} in many creative ways."),
    ("Why is {} important in development?", "{} is important because it helps organize and structure code. It is a building block of modern software development and enables complex functionality."),
    ("When should I use {}?", "Use {} when you need to handle specific requirements. It is particularly useful in scenarios involving data processing, validation, and transformation."),
    ("How does {} improve code quality?", "{} improves code quality by making it more readable, maintainable, and efficient. Following best practices with {} leads to better software."),
    ("Common mistakes with {}?", "Common mistakes with {} include forgetting edge cases, incorrect syntax, and not considering performance. Always test thoroughly."),
    ("What are the benefits of {}?", "The benefits of {} include cleaner code, better organization, reusable components, and easier debugging. It is widely adopted in the industry."),
    ("How to optimize {} for performance?", "To optimize {} for performance, avoid unnecessary operations, use efficient data structures, and leverage caching where appropriate. Profile your code first."),
    ("{} vs {} – which is better?", "{} and {} serve different purposes. {} is better for certain use cases, while {} excels in others. Consider your specific needs."),
    ("Best practices for {}?", "Best practices for {} include consistent naming, proper documentation, unit testing, and following language idioms. Study existing codebases for examples."),
    ("How do I debug {} issues?", "To debug {} issues, start by reproducing the problem, check input values, add logging, use a debugger, and isolate the failing component."),
    ("What tools work with {}?", "Several tools work with {} including linters, formatters, debuggers, and profilers. Choose tools that integrate well with your workflow."),
    ("{} in large projects?", "In large projects, {} should be organized consistently. Use modular design, clear interfaces, and documentation to manage complexity."),
    ("How to test {} code?", "Test {} code with unit tests, integration tests, and edge cases. Aim for good coverage and use test-driven development when appropriate."),
    ("{} alternatives?", "Alternatives to {} exist depending on your tech stack. Evaluate each option based on your project's requirements, team expertise, and ecosystem."),
    ("Learning resources for {}?", "To learn {}, start with official documentation, tutorials, and practice projects. Online courses and community forums are also helpful."),
    ("{} security considerations?", "Security with {} involves input validation, proper error handling, avoiding common vulnerabilities, and keeping dependencies updated."),
    ("How does {} handle errors?", "{} handles errors through various mechanisms. Always validate inputs, handle exceptions, and provide meaningful error messages."),
]

# ── HTML patterns ────────────────────────────────────────────────
HTML_PATTERNS = []
for tag, desc in [
    ("div", "generic container"),
    ("span", "inline container"),
    ("section", "themed section"),
    ("article", "self-contained content"),
    ("nav", "navigation links"),
    ("header", "introductory content"),
    ("footer", "footer information"),
    ("main", "main content area"),
    ("aside", "sidebar content"),
    ("form", "user input form"),
    ("table", "tabular data"),
    ("ul", "unordered list"),
    ("ol", "ordered list"),
    ("figure", "illustrated figure"),
    ("details", "expandable details"),
    ("dialog", "dialog box"),
]:
    HTML_PATTERNS.append((tag, desc))

# ── CSS patterns ──────────────────────────────────────────────────
CSS_PATTERNS = []
for selector, desc, prop, val in [
    (".container", "flex layout", "display", "flex"),
    (".grid", "grid layout", "display", "grid"),
    ("body", "page text", "font-family", "Arial, sans-serif"),
    ("h1", "main heading", "font-size", "2em"),
    ("a", "link style", "color", "#0066cc"),
    ("button", "button style", "padding", "10px 20px"),
    (".hidden", "hidden element", "display", "none"),
    (".center", "centered text", "text-align", "center"),
    (".bold", "bold text", "font-weight", "bold"),
    (".italic", "italic text", "font-style", "italic"),
    (".card", "card layout", "border", "1px solid #ddd"),
    (".wrapper", "content wrapper", "max-width", "1200px"),
    (".sidebar", "side panel", "width", "250px"),
    (".modal", "modal overlay", "position", "fixed"),
    (".tooltip", "tooltip popup", "position", "absolute"),
]:
    CSS_PATTERNS.append((selector, desc, prop, val))

# ── Generation functions ──────────────────────────────────────────

def fill(template, *args):
    """Fill template placeholders with words."""
    params = {}
    for i, arg in enumerate(args):
        params[chr(97 + i)] = arg  # a, b, c, ...
    for i, arg in enumerate(args):
        params[f"p{i+1}"] = arg
    return template.format(**params)

def py_functions(count):
    lines = []
    for i in range(1, count + 1):
        cat, pname, nargs, template, keywords = random.choice(PY_PATTERNS)
        args = [random.choice(NOUNS) for _ in range(nargs)]
        name = f"{random.choice(VERBS)}_{random.choice(ADJS)}_{cat}_{i}"
        desc = f"{random.choice(VERBS).capitalize()} {random.choice(ADJS)} {random.choice(NOUNS)}. Category: {cat}."
        fargs_py = ", ".join(args)
        body = template.format(name=name, desc=desc, **dict(zip([chr(97+i) for i in range(nargs)], args)))
        body = body.replace(f"def {name}(", f"def compute_{cat}_{i}(")
        final_name = f"compute_{cat}_{i}"
        body = body.replace(f"def {name}(", f"def {final_name}(", 1)
        body = body.replace(f"\"\"\"{desc}\"\"\"", f"\"\"\"{desc}\"\"\"", 1)
        lines.append(body)
    return lines

def ais_functions(count):
    lines = []
    for i in range(1, count + 1):
        _, _, nargs, template, keywords = random.choice(AIS_PATTERNS)
        args = [random.choice(NOUNS) for _ in range(nargs)]
        name = f"demo_{random.choice(VERBS)}_{i}"
        desc = f"Demonstrates {random.choice(VERBS)} {random.choice(ADJS)} {random.choice(NOUNS)}"
        arglist = ", ".join(args)
        body = template.format(name=name, desc=desc, **dict(zip([chr(97+i) for i in range(nargs)], args)))
        body = body.replace(f"def {name}(", f"def demo_ais_{i}(", 1)
        lines.append(body)
    return lines

def json_qa(count):
    pairs = []
    words = NOUNS + ADJS + VERBS + TOPICS
    for _ in range(count):
        t = random.choice(QA_TEMPLATES)
        w1 = random.choice(words)
        w2 = random.choice(words)
        q = t[0].format(w1, w2) if "{}" in t[0] and t[0].count("{}") > 1 else t[0].format(w1)
        a = t[1].format(w1, w2)
        pairs.append({"question": q, "answer": a, "keywords": [w1, w2]})
    return pairs

def html_snippets(count):
    snips = []
    for i in range(1, count + 1):
        tag, desc = random.choice(HTML_PATTERNS)
        snips.append(f"<!-- {desc} example {i} -->\n<{tag} class=\"example-{i}\" id=\"item-{i}\">\n    <p>Content for {tag} example {i}</p>\n</{tag}>\n")
    return snips

def css_rules(count):
    rules = []
    for i in range(1, count + 1):
        sel, desc, prop, val = random.choice(CSS_PATTERNS)
        rules.append(f"/* {desc} rule {i} */\n{sel}-{i} {{\n    {prop}: {val};\n    margin: {random.choice(['0', '10px', 'auto'])};\n    padding: {random.choice(['5px', '10px', '20px'])};\n}}\n")
    return rules

# ── Write files (same as before) ──────────────────────────────────
def write_chunked(path, lines, chunk_size=5000):
    if len(lines) <= chunk_size:
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        return [path]
    paths = []
    base, ext = os.path.splitext(path)
    for chunk_idx in range(0, len(lines), chunk_size):
        chunk_path = f"{base}_{chunk_idx // chunk_size + 1}{ext}"
        with open(chunk_path, 'w', encoding='utf-8') as f:
            f.writelines(lines[chunk_idx:chunk_idx + chunk_size])
        paths.append(chunk_path)
    return paths

def main():
    print("Generating 10000+ .py functions...")
    py_lines = py_functions(10100)
    write_chunked(os.path.join(OUT, "coding_basics.py"), py_lines, 5000)
    print(f"  -> {len(py_lines)} functions")

    print("Generating 10000+ .ais functions...")
    ais_lines = ais_functions(10100)
    write_chunked(os.path.join(OUT, "python_coding.ais"), ais_lines, 5000)
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
