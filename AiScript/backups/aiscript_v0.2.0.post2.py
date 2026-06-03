# ============================================================
# AiScript v0.2.0.post2 - Python-like scripting language
# Single-file interpreter: lexer, parser, AST, evaluator, REPL
# ============================================================
__version__ = "0.2.0.post2"
import sys as _sys, os as _os, random as _random, math as _math, json as _json, time as _time

# ---- TOKEN TYPES ----
_EOF = "EOF"; _NEWLINE = "NEWLINE"; _NUMBER = "NUMBER"; _STRING = "STRING"
_ID = "IDENTIFIER"; _INDENT = "INDENT"; _DEDENT = "DEDENT"
_KW = "KEYWORD"; _OP = "OPERATOR"; _ASSIGN = "ASSIGN"

_KEYWORDS = {"if","elif","else","while","for","in","def","class","return",
             "import","from","as","pass","break","continue","and","or","not",
             "True","False","None","del"}

_OP2TOK = {"+":"PLUS","-":"MINUS","*":"MUL","/":"DIV","%":"MOD","**":"POW",
           "==":"EQ","!=":"NE","<":"LT",">":"GT","<=":"LE",">=":"GE",
           "=":"ASSIGN","+=":"PLUSEQ","-=":"MINUSEQ","*=":"MULEQ","/=":"DIVEQ"}

class _Tok:
    __slots__ = ("type","value","line","col")
    def __init__(self, t, v="", line=0, col=0):
        self.type=t; self.value=v; self.line=line; self.col=col
    def __repr__(self): return "Tok({},{})".format(self.type,self.value)

# ---- LEXER ----
class _Lexer:
    def __init__(self, src):
        self.src=src; self.pos=0; self.line=1; self.col=1; self.ch=src[0] if src else ""
        self._indents=[0]; self._tokens=[]; self._idx=0
    def _adv(self):
        if self.ch: self.col+=1
        self.pos+=1
        if self.pos>=len(self.src): self.ch=""
        else: self.ch=self.src[self.pos]
        if self.ch=="\n": self.line+=1; self.col=1
    def _peek(self, n=0):
        p=self.pos+n+1
        return self.src[p] if 0<=p<len(self.src) else ""
    def _skip_ws(self, break_newline=True):
        while self.ch and self.ch in " \t\r":
            self._adv()
        if break_newline and self.ch=="#":
            while self.ch and self.ch!="\n": self._adv()
    def _read_num(self):
        p=self.pos; dots=0
        while self.ch and (self.ch.isdigit() or (self.ch=="." and self._peek().isdigit() and not dots)):
            if self.ch==".": dots+=1
            self._adv()
        return _Tok(_NUMBER, self.src[p:self.pos], self.line, self.col)
    def _read_str(self, quote):
        raw=""; self._adv()
        while self.ch and self.ch!=quote:
            if self.ch=="\\":
                self._adv()
                if self.ch=="n": raw+="\n"
                elif self.ch=="t": raw+="\t"
                elif self.ch=="\\": raw+="\\"
                elif self.ch==quote: raw+=quote
                else: raw+="\\"+self.ch
            else: raw+=self.ch
            self._adv()
        if self.ch==quote: self._adv()
        return _Tok(_STRING, raw, self.line, self.col)
    def _read_id(self):
        p=self.pos
        while self.ch and (self.ch.isalnum() or self.ch=="_"): self._adv()
        w=self.src[p:self.pos]
        return _Tok(_KW if w in _KEYWORDS else _ID, w, self.line, self.col)
    def _handle_indent(self):
        spaces=0
        while self.ch==" ": spaces+=1; self._adv()
        if self.ch in ("\n","#",""): return
        top=self._indents[-1]
        if spaces>top: self._indents.append(spaces); self._tokens.append(_Tok(_INDENT,line=self.line))
        elif spaces<top:
            while self._indents and spaces<self._indents[-1]:
                self._indents.pop(); self._tokens.append(_Tok(_DEDENT,line=self.line))
            if self._indents and spaces!=self._indents[-1]:
                raise SyntaxError("AiScript: inconsistent indentation line {}".format(self.line))
    def tokenize(self):
        while self.ch:
            self._skip_ws()
            if not self.ch: break
            if self.ch=="\n":
                self._tokens.append(_Tok(_NEWLINE,line=self.line))
                self._adv()
                self._handle_indent()
                continue
            if self.ch.isdigit() or (self.ch=="." and self._peek().isdigit()):
                self._tokens.append(self._read_num()); continue
            if self.ch=="\"" or self.ch=="'":
                self._tokens.append(self._read_str(self.ch)); continue
            if self.ch.isalpha() or self.ch=="_":
                self._tokens.append(self._read_id()); continue
            if self.ch=="=" and self._peek()!="=":
                self._tokens.append(_Tok(_ASSIGN,"=",self.line,self.col))
                self._adv(); continue
            if self.ch in "+-*/%=<>!":
                two=self.ch+self._peek()
                if two in _OP2TOK:
                    self._tokens.append(_Tok(_OP, _OP2TOK[two], self.line, self.col))
                    self._adv(); self._adv(); continue
                one=self.ch
                if one in _OP2TOK:
                    self._tokens.append(_Tok(_OP, _OP2TOK[one], self.line, self.col))
                    self._adv(); continue
            if self.ch=="(": self._tokens.append(_Tok("LPAREN","(",self.line,self.col)); self._adv(); continue
            if self.ch==")": self._tokens.append(_Tok("RPAREN",")",self.line,self.col)); self._adv(); continue
            if self.ch=="[": self._tokens.append(_Tok("LBRACKET","[",self.line,self.col)); self._adv(); continue
            if self.ch=="]": self._tokens.append(_Tok("RBRACKET","]",self.line,self.col)); self._adv(); continue
            if self.ch=="{": self._tokens.append(_Tok("LBRACE","{",self.line,self.col)); self._adv(); continue
            if self.ch=="}": self._tokens.append(_Tok("RBRACE","}",self.line,self.col)); self._adv(); continue
            if self.ch==",": self._tokens.append(_Tok("COMMA",",",self.line,self.col)); self._adv(); continue
            if self.ch==":": self._tokens.append(_Tok("COLON",":",self.line,self.col)); self._adv(); continue
            if self.ch==".": self._tokens.append(_Tok("DOT",".",self.line,self.col)); self._adv(); continue
            if self.ch=="&" and self._peek()=="&": self._tokens.append(_Tok(_OP,"AND",self.line,self.col)); self._adv(); self._adv(); continue
            if self.ch=="|" and self._peek()=="|": self._tokens.append(_Tok(_OP,"OR",self.line,self.col)); self._adv(); self._adv(); continue
            raise SyntaxError("AiScript: unexpected char '{}' line {}".format(self.ch, self.line))
        while len(self._indents)>1: self._indents.pop(); self._tokens.append(_Tok(_DEDENT,line=self.line))
        self._tokens.append(_Tok(_EOF,line=self.line))
        return self._tokens

