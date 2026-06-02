(function () {
  "use strict";

  /* =================================================================
     UTILITIES
   ================================================================= */
  var Utils = {
    $: function (s, c) { return (c || document).querySelector(s); },
    $$: function (s, c) { return Array.from((c || document).querySelectorAll(s)); },
    on: function (el, ev, fn) { (typeof el === "string" ? Utils.$$(el) : [el]).forEach(function (e) { e.addEventListener(ev, fn); }); },
    delegate: function (parent, sel, ev, fn) {
      (typeof parent === "string" ? Utils.$$(parent) : [parent]).forEach(function (p) {
        p.addEventListener(ev, function (e) {
          var t = e.target.closest(sel);
          if (t && p.contains(t)) fn.call(t, e);
        });
      });
    },
    esc: function (s) {
      var d = document.createElement("div");
      d.textContent = s;
      return d.innerHTML;
    }
  };

  /* =================================================================
     1. INJECT SHARED CSS
   ================================================================= */
  (function injectCSS() {
    if (document.getElementById("ai-py-global-css")) return;
    var s = document.createElement("style");
    s.id = "ai-py-global-css";

    // Light theme variables
    s.textContent =
      ".light-theme{--bg:#f6f8fa;--bg2:#fff;--bg3:#e1e4e8;--fg:#24292e;--fg2:#586069;--border:#d1d5da}" +
      ".light-theme{background:var(--bg)!important;color:var(--fg)!important}" +
      ".light-theme a{color:#0366d6!important}" +
      ".light-theme .nav,.light-theme .navbar,.light-theme [style*='background:#161b22']{background:var(--bg2)!important;border-color:var(--border)!important}" +
      ".light-theme .container,.light-theme .stat-card,.light-theme .feature-card,.light-theme .card," +
      ".light-theme .cmd-table tr:hover,.light-theme table tr:hover,.light-theme .stat-box{background:var(--bg2)!important}" +
      ".light-theme .stat-card,.light-theme .feature-card,.light-theme .card," +
      ".light-theme pre,.light-theme code,.light-theme table th,.light-theme table td," +
      ".light-theme .cmd-table th,.light-theme .cmd-table td," +
      ".light-theme input,.light-theme select," +
      ".light-theme .badge-user,.light-theme .tag-bulk{background:var(--bg3)!important}" +
      ".light-theme pre,.light-theme code," +
      ".light-theme .stat-card,.light-theme .feature-card,.light-theme .card," +
      ".light-theme table th,.light-theme table td," +
      ".light-theme .cmd-table th,.light-theme .cmd-table td," +
      ".light-theme input,.light-theme select," +
      ".light-theme [style*='border']{border-color:var(--border)!important}" +
      ".light-theme .subtitle,.light-theme .lbl,.light-theme .label,.light-theme .footer," +
      ".light-theme .badge-user,.light-theme .tag-bulk," +
      ".light-theme .stat-box .lbl{color:var(--fg2)!important}" +
      ".light-theme [style*='color:#8b949e']{color:var(--fg2)!important}" +
      ".light-theme [style*='color:#c9d1d9']{color:var(--fg)!important}" +
      ".light-theme [style*='color:#484f58']{color:var(--fg2)!important}" +
      ".light-theme .stat-card .num{color:#0366d6!important}" +
      /* Mobile nav */
      ".ai-py-nav-toggle{display:none;background:transparent;border:none;color:#58a6ff;font-size:24px;cursor:pointer;padding:4px 8px}" +
      ".ai-py-nav-overlay{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.5);z-index:998}" +
      ".ai-py-nav-overlay.show{display:block}" +
      ".ai-py-nav-drawer{position:fixed;top:0;left:-280px;width:260px;height:100%;background:#161b22;border-right:1px solid #30363d;z-index:999;transition:left 0.25s;overflow-y:auto;padding:60px 20px 20px}" +
      ".light-theme .ai-py-nav-drawer{background:#fff}" +
      ".ai-py-nav-drawer.open{left:0}" +
      ".ai-py-nav-drawer a{display:block;padding:8px 12px;color:#c9d1d9;text-decoration:none;border-radius:4px;font-size:0.9em}" +
      ".light-theme .ai-py-nav-drawer a{color:#24292e}" +
      ".ai-py-nav-drawer a:hover,.ai-py-nav-drawer a.active{background:#21262d;color:#58a6ff}" +
      ".light-theme .ai-py-nav-drawer a:hover,.light-theme .ai-py-nav-drawer a.active{background:#e1e4e8}" +
      ".ai-py-nav-close{position:absolute;top:12px;right:12px;background:transparent;border:none;color:#8b949e;font-size:24px;cursor:pointer}" +
      /* Scroll-to-top */
      ".ai-py-scroll-top{position:fixed;bottom:64px;right:16px;z-index:9998;width:40px;height:40px;border-radius:50%;border:1px solid #30363d;background:#161b22;color:#c9d1d9;font-size:18px;cursor:pointer;display:none;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.4);transition:opacity 0.2s}" +
      ".ai-py-scroll-top:hover{background:#21262d}" +
      ".light-theme .ai-py-scroll-top{background:#e1e4e8;color:#24292e;border-color:#d1d5da}" +
      /* Command browser */
      ".ai-py-cmd-browser{margin:20px 0}" +
      ".ai-py-cat-tabs{display:flex;flex-wrap:wrap;gap:4px;margin:10px 0}" +
      ".ai-py-cat-tab{padding:5px 14px;border:1px solid #30363d;border-radius:4px;cursor:pointer;font-size:0.8em;background:#161b22;color:#8b949e;transition:all 0.15s}" +
      ".light-theme .ai-py-cat-tab{background:#e1e4e8;color:#586069;border-color:#d1d5da}" +
      ".ai-py-cat-tab.active{background:#1f6feb;color:#fff;border-color:#1f6feb}" +
      ".ai-py-cat-tab .cnt{opacity:0.6;font-size:0.85em;margin-left:4px}" +
      ".ai-py-cmd-search-wrap{display:flex;gap:8px;margin:10px 0}" +
      ".ai-py-cmd-search-wrap input{flex:1;background:#161b22;border:1px solid #30363d;color:#c9d1d9;padding:10px 14px;border-radius:6px;font-size:0.95em;max-width:500px}" +
      ".light-theme .ai-py-cmd-search-wrap input{background:#fff;color:#24292e;border-color:#d1d5da}" +
      ".ai-py-cmd-search-wrap input:focus{outline:none;border-color:#58a6ff}" +
      ".ai-py-cmd-results{color:#8b949e;font-size:0.85em;margin:6px 0}" +
      ".ai-py-cmd-table{width:100%;border-collapse:collapse;margin:10px 0}" +
      ".ai-py-cmd-table th{text-align:left;color:#8b949e;border-bottom:1px solid #30363d;padding:6px 10px;font-size:0.85em;cursor:pointer}" +
      ".ai-py-cmd-table th:hover{color:#58a6ff}" +
      ".ai-py-cmd-table td{padding:4px 10px;border-bottom:1px solid #21262d;font-size:0.9em}" +
      ".ai-py-cmd-table .num{color:#58a6ff;font-weight:bold;width:60px}" +
      ".ai-py-cmd-table tr:hover{background:#161b22}" +
      ".light-theme .ai-py-cmd-table tr:hover{background:#e1e4e8}" +
      /* Data preview modal */
      ".ai-py-modal-overlay{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.7);z-index:10000;justify-content:center;align-items:center}" +
      ".ai-py-modal-overlay.show{display:flex}" +
      ".ai-py-modal{background:#161b22;border:1px solid #30363d;border-radius:10px;max-width:600px;width:90%;max-height:80vh;overflow-y:auto;padding:25px;position:relative}" +
      ".light-theme .ai-py-modal{background:#fff;border-color:#d1d5da}" +
      ".ai-py-modal h3{color:#58a6ff;margin-bottom:10px}" +
      ".ai-py-modal-close{position:absolute;top:12px;right:16px;background:transparent;border:none;color:#8b949e;font-size:22px;cursor:pointer}" +
      ".ai-py-modal table{width:100%;border-collapse:collapse;margin:10px 0}" +
      ".ai-py-modal th{text-align:left;color:#8b949e;border-bottom:1px solid #30363d;padding:5px 8px;font-size:0.8em}" +
      ".ai-py-modal td{border-bottom:1px solid #21262d;padding:4px 8px;font-size:0.85em}" +
      /* TOC sidebar */
      ".ai-py-toc{position:sticky;top:20px;max-height:calc(100vh - 40px);overflow-y:auto;padding-right:10px}" +
      ".ai-py-toc a{display:block;padding:4px 8px;font-size:0.8em;color:#8b949e;text-decoration:none;border-left:2px solid transparent;margin:1px 0}" +
      ".ai-py-toc a:hover,.ai-py-toc a.active{color:#58a6ff;border-left-color:#58a6ff}" +
      ".ai-py-toc .toc-h2{margin-top:6px}" +
      ".ai-py-toc .toc-h3{padding-left:20px;font-size:0.75em}" +
      /* Keyboard shortcuts help */
      ".ai-py-shortcuts{position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.7);z-index:10001;display:none;justify-content:center;align-items:center}" +
      ".ai-py-shortcuts.show{display:flex}" +
      ".ai-py-shortcuts-inner{background:#161b22;border:1px solid #30363d;border-radius:10px;padding:25px;max-width:400px;width:90%}" +
      ".light-theme .ai-py-shortcuts-inner{background:#fff;border-color:#d1d5da}" +
      ".ai-py-shortcuts-inner h3{color:#58a6ff;margin-bottom:15px}" +
      ".ai-py-shortcuts-inner .row{display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #21262d;font-size:0.9em}" +
      ".ai-py-shortcuts-inner .key{background:#21262d;padding:2px 8px;border-radius:3px;font-family:monospace;font-size:0.85em;color:#c9d1d9}" +
      ".light-theme .ai-py-shortcuts-inner .key{background:#e1e4e8;color:#24292e}" +
      /* Responsive */
      "@media(max-width:700px){.ai-py-nav-toggle{display:inline-block}";

    document.head.appendChild(s);
  })();

  /* =================================================================
     2. THEME TOGGLE (floating button)
   ================================================================= */
  (function initTheme() {
    var btn = document.createElement("button");
    btn.id = "ai-py-theme-btn";
    btn.innerHTML = "&#9790;";
    btn.title = "Toggle theme (t)";
    Object.assign(btn.style, {
      position: "fixed", bottom: "16px", right: "16px", zIndex: "9999",
      width: "40px", height: "40px", borderRadius: "50%",
      border: "1px solid #30363d", background: "#161b22", color: "#c9d1d9",
      fontSize: "20px", cursor: "pointer", display: "flex",
      alignItems: "center", justifyContent: "center",
      boxShadow: "0 2px 8px rgba(0,0,0,0.4)", transition: "all 0.2s",
      lineHeight: "1", padding: "0"
    });
    btn.addEventListener("click", toggleTheme);
    document.body.appendChild(btn);

    function themeActive() { return document.body.classList.contains("light-theme"); }

    function toggleTheme() {
      document.body.classList.toggle("light-theme");
      var a = themeActive();
      localStorage.setItem("ai-py-theme", a ? "light" : "dark");
      btn.innerHTML = a ? "&#9789;" : "&#9790;";
      btn.style.background = a ? "#e1e4e8" : "#161b22";
      btn.style.color = a ? "#24292e" : "#c9d1d9";
    }

    if (localStorage.getItem("ai-py-theme") === "light" && !themeActive()) toggleTheme();
  })();

  /* =================================================================
     3. SCROLL-TO-TOP BUTTON
   ================================================================= */
  (function initScrollTop() {
    var btn = document.createElement("button");
    btn.className = "ai-py-scroll-top";
    btn.innerHTML = "&#8593;";
    btn.title = "Scroll to top";
    btn.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: "smooth" }); });
    document.body.appendChild(btn);
    var ticking = false;
    window.addEventListener("scroll", function () {
      if (!ticking) {
        requestAnimationFrame(function () {
          btn.style.display = window.scrollY > 300 ? "flex" : "none";
          ticking = false;
        });
        ticking = true;
      }
    });
  })();

  /* =================================================================
     4. COPY-TO-CLIPBOARD (improved)
   ================================================================= */
  (function initCopy() {
    document.addEventListener("DOMContentLoaded", function () {
      Utils.$$("pre").forEach(function (pre) {
        if (pre.querySelector(".ai-py-copy-btn")) return;
        var btn = document.createElement("button");
        btn.className = "ai-py-copy-btn";
        btn.textContent = "Copy";
        Object.assign(btn.style, {
          position: "absolute", top: "4px", right: "4px",
          background: "#21262d", color: "#8b949e",
          border: "1px solid #30363d", borderRadius: "4px",
          padding: "2px 8px", fontSize: "11px", cursor: "pointer",
          fontFamily: "inherit", zIndex: "10",
          opacity: "0", transition: "opacity 0.2s"
        });
        pre.style.position = pre.style.position || "relative";
        pre.appendChild(btn);
        pre.addEventListener("mouseenter", function () { btn.style.opacity = "1"; });
        pre.addEventListener("mouseleave", function () { btn.style.opacity = "0"; });
        btn.addEventListener("click", function (e) {
          e.stopPropagation();
          var text = pre.textContent;
          if (btn.textContent === "Copied!") return;
          navigator.clipboard.writeText(text).then(
            function () {
              btn.textContent = "Copied!";
              btn.style.color = "#7ee787";
              btn.style.borderColor = "#30a745";
              setTimeout(function () { btn.textContent = "Copy"; btn.style.color = "#8b949e"; btn.style.borderColor = "#30363d"; }, 2000);
            },
            function () {
              btn.textContent = "Failed";
              btn.style.color = "#f85149";
              setTimeout(function () { btn.textContent = "Copy"; btn.style.color = "#8b949e"; }, 2000);
            }
          );
        });
      });
    });
  })();

  /* =================================================================
     5. MOBILE NAV + NAV HIGHLIGHT
   ================================================================= */
  (function initNav() {
    document.addEventListener("DOMContentLoaded", function () {
      // Find nav bars
      var navEls = Utils.$$('.nav, [class*="navbar"], [style*="text-align:center"][style*="padding"]');
      navEls = navEls.filter(function (n) { return n.querySelector("a"); });
      if (navEls.length === 0) return;
      var navBar = navEls[0];

      // --- Mobile toggle ---
      var toggle = document.createElement("button");
      toggle.className = "ai-py-nav-toggle";
      toggle.innerHTML = "&#9776;";
      toggle.title = "Navigation menu";
      navBar.insertBefore(toggle, navBar.firstChild);

      // Build drawer
      var overlay = document.createElement("div");
      overlay.className = "ai-py-nav-overlay";
      var drawer = document.createElement("div");
      drawer.className = "ai-py-nav-drawer";
      var closeBtn = document.createElement("button");
      closeBtn.className = "ai-py-nav-close";
      closeBtn.innerHTML = "&times;";
      drawer.appendChild(closeBtn);

      var page = document.location.pathname.split("/").pop().toLowerCase() || "index.html";

      // Collect nav links
      var links = Utils.$$("a", navBar);
      links.forEach(function (a) {
        var clone = a.cloneNode(true);
        var href = clone.getAttribute("href");
        if (href && href.toLowerCase() === page) clone.className = "active";
        drawer.appendChild(clone);
      });

      overlay.appendChild(drawer);
      document.body.appendChild(overlay);

      function openNav() { drawer.classList.add("open"); overlay.classList.add("show"); }
      function closeNav() { drawer.classList.remove("open"); overlay.classList.remove("show"); }
      toggle.addEventListener("click", openNav);
      closeBtn.addEventListener("click", closeNav);
      overlay.addEventListener("click", function (e) { if (e.target === overlay) closeNav(); });

      // --- Highlight current page ---
      links.forEach(function (a) {
        var href = a.getAttribute("href");
        if (href && href.toLowerCase() === page) a.style.fontWeight = "bold";
      });
    });
  })();

  /* =================================================================
     6. DATA INDEX (data-index.html) — enhanced browser
   ================================================================= */
  window.filterTable = function filterTable() {
    var q = ((document.getElementById("search") || {}).value || "").toLowerCase();
    var filterVal = (document.getElementById("filter") || {}).value || "all";
    var sortVal = (document.getElementById("sort") || {}).value || "name";
    var tbody = document.getElementById("table");
    if (!tbody || typeof DATA === "undefined") return;

    var filtered = DATA.filter(function (d) {
      if (filterVal === "curated" && d.t !== "curated") return false;
      if (filterVal === "bulk" && d.t !== "bulk") return false;
      return !(q && !d.d.toLowerCase().includes(q));
    });

    filtered.sort(function (a, b) {
      return sortVal === "count" ? b.c - a.c : a.d.localeCompare(b.d);
    });

    tbody.innerHTML = '<tr><th onclick="sortTable(0)">#</th><th onclick="sortTable(1)">Table Name</th><th onclick="sortTable(2)">Entries</th><th onclick="sortTable(3)">Type</th></tr>';
    filtered.forEach(function (d, i) {
      var tr = tbody.insertRow();
      tr.style.cursor = "pointer";
      tr.title = "Click to copy function name";
      tr.insertCell().textContent = i + 1;
      tr.insertCell().textContent = d.d;
      var c3 = tr.insertCell();
      c3.textContent = d.c.toLocaleString();
      c3.style.color = "#58a6ff";
      c3.style.fontFamily = "monospace";
      var c4 = tr.insertCell();
      c4.innerHTML = d.t === "curated" ? '<span class="tag-curated">Curated</span>' : '<span class="tag-bulk">Bulk (' + d.c + ")</span>";
      // Click to copy
      tr.addEventListener("click", function () {
        navigator.clipboard.writeText(d.n).then(function () {
          var orig = c4.innerHTML;
          c4.innerHTML = '<span style="color:#7ee787;font-size:0.85em">Copied!</span>';
          setTimeout(function () { c4.innerHTML = orig; }, 1500);
        });
      });
    });
    var statsEl = document.getElementById("stats");
    if (statsEl) {
      statsEl.textContent = filtered.length + " of " + DATA.length + " tables \u2014 " + filtered.reduce(function (s, d) { return s + d.c; }, 0).toLocaleString() + " entries";
    }
  };

  window.sortTable = function sortTable(col) {
    var sortEl = document.getElementById("sort");
    if (!sortEl) return;
    if (col === 1 || col === 0) sortEl.value = "name";
    else if (col === 2) sortEl.value = "count";
    window.filterTable();
  };

  if (typeof DATA !== "undefined") {
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", window.filterTable);
    else window.filterTable();
  }

  /* =================================================================
     7. DOCS PAGE — Interactive Command Browser (AI.py-docs.html)
   ================================================================= */
  (function initCmdBrowser() {
    document.addEventListener("DOMContentLoaded", function () {
      var tables = Utils.$$("table.cmd-table");
      if (tables.length === 0) return;

      // Parse all commands from existing tables
      var allCmds = [];
      var cats = [];
      tables.forEach(function (tbl) {
        // Find the category from preceding h3
        var h3 = tbl.previousElementSibling;
        while (h3 && h3.tagName !== "H3") h3 = h3.previousElementSibling;
        var catName = h3 ? h3.textContent.trim() : "Other";
        if (cats.indexOf(catName) === -1) cats.push(catName);
        var rows = Utils.$$("tr", tbl);
        rows.forEach(function (tr, idx) {
          if (idx === 0) return; // skip header
          var cells = Utils.$$("td", tr);
          if (cells.length < 2) return;
          // Some tables have mixed number formats (numeric or text)
          var num = cells[0].textContent.trim();
          var name = cells[1].textContent.trim();
          if (name) allCmds.push({ num: num, name: name, cat: catName });
        });
        // Hide the original static table
        if (h3) h3.style.display = "none";
        tbl.style.display = "none";
      });

      if (allCmds.length === 0) return;

      // Build the interactive browser UI
      var container = document.createElement("div");
      container.className = "ai-py-cmd-browser";

      // Category tabs
      var tabBar = document.createElement("div");
      tabBar.className = "ai-py-cat-tabs";
      var allTab = document.createElement("span");
      allTab.className = "ai-py-cat-tab active";
      allTab.textContent = "All (" + allCmds.length + ")";
      allTab.dataset.cat = "__all__";
      tabBar.appendChild(allTab);
      cats.forEach(function (c) {
        var cnt = allCmds.filter(function (cmd) { return cmd.cat === c; }).length;
        var tab = document.createElement("span");
        tab.className = "ai-py-cat-tab";
        tab.innerHTML = Utils.esc(c) + ' <span class="cnt">' + cnt + "</span>";
        tab.dataset.cat = c;
        tabBar.appendChild(tab);
      });

      // Search
      var searchWrap = document.createElement("div");
      searchWrap.className = "ai-py-cmd-search-wrap";
      var searchInput = document.createElement("input");
      searchInput.type = "text";
      searchInput.placeholder = "Search " + allCmds.length + " commands...";
      var resultsLabel = document.createElement("span");
      resultsLabel.className = "ai-py-cmd-results";
      resultsLabel.textContent = allCmds.length + " commands";
      searchWrap.appendChild(searchInput);
      searchWrap.appendChild(resultsLabel);

      // Table
      var table = document.createElement("table");
      table.className = "ai-py-cmd-table";
      table.innerHTML =
        "<tr><th>#</th><th>Command</th><th>Category</th></tr>";

      container.appendChild(tabBar);
      container.appendChild(searchWrap);
      container.appendChild(table);

      // Insert before the first h2 in content area
      var content = Utils$(".container") || document.body;
      var firstH2 = Utils$("h2", content);
      if (firstH2) content.insertBefore(container, firstH2);
      else content.insertBefore(container, content.firstChild);

      var activeCat = "__all__";
      var sortDir = [1, 1, 1];

      function render() {
        var q = searchInput.value.toLowerCase();
        var filtered = allCmds.filter(function (cmd) {
          if (activeCat !== "__all__" && cmd.cat !== activeCat) return false;
          if (q && cmd.name.toLowerCase().indexOf(q) === -1 && cmd.num.toLowerCase().indexOf(q) === -1) return false;
          return true;
        });

        resultsLabel.textContent = filtered.length + " of " + allCmds.length + " commands";

        table.innerHTML = "<tr><th onclick='sortCmds(0)'>#</th><th onclick='sortCmds(1)'>Command</th><th onclick='sortCmds(2)'>Category</th></tr>";
        filtered.forEach(function (cmd) {
          var tr = table.insertRow();
          tr.style.cursor = "pointer";
          tr.title = "Click to copy command name";
          var n = tr.insertCell();
          n.textContent = cmd.num;
          n.className = "num";
          tr.insertCell().textContent = cmd.name;
          tr.insertCell().textContent = cmd.cat;
          tr.addEventListener("click", function () {
            navigator.clipboard.writeText(cmd.name).then(function () {
              var orig = tr.style.background;
              tr.style.background = "#1f6feb44";
              setTimeout(function () { tr.style.background = orig; }, 600);
            });
          });
        });
      }

      // Tab switching
      tabBar.addEventListener("click", function (e) {
        var tab = e.target.closest(".ai-py-cat-tab");
        if (!tab) return;
        Utils.$$(".ai-py-cat-tab", tabBar).forEach(function (t) { t.classList.remove("active"); });
        tab.classList.add("active");
        activeCat = tab.dataset.cat;
        render();
      });

      searchInput.addEventListener("input", render);

      // Expose sort function globally for onclick
      window.sortCmds = function sortCmds(col) {
        sortDir[col] *= -1;
        var rows = Array.from(table.rows).slice(1);
        rows.sort(function (a, b) {
          var va = a.cells[col].textContent.toLowerCase();
          var vb = b.cells[col].textContent.toLowerCase();
          return va < vb ? -1 * sortDir[col] : va > vb ? 1 * sortDir[col] : 0;
        });
        for (var i = 1; i < table.rows.length; i++) table.deleteRow(i);
        rows.forEach(function (r) { table.appendChild(r); });
      };

      render();
    });
  })();

  /* =================================================================
     8. DATA PREVIEW MODAL (data-index.html)
   ================================================================= */
  (function initDataPreview() {
    // Only on data-index.html with DATA available
    if (typeof DATA === "undefined") return;

    // Build modal
    var overlay = document.createElement("div");
    overlay.className = "ai-py-modal-overlay";
    overlay.id = "ai-py-data-modal";
    overlay.innerHTML =
      '<div class="ai-py-modal">' +
      '<button class="ai-py-modal-close" onclick="closeDataPreview()">&times;</button>' +
      '<h3 id="ai-py-modal-title">Table Details</h3>' +
      '<div id="ai-py-modal-body"></div>' +
      "</div>";
    document.body.appendChild(overlay);

    window.closeDataPreview = function () {
      overlay.classList.remove("show");
    };

    overlay.addEventListener("click", function (e) {
      if (e.target === overlay) closeDataPreview();
    });

    // Expose global open function
    window.openDataPreview = function (name) {
      var d = DATA.find(function (x) { return x.n === name; });
      if (!d) return;
      document.getElementById("ai-py-modal-title").textContent = d.d;
      var body = document.getElementById("ai-py-modal-body");
      body.innerHTML =
        "<table>" +
        "<tr><th>Property</th><th>Value</th></tr>" +
        "<tr><td>Function Name</td><td><code>" + Utils.esc(d.n) + "</code></td></tr>" +
        "<tr><td>Display Name</td><td>" + Utils.esc(d.d) + "</td></tr>" +
        "<tr><td>Entries</td><td>" + d.c.toLocaleString() + "</td></tr>" +
        "<tr><td>Type</td><td>" + (d.t === "curated" ? "Curated (real data)" : "Bulk (generated)") + "</td></tr>" +
        "</table>" +
        '<button style="background:#1f6feb;color:#fff;border:none;padding:8px 16px;border-radius:4px;cursor:pointer;margin-top:10px" onclick="navigator.clipboard.writeText(\'' + d.n + "').then(function(){this.textContent='Copied!'}.bind(this))" +
        '">Copy Function Name</button>';
      overlay.classList.add("show");
    };

    // Attach click to data-index table rows
    document.addEventListener("DOMContentLoaded", function () {
      var tbody = document.getElementById("table");
      if (!tbody) return;
      tbody.addEventListener("click", function (e) {
        var tr = e.target.closest("tr");
        if (!tr || !tr.parentNode || tr.parentNode !== tbody) return;
        var nameCell = tr.cells[1];
        if (!nameCell) return;
        var displayName = nameCell.textContent;
        var d = DATA.find(function (x) { return x.d === displayName; });
        if (d) openDataPreview(d.n);
      });
    });
  })();

  /* =================================================================
     9. TABLE OF CONTENTS SIDEBAR (long pages)
   ================================================================= */
  (function initTOC() {
    document.addEventListener("DOMContentLoaded", function () {
      var content = Utils$(".container");
      if (!content) return;
      var headings = Utils.$$("h2, h3", content);
      if (headings.length < 3) return;

      // Only on wider screens
      if (window.innerWidth < 900) return;

      // Create sidebar layout
      var sidebar = document.createElement("div");
      sidebar.className = "ai-py-toc";
      sidebar.style.cssText = "position:sticky;top:20px;max-height:calc(100vh-40px);overflow-y:auto;padding-right:10px;";

      var title = document.createElement("div");
      title.style.cssText = "font-size:0.85em;font-weight:bold;color:#58a6ff;margin-bottom:8px;padding:4px 8px;";
      title.textContent = "On this page";
      sidebar.appendChild(title);

      headings.forEach(function (h) {
        var id = h.id || h.textContent.trim().toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
        if (!h.id) h.id = id;
        var a = document.createElement("a");
        a.href = "#" + id;
        a.textContent = h.textContent.trim();
        a.className = h.tagName === "H2" ? "toc-h2" : "toc-h3";
        sidebar.appendChild(a);
      });

      // Wrap container + sidebar in a flex row
      var parent = content.parentNode;
      var wrapper = document.createElement("div");
      wrapper.style.cssText = "display:flex;gap:30px;";
      wrapper.id = "ai-py-toc-wrapper";
      parent.insertBefore(wrapper, content);
      wrapper.appendChild(content);
      wrapper.appendChild(sidebar);

      // Scroll spy
      var tocLinks = Utils.$$("a", sidebar);
      var sectionIds = tocLinks.map(function (a) { return a.getAttribute("href").slice(1); });

      var ticking = false;
      window.addEventListener("scroll", function () {
        if (!ticking) {
          requestAnimationFrame(function () {
            var scrollY = window.scrollY + 80;
            var active = "";
            sectionIds.forEach(function (id) {
              var el = document.getElementById(id);
              if (el && el.offsetTop <= scrollY) active = id;
            });
            tocLinks.forEach(function (a) {
              a.classList.toggle("active", a.getAttribute("href") === "#" + active);
            });
            ticking = false;
          });
          ticking = true;
        }
      });
    });
  })();

  /* =================================================================
     10. SMOOTH SCROLL FOR ANCHOR LINKS
   ================================================================= */
  (function initSmoothScroll() {
    document.addEventListener("click", function (e) {
      var a = e.target.closest('a[href^="#"]');
      if (!a) return;
      var target = document.getElementById(a.getAttribute("href").slice(1));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  })();

  /* =================================================================
     11. KEYBOARD SHORTCUTS
   ================================================================= */
  (function initShortcuts() {
    // Build shortcuts modal
    var modal = document.createElement("div");
    modal.className = "ai-py-shortcuts";
    modal.id = "ai-py-shortcuts-modal";
    modal.innerHTML =
      '<div class="ai-py-shortcuts-inner">' +
      '<h3>Keyboard Shortcuts</h3>' +
      '<div class="row"><span>Toggle theme</span><span class="key">T</span></div>' +
      '<div class="row"><span>Focus search</span><span class="key">S</span></div>' +
      '<div class="row"><span>Close modal / search</span><span class="key">Esc</span></div>' +
      '<div class="row"><span>Show this help</span><span class="key">?</span></div>' +
      '<div style="margin-top:15px;text-align:right"><button style="background:#21262d;border:1px solid #30363d;color:#c9d1d9;padding:6px 16px;border-radius:4px;cursor:pointer" onclick="closeShortcuts()">Close</button></div>' +
      "</div>";
    document.body.appendChild(modal);

    window.closeShortcuts = function () { modal.classList.remove("show"); };
    modal.addEventListener("click", function (e) { if (e.target === modal) closeShortcuts(); });

    document.addEventListener("keydown", function (e) {
      // Don't trigger if user is typing in an input
      if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA" || e.target.tagName === "SELECT") {
        if (e.key === "Escape") {
          e.target.blur();
          // Also close any open modals
          Utils.$$(".ai-py-modal-overlay.show, .ai-py-shortcuts.show").forEach(function (m) {
            m.classList.remove("show");
          });
        }
        return;
      }
      if (e.key === "?" || (e.key === "/" && !e.ctrlKey)) {
        e.preventDefault();
        modal.classList.toggle("show");
      }
      if (e.key === "t" || e.key === "T") {
        e.preventDefault();
        var themeBtn = document.getElementById("ai-py-theme-btn");
        if (themeBtn) themeBtn.click();
      }
      if (e.key === "s" || e.key === "S") {
        e.preventDefault();
        var searchInput = Utils$(".ai-py-cmd-search-wrap input, #search, #cmd-search");
        if (searchInput) searchInput.focus();
      }
    });
  })();

  /* =================================================================
     12. STAT COUNTERS (animate numbers on scroll)
   ================================================================= */
  (function initCounters() {
    document.addEventListener("DOMContentLoaded", function () {
      var numEls = Utils.$$(".num, .stat-card .num, .stat-box .num");
      numEls = numEls.filter(function (el) {
        var txt = el.textContent.trim();
        return /^[\d,.]+$/.test(txt.replace(/[^0-9,.]/g, ""));
      });
      if (numEls.length === 0) return;

      var animated = false;

      function animate() {
        if (animated) return;
        animated = true;
        numEls.forEach(function (el) {
          var txt = el.textContent.trim();
          var target = parseFloat(txt.replace(/,/g, ""));
          if (isNaN(target) || target < 10) return;
          if (target > 100000) return; // skip very large numbers
          var duration = 1500;
          var start = performance.now();
          var isFloat = txt.indexOf(".") > -1;
          function step(now) {
            var p = Math.min((now - start) / duration, 1);
            var val = Math.round(p * target);
            el.textContent = isFloat ? (p * target).toFixed(1) : val.toLocaleString();
            if (p < 1) requestAnimationFrame(step);
            else el.textContent = txt; // restore original
          }
          requestAnimationFrame(step);
        });
      }

      // Check on scroll
      var checked = false;
      window.addEventListener("scroll", function () {
        if (checked) return;
        var rect = numEls[0].getBoundingClientRect();
        if (rect.top < window.innerHeight) {
          checked = true;
          animate();
        }
      });
      // Also try on load
      setTimeout(function () {
        var rect = numEls[0].getBoundingClientRect();
        if (rect.top < window.innerHeight) animate();
      }, 500);
    });
  })();
})();
