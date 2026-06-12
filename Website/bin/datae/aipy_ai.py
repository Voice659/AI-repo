import os, json, re

_TRAINING_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Training_data')

class _AIModel:
    def __init__(self):
        self._qa_pairs = []
        self._code_examples = []
        self._ready = False

    def load(self):
        self._qa_pairs = []
        self._code_examples = []
        if not os.path.isdir(_TRAINING_DIR):
            return False
        for fname in os.listdir(_TRAINING_DIR):
            path = os.path.join(_TRAINING_DIR, fname)
            if not os.path.isfile(path):
                continue
            if fname.endswith('.ais'):
                self._load_ais(path)
            elif fname.endswith('.json'):
                self._load_json(path)
            elif fname.endswith('.py'):
                self._load_py(path)
            elif fname.endswith('.html'):
                self._load_html(path)
            elif fname.endswith('.css'):
                self._load_css(path)
        self._ready = bool(self._qa_pairs or self._code_examples)
        return self._ready

    def _load_ais(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        for match in re.finditer(r'def\s+(\w+)\s*\([^)]*\)\s*:\n\s*//(.+)', content):
            name = match.group(1)
            doc = match.group(2).strip()
            lines = content[match.start():].split('\n')
            body = []
            indent = None
            for line in lines:
                if indent is None and line.strip():
                    indent = len(line) - len(line.lstrip())
                if indent is not None and line.strip() and len(line) - len(line.lstrip()) < indent and not line.strip().startswith('//'):
                    break
                body.append(line)
            code = '\n'.join(body)
            kw = set(re.findall(r'\w+', doc.lower()))
            kw.add(name.lower())
            self._code_examples.append({'name': name, 'doc': doc, 'code': code, 'keywords': kw})

    def _load_json(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for item in data:
            q = item.get('question', '')
            a = item.get('answer', '')
            kw = set(w.lower() for w in item.get('keywords', []))
            kw.update(re.findall(r'\w+', q.lower()))
            self._qa_pairs.append({'question': q, 'answer': a, 'keywords': kw})

    def _load_py(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        for match in re.finditer(r'((?:def|class)\s+\w+[^:]*:.*?)(?=\n\S|\Z)', content, re.DOTALL):
            block = match.group(1).strip()
            name_m = re.match(r'(?:def|class)\s+(\w+)', block)
            if not name_m:
                continue
            name = name_m.group(1)
            doc_m = re.search(r'"""(.*?)"""', block, re.DOTALL)
            doc = doc_m.group(1).strip() if doc_m else ''
            kw = set(re.findall(r'\w+', (doc + ' ' + name).lower()))
            for c_m in re.finditer(r'# (.+)', block):
                kw.update(re.findall(r'\w+', c_m.group(1).lower()))
            self._code_examples.append({'name': name, 'doc': doc, 'code': block, 'keywords': kw})

    def _load_html(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Extract <pre>/<code> blocks as code examples
        for match in re.finditer(r'<(?:pre|code)[^>]*>(.*?)</(?:pre|code)>', content, re.DOTALL | re.IGNORECASE):
            code = match.group(1).strip()
            lines = [l for l in code.split('\n') if l.strip()]
            if not lines:
                continue
            kw = set(re.findall(r'\w+', code.lower()))
            self._code_examples.append({'name': 'html_code', 'doc': code[:60], 'code': code, 'keywords': kw})
        # Extract comments
        for match in re.finditer(r'<!--(.*?)-->', content, re.DOTALL):
            text = match.group(1).strip()
            if text:
                kw = set(re.findall(r'\w+', text.lower()))
                self._code_examples.append({'name': 'html_comment', 'doc': text[:60], 'code': text, 'keywords': kw})

    def _load_css(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        for match in re.finditer(r'([^}]+?\{[^}]+\})', content):
            rule = match.group(1).strip()
            if not rule:
                continue
            sel_m = re.match(r'([^{]+)', rule)
            sel = sel_m.group(1).strip() if sel_m else ''
            kw = set(re.findall(r'\w+', rule.lower()))
            self._code_examples.append({'name': sel, 'doc': sel, 'code': rule, 'keywords': kw})
        for match in re.finditer(r'/\*(.*?)\*/', content, re.DOTALL):
            text = match.group(1).strip()
            if text:
                kw = set(re.findall(r'\w+', text.lower()))
                self._code_examples.append({'name': 'css_comment', 'doc': text[:60], 'code': text, 'keywords': kw})

    def ask(self, query):
        if not self._ready:
            return "AI not trained. Use 'ai_train' first."
        qw = set(re.findall(r'\w+', query.lower()))
        best = ('', 0, None)
        for qa in self._qa_pairs:
            s = len(qw & qa['keywords'])
            if s > best[1]:
                best = (qa['answer'], s, 'qa')
        for ex in self._code_examples:
            s = len(qw & ex['keywords'])
            if s > best[1]:
                best = (ex, s, 'code')
        if best[2] is None:
            return "I don't know. Try 'ai_train' to reload data, or rephrase."
        if best[2] == 'code':
            ex = best[0]
            return "Code example: {}\n\n{}".format(ex['name'], ex['code'])
        return best[0]

    def reload(self):
        self._ready = self.load()
        return self._ready

_ai = _AIModel()
_ai.load()

def ask(query):
    return _ai.ask(query)

def reload():
    return _ai.reload()
