"""AI.py Visual Installer — tkinter-based GUI installer with progress bars."""
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading, os, sys, json, re, shutil, tempfile
from urllib.request import urlopen, Request
from urllib.parse import urlparse

VERSION = "4.4.0"
APP_NAME = "AI.py"
CONFIG_FILE = "installer_config.json"
ALL_FILES = ["AI.py", "space_data.py", "mini_games.py", "trivia_pack.py",
             "word_play.py", "art_extra.py", "world_data.py", "story_data.py",
             "data_bulk.py", "data_bulk2.py", "data_bulk3.py", "data_bulk4.py",
             "data_bulk5.py", "data_bulk6.py", "data_bulk7.py", "data_bulk8.py", "data_bulk9.py", "data_bulk10.py", "data_bulk11.py", "data_bulk12.py", "data_bulk13.py", "data_bulk14.py", "data_bulk15.py", "data_bulk16.py", "data_bulk17.py", "data_bulk18.py", "data_bulk19.py", "data_bulk20.py", "data_bulk21.py", "data_bulk22.py", "data_bulk23.py", "data_bulk24.py", "data_bulk25.py", "data_bulk26.py", "data_bulk27.py", "data_bulk28.py", "data_bulk29.py", "data_bulk30.py", "hbpe_compat.py",
             "gen_code4.py", "installer.py", "updater.py"]
DEFAULT_URL = "https://raw.githubusercontent.com/Voice659/AI-repo/master/AI.py"

def normalize_url(url):
    """Convert github.com/blob/ URLs to raw.githubusercontent.com URLs."""
    url = url.strip()
    # github.com/user/repo/blob/branch/file → raw.githubusercontent.com/user/repo/branch/file
    if "github.com" in url and "/blob/" in url:
        url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    # Also handle /raw/ → already raw
    if "github.com" in url and "/raw/" in url:
        url = url.replace("github.com", "raw.githubusercontent.com").replace("/raw/", "/")
    return url

def app_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.abspath(__file__))

def resource_dir():
    if getattr(sys, "frozen", False):
        return sys._MEIPASS
    return app_dir()