# ---- AST NODES ----
class _AST: pass

class _Program(_AST):
    __slots__=("stmts",)
    def __init__(self,s): self.stmts=s
class _Number(_AST):
    __slots__=("value",)
    def __init__(self,v): self.value=v
class _String(_AST):
    __slots__=("value",)
    def __init__(self,v): self.value=v
class _Bool(_AST):
    __slots__=("value",)
    def __init__(self,v): self.value=v
class _None(_AST):
    __slots__=()
class _Ident(_AST):
    __slots__=("name",)
    def __init__(self,n): self.name=n
class _BinOp(_AST):
    __slots__=("left","op","right")
    def __init__(self,l,o,r): self.left=l; self.op=o; self.right=r
class _UnaryOp(_AST):
    __slots__=("op","expr")
    def __init__(self,o,e): self.op=o; self.expr=e
class _Assign(_AST):
    __slots__=("targets","value")
    def __init__(self,t,v): self.targets=t; self.value=v
class _AugAssign(_AST):
    __slots__=("target","op","value")
    def __init__(self,t,o,v): self.target=t; self.op=o; self.value=v
class _If(_AST):
    __slots__=("cond","body","orelse")
    def __init__(self,c,b,o): self.cond=c; self.body=b; self.orelse=o
class _While(_AST):
    __slots__=("cond","body")
    def __init__(self,c,b): self.cond=c; self.body=b
class _For(_AST):
    __slots__=("var","iter","body")
    def __init__(self,v,i,b): self.var=v; self.iter=i; self.body=b
class _Break(_AST):
    __slots__=()
class _Continue(_AST):
    __slots__=()
class _Return(_AST):
    __slots__=("value",)
    def __init__(self,v): self.value=v
class _FuncDef(_AST):
    __slots__=("name","params","body")
    def __init__(self,n,p,b): self.name=n; self.params=p; self.body=b
class _Call(_AST):
    __slots__=("func","args")
    def __init__(self,f,a): self.func=f; self.args=a
class _ClassDef(_AST):
    __slots__=("name","body")
    def __init__(self,n,b): self.name=n; self.body=b
class _List(_AST):
    __slots__=("items",)
    def __init__(self,i): self.items=i
class _Dict(_AST):
    __slots__=("pairs",)
    def __init__(self,p): self.pairs=p
class _Subscript(_AST):
    __slots__=("obj","key")
    def __init__(self,o,k): self.obj=o; self.key=k
class _Pass(_AST):
    __slots__=()
class _Delete(_AST):
    __slots__=("expr",)
    def __init__(self,e): self.expr=e
class _Import(_AST):
    __slots__=("names",)
    def __init__(self,n): self.names=n
class _FromImport(_AST):
    __slots__=("module","names")
    def __init__(self,m,n): self.module=m; self.names=n

# ---- PARSER ----
class _ParseError(Exception): pass

