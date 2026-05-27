import sys, os, shutil, tempfile, json, re
from urllib.request import urlopen, Request
from urllib.parse import urlparse

VERSION = "4.4.0"
CONFIG_FILE = "updater_config.json"
ALL_FILES = ["AI.py", "space_data.py", "mini_games.py", "trivia_pack.py",
             "word_play.py", "art_extra.py", "world_data.py", "story_data.py",
             "data_bulk.py", "data_bulk2.py", "data_bulk3.py", "data_bulk4.py",
             "data_bulk5.py", "data_bulk6.py", "data_bulk7.py", "data_bulk8.py", "data_bulk9.py", "data_bulk10.py", "data_bulk11.py", "data_bulk12.py", "data_bulk13.py", "data_bulk14.py", "data_bulk15.py", "data_bulk16.py", "data_bulk17.py", "data_bulk18.py", "data_bulk19.py", "data_bulk20.py", "data_bulk21.py", "data_bulk22.py", "data_bulk23.py", "data_bulk24.py", "hbpe_compat.py",
             "gen_code4.py", "installer.py", "updater.py"]
DEFAULT_URL = "https://raw.githubusercontent.com/Voice659/AI-repo/master/AI.py"

def normalize_url(url):
    url = url.strip()
    if "github.com" in url and "/blob/" in url:
        url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
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

def cfg_path():
    return os.path.join(app_dir(), CONFIG_FILE)

def get_url():
    if len(sys.argv) > 1:
        return sys.argv[1]
    path = cfg_path()
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f).get("url", DEFAULT_URL)
    return None

def save_config(url):
    with open(cfg_path(), "w") as f:
        json.dump({"url": url}, f)
    print("URL saved to {}".format(CONFIG_FILE))

def file_urls(base_url):
    parts = urlparse(base_url)
    path = parts.path.rsplit("/", 1)[0]
    return {f: "{}://{}{}/{}".format(parts.scheme, parts.netloc, path, f) for f in ALL_FILES}

def parse_version(data):
    try:
        text = data.decode("utf-8", errors="replace")
        m = re.search(r'__version__\s*=\s*["\']([\w.]+)["\']', text[:500])
        if m:
            return m.group(1)
    except:
        pass
    return None

def version_cmp(v1, v2):
    try:
        p1 = [int(x) for x in v1.split(".")]
        p2 = [int(x) for x in v2.split(".")]
        for a, b in zip(p1, p2):
            if a > b:
                return 1
            if a < b:
                return -1
        return 0
    except:
        return None

def download(url, filename):
    print("  Downloading {}...".format(filename), end=" ")
    req = Request(url, headers={"User-Agent": "AI-Updater/2.0"})
    resp = urlopen(req, timeout=30)
    data = resp.read()
    size = len(data) / 1024
    print("{:.1f} KB".format(size))
    return data

def extract_bundled(filename):
    path = os.path.join(resource_dir(), filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f.read()
    return None

def local_version(filename):
    path = os.path.join(app_dir(), filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = f.read()
        return parse_version(data)
    return None

def needs_update(remote_data, filename):
    local = local_version(filename)
    remote = parse_version(remote_data)
    if local is None:
        return True, local, remote
    if remote is None:
        return False, local, remote
    cmp = version_cmp(remote, local)
    if cmp is None:
        return True, local, remote
    return cmp > 0, local, remote

def write_file(data, filename):
    path = os.path.join(app_dir(), filename)
    backup = path + ".bak"
    if os.path.exists(path):
        shutil.copy2(path, backup)
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".py")
    try:
        tmp.write(data)
        tmp.close()
        shutil.copy2(tmp.name, path)
        print("  Written: {} (backup: {}.bak)".format(filename, filename))
    finally:
        os.unlink(tmp.name)

def verify(data, filename):
    try:
        compile(data, filename, "exec")
        return True
    except SyntaxError as e:
        print("  Syntax error in {}: {}".format(filename, e))
        return False

def prompt_for_url():
    print("No saved URL found. Enter the raw GitHub URL of AI.py:")
    print("Example: https://raw.githubusercontent.com/user/repo/main/AI.py")
    return input("URL: ").strip()

def main():
    url = get_url()
    if url is None:
        url = prompt_for_url()
        if input("Save this URL? (y/n): ").strip().lower() == "y":
            save_config(url)
    url = normalize_url(url)
    if not url or not url.startswith("http"):
        url = prompt_for_url()
        if input("Save this URL? (y/n): ").strip().lower() == "y":
            save_config(url)
    urls = file_urls(url)
    updated_count = 0
    skip_count = 0
    fail_count = 0
    for filename in ALL_FILES:
        print("--- {} ---".format(filename))
        data = None
        try:
            data = download(urls[filename], filename)
        except Exception as e:
            print("  Download failed: {}".format(e))
            fallback = extract_bundled(filename)
            if fallback:
                print("  Using bundled {} as fallback.".format(filename))
                data = fallback
            else:
                print("  No fallback for {}. Skipping.".format(filename))
                fail_count += 1
                continue
        if not verify(data, filename):
            fallback = extract_bundled(filename)
            if fallback and verify(fallback, filename):
                print("  Downloaded file has errors. Using bundled version.")
                data = fallback
            else:
                print("  Skipping {} due to errors.".format(filename))
                fail_count += 1
                continue
        should, local_ver, remote_ver = needs_update(data, filename)
        if not should:
            print("  Local version {} is current (remote {}). Skipping.".format(local_ver, remote_ver if remote_ver else "?"))
            skip_count += 1
            continue
        if local_ver and remote_ver:
            print("  Updating from {} to {}".format(local_ver, remote_ver))
        elif local_ver:
            print("  New file (local: {}, remote will be set)".format(local_ver))
        else:
            print("  New file, no local version found.")
        write_file(data, filename)
        updated_count += 1
    print("\n--- Summary ---")
    print("  Updated: {}".format(updated_count))
    print("  Skipped (current): {}".format(skip_count))
    print("  Failed: {}".format(fail_count))
    if updated_count > 0:
        print("Update complete! Restart AI.py to use the new version.")
    else:
        print("All files are already up to date.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
