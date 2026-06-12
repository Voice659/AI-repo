import os, json, random, math

OUT = os.path.dirname(os.path.abspath(__file__))
random.seed(42)

# ── Word pools ──────────────────────────────────────────────────
NOUNS = "value data item element entry record field property key index count total sum product difference quotient remainder modulus power root base exponent coefficient factor term operand result output input argument parameter variable constant flag option setting mode type kind category group set collection sequence series range interval limit boundary edge case scenario situation context scope domain namespace identifier label tag name title header footer body content container wrapper holder".split()
ADJS = "basic advanced simple complex nested flat deep shallow wide narrow long short big small large tiny huge massive minimal primary secondary tertiary final initial previous next current active passive static dynamic constant variable temporary permanent local global internal external public private protected abstract concrete virtual real physical logical numerical textual binary decimal hex octal raw cooked processed raw refined pure mixed combined separated joined split merged".split()
VERBS = "calculate compute evaluate solve process handle parse validate check verify test run execute perform generate create build construct form produce return yield emit send receive fetch load save store cache buffer flush clear reset init setup configure adjust tune calibrate convert transform map reduce filter sort search find locate match compare merge split join flatten expand compress encode decode encrypt decrypt hash sign".split()
TOPICS = "math string list dict set tuple file io datetime network validation crypto random statistics sort search algorithm data structure recursion loop conditional function class module package library framework error exception handling input output format parse serialize deserialize config environment system process thread async concurrent parallel stream buffer cache memory disk network socket protocol encode decode serialize".split()

# ── Python patterns ──────────────────────────────────────────────
# Each: (category, param_hint, nargs, template_str, keywords)
# Template uses {name}, {desc}, {a}, {b}, {c} for parameter names.

PY_PATTERNS = []

def py(template, kw, cat="math", nargs=2):
    PY_PATTERNS.append((cat, nargs, template, kw))

# math
py("def {name}({a}, {b}):\n    \"\"\"{desc}\"\"\"\n    return {a} + {b}\n", ["add", "sum", "math"])
py("def {name}({a}, {b}):\n    \"\"\"{desc}\"\"\"\n    return {a} - {b}\n", ["subtract", "difference", "math"])
py("def {name}({a}, {b}):\n    \"\"\"{desc}\"\"\"\n    return {a} * {b}\n", ["multiply", "product", "math"])
py("def {name}({a}, {b}):\n    \"\"\"{desc}\"\"\"\n    return {a} / {b}\n", ["divide", "quotient", "math"])
py("def {name}({a}, {b}):\n    \"\"\"{desc}\"\"\"\n    return {a} ** {b}\n", ["power", "exponent", "math"])
py("def {name}({a}, {b}):\n    \"\"\"{desc}\"\"\"\n    return {a} % {b}\n", ["mod", "remainder", "math"])
py("def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return abs(n)\n", ["absolute", "abs", "math"], nargs=1)
py("def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return n * n\n", ["square", "math"], nargs=1)
py("def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return n ** 3\n", ["cube", "math"], nargs=1)
py("def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return math.sqrt(n)\n", ["sqrt", "root", "math"], nargs=1)
py("def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return math.floor(n)\n", ["floor", "math"], nargs=1)
py("def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return math.ceil(n)\n", ["ceil", "math"], nargs=1)
py("def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return round(n, 2)\n", ["round", "decimal", "math"], nargs=1)
py("def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return n % 2 == 0\n", ["even", "check", "math"], nargs=1)
py("def {name}({a}, {b}):\n    \"\"\"{desc}\"\"\"\n    return math.gcd({a}, {b})\n", ["gcd", "math"])
py("def {name}(n):\n    \"\"\"{desc}\"\"\"\n    return 1 if n <= 1 else n * {name}(n - 1)\n", ["factorial", "recursion", "math"], nargs=1)