class _Parser:
    def __init__(self, tokens):
        self.toks=tokens; self.idx=0
        self._at=lambda: self.toks[self.idx] if self.idx<len(self.toks) else _Tok(_EOF)
    def _peek(self): return self._at().type
    def _peek_val(self): return self._at().value
    def _eat(self, t=None):
        tok=self._at()
        if t and tok.type!=t:
            raise _ParseError("AiScript: expected {} got '{}' line {}".format(t,tok.value,tok.line))
        self.idx+=1
        return tok
    def _skip_newlines(self):
        while self._peek()==_NEWLINE: self.idx+=1
    def _expect(self, t):
        tok=self._at()
        if tok.type!=t: raise _ParseError("AiScript: expected {} got '{}' line {}".format(t,tok.value,tok.line))
        self.idx+=1
        return tok
    def parse(self):
        stmts=self._block()
        self._expect(_EOF)
        return _Program(stmts)
    def _block(self):
        stmts=[]
        while self._peek() not in (_EOF,_DEDENT,_INDENT):
            if self._peek()==_NEWLINE: self.idx+=1; continue
            stmts.append(self._stmt())
            self._skip_newlines()
        return stmts
    def _stmt(self):
        t=self._peek()
        if t==_KW:
            kw=self._peek_val()
            if kw=="if": return self._if_stmt()
            if kw=="while": return self._while_stmt()
            if kw=="for": return self._for_stmt()
            if kw=="def": return self._func_def()
            if kw=="class": return self._class_def()
            if kw=="return": return self._return_stmt()
            if kw=="pass": self.idx+=1; return _Pass()
            if kw=="break": self.idx+=1; return _Break()
            if kw=="continue": self.idx+=1; return _Continue()
            if kw=="import": return self._import_stmt()
            if kw=="from": return self._from_import()
            if kw=="del": return self._del_stmt()
        if t==_ID or t==_NUMBER or t==_STRING or t=="LPAREN" or t=="LBRACKET" or t=="LBRACE" or t=="MINUS" or t=="NOT":
            return self._expr_stmt()
        if t==_OP and self._peek_val()=="NOT":
            return self._expr_stmt()
        raise _ParseError("AiScript: unexpected token '{}' line {}".format(self._peek_val(),self._at().line))
    def _if_stmt(self):
        self._expect(_KW)
        cond=self._expr()
        self._expect("COLON"); self._expect(_NEWLINE); self._expect(_INDENT)
        body=self._block()
        self._expect(_DEDENT)
        return _If(cond,body,self._elif_else())
    def _elif_else(self):
        if self._peek()==_KW and self._peek_val()=="elif":
            self.idx+=1; c=self._expr(); self._expect("COLON")
            self._expect(_NEWLINE); self._expect(_INDENT)
            b=self._block(); self._expect(_DEDENT)
            return [self._elif_chain(c,b)]
        if self._peek()==_KW and self._peek_val()=="else":
            self.idx+=1; self._expect("COLON"); self._expect(_NEWLINE)
            self._expect(_INDENT); b=self._block(); self._expect(_DEDENT)
            return b
        return []
    def _elif_chain(self,cond,body):
        n=self._elif_else()
        if n and len(n)==1 and isinstance(n[0],_If):
            return _If(cond,body,n)
        return _If(cond,body,n)
    def _while_stmt(self):
        self._expect(_KW); cond=self._expr(); self._expect("COLON"); self._expect(_NEWLINE)
        self._expect(_INDENT); body=self._block(); self._expect(_DEDENT)
        return _While(cond,body)
    def _for_stmt(self):
        self._expect(_KW); var=self._expect(_ID).value; self._expect(_KW)  # in
        iter=self._expr(); self._expect("COLON"); self._expect(_NEWLINE); self._expect(_INDENT)
        body=self._block(); self._expect(_DEDENT)
        return _For(var,iter,body)
    def _func_def(self):
        self._expect(_KW); name=self._expect(_ID).value; self._expect("LPAREN")
        params=[]
        if self._peek()!="RPAREN":
            params.append(self._expect(_ID).value)
            while self._peek()=="COMMA": self.idx+=1; params.append(self._expect(_ID).value)
        self._expect("RPAREN"); self._expect("COLON"); self._expect(_NEWLINE); self._expect(_INDENT)
        body=self._block(); self._expect(_DEDENT)
        return _FuncDef(name,params,body)
    def _class_def(self):
        self._expect(_KW); name=self._expect(_ID).value
        self._expect("COLON"); self._expect(_NEWLINE); self._expect(_INDENT)
        body=self._block(); self._expect(_DEDENT)
        return _ClassDef(name,body)
    def _return_stmt(self):
        self._expect(_KW)
        if self._peek() in (_NEWLINE,_DEDENT,_EOF): return _Return(None)
        return _Return(self._expr())
    def _import_stmt(self):
        self._expect(_KW)
        names=[self._expect(_ID).value]
        while self._peek()=="COMMA": self.idx+=1; names.append(self._expect(_ID).value)
        return _Import(names)
    def _from_import(self):
        self._expect(_KW); module=self._expect(_ID).value; self._expect(_KW)  # import
        self._expect(_KW)
        names=[self._expect(_ID).value]
        while self._peek()=="COMMA": self.idx+=1; names.append(self._expect(_ID).value)
        return _FromImport(module,names)
    def _del_stmt(self):
        self._expect(_KW); expr=self._expr()
        return _Delete(expr)
    def _expr_stmt(self):
        expr=self._expr()
        if self._peek()==_ASSIGN:
            targets=[expr]; self.idx+=1; val=self._expr()
            while self._peek()=="COMMA": self.idx+=1; targets.append(self._expr())
            return _Assign(targets,val)
        if self._peek()==_OP and self._peek_val() in ("PLUSEQ","MINUSEQ","MULEQ","DIVEQ"):
            op={"PLUSEQ":"+=","MINUSEQ":"-=","MULEQ":"*=","DIVEQ":"/="}[self._peek_val()]
            self.idx+=1; val=self._expr()
            return _AugAssign(expr,op,val)
        return expr
    def _expr(self):
        return self._or_expr()
    def _or_expr(self):
        left=self._and_expr()
        while self._peek()==_OP and self._peek_val()=="OR":
            self.idx+=1; right=self._and_expr(); left=_BinOp(left,"||",right)
        return left
    def _and_expr(self):
        left=self._not_expr()
        while self._peek()==_OP and self._peek_val()=="AND":
            self.idx+=1; right=self._not_expr(); left=_BinOp(left,"&&",right)
        return left
    def _not_expr(self):
        if self._peek()==_OP and self._peek_val()=="NOT":
            self.idx+=1; return _UnaryOp("not",self._not_expr())
        return self._in_expr()
    def _in_expr(self):
        left=self._cmp_expr()
        if self._peek()==_KW and self._peek_val()=="in":
            self.idx+=1; right=self._cmp_expr()
            return _BinOp(left,"in",right)
        return left
    def _cmp_expr(self):
        left=self._arith_expr()
        if self._peek()==_OP:
            op=self._peek_val()
            if op in ("EQ","NE","LT","GT","LE","GE"):
                self.idx+=1; right=self._arith_expr()
                return _BinOp(left,op,right)
        return left
    def _arith_expr(self):
        left=self._term()
        while self._peek()==_OP:
            op=self._peek_val()
            if op in ("PLUS","MINUS"):
                self.idx+=1; right=self._term(); left=_BinOp(left,op,right)
            else: break
        return left
    def _term(self):
        left=self._power()
        while self._peek()==_OP:
            op=self._peek_val()
            if op in ("MUL","DIV","MOD"):
                self.idx+=1; right=self._power(); left=_BinOp(left,op,right)
            else: break
        return left
    def _power(self):
        left=self._unary()
        if self._peek()==_OP and self._peek_val()=="POW":
            self.idx+=1; right=self._power(); left=_BinOp(left,"**",right)
        return left
    def _unary(self):
        if self._peek()==_OP:
            if self._peek_val()=="MINUS": self.idx+=1; return _UnaryOp("-",self._unary())
        return self._call()
    def _call(self):
        expr=self._primary()
        while True:
            if self._peek()=="LPAREN":
                self.idx+=1; args=[]
                if self._peek()!="RPAREN":
                    args.append(self._expr())
                    while self._peek()=="COMMA": self.idx+=1; args.append(self._expr())
                self._expect("RPAREN")
                expr=_Call(expr,args)
            elif self._peek()=="LBRACKET":
                self.idx+=1; key=self._expr(); self._expect("RBRACKET")
                expr=_Subscript(expr,key)
            elif self._peek()=="DOT":
                self.idx+=1; attr=self._expect(_ID).value
                expr=_Subscript(expr,_String(attr))
            else: break
        return expr
    def _primary(self):
        t=self._peek()
        if t==_NUMBER: v=self._eat(_NUMBER); return _Number(float(v.value) if "." in v.value else int(v.value))
        if t==_STRING: return _String(self._eat(_STRING).value)
        if t==_KW:
            kw=self._peek_val()
            if kw=="True": self.idx+=1; return _Bool(True)
            if kw=="False": self.idx+=1; return _Bool(False)
            if kw=="None": self.idx+=1; return _None()
        if t==_ID: return _Ident(self._eat(_ID).value)
        if t=="LPAREN":
            self.idx+=1; expr=self._expr(); self._expect("RPAREN"); return expr
        if t=="LBRACKET":
            self.idx+=1; items=[]
            if self._peek()!="RBRACKET":
                items.append(self._expr())
                while self._peek()=="COMMA": self.idx+=1; items.append(self._expr())
            self._expect("RBRACKET"); return _List(items)
        if t=="LBRACE":
            self.idx+=1; pairs=[]
            if self._peek()!="RBRACE":
                k=self._expr(); self._expect("COLON"); v=self._expr(); pairs.append((k,v))
                while self._peek()=="COMMA": self.idx+=1; k=self._expr(); self._expect("COLON"); v=self._expr(); pairs.append((k,v))
            self._expect("RBRACE"); return _Dict(pairs)
        raise _ParseError("AiScript: unexpected token '{}' line {}".format(self._peek_val(),self._at().line))

