(function () {
  "use strict";

  /* ========== 1. THEME TOGGLE ========== */
  (function initTheme() {
    // Inject light-theme CSS once
    if (!document.getElementById("ai-py-theme-css")) {
      var style = document.createElement("style");
      style.id = "ai-py-theme-css";
      style.textContent =
        ".light-theme{--bg:#f6f8fa;--bg2:#fff;--bg3:#e1e4e8;--fg:#24292e;--fg2:#586069;--border:#d1d5da}" +
        ".light-theme{background:var(--bg);color:var(--fg)}" +
        ".light-theme a{color:#0366d6}" +
        ".light-theme .nav,.light-theme .navbar,.light-theme [style*='background:#161b22']{background:var(--bg2)!important;border-color:var(--border)!important}" +
        ".light-theme .container,.light-theme .stat-card,.light-theme .feature-card,.light-theme .card," +
        ".light-theme .cmd-table tr:hover,.light-theme table tr:hover{background:var(--bg2)}" +
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
        ".light-theme [style*='color:#484f58']{color:var(--fg2)!important}";
      document.head.appendChild(style);
    }

    // Floating theme toggle button
    if (!document.getElementById("ai-py-theme-btn")) {
      var btn = document.createElement("button");
      btn.id = "ai-py-theme-btn";
      btn.textContent = "☀";
      Object.assign(btn.style, {
        position: "fixed",
        bottom: "16px",
        right: "16px",
        zIndex: "9999",
        width: "40px",
        height: "40px",
        borderRadius: "50%",
        border: "1px solid #30363d",
        background: "#161b22",
        color: "#c9d1d9",
        fontSize: "18px",
        cursor: "pointer",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        boxShadow: "0 2px 8px rgba(0,0,0,0.4)",
        transition: "background 0.2s, color 0.2s",
        lineHeight: "1",
        padding: "0",
      });
      btn.addEventListener("mouseenter", function () {
        btn.style.background = "#21262d";
      });
      btn.addEventListener("mouseleave", function () {
        btn.style.background = themeActive() ? "#e1e4e8" : "#161b22";
      });
      btn.addEventListener("click", toggleTheme);
      document.body.appendChild(btn);
    }

    function themeActive() {
      return document.body.classList.contains("light-theme");
    }

    function toggleTheme() {
      document.body.classList.toggle("light-theme");
      var active = themeActive();
      localStorage.setItem("ai-py-theme", active ? "light" : "dark");
      var btn = document.getElementById("ai-py-theme-btn");
      if (btn) {
        btn.textContent = active ? "☾" : "☀";
        btn.style.background = active ? "#e1e4e8" : "#161b22";
        btn.style.color = active ? "#24292e" : "#c9d1d9";
      }
    }

    // Restore saved theme
    if (
      localStorage.getItem("ai-py-theme") === "light" &&
      !themeActive()
    ) {
      toggleTheme();
    }
  })();

  /* ========== 2. COPY-TO-CLIPBOARD ========== */
  (function initCopyButtons() {
    document.addEventListener("DOMContentLoaded", function () {
      document.querySelectorAll("pre").forEach(function (pre) {
        if (pre.querySelector(".ai-py-copy-btn")) return;
        var btn = document.createElement("button");
        btn.className = "ai-py-copy-btn";
        btn.textContent = "Copy";
        Object.assign(btn.style, {
          position: "absolute",
          top: "4px",
          right: "4px",
          background: "#21262d",
          color: "#8b949e",
          border: "1px solid #30363d",
          borderRadius: "4px",
          padding: "2px 8px",
          fontSize: "11px",
          cursor: "pointer",
          fontFamily: "inherit",
          zIndex: "10",
          opacity: "0",
          transition: "opacity 0.2s",
        });
        if (pre.style.position === "") pre.style.position = "relative";
        pre.style.position = pre.style.position || "relative";
        pre.appendChild(btn);
        pre.addEventListener("mouseenter", function () {
          btn.style.opacity = "1";
        });
        pre.addEventListener("mouseleave", function () {
          btn.style.opacity = "0";
        });
        btn.addEventListener("click", function (e) {
          e.stopPropagation();
          var text = pre.textContent;
          if (btn.textContent === "Copied!" || btn.textContent === "Copied")
            return;
          navigator.clipboard.writeText(text).then(
            function () {
              btn.textContent = "Copied!";
              btn.style.color = "#7ee787";
              btn.style.borderColor = "#30a745";
              setTimeout(function () {
                btn.textContent = "Copy";
                btn.style.color = "#8b949e";
                btn.style.borderColor = "#30363d";
              }, 2000);
            },
            function () {
              btn.textContent = "Failed";
              btn.style.color = "#f85149";
              setTimeout(function () {
                btn.textContent = "Copy";
                btn.style.color = "#8b949e";
              }, 2000);
            }
          );
        });
      });
    });
  })();

  /* ========== 3. NAV HIGHLIGHT ========== */
  (function initNavHighlight() {
    document.addEventListener("DOMContentLoaded", function () {
      var page = document.location.pathname
        .split("/")
        .pop()
        .toLowerCase();
      if (!page) page = "index.html";
      document.querySelectorAll(
        '.nav a, [class*="nav"] a, div[style*="padding"] a'
      ).forEach(function (a) {
        var href = a.getAttribute("href");
        if (href && href.toLowerCase() === page) {
          a.style.fontWeight = "bold";
        }
      });
    });
  })();

  /* ========== 4. DATA INDEX (data-index.html) ========== */
  // Provide global filterTable/sortTable for data-index.html
  window.filterTable = function filterTable() {
    var q = (document.getElementById("search") || {}).value || "";
    q = q.toLowerCase();
    var filterEl = document.getElementById("filter");
    var filterVal = filterEl ? filterEl.value : "all";
    var sortEl = document.getElementById("sort");
    var sortVal = sortEl ? sortEl.value : "name";
    var tbody = document.getElementById("table");
    if (!tbody || typeof DATA === "undefined") return;

    var filtered = DATA.filter(function (d) {
      if (filterVal === "curated" && d.t !== "curated") return false;
      if (filterVal === "bulk" && d.t !== "bulk") return false;
      if (q && !d.d.toLowerCase().includes(q)) return false;
      return true;
    });

    filtered.sort(function (a, b) {
      if (sortVal === "count") return b.c - a.c;
      return a.d.localeCompare(b.d);
    });

    // Rebuild header
    tbody.innerHTML =
      '<tr><th onclick="sortTable(0)">#</th><th onclick="sortTable(1)">Table Name</th><th onclick="sortTable(2)">Entries</th><th onclick="sortTable(3)">Type</th></tr>';

    filtered.forEach(function (d, i) {
      var tr = tbody.insertRow();
      tr.insertCell().textContent = i + 1;
      tr.insertCell().textContent = d.d;
      var cell3 = tr.insertCell();
      cell3.textContent = d.c.toLocaleString();
      cell3.style.color = "#58a6ff";
      cell3.style.fontFamily = "monospace";
      var cell4 = tr.insertCell();
      if (d.t === "curated") {
        cell4.innerHTML =
          '<span class="tag-curated">Curated</span>';
      } else {
        cell4.innerHTML =
          '<span class="tag-bulk">Bulk (' + d.c + ")</span>";
      }
    });

    // Update stats
    var statsEl = document.getElementById("stats");
    if (statsEl) {
      statsEl.textContent =
        filtered.length +
        " of " +
        DATA.length +
        " tables — " +
        filtered.reduce(function (s, d) {
          return s + d.c;
        }, 0).toLocaleString() +
        " entries";
    }
  };

  window.sortTable = function sortTable(col) {
    var sortEl = document.getElementById("sort");
    if (!sortEl) return;
    if (col === 1) sortEl.value = "name";
    else if (col === 2) sortEl.value = "count";
    else if (col === 0) sortEl.value = "name";
    window.filterTable();
  };

  // Call filterTable on load if DATA exists
  if (typeof DATA !== "undefined") {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", window.filterTable);
    } else {
      window.filterTable();
    }
  }

  /* ========== 5. DOCS PAGE SEARCH (AI.py-docs.html) ========== */
  (function initDocsSearch() {
    document.addEventListener("DOMContentLoaded", function () {
      var tables = document.querySelectorAll("table.cmd-table");
      if (tables.length === 0) return;

      // Create search UI
      var container = tables[0].parentNode;
      var searchDiv = document.createElement("div");
      searchDiv.style.cssText =
        "margin: 10px 0; display: flex; gap: 8px; align-items: center;";
      var input = document.createElement("input");
      input.type = "text";
      input.placeholder = "Search commands...";
      input.style.cssText =
        "background: #161b22; border: 1px solid #30363d; color: #c9d1d9; padding: 8px 12px; border-radius: 4px; font-size: 0.9em; flex: 1; max-width: 400px;";
      input.addEventListener("input", function () {
        var q = input.value.toLowerCase();
        document
          .querySelectorAll("table.cmd-table tr")
          .forEach(function (tr, idx) {
            if (idx === 0) return; // skip header
            var text = tr.textContent.toLowerCase();
            tr.style.display = text.includes(q) ? "" : "none";
          });
      });
      // Clear button
      var clearBtn = document.createElement("button");
      clearBtn.textContent = "Clear";
      clearBtn.style.cssText =
        "background: #21262d; border: 1px solid #30363d; color: #8b949e; padding: 8px 12px; border-radius: 4px; cursor: pointer; font-size: 0.85em;";
      clearBtn.addEventListener("click", function () {
        input.value = "";
        input.dispatchEvent(new Event("input"));
      });
      searchDiv.appendChild(input);
      searchDiv.appendChild(clearBtn);
      container.insertBefore(searchDiv, tables[0]);
    });
  })();
})();