# string
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text[::-1]\n", ["reverse", "string"], nargs=1)
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.upper()\n", ["uppercase", "string"], nargs=1)
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.lower()\n", ["lowercase", "string"], nargs=1)
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.strip()\n", ["strip", "trim", "string"], nargs=1)
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.replace(' ', '_')\n", ["replace", "space", "string"], nargs=1)
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    words = text.split()\n    return len(words)\n", ["word", "count", "string"], nargs=1)
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return len(text)\n", ["length", "string"], nargs=1)
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.capitalize()\n", ["capitalize", "string"], nargs=1)
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.title()\n", ["title", "case", "string"], nargs=1)
py("def {name}(text, ch):\n    \"\"\"{desc}\"\"\"\n    return text.count(ch)\n", ["count", "character", "string"], nargs=2)
py("def {name}(text, old, new):\n    \"\"\"{desc}\"\"\"\n    return text.replace(old, new)\n", ["replace", "substring", "string"], nargs=3)
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return ''.join(sorted(text))\n", ["sort", "chars", "string"], nargs=1)
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return all(c.isdigit() for c in text)\n", ["digit", "check", "string"], nargs=1)

# list
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return len(items)\n", ["list", "length"], nargs=1)
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return sum(items)\n", ["list", "sum"], nargs=1)
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return sum(items) / len(items) if items else 0\n", ["average", "mean"], nargs=1)
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return max(items)\n", ["max", "maximum"], nargs=1)
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return min(items)\n", ["min", "minimum"], nargs=1)
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return sorted(items)\n", ["sort", "sorted"], nargs=1)
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return list(set(items))\n", ["unique", "distinct"], nargs=1)
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return items[::-1]\n", ["reverse", "order"], nargs=1)
py("def {name}(items, value):\n    \"\"\"{desc}\"\"\"\n    return [x for x in items if x == value]\n", ["filter", "find"], nargs=2)
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return [x * 2 for x in items]\n", ["double", "multiply"], nargs=1)
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return [x for x in items if x > 0]\n", ["positive", "filter"], nargs=1)
py("def {name}(items):\n    \"\"\"{desc}\"\"\"\n    return [x for x in items if x % 2 == 0]\n", ["even", "filter"], nargs=1)

# dict
py("def {name}(data):\n    \"\"\"{desc}\"\"\"\n    return len(data)\n", ["dict", "size"], nargs=1)
py("def {name}(data):\n    \"\"\"{desc}\"\"\"\n    return list(data.keys())\n", ["dict", "keys"], nargs=1)
py("def {name}(data):\n    \"\"\"{desc}\"\"\"\n    return list(data.values())\n", ["dict", "values"], nargs=1)
py("def {name}(data, key):\n    \"\"\"{desc}\"\"\"\n    return data.get(key, None)\n", ["dict", "get"], nargs=2)

# validate
py("def {name}(value):\n    \"\"\"{desc}\"\"\"\n    return '@' in value and '.' in value.split('@')[-1]\n", ["email", "validate"], nargs=1)
py("def {name}(value):\n    \"\"\"{desc}\"\"\"\n    return isinstance(value, int) and value > 0\n", ["positive", "integer"], nargs=1)
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    import re\n    return bool(re.match(r'^[a-zA-Z0-9_]+$', text))\n", ["alphanumeric", "regex"], nargs=1)
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.isalnum()\n", ["alnum", "check"], nargs=1)
py("def {name}(text):\n    \"\"\"{desc}\"\"\"\n    return text.isalpha()\n", ["alpha", "letter"], nargs=1)

# convert
py("def {name}(value):\n    \"\"\"{desc}\"\"\"\n    return int(value)\n", ["to", "integer"], nargs=1)
py("def {name}(value):\n    \"\"\"{desc}\"\"\"\n    return float(value)\n", ["to", "float"], nargs=1)
py("def {name}(value):\n    \"\"\"{desc}\"\"\"\n    return str(value)\n", ["to", "string"], nargs=1)
py("def {name}(value):\n    \"\"\"{desc}\"\"\"\n    return list(value)\n", ["to", "list"], nargs=1)
py("def {name}(c):\n    \"\"\"{desc}\"\"\"\n    return c * 9 / 5 + 32\n", ["celsius", "fahrenheit"], nargs=1)
py("def {name}(f):\n    \"\"\"{desc}\"\"\"\n    return (f - 32) * 5 / 9\n", ["fahrenheit", "celsius"], nargs=1)