# ---- RUNTIME VALUES ----
class _AiScriptFunc:
    __slots__=("node","env","is_method")
    def __init__(self,node,env,is_method=False):
        self.node=node; self.env=env; self.is_method=is_method
    def __repr__(self): return "<aiscript fn {}>".format(self.node.name)

class _AiScriptClass:
    __slots__=("name","body","env")
    def __init__(self,name,body,env):
        self.name=name; self.body=body; self.env=env
    def __repr__(self): return "<aiscript class {}>".format(self.name)

class _AiScriptInstance:
    __slots__=("cls","attrs")
    def __init__(self,cls):
        self.cls=cls; self.attrs={}
    def __repr__(self): return "<aiscript {} instance>".format(self.cls.name)

class _ReturnSignal(Exception):
    __slots__=("value",)
    def __init__(self,v): self.value=v

class _BreakSignal(Exception): pass
class _ContinueSignal(Exception): pass
class _StopSignal(Exception): pass

# ---- ENVIRONMENT ----
class _Env:
    def __init__(self, parent=None):
        self.bindings={}; self.parent=parent
    def get(self, name):
        if name in self.bindings: return self.bindings[name]
        if self.parent: return self.parent.get(name)
        raise NameError("AiScript: name '{}' not defined".format(name))
    def set(self, name, val):
        if name in self.bindings: self.bindings[name]=val; return
        if self.parent: self.parent.set(name,val); return
        self.bindings[name]=val
    def let(self, name, val):
        self.bindings[name]=val
    def has(self, name): return name in self.bindings or (self.parent and self.parent.has(name))

