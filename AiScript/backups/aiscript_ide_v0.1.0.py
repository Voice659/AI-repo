"""AiScript IDE — A lightweight code editor + runner for AiScript (.ais files)
   Inspired by Python's IDLE, built with tkinter."""
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import sys, os, threading, queue

# Add project dir to path so aiscript can be imported
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if _SCRIPT_DIR not in sys.path: sys.path.insert(0, _SCRIPT_DIR)

import aiscript

__version__ = "0.1.0"

BG = "#1e1e1e"          # editor background
FG = "#d4d4d4"          # default text
LINE_BG = "#252526"     # line number background
LINE_FG = "#858585"     # line number color
CONSOLE_BG = "#0d1117"  # console background
CONSOLE_FG = "#c9d1d9"
KEYWORD_COLOR = "#569cd6"
STRING_COLOR = "#ce9178"
NUMBER_COLOR = "#b5cea8"
COMMENT_COLOR = "#6a9955"
BUILTIN_COLOR = "#dcdcaa"
FONT = ("Consolas", 11)


class AiScriptIDE:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AiScript IDE v{}".format(__version__))
        self.root.geometry("900x650")
        self.root.minsize(600, 400)
        self.current_file = None
        self.modified = False
        self.output_queue = queue.Queue()
        self._build_ui()
        self._setup_menu()
        self._setup_bindings()
        self._poll_output()
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    # ── UI ──────────────────────────────────────────────
    def _build_ui(self):
        # Main paned window: editor (top) + console (bottom)
        self.paned = tk.PanedWindow(self.root, orient=tk.VERTICAL, bg="#252526",
                                     sashwidth=4, sashrelief=tk.FLAT)
        self.paned.pack(fill=tk.BOTH, expand=True)

        # ── Editor frame with line numbers ──
        editor_frame = tk.Frame(self.paned, bg=BG)
        self.paned.add(editor_frame, height=400)

        # Line number canvas
        self.line_numbers = tk.Canvas(editor_frame, width=50, bg=LINE_BG,
                                      highlightthickness=0)
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        # Text widget
        self.text = tk.Text(editor_frame, font=FONT, bg=BG, fg=FG,
                            insertbackground=FG, wrap=tk.NONE,
                            relief=tk.FLAT, bd=0, padx=8, pady=6,
                            undo=True, maxundo=100,
                            highlightthickness=0)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbars
        v_scroll = tk.Scrollbar(editor_frame, orient=tk.VERTICAL,
                                command=self._scroll_v)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.config(yscrollcommand=self._sync_vscroll)

        h_scroll = tk.Scrollbar(self.root, orient=tk.HORIZONTAL,
                                command=self.text.xview)
        self.text.config(xscrollcommand=h_scroll.set)
        h_scroll.pack(fill=tk.X, before=self.paned)

        # ── Console frame ──
        console_frame = tk.Frame(self.paned, bg=CONSOLE_BG)
        self.paned.add(console_frame, height=180)

        console_header = tk.Frame(console_frame, bg="#161b22")
        console_header.pack(fill=tk.X)
        tk.Label(console_header, text=" OUTPUT ", font=("Consolas", 8, "bold"),
                 fg="#58a6ff", bg="#161b22").pack(side=tk.LEFT, padx=6)
        self.run_btn = tk.Button(console_header, text="Run (F5)",
                                 font=("Segoe UI", 8, "bold"),
                                 bg="#238636", fg="white", relief=tk.FLAT,
                                 padx=10, cursor="hand2", command=self._run_code)
        self.run_btn.pack(side=tk.RIGHT, padx=4, pady=2)
        tk.Button(console_header, text="Clear", font=("Segoe UI", 8),
                  bg="#21262d", fg="#c9d1d9", relief=tk.FLAT, padx=8,
                  cursor="hand2", command=self._clear_console).pack(side=tk.RIGHT, padx=4, pady=2)

        self.console = tk.Text(console_frame, font=("Consolas", 10),
                               bg=CONSOLE_BG, fg=CONSOLE_FG,
                               relief=tk.FLAT, bd=0, padx=6, pady=4,
                               state=tk.DISABLED, wrap=tk.WORD,
                               highlightthickness=0)
        self.console.pack(fill=tk.BOTH, expand=True)

        # ── Status bar ──
        self.status = tk.Label(self.root, text="Ready", font=("Segoe UI", 8),
                               bg="#161b22", fg="#8b949e", anchor=tk.W, padx=10)
        self.status.pack(fill=tk.X)

    # ── Menu ────────────────────────────────────────────
    def _setup_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New        Ctrl+N", command=self._new_file)
        file_menu.add_command(label="Open...    Ctrl+O", command=self._open_file)
        file_menu.add_command(label="Save       Ctrl+S", command=self._save_file)
        file_menu.add_command(label="Save As...", command=self._save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._on_close)

        run_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Run", menu=run_menu)
        run_menu.add_command(label="Run Code     F5", command=self._run_code)
        run_menu.add_command(label="Run File (external)  Ctrl+F5",
                             command=self._run_external)

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About AiScript IDE", command=self._show_about)

    # ── Key bindings ────────────────────────────────────
    def _setup_bindings(self):
        self.text.bind("<KeyRelease>", self._on_key)
        self.text.bind("<Control-n>", lambda e: self._new_file())
        self.text.bind("<Control-o>", lambda e: self._open_file())
        self.text.bind("<Control-s>", lambda e: self._save_file())
        self.text.bind("<Control-S>", lambda e: self._save_as())
        self.text.bind("<F5>", lambda e: self._run_code())
        self.text.bind("<Control-F5>", lambda e: self._run_external())
        self.root.bind("<KeyRelease>", self._update_status)

    # ── Line numbers & scroll sync ──────────────────────
    def _sync_vscroll(self, *args):
        self.text.yview(*args)
        self.line_numbers.yview(*args)
        self._draw_line_numbers()

    def _scroll_v(self, *args):
        self.text.yview(*args)
        self.line_numbers.yview(*args)
        self._draw_line_numbers()

    def _draw_line_numbers(self, event=None):
        self.line_numbers.delete("all")
        first = self.text.index("@0,0")
        line_count = int(self.text.index("end-1c").split(".")[0])
        top_line = int(first.split(".")[0])
        height = self.line_numbers.winfo_height()
        line_height = 22
        visible = height // line_height + 2
        for i in range(top_line, min(top_line + visible, line_count + 1)):
            y = (i - top_line) * line_height + 4
            self.line_numbers.create_text(40, y, anchor=tk.NE, text=str(i),
                                          fill=LINE_FG, font=("Consolas", 9))
        self.line_numbers.config(scrollregion=(0, 0, 50, line_count * line_height))

    # ── Syntax highlighting ─────────────────────────────
    def _highlight(self, event=None):
        self.text.mark_set("range_start", "1.0")
        self.text.tag_remove("keyword", "1.0", tk.END)
        self.text.tag_remove("string", "1.0", tk.END)
        self.text.tag_remove("number", "1.0", tk.END)
        self.text.tag_remove("comment", "1.0", tk.END)
        self.text.tag_remove("builtin", "1.0", tk.END)

        keywords = {"if","elif","else","while","for","in","def","class",
                     "return","import","from","as","pass","break","continue",
                     "and","or","not","True","False","None","del"}
        builtins = {"print","input","len","range","int","str","float","list",
                     "dict","type","abs","min","max","round","sqrt","rand",
                     "randint","append","pop","keys","values","split","join",
                     "open","exit","sum","any","all","sorted","reversed",
                     "enumerate","zip","isinstance","insert","remove","sort",
                     "reverse","clear","items","dict_get","update","upper",
                     "lower","strip","replace","startswith","endswith","find",
                     "capitalize"}

        src = self.text.get("1.0", tk.END)

        # Comments
        for i, line in enumerate(src.split("\n"), 1):
            pos = line.find("#")
            if pos >= 0:
                idx = "{}.{}".format(i, pos)
                self.text.tag_add("comment", idx, "{}.{}".format(i, len(line)))

        # Keywords & builtins
        for i, line in enumerate(src.split("\n"), 1):
            j = 0
            while j < len(line):
                if line[j] in ("#", '"', "'"): break
                if line[j].isalpha() or line[j] == "_":
                    k = j
                    while k < len(line) and (line[k].isalnum() or line[k] == "_"):
                        k += 1
                    word = line[j:k]
                    idx = "{}.{}".format(i, j)
                    end_idx = "{}.{}".format(i, k)
                    if word in keywords:
                        self.text.tag_add("keyword", idx, end_idx)
                    elif word in builtins:
                        self.text.tag_add("builtin", idx, end_idx)
                    j = k
                elif line[j].isdigit() or (line[j] == "." and j+1 < len(line) and line[j+1].isdigit()):
                    k = j
                    has_dot = False
                    while k < len(line) and (line[k].isdigit() or (line[k] == "." and not has_dot)):
                        if line[k] == ".": has_dot = True
                        k += 1
                    self.text.tag_add("number", "{}.{}".format(i, j), "{}.{}".format(i, k))
                    j = k
                else:
                    j += 1

        # Strings (heuristic: any text between quotes on same line)
        in_str = False
        str_start = None
        str_quote = None
        for i, line in enumerate(src.split("\n"), 1):
            j = 0
            while j < len(line):
                ch = line[j]
                if ch == "\\": j += 2; continue
                if ch in ("\"", "'"):
                    if not in_str:
                        in_str = True; str_start = (i, j); str_quote = ch
                    elif ch == str_quote:
                        self.text.tag_add("string",
                            "{}.{}".format(str_start[0], str_start[1]),
                            "{}.{}".format(i, j+1))
                        in_str = False; str_start = None
                j += 1
            if in_str:
                self.text.tag_add("string",
                    "{}.{}".format(str_start[0], str_start[1]),
                    "{}.{}".format(i+1, 0))
                in_str = False; str_start = None

        self.text.tag_config("keyword", foreground=KEYWORD_COLOR)
        self.text.tag_config("string", foreground=STRING_COLOR)
        self.text.tag_config("number", foreground=NUMBER_COLOR)
        self.text.tag_config("comment", foreground=COMMENT_COLOR)
        self.text.tag_config("builtin", foreground=BUILTIN_COLOR)

    # ── File operations ─────────────────────────────────
    def _new_file(self):
        if self.modified:
            if not messagebox.askyesno("Unsaved Changes",
                                       "Discard current changes?"):
                return
        self.text.delete("1.0", tk.END)
        self.current_file = None
        self.modified = False
        self.root.title("AiScript IDE v{} - Untitled".format(__version__))

    def _open_file(self):
        path = filedialog.askopenfilename(
            title="Open .ais file",
            filetypes=[("AiScript files", "*.ais"),
                       ("Python files", "*.py"),
                       ("All files", "*.*")])
        if not path: return
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.text.delete("1.0", tk.END)
            self.text.insert("1.0", content)
            self.current_file = path
            self.modified = False
            self.root.title("AiScript IDE v{} - {}".format(__version__,
                           os.path.basename(path)))
            self._highlight()
        except Exception as e:
            messagebox.showerror("Error", "Cannot open file:\n{}".format(e))

    def _save_file(self):
        if self.current_file:
            try:
                content = self.text.get("1.0", tk.END).rstrip("\n")
                with open(self.current_file, "w", encoding="utf-8") as f:
                    f.write(content)
                self.modified = False
                self.root.title("AiScript IDE v{} - {}".format(__version__,
                               os.path.basename(self.current_file)))
            except Exception as e:
                messagebox.showerror("Error", "Cannot save file:\n{}".format(e))
        else:
            self._save_as()

    def _save_as(self):
        path = filedialog.asksaveasfilename(
            title="Save As",
            defaultextension=".ais",
            filetypes=[("AiScript files", "*.ais"),
                       ("All files", "*.*")])
        if not path: return
        self.current_file = path
        self._save_file()

    # ── Run code ────────────────────────────────────────
    def _run_code(self):
        src = self.text.get("1.0", tk.END)
        self._console_write(">>> Running AiScript...\n")
        threading.Thread(target=self._execute, args=(src,), daemon=True).start()

    def _execute(self, src):
        try:
            tokens = aiscript._Lexer(src).tokenize()
            ast = aiscript._Parser(tokens).parse()
            evaluator = aiscript._Eval()
            # Redirect print to console
            old_print = aiscript._builtin_print
            aiscript._builtin_print = lambda *a: self._console_write(" ".join(str(x) for x in a) + "\n")
            try:
                result = evaluator.eval(ast)
                if result is not None:
                    self._console_write(repr(result) + "\n")
            finally:
                aiscript._builtin_print = old_print
            self._console_write(">>> Done.\n")
        except SyntaxError as e:
            self._console_write("SyntaxError: {}\n".format(e))
        except Exception as e:
            self._console_write("Error: {}\n".format(e))
        self._update_status()

    def _run_external(self):
        if not self.current_file:
            self._save_as()
            if not self.current_file: return
        self._save_file()
        src = self.text.get("1.0", tk.END).rstrip("\n")
        self._console_write(">>> Running {} externally...\n".format(
            os.path.basename(self.current_file)))
        threading.Thread(target=self._execute, args=(src,), daemon=True).start()

    # ── Console ─────────────────────────────────────────
    def _console_write(self, text):
        self.output_queue.put(text)

    def _poll_output(self):
        while True:
            try:
                text = self.output_queue.get_nowait()
            except queue.Empty:
                break
            self.console.config(state=tk.NORMAL)
            self.console.insert(tk.END, text)
            self.console.see(tk.END)
            self.console.config(state=tk.DISABLED)
        self.root.after(50, self._poll_output)

    def _clear_console(self):
        self.console.config(state=tk.NORMAL)
        self.console.delete("1.0", tk.END)
        self.console.config(state=tk.DISABLED)

    # ── Event handlers ──────────────────────────────────
    def _on_key(self, event):
        if event.keysym not in ("Control_L", "Control_R", "Shift_L", "Shift_R",
                                "Alt_L", "Alt_R"):
            self.modified = True
            self.root.title("{} *".format(self.root.title().rstrip(" *")))
        self._draw_line_numbers()

    def _update_status(self, event=None):
        line, col = self.text.index(tk.INSERT).split(".")
        words = len(self.text.get("1.0", tk.END).split())
        fn = os.path.basename(self.current_file) if self.current_file else "Untitled"
        self.status.config(text=" {}  |  Line: {}  Col: {}  |  Words: {}".format(
            fn, line, col, words))

    def _on_close(self):
        if self.modified:
            if not messagebox.askyesno("Unsaved Changes",
                                       "Save before closing?"):
                self.root.destroy(); return
            self._save_file()
        self.root.destroy()

    def _show_about(self):
        messagebox.showinfo("About AiScript IDE",
            "AiScript IDE v{}\n\n"
            "A lightweight code editor and runner\n"
            "for AiScript (.ais) files.\n\n"
            "Built with tkinter.\n"
            "AiScript engine v{}".format(__version__, aiscript.__version__))

    # ── Run ─────────────────────────────────────────────
    def run(self):
        self._draw_line_numbers()
        self.root.mainloop()


if __name__ == "__main__":
    AiScriptIDE().run()