# ── AiScript patterns ────────────────────────────────────────────
AIS_PATTERNS = []

def ais(template, kw, nargs=2):
    AIS_PATTERNS.append((nargs, template, kw))

ais("def {name}(a, b):\n    //{desc}\n    print(a + b)\n", ["add", "aiscript"])
ais("def {name}(a, b):\n    //{desc}\n    print(a - b)\n", ["subtract", "aiscript"])
ais("def {name}(a, b):\n    //{desc}\n    print(a * b)\n", ["multiply", "aiscript"])
ais("def {name}(a, b):\n    //{desc}\n    print(a / b)\n", ["divide", "aiscript"])
ais("def {name}(a, b):\n    //{desc}\n    print(a // b)\n", ["floor", "divide"])
ais("def {name}(a, b):\n    //{desc}\n    print(a % b)\n", ["modulo"])
ais("def {name}(n):\n    //{desc}\n    if n > 0:\n        print(\"positive\")\n    elif n == 0:\n        print(\"zero\")\n    else:\n        print(\"negative\")\n", ["if", "elif"], nargs=1)
ais("def {name}(n):\n    //{desc}\n    for i in range(n):\n        print(i)\n", ["for", "loop"], nargs=1)
ais("def {name}(n):\n    //{desc}\n    while n > 0:\n        print(n)\n        n = n - 1\n", ["while", "loop"], nargs=1)
ais("def {name}(items):\n    //{desc}\n    print(len(items))\n    print(items[0])\n", ["list", "length"], nargs=1)
ais("def {name}(items, x):\n    //{desc}\n    append(items, x)\n    print(len(items))\n", ["list", "append"])
ais("def {name}(d, key):\n    //{desc}\n    print(d[key])\n", ["dict", "key"])
ais("def {name}(a, b):\n    //{desc}\n    return a + b\n", ["return"])
ais("def {name}(msg):\n    //{desc}\n    print(\"Message: \" + msg)\n", ["print", "string"], nargs=1)
ais("def {name}(name):\n    //{desc}\n    result = \"Hello \" + name\n    print(result)\n", ["concat"], nargs=1)
ais("def {name}(x, y):\n    //{desc}\n    if x > y:\n        print(x)\n    else:\n        print(y)\n", ["max", "compare"])

# ── JSON Q&A ─────────────────────────────────────────────────────
QA_TEMPLATES = []

def qa(q, a):
    """Register a Q&A pair template with {}/{} placeholders counting."""
    qn = q.count("{}")
    an = a.count("{}")
    QA_TEMPLATES.append((q, a, qn, an))