# ---- EVALUATOR ----
class _Eval:
    def __init__(self):
        self.globals=_Env()
        self._init_builtins()
    def _init_builtins(self):
        g=self.globals
        g.let("True",True); g.let("False",False); g.let("None",None)
        g.let("print",_AiScriptBuiltin("print",_builtin_print))
        g.let("input",_AiScriptBuiltin("input",_builtin_input))
        g.let("len",_AiScriptBuiltin("len",_builtin_len))
        g.let("range",_AiScriptBuiltin("range",_builtin_range))
        g.let("int",_AiScriptBuiltin("int",_builtin_int))
        g.let("str",_AiScriptBuiltin("str",_builtin_str))
        g.let("float",_AiScriptBuiltin("float",_builtin_float))
        g.let("list",_AiScriptBuiltin("list",_builtin_list))
        g.let("dict",_AiScriptBuiltin("dict",_builtin_dict))
        g.let("type",_AiScriptBuiltin("type",_builtin_type))
        g.let("abs",_AiScriptBuiltin("abs",_builtin_abs))
        g.let("min",_AiScriptBuiltin("min",_builtin_min))
        g.let("max",_AiScriptBuiltin("max",_builtin_max))
        g.let("round",_AiScriptBuiltin("round",_builtin_round))
        g.let("sqrt",_AiScriptBuiltin("sqrt",_builtin_sqrt))
        g.let("rand",_AiScriptBuiltin("rand",_builtin_rand))
        g.let("randint",_AiScriptBuiltin("randint",_builtin_randint))
        g.let("append",_AiScriptBuiltin("append",_builtin_append))
        g.let("pop",_AiScriptBuiltin("pop",_builtin_pop))
        g.let("keys",_AiScriptBuiltin("keys",_builtin_keys))
        g.let("values",_AiScriptBuiltin("values",_builtin_values))
        g.let("split",_AiScriptBuiltin("split",_builtin_split))
        g.let("join",_AiScriptBuiltin("join",_builtin_join))
        g.let("open",_AiScriptBuiltin("open",_builtin_open))
        g.let("exit",_AiScriptBuiltin("exit",_builtin_exit))
        g.let("sum",_AiScriptBuiltin("sum",_builtin_sum))
        g.let("any",_AiScriptBuiltin("any",_builtin_any))
        g.let("all",_AiScriptBuiltin("all",_builtin_all))
        g.let("sorted",_AiScriptBuiltin("sorted",_builtin_sorted))
        g.let("reversed",_AiScriptBuiltin("reversed",_builtin_reversed))
        g.let("enumerate",_AiScriptBuiltin("enumerate",_builtin_enumerate))
        g.let("zip",_AiScriptBuiltin("zip",_builtin_zip))
        g.let("isinstance",_AiScriptBuiltin("isinstance",_builtin_isinstance))
        g.let("insert",_AiScriptBuiltin("insert",_builtin_insert))
        g.let("remove",_AiScriptBuiltin("remove",_builtin_remove))
        g.let("sort",_AiScriptBuiltin("sort",_builtin_sort))
        g.let("reverse",_AiScriptBuiltin("reverse",_builtin_reverse))
        g.let("clear",_AiScriptBuiltin("clear",_builtin_clear))
        g.let("items",_AiScriptBuiltin("items",_builtin_items))
        g.let("dict_get",_AiScriptBuiltin("dict_get",_builtin_dict_get))
        g.let("update",_AiScriptBuiltin("update",_builtin_update))
        g.let("upper",_AiScriptBuiltin("upper",_builtin_upper))
        g.let("lower",_AiScriptBuiltin("lower",_builtin_lower))
        g.let("strip",_AiScriptBuiltin("strip",_builtin_strip))
        g.let("replace",_AiScriptBuiltin("replace",_builtin_replace))
        g.let("startswith",_AiScriptBuiltin("startswith",_builtin_startswith))
        g.let("endswith",_AiScriptBuiltin("endswith",_builtin_endswith))
        g.let("find",_AiScriptBuiltin("find",_builtin_find))
        g.let("capitalize",_AiScriptBuiltin("capitalize",_builtin_capitalize))
    def eval(self, node, env=None):
        if env is None: env=self.globals
        t=type(node)
        if t is _Program:
            r=None
            for s in node.stmts: r=self.eval(s,env)
            return r
        if t is _Number: return node.value
        if t is _String: return node.value
        if t is _Bool: return node.value
        if t is _None: return None
        if t is _Ident: return env.get(node.name)
        if t is _BinOp:
            l=self.eval(node.left,env); r=self.eval(node.right,env)
            op=node.op
            if op=="PLUS": return l+r
            if op=="MINUS": return l-r
            if op=="MUL": return l*r
            if op=="DIV":
                if isinstance(l,int) and isinstance(r,int): return l//r
                return l/r
            if op=="MOD": return l%r
            if op=="POW": return l**r
            if op=="EQ": return l==r
            if op=="NE": return l!=r
            if op=="LT": return l<r
            if op=="GT": return l>r
            if op=="LE": return l<=r
            if op=="GE": return l>=r
            if op=="&&": return l and r
            if op=="||": return l or r
            if op=="in": return l in r
            raise TypeError("AiScript: unknown operator {}".format(op))
        if t is _UnaryOp:
            v=self.eval(node.expr,env)
            if node.op=="-": return -v
            if node.op=="not": return not v
        if t is _Assign:
            val=self.eval(node.value,env)
            for tgt in node.targets:
                if isinstance(tgt,_Ident): env.set(tgt.name,val)
                elif isinstance(tgt,_Subscript):
                    obj=self.eval(tgt.obj,env)
                    key=self.eval(tgt.key,env)
                    obj[key]=val
            return val
        if t is _AugAssign:
            target=self.eval(node.target,env)
            val=self.eval(node.value,env)
            op=node.op
            if op=="+=": nv=target+val
            elif op=="-=": nv=target-val
            elif op=="*=": nv=target*val
            elif op=="/=":
                if isinstance(target,int) and isinstance(val,int): nv=target//val
                else: nv=target/val
            if isinstance(node.target,_Ident): env.set(node.target.name,nv)
            elif isinstance(node.target,_Subscript):
                obj=self.eval(node.target.obj,env); key=self.eval(node.target.key,env); obj[key]=nv
            return nv
        if t is _If:
            if self.eval(node.cond,env): return self._exec_block(node.body,env)
            elif node.orelse: return self._exec_block(node.orelse,env)
            return None
        if t is _While:
            r=None
            while self.eval(node.cond,env):
                try: r=self._exec_block(node.body,env)
                except _BreakSignal: break
                except _ContinueSignal: continue
            return r
        if t is _For:
            r=None; iterable=self.eval(node.iter,env)
            for item in iterable:
                env.set(node.var,item)
                try: r=self._exec_block(node.body,env)
                except _BreakSignal: break
                except _ContinueSignal: continue
            return r
        if t is _Break: raise _BreakSignal()
        if t is _Continue: raise _ContinueSignal()
        if t is _Return: raise _ReturnSignal(self.eval(node.value,env) if node.value is not None else None)
        if t is _FuncDef:
            f=_AiScriptFunc(node,env)
            env.set(node.name,f)
            return f
        if t is _Call:
            func=self.eval(node.func,env)
            args=[self.eval(a,env) for a in node.args]
            if isinstance(func,_AiScriptBuiltin): return func.fn(*args)
            if isinstance(func,_AiScriptFunc):
                new_env=_Env(func.env)
                params=func.node.params
                if func.is_method:
                    obj=env.get("self") if env.has("self") else None
                    if obj is not None:
                        new_env.let("self",obj)
                for p,a in zip(params,args): new_env.let(p,a)
                try: self._exec_block(func.node.body,new_env); return None
                except _ReturnSignal as e: return e.value
            if isinstance(func,_AiScriptClass):
                inst=_AiScriptInstance(func)
                init_env=_Env(func.env)
                init_env.let("self",inst)
                for s in func.body:
                    if isinstance(s,_FuncDef):
                        f=_AiScriptFunc(s,init_env,is_method=True)
                        init_env.let(s.name,f)
                        inst.attrs[s.name]=f
                    elif isinstance(s,_Assign):
                        val=self.eval(s.value,init_env)
                        for tgt in s.targets:
                            if isinstance(tgt,_Ident):
                                if tgt.name!="self": inst.attrs[tgt.name]=val
                    else: self.eval(s,init_env)
                if "init" in inst.attrs:
                    self._call_method(inst,"init",args)
                return inst
            if isinstance(func,_AiScriptInstance):
                if node.func.name in func.attrs:
                    m=func.attrs[node.func.name]
                    if isinstance(m,_AiScriptFunc):
                        new_env=_Env(m.env)
                        new_env.let("self",func)
                        for p,a in zip(m.node.params,args): new_env.let(p,a)
                        try: self._exec_block(m.node.body,new_env); return None
                        except _ReturnSignal as e: return e.value
                raise TypeError("AiScript: '{}' has no method '{}'".format(type(func).__name__,node.func.name))
            if callable(func): return func(*args)
            raise TypeError("AiScript: cannot call '{}'".format(type(func).__name__))
        if t is _ClassDef:
            cls=_AiScriptClass(node.name,node.body,env)
            env.set(node.name,cls)
            return cls
        if t is _List:
            return [self.eval(i,env) for i in node.items]
        if t is _Dict:
            return {self.eval(k,env):self.eval(v,env) for k,v in node.pairs}
        if t is _Subscript:
            obj=self.eval(node.obj,env)
            key=self.eval(node.key,env)
            if isinstance(key,str) and hasattr(obj,key):
                attr=getattr(obj,key)
                if callable(attr): return attr
                return attr
            return obj[key]
        if t is _Delete:
            obj=self.eval(node.expr,env)
            if isinstance(node.expr,_Ident):
                n=node.expr.name
                e = env
                while e:
                    if n in e.bindings: del e.bindings[n]; return None
                    e = e.parent
                raise NameError("AiScript: name '{}' not defined".format(n))
            if isinstance(node.expr,_Subscript):
                o=self.eval(node.expr.obj,env); k=self.eval(node.expr.key,env)
                del o[k]; return None
            raise TypeError("AiScript: cannot delete '{}'".format(type(obj).__name__))
        if t is _Pass: return None
        if t is _Import:
            for name in node.names:
                self._import_module(name,env)
            return None
        if t is _FromImport:
            self._import_module(node.module,env,node.names)
            return None
        raise TypeError("AiScript: unknown AST node {}".format(t.__name__))
    def _call_method(self, inst, name, args):
        if name in inst.attrs:
            m=inst.attrs[name]
            if isinstance(m,_AiScriptFunc):
                new_env=_Env(m.env); new_env.let("self",inst)
                for p,a in zip(m.node.params,args): new_env.let(p,a)
                try: self._exec_block(m.node.body,new_env); return None
                except _ReturnSignal as e: return e.value
    def _exec_block(self, stmts, env):
        r=None
        for s in stmts:
            if getattr(self, '_stop_flag', None) and self._stop_flag.is_set():
                raise _StopSignal()
            r=self.eval(s,env)
        return r
    def _import_module(self, name, env, names=None):
        mod=_AiScriptModule(name,self)
        env.let(name,mod)
        if names:
            for n in names: env.let(n, getattr(mod,n))

