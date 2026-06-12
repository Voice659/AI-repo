import os, json, random, itertools

OUT = os.path.dirname(os.path.abspath(__file__))
random.seed(42)

# ── Word pools for variety ──────────────────────────────────────────
NOUNS = "array list dict set string number integer float boolean byte char file stream buffer socket port protocol packet frame angle axis vector matrix pixel sample signal wave pulse amplitude frequency voltage current resistor capacitor transistor diode led motor sensor actuator robot drone camera lens filter kernel layer node edge graph tree heap queue stack pipe process thread task job event handler callback promise stream chunk blob column row table index key value pair tuple record field attribute property method class object instance module package library framework tool utility script program app service daemon agent broker proxy gateway tunnel cable wire bus connector pin header socket plug adapter converter encoder decoder parser lexer token ast ir optimizer compiler interpreter vm runtime kernel shell terminal console monitor display screen window panel dialog button menu tab bar slider knob switch relay fuse breaker wire cable antenna satellite beacon radar sonar lidar scanner imager spectrometer microscope telescope binocular periscope gyro compass beacon lighthouse flare signal symbol code cipher key hash salt pepper iv nonce tag mac sig cert ca root leaf chain link ring circle sphere cube cone cylinder prism pyramid torus knot braid weave fabric thread yarn fiber cloth garment hat shoe glove sock belt buckle zipper button lace strap handle grip knob lever pedal crank wheel axle shaft gear belt chain sprocket cam pin joint hinge pivot bearing bushing seal gasket ring o-ring washer nut bolt screw nail rivet clamp bracket mount frame chassis housing cover lid door hatch window panel screen mesh grill vent duct pipe tube hose nozzle tip blade cutter shear punch die mold cast forge weld solder braze glue tape adhesive fastener anchor tie wrap coil spring damper piston rod cylinder tank vessel boiler heater cooler chiller pump fan blower compressor turbine engine motor generator alternator dynamo converter inverter rectifier chopper cycloconverter matrix vector tensor scalar spin charge flux field wave particle photon electron proton neutron atom molecule compound element alloy composite ceramic polymer plastic resin rubber foam gel crystal glass ceramic porcelain tile brick stone concrete mortar plaster paint coating finish polish wax oil grease lubricant coolant refrigerant solvent acid base salt buffer solution mixture blend compound formula equation expression variable constant parameter argument return yield throw raise catch finally except else elif if while for in range len map filter reduce zip enumerate sorted reversed min max sum abs pow round floor ceil trunc sqrt exp log sin cos tan asin acos atan sinh cosh tanh degrees radians hypot gcd lcm factorial comb perm prod cumsum cumprod diff gradient jacobian hessian laplacian div grad curl dot cross norm trace det inv solve eig svd qr lu cholesky fft ifft dct idct wavelet filter convolution correlation mean median mode var std cov pearson spearman kendall entropy mi kl js wasserstein emd mse mae rmse nse kge r2 adj_r2 aic bic mle map bayes mcmc gibbs metropolis hmc nuts sgd adam rmsprop momentum nag adagrad adadelta adamax nadam radam lamb lookahead sam swa ema f1 precision recall accuracy auc roc pr logloss hinge huber epsilon squared absolute quantile poisson gamma tweedie custom".split()

ADJECTIVES = "fast slow quick rapid swift sudden gradual steady constant variable dynamic static active passive direct indirect linear nonlinear convex concave increasing decreasing growing shrinking expanding contracting rising falling floating sinking climbing sliding rolling spinning twisting bending folding breaking cracking splitting joining merging connecting linking binding tying wrapping covering hiding revealing showing displaying presenting representing depicting illustrating demonstrating explaining describing defining classifying grouping sorting ordering ranking rating scoring grading leveling balancing aligning adjusting tuning calibrating measuring testing verifying validating checking inspecting scanning examining studying analyzing evaluating assessing comparing contrasting differentiating discriminating selecting choosing picking filtering screening sorting ordering ranking rating scoring grading leveling".split()

VERBS = "calculate compute evaluate solve determine find derive generate create build construct form shape design plan prepare produce make do perform execute run process handle manage control operate drive move shift turn rotate scale translate transform convert encode decode encrypt decrypt hash sign verify authenticate authorize validate check test run debug profile trace log monitor watch observe measure sample collect gather accumulate aggregate summarize report display show print write read load save store cache buffer stream pipe filter map reduce sort search find locate match compare merge split join flatten expand compress pack unpack serialize deserialize marshal unmarshal parse tokenize lex analyze compile interpret execute run evaluate render paint draw plot graph chart map project transform warp distort displace displace wrap fold unfold roll unroll spin twist bend curve straighten level align center justify distribute space arrange order sort rank rate score grade mark label tag name classify categorize group cluster segment partition separate divide split isolate extract filter prune cut trim clip crop resize scale zoom pan tilt dolly track follow chase hunt seek find locate pinpoint focus".split()

TOPICS = "math algebra geometry calculus trigonometry statistics probability linear algebra calculus differential equations number theory combinatorics graph theory topology optimization algorithms data structures sorting searching recursion dynamic programming greedy divide conquer backtracking branch bound network flow string matching pattern recognition machine learning deep learning neural networks computer vision natural language processing reinforcement learning databases sql nosql indexing querying modeling design normalisation transactions concurrency security cryptography authentication authorization networking protocols routing switching addressing subnets firewalls vpns dns http tcp ip udp rest graphql websockets operating systems processes threads memory management scheduling file systems io devices drivers embedded systems robotics control systems signal processing image processing audio processing video processing game development physics simulation rendering shaders animation".split()