qa("What is a {} in programming?", "A {} is a fundamental building block in programming used to store, organize, and manipulate data during program execution.")
qa("How do I use {} in Python?", "To use {} in Python, learn its syntax and operations, then practice with simple examples before combining with other features.")
qa("What is the difference between {} and {}?", "{} and {} serve different purposes. {} handles one scenario while {} handles another. Choose based on your specific requirements.")
qa("Give an example of {} in code", "Example: declare a variable of type {}, assign it a value, then use it in an operation. Real projects apply {} in many creative ways.")
qa("Why is {} important?", "{} is important because it helps organize code and enables complex functionality. It is a core concept in modern programming.")
qa("When should I use {}?", "Use {} when you need to handle specific requirements like data processing, validation, transformation, or state management.")
qa("How does {} improve code quality?", "{} improves code quality by making it more readable, maintainable, and efficient when following established patterns.")
qa("Common mistakes with {}?", "Common mistakes include forgetting edge cases, using incorrect syntax, and not considering performance implications. Always test thoroughly.")
qa("Benefits of {}?", "Benefits include cleaner code, better organization, reusable logic, and simplified debugging. It is widely adopted across the industry.")
qa("How to optimize {} for performance?", "Avoid unnecessary operations, use efficient data structures, and profile before optimizing. Measure, then improve.")
qa("{} vs {} — which is better?", "{} and {} serve different use cases. {} excels in certain scenarios while {} is better for others. Evaluate based on your project needs.")
qa("Best practices for {}?", "Use consistent naming, write documentation, include unit tests, and follow language idioms. Study well-known codebases for examples.")
qa("How to debug {} issues?", "Reproduce the problem, check inputs, add logging, use a debugger, and isolate the component. Systematic debugging finds issues faster.")
qa("What tools work with {}?", "Tools include linters, formatters, debuggers, and profilers. Pick tools that integrate well with your development workflow and team.")
qa("{} in large projects?", "Organize {} with modular design, clear interfaces, consistent naming, and thorough documentation to manage complexity at scale.")
qa("How to test {} code?", "Write unit tests, integration tests, and edge case coverage. Use test-driven development for critical components and aim for high coverage.")
qa("{} alternatives?", "Alternatives depend on your tech stack and requirements. Evaluate each option based on team expertise, ecosystem, and long-term maintainability.")
qa("Learning resources for {}?", "Start with official documentation, tutorials, and small practice projects. Online courses, forums, and open-source code also help.")
qa("{} security considerations?", "Validate inputs, handle errors gracefully, avoid common vulnerabilities like injection attacks, and keep dependencies updated.")
qa("How does {} handle errors?", "Use proper error handling mechanisms. Always validate inputs, raise meaningful exceptions, and provide user-friendly error messages.")

# ── HTML patterns ────────────────────────────────────────────────
HTML_PATTERNS = []
for tag in ["div","span","section","article","nav","header","footer","main","aside","form","table","ul","ol","figure","details","dialog"]:
    HTML_PATTERNS.append(tag)

# ── CSS patterns ──────────────────────────────────────────────────
CSS_PATTERNS = []
for sel, prop, val in [
    (".container", "display", "flex"),
    (".grid", "display", "grid"),
    ("body", "font-family", "Arial, sans-serif"),
    ("h1", "font-size", "2em"),
    ("a", "color", "#0066cc"),
    ("button", "padding", "10px 20px"),
    (".hidden", "display", "none"),
    (".center", "text-align", "center"),
    (".bold", "font-weight", "bold"),
    (".italic", "font-style", "italic"),
    (".card", "border", "1px solid #ddd"),
    (".wrapper", "max-width", "1200px"),
    (".sidebar", "width", "250px"),
    (".modal", "position", "fixed"),
    (".tooltip", "position", "absolute"),
]:
    CSS_PATTERNS.append((sel, prop, val))

# ── Generation ────────────────────────────────────────────────────

def make_name(prefix, i, n=0):
    parts = [prefix]
    if n:
        parts.append(str(n))
    parts.append(str(i))
    return "_".join(parts)

def py_functions(count):
    lines = []
    needs_math = False
    for i in range(1, count + 1):
        cat, nargs, template, keywords = random.choice(PY_PATTERNS)
        args = [random.choice(NOUNS) for _ in range(nargs)]
        name = f"compute_{cat}_{i}"
        desc = f"{random.choice(VERBS).capitalize()} {random.choice(ADJS)} {random.choice(NOUNS)}."
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
        nargs, template, keywords = random.choice(AIS_PATTERNS)
        name = make_name("demo", i)
        desc = f"Demonstrates {random.choice(VERBS)} {random.choice(ADJS)} {random.choice(NOUNS)}"
        body = template.format(name=name, desc=desc)
        lines.append(body)
    return lines

def json_qa(count):
    pairs = []
    words = NOUNS + ADJS + VERBS + TOPICS
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
        tag = random.choice(HTML_PATTERNS)
        snips.append(f"<!-- Container example {i} -->\n<{tag} class=\"box-{i}\" id=\"id-{i}\">\n    <p>Sample content for {tag} #{i}</p>\n</{tag}>\n")
    return snips

def css_rules(count):
    rules = []
    for i in range(1, count + 1):
        sel, prop, val = random.choice(CSS_PATTERNS)
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