class _AiScriptModule:
    def __init__(self, name, evaluator):
        self.name=name; self._eval=evaluator
        self._load()
    def _load(self):
        if self.name=="math":
            self.sqrt=_AiScriptBuiltin("sqrt",_builtin_sqrt)
            self.sin=_AiScriptBuiltin("sin",lambda x: _math.sin(x))
            self.cos=_AiScriptBuiltin("cos",lambda x: _math.cos(x))
            self.abs=_AiScriptBuiltin("abs",_builtin_abs)
            self.floor=_AiScriptBuiltin("floor",lambda x: int(_math.floor(x)))
            self.ceil=_AiScriptBuiltin("ceil",lambda x: int(_math.ceil(x)))
        elif self.name=="random":
            self.rand=_AiScriptBuiltin("rand",_builtin_rand)
            self.randint=_AiScriptBuiltin("randint",_builtin_randint)
            self.seed=_AiScriptBuiltin("seed",lambda s=None: _random.seed(s))
        elif self.name=="os":
            self.cwd=_AiScriptBuiltin("cwd",lambda: _os.getcwd())
            self.ls=_AiScriptBuiltin("ls",lambda d=".": _os.listdir(d))
            self.cmd=_AiScriptBuiltin("cmd",lambda c: _os.system(c))
            self.exists=_AiScriptBuiltin("exists",lambda p: _os.path.exists(p))
        elif self.name=="json":
            self.dumps=_AiScriptBuiltin("dumps",lambda o: _json.dumps(o))
            self.loads=_AiScriptBuiltin("loads",lambda s: _json.loads(s))
            def _ai_json_dump(o, f):
                with open(f, "w") as fp: _json.dump(o, fp)
            def _ai_json_load(f):
                with open(f) as fp: return _json.load(fp)
            self.dump=_AiScriptBuiltin("dump", _ai_json_dump)
            self.load=_AiScriptBuiltin("load", _ai_json_load)
        elif self.name=="time":
            self.time=_AiScriptBuiltin("time",lambda: _time.time())
            self.sleep=_AiScriptBuiltin("sleep",lambda s: _time.sleep(s))
        elif self.name=="sys":
            self.argv=_sys.argv
            self.exit=_AiScriptBuiltin("exit",_builtin_exit)
    def __repr__(self): return "<aiscript module '{}'>".format(self.name)