# ── Generators ──────────────────────────────────────────────────────

def py_functions(count):
    """Generate Python function definitions with docstrings."""
    lines = []
    topics_list = list(TOPICS)
    for i in range(1, count + 1):
        topic = random.choice(topics_list)
        noun = random.choice(NOUNS)
        adj = random.choice(ADJECTIVES)
        verb = random.choice(VERBS)
        name = f"{verb}_{adj}_{noun}_{i}"
        doc = f"{verb.capitalize()} {adj} {noun}. Topic: {topic}."
        body = f"    # {topic} operation\n    result = {noun}\n    return result"
        lines.append(f"def {name}():\n    \"\"\"{doc}\"\"\"\n{body}\n")
    return lines

def ais_functions(count):
    """Generate AiScript function definitions with // comments."""
    lines = []
    for i in range(1, count + 1):
        noun = random.choice(NOUNS)
        adj = random.choice(ADJECTIVES)
        verb = random.choice(VERBS)
        name = f"{verb}_{adj}_{noun}_{i}"
        doc = f"{verb.capitalize()} {adj} {noun}"
        lines.append(f"def {name}():\n    //{doc}\n    print(\"{doc}\")\n")
    return lines

def json_qa(count):
    """Generate JSON Q&A pairs."""
    pairs = []
    topics = list(TOPICS)
    for i in range(1, count + 1):
        topic = random.choice(topics)
        noun = random.choice(NOUNS)
        adj = random.choice(ADJECTIVES)
        verb = random.choice(VERBS)
        q = f"What is {adj} {noun} in {topic}?"
        a = f"{adj.capitalize()} {noun} in {topic} is used for {verb} operations. It is an important concept."
        kw = [topic, noun, adj, verb]
        pairs.append({"question": q, "answer": a, "keywords": kw})
    return pairs

def html_snippets(count):
    """Generate HTML snippets with comments."""
    snips = []
    tags = ["div", "span", "section", "article", "nav", "header", "footer", "main", "aside", "form", "table", "ul", "ol", "dl", "figure", "details", "summary", "dialog", "template", "canvas"]
    attrs = ["class", "id", "style", "data-*", "role", "aria-*", "href", "src", "alt", "title", "rel", "target", "type", "name", "value", "placeholder", "required", "disabled", "readonly", "checked", "selected"]
    for i in range(1, count + 1):
        tag = random.choice(tags)
        attr = random.choice(attrs)
        comment = f" HTML {tag} element with {attr} attribute "
        snips.append(f"<!--{comment}-->\n<{tag} {attr}=\"example-{i}\">Content {i}</{tag}>\n")
    return snips

def css_rules(count):
    """Generate CSS rules with comments."""
    rules = []
    selectors = [".class", "#id", "element", "[attr]", ":pseudo", "::before", "::after", "> child", "+ sibling", "~ general"]
    properties = ["display", "position", "margin", "padding", "color", "background", "font-size", "border", "width", "height", "flex", "grid", "transform", "animation", "transition", "opacity", "z-index", "overflow", "cursor", "box-shadow"]
    values = ["flex", "grid", "block", "inline", "absolute", "relative", "fixed", "10px", "1rem", "auto", "100%", "red", "blue", "none", "hidden", "scroll", "center", "bold", "italic", "underline"]
    for i in range(1, count + 1):
        sel = random.choice(selectors)
        prop = random.choice(properties)
        val = random.choice(values)
        comment = f" CSS rule for {sel} with {prop} "
        rules.append(f"/*{comment}*/\n{sel}-{i} {{\n    {prop}: {val};\n}}\n")
    return rules

# ── Write files ─────────────────────────────────────────────────────

def write_chunked(path, lines, chunk_size=5000):
    """Write content, splitting into chunks if too large."""
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
    written = write_chunked(os.path.join(OUT, "coding_basics.py"), py_lines, 5000)
    print(f"  -> {', '.join(written)} ({len(py_lines)} functions)")

    print("Generating 10000+ .ais functions...")
    ais_lines = ais_functions(10100)
    written = write_chunked(os.path.join(OUT, "python_coding.ais"), ais_lines, 5000)
    print(f"  -> {', '.join(written)} ({len(ais_lines)} functions)")

    print("Generating 100000+ .json Q&A pairs...")
    qa = json_qa(100100)
    with open(os.path.join(OUT, "general_knowledge.json"), 'w', encoding='utf-8') as f:
        json.dump(qa, f, indent=2, ensure_ascii=False)
    print(f"  -> general_knowledge.json ({len(qa)} pairs)")

    print("Generating 1000+ .html snippets...")
    html_lines = html_snippets(1050)
    written = write_chunked(os.path.join(OUT, "html_basics.html"), html_lines)
    print(f"  -> {', '.join(written)} ({len(html_lines)} snippets)")

    print("Generating 1000+ .css rules...")
    css_lines = css_rules(1050)
    written = write_chunked(os.path.join(OUT, "css_basics.css"), css_lines)
    print(f"  -> {', '.join(written)} ({len(css_lines)} rules)")

    print("Done!")

if __name__ == "__main__":
    main()