class AIInstaller:
    def __init__(self, root):
        self.root = root
        self.root.title("AI.py v{} Visual Installer".format(VERSION))
        self.root.geometry("600x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#0d1117")

        try:
            self.root.iconbitmap(default="")
        except:
            pass

        self.url = DEFAULT_URL
        self.install_path = os.path.join(os.path.expanduser("~"), "AI")
        self.status_text = tk.StringVar(value="Ready")
        self.progress_var = tk.DoubleVar(value=0.0)
        self.file_progress_var = tk.DoubleVar(value=0.0)

        self._build_ui()
        self._center_window()

    def _center_window(self):
        self.root.update_idletasks()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.root.geometry("+{}+{}".format(x, y))

    def _browse_path(self):
        selected = filedialog.askdirectory(title="Select Install Folder",
                                           initialdir=self.path_var.get() or os.path.expanduser("~"))
        if selected:
            self.path_var.set(selected)

    def _build_ui(self):
        bg = "#0d1117"
        fg = "#c9d1d9"
        accent = "#58a6ff"
        accent2 = "#79c0ff"
        border = "#30363d"

        # Header
        header = tk.Frame(self.root, bg="#161b22", bd=0, highlightthickness=1, highlightcolor=border)
        header.pack(fill=tk.X, pady=(0, 15))

        tk.Label(header, text=APP_NAME, font=("Courier New", 22, "bold"),
                 fg=accent, bg="#161b22", padx=20, pady=12).pack()
        sub = tk.Frame(header, bg="#161b22")
        sub.pack(fill=tk.X, pady=(0, 12))
        tk.Label(sub, text="Visual Installer v{}".format(VERSION),
                 font=("Courier New", 11), fg=accent2, bg="#161b22").pack(padx=20)

        # Main content
        main = tk.Frame(self.root, bg=bg, padx=25)
        main.pack(fill=tk.BOTH, expand=True)

        # Install path
        path_frame = tk.Frame(main, bg=bg)
        path_frame.pack(fill=tk.X, pady=(0, 10))
        tk.Label(path_frame, text="Install Location:", font=("Segoe UI", 9),
                 fg=fg, bg=bg).pack(anchor=tk.W)
        path_row = tk.Frame(path_frame, bg=bg)
        path_row.pack(fill=tk.X, pady=(3, 0))
        self.path_var = tk.StringVar(value=self.install_path)
        path_entry = tk.Entry(path_row, textvariable=self.path_var,
                              font=("Segoe UI", 9), bg="#161b22", fg=fg,
                              insertbackground=fg, relief=tk.FLAT, bd=1,
                              highlightthickness=1, highlightcolor=border)
        path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        browse_btn = tk.Button(path_row, text="Browse...",
                               font=("Segoe UI", 8), bg="#21262d", fg=fg,
                               relief=tk.FLAT, bd=1, padx=8, cursor="hand2",
                               command=self._browse_path,
                               activebackground="#30363d", activeforeground=fg)
        browse_btn.pack(side=tk.RIGHT, padx=(6, 0))

        # URL
        url_frame = tk.Frame(main, bg=bg)
        url_frame.pack(fill=tk.X, pady=(0, 10))
        tk.Label(url_frame, text="Repository URL:", font=("Segoe UI", 9),
                 fg=fg, bg=bg).pack(anchor=tk.W)
        self.url_var = tk.StringVar(value=self.url)
        url_entry = tk.Entry(url_frame, textvariable=self.url_var,
                             font=("Segoe UI", 9), bg="#161b22", fg=fg,
                             insertbackground=fg, relief=tk.FLAT, bd=1,
                             highlightthickness=1, highlightcolor=border)
        url_entry.pack(fill=tk.X, pady=(3, 0))

        # Buttons row
        btn_frame = tk.Frame(main, bg=bg)
        btn_frame.pack(fill=tk.X, pady=(5, 10))

        self.check_btn = self._make_button(btn_frame, "Check for Updates", self._check_updates, "#238636")
        self.check_btn.pack(side=tk.LEFT, padx=(0, 8))

        self.install_btn = self._make_button(btn_frame, "Install / Update", self._install_files, "#1f6feb")
        self.install_btn.pack(side=tk.LEFT)

        self.verify_btn = self._make_button(btn_frame, "Verify Files", self._verify_files, "#9e6a03")
        self.verify_btn.pack(side=tk.LEFT, padx=(8, 0))

        # Progress section
        prog_frame = tk.Frame(main, bg=bg)
        prog_frame.pack(fill=tk.X, pady=(5, 5))

        self.status_label = tk.Label(prog_frame, textvariable=self.status_text,
                                     font=("Segoe UI", 9), fg="#8b949e", bg=bg)
        self.status_label.pack(anchor=tk.W)

        # Overall progress bar
        self.progress_bar = ttk.Progressbar(prog_frame, variable=self.progress_var,
                                            length=540, mode="determinate")
        self.progress_bar.pack(fill=tk.X, pady=(5, 2))

        # File progress bar
        self.file_bar = ttk.Progressbar(prog_frame, variable=self.file_progress_var,
                                        length=540, mode="determinate")
        self.file_bar.pack(fill=tk.X, pady=(2, 5))

        # Log area
        log_frame = tk.Frame(main, bg=bg)
        log_frame.pack(fill=tk.BOTH, expand=True)

        text_container = tk.Frame(log_frame, bg=bg)
        text_container.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(text_container, bg="#30363d")
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.log_text = tk.Text(text_container, font=("Courier New", 8), bg="#161b22",
                                fg="#8b949e", relief=tk.FLAT, bd=1,
                                highlightthickness=1, highlightcolor=border,
                                wrap=tk.WORD, state=tk.DISABLED,
                                yscrollcommand=scrollbar.set)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.log_text.yview)

        # Footer
        footer = tk.Frame(self.root, bg="#161b22", bd=0, highlightthickness=1, highlightcolor=border)
        footer.pack(fill=tk.X, side=tk.BOTTOM, pady=(15, 0))
        tk.Label(footer, text="AI.py v{} \u2022 1.3M+ lines \u2022 950 data tables".format(VERSION),
                 font=("Courier New", 8), fg="#484f58", bg="#161b22", padx=20, pady=8).pack()

    def _make_button(self, parent, text, command, color):
        btn = tk.Button(parent, text=text, command=command,
                        font=("Segoe UI", 9, "bold"), bg=color, fg="#ffffff",
                        relief=tk.FLAT, bd=0, padx=14, pady=6, cursor="hand2")
        btn.bind("<Enter>", lambda e: btn.config(bg=color + "cc"))
        btn.bind("<Leave>", lambda e: btn.config(bg=color))
        return btn

    def log(self, msg, msg_type="info"):
        colors = {"info": "#8b949e", "success": "#7ee787", "error": "#f85149",
                  "warn": "#d29922", "highlight": "#58a6ff"}
        color = colors.get(msg_type, "#8b949e")
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, msg + "\n", ("msg",))
        self.log_text.tag_config("msg", foreground=color)
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
        self.root.update()

    def set_status(self, text):
        self.status_text.set(text)
        self.root.update()

    def parse_version(self, data):
        try:
            text = data.decode("utf-8", errors="replace")
            m = re.search(r'__version__\s*=\s*["\']([\w.]+)["\']', text[:500])
            if m:
                return m.group(1)
        except:
            pass
        return None

    def download_file(self, url, filename):
        req = Request(url, headers={"User-Agent": "AI-Installer/4.0"})
        resp = urlopen(req, timeout=30)
        data = resp.read()
        size = len(data) / 1024
        self.log("  Downloaded {:.1f} KB: {}".format(size, filename), "info")
        return data

    def _check_updates(self):
        threading.Thread(target=self._do_check, daemon=True).start()

    def _do_check(self):
        self.set_status("Checking for updates...")
        self.log("Checking repository for updates...", "info")
        url = normalize_url(self.url_var.get())
        if not url:
            self.log("ERROR: No URL provided.", "error")
            self.set_status("Error: No URL")
            return
        try:
            req = Request(url, headers={"User-Agent": "AI-Installer/4.0"})
            resp = urlopen(req, timeout=15)
            data = resp.read()
            remote_ver = self.parse_version(data)
            if remote_ver:
                self.log("Remote version: {}".format(remote_ver), "highlight")
                local_ver = self._local_version("AI.py")
                if local_ver:
                    self.log("Local version: {}".format(local_ver), "info")
                    def _cmp(a, b):
                        pa = [int(x) for x in a.split(".")]
                        pb = [int(x) for x in b.split(".")]
                        for va, vb in zip(pa, pb):
                            if va > vb: return 1
                            if va < vb: return -1
                        return len(pa) - len(pb)
                    if _cmp(remote_ver, local_ver) > 0:
                        self.log("UPDATE AVAILABLE: {} -> {}".format(local_ver, remote_ver), "success")
                        self.set_status("Update available: v{} -> v{}".format(local_ver, remote_ver))
                    elif remote_ver == local_ver:
                        self.log("Already up to date at v{}".format(local_ver), "success")
                        self.set_status("Up to date (v{})".format(local_ver))
                    else:
                        self.log("Local version is newer ({} > {}).".format(local_ver, remote_ver), "warn")
                        self.set_status("Local version is newer")
                else:
                    self.log("No local AI.py found. Remote version: {}".format(remote_ver), "warn")
                    self.set_status("Not installed (remote: v{})".format(remote_ver))
            else:
                self.log("Could not parse version from remote.", "error")
                self.set_status("Parse error")
        except Exception as e:
            self.log("Connection failed: {}".format(e), "error")
            self.set_status("Connection failed")

    def _target_dir(self):
        return self.path_var.get() or app_dir()

    def _local_version(self, filename):
        path = os.path.join(self._target_dir(), filename)
        if os.path.exists(path):
            with open(path, "rb") as f:
                return self.parse_version(f.read())
        return None

    def _install_files(self):
        threading.Thread(target=self._do_install, daemon=True).start()

    def _do_install(self):
        self.set_status("Installing...")
        self.log("Starting installation...", "highlight")
        self.install_btn.config(state=tk.DISABLED)
        self.check_btn.config(state=tk.DISABLED)

        url = normalize_url(self.url_var.get())
        if not url or not url.startswith("http"):
            self.log("Please set a valid repository URL.", "error")
            self.set_status("No URL set")
            self.install_btn.config(state=tk.NORMAL)
            self.check_btn.config(state=tk.NORMAL)
            return

        total = len(ALL_FILES)
        self.progress_var.set(0)
        self.file_progress_var.set(0)
        success_count = 0
        fail_count = 0

        for i, filename in enumerate(ALL_FILES):
            self.set_status("Downloading {} ({}/{})...".format(filename, i+1, total))
            self.progress_var.set((i / total) * 100)
            self.file_progress_var.set(0)

            try:
                base = url.rsplit("/", 1)[0]
                file_url = "{}/{}".format(base, filename)
                data = self.download_file(file_url, filename)

                if filename == "AI.py":
                    ver = self.parse_version(data)
                    if ver:
                        self.log("  Version: {}".format(ver), "success")
                    else:
                        self.log("  Warning: Could not verify version.", "warn")

                # Verify syntax for .py files
                if filename.endswith(".py"):
                    try:
                        compile(data, filename, "exec")
                        self.log("  Syntax OK", "success")
                    except SyntaxError as e:
                        self.log("  Syntax error: {}".format(e), "error")
                        fail_count += 1
                        continue

                dest = os.path.join(self._target_dir(), filename)
                backup = dest + ".bak"
                if os.path.exists(dest):
                    shutil.copy2(dest, backup)
                    self.log("  Backup created: {}.bak".format(filename), "info")

                tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".py")
                try:
                    tmp.write(data)
                    tmp.close()
                    shutil.copy2(tmp.name, dest)
                    self.log("  Written: {}".format(filename), "success")
                    success_count += 1
                finally:
                    os.unlink(tmp.name)

                self.file_progress_var.set(100)

            except Exception as e:
                self.log("  Failed: {} - {}".format(filename, e), "error")
                fail_count += 1

            self.root.update()

        self.progress_var.set(100)
        summary = "Installed: {}, Failed: {}, Total: {}".format(success_count, fail_count, total)
        self.log(summary, "highlight" if fail_count == 0 else "warn")
        self.set_status("Done: {} installed, {} failed".format(success_count, fail_count))

        if fail_count == 0:
            self.log("Installation complete! Restart AI.py to use.", "success")
        else:
            self.log("Installation completed with errors.", "warn")

        self.install_btn.config(state=tk.NORMAL)
        self.check_btn.config(state=tk.NORMAL)

    def _verify_files(self):
        threading.Thread(target=self._do_verify, daemon=True).start()

    def _do_verify(self):
        self.set_status("Verifying files...")
        self.log("Verifying local files...", "info")
        ok = 0
        fail = 0
        for filename in ALL_FILES:
            path = os.path.join(self._target_dir(), filename)
            if not os.path.exists(path):
                self.log("  MISSING: {}".format(filename), "error")
                fail += 1
                continue
            size = os.path.getsize(path)
            ver = "?"
            if filename.endswith(".py"):
                with open(path, "rb") as f:
                    data = f.read()
                ver = self.parse_version(data)
                ver_str = " v{}".format(ver) if ver else ""
                try:
                    compile(data, filename, "exec")
                    self.log("  OK: {} ({:.1f} KB{})".format(filename, size/1024, ver_str), "success")
                    ok += 1
                except SyntaxError as e:
                    self.log("  SYNTAX ERROR in {}: {}".format(filename, e), "error")
                    fail += 1
            else:
                self.log("  OK: {} ({:.1f} KB)".format(filename, size/1024), "success")
                ok += 1
        self.log("Verified: {} OK, {} issues".format(ok, fail), "highlight" if fail == 0 else "warn")
        self.set_status("Verified: {} OK, {} failed".format(ok, fail))

def main():
    root = tk.Tk()
    app = AIInstaller(root)
    root.mainloop()

if __name__ == "__main__":
    main()