class _AiScriptBuiltin:
    __slots__=("name","fn")
    def __init__(self,n,f): self.name=n; self.fn=f
    def __repr__(self): return "<builtin {}>".format(self.name)

# ---- BUILTIN FUNCTIONS ----
def _builtin_print(*a): print(*a)
def _builtin_input(p=""): return input(p)
def _builtin_len(x): return len(x)
def _builtin_range(*a): return list(range(*a))
def _builtin_int(x): return int(x)
def _builtin_str(x): return str(x)
def _builtin_float(x): return float(x)
def _builtin_list(x=None): return list(x) if x is not None else []
def _builtin_dict(x=None): return dict(x) if x is not None else {}
def _builtin_type(x):
    if isinstance(x,int): return "int"
    if isinstance(x,float): return "float"
    if isinstance(x,str): return "str"
    if isinstance(x,list): return "list"
    if isinstance(x,dict): return "dict"
    if isinstance(x,bool): return "bool"
    if x is None: return "NoneType"
    if isinstance(x,_AiScriptInstance): return x.cls.name
    return type(x).__name__
def _builtin_abs(x): return abs(x)
def _builtin_min(*a): return min(*a) if len(a)>1 else min(a[0])
def _builtin_max(*a): return max(*a) if len(a)>1 else max(a[0])
def _builtin_round(x,n=0): return round(x,n)
def _builtin_sqrt(x): return _math.sqrt(x)
def _builtin_rand(): return _random.random()
def _builtin_randint(a,b): return _random.randint(a,b)
def _builtin_append(l,v): l.append(v); return l
def _builtin_pop(l,i=-1): return l.pop(i)
def _builtin_keys(d): return list(d.keys())
def _builtin_values(d): return list(d.values())
def _builtin_split(s,sep=None): return s.split(sep) if sep else s.split()
def _builtin_join(sep,l): return sep.join(str(x) for x in l)
def _builtin_open(path,mode="r"):
    try:
        with open(path,mode) as f: return f.read()
    except Exception as e: raise IOError("AiScript: cannot open '{}': {}".format(path,e))
def _builtin_exit(c=0): _sys.exit(c)
def _builtin_sum(x): return sum(x)
def _builtin_any(x): return any(x)
def _builtin_all(x): return all(x)
def _builtin_sorted(x): return sorted(x)
def _builtin_reversed(x): return list(reversed(x))
def _builtin_enumerate(x): return list(enumerate(x))
def _builtin_zip(*a): return list(zip(*a))
def _builtin_isinstance(x,t):
    if t=="int": return isinstance(x,int)
    if t=="float": return isinstance(x,float)
    if t=="str": return isinstance(x,str)
    if t=="list": return isinstance(x,list)
    if t=="dict": return isinstance(x,dict)
    if t=="bool": return isinstance(x,bool)
    return False
def _builtin_insert(l,i,v): l.insert(i,v); return l
def _builtin_remove(l,v): l.remove(v); return l
def _builtin_sort(l): l.sort(); return l
def _builtin_reverse(l): l.reverse(); return l
def _builtin_clear(l): l.clear(); return l
def _builtin_items(d): return list(d.items())
def _builtin_dict_get(d,k,default=None): return d.get(k,default)
def _builtin_update(d,o): d.update(o); return d
def _builtin_upper(s): return s.upper()
def _builtin_lower(s): return s.lower()
def _builtin_strip(s): return s.strip()
def _builtin_replace(s,old,new): return s.replace(old,new)
def _builtin_startswith(s,p): return s.startswith(p)
def _builtin_endswith(s,p): return s.endswith(p)
def _builtin_find(s,p): return s.find(p)
def _builtin_capitalize(s): return s.capitalize()

# ---- REPL ----
def repl():
    e=_Eval(); print("AiScript v{} - type 'exit()' to quit".format(__version__))
    src=""
    while True:
        try:
            line=input(">>> " if not src else "... ")
            src+=line+"\n"
            if line and (line.rstrip().endswith(":") or line.startswith(" ") or line.startswith("\t") or src.count("\n")>1 and not line.strip()): continue
            if not src.strip(): continue
            tokens=_Lexer(src).tokenize()
            ast=_Parser(tokens).parse()
            r=e.eval(ast)
            if r is not None: print(r)
            src=""
        except _ParseError as ex: print("SyntaxError:",ex); src=""
        except SyntaxError as ex: print("SyntaxError:",ex); src=""
        except EOFError: break
        except KeyboardInterrupt: print("\nInterrupted"); src=""
        except Exception as ex: print("Error:",ex); src=""

# ---- CLI ----
def run_file(path):
    try:
        with open(path,encoding="utf-8") as f: src=f.read()
        tokens=_Lexer(src).tokenize()
        ast=_Parser(tokens).parse()
        e=_Eval()
        e.eval(ast)
    except _ParseError as ex: _sys.stderr.write("SyntaxError: {}\n".format(ex)); _sys.exit(1)
    except SyntaxError as ex: _sys.stderr.write("SyntaxError: {}\n".format(ex)); _sys.exit(1)
    except Exception as ex: _sys.stderr.write("Error: {}\n".format(ex)); _sys.exit(1)

def main():
    if len(_sys.argv)>1 and _sys.argv[1] in ("-h","--help"):
        print("Usage: python aiscript.py [file.ais] [args...]")
        print("       python aiscript.py          (REPL)")
    elif len(_sys.argv)>1:
        _sys.ais_argv = _sys.argv[2:]
        run_file(_sys.argv[1])
    else:
        repl()

if __name__=="__main__":
    main()
