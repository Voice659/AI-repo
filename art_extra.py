import math

def draw_chessboard(n=8):
    lines = []
    for i in range(n):
        line = ""
        for j in range(n):
            if (i + j) % 2 == 0:
                line += "##"
            else:
                line += "  "
        lines.append(line)
    return "\n".join(lines)

def draw_sierpinski(n=5):
    def triangle(level):
        if level == 0:
            return ["*"]
        sub = triangle(level - 1)
        result = []
        for s in sub:
            result.append(" " * (2 ** (level - 1)) + s)
        for s in sub:
            result.append(s + " " + s)
        return result
    return "\n".join(triangle(n))

def draw_radial_star(n=7):
    lines = []
    for i in range(-n, n + 1):
        line = ""
        for j in range(-n, n + 1):
            val = abs(i) + abs(j)
            if val <= n and (val % 2 == 0):
                line += "*"
            else:
                line += " "
        lines.append(line)
    return "\n".join(lines)

def draw_spiral(n=20):
    lines = [[" "] * n for _ in range(n)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    r, c, di = 0, 0, 0
    for i in range(n * n):
        if 0 <= r < n and 0 <= c < n and lines[r][c] == " ":
            lines[r][c] = "*" if i % 2 == 0 else "."
        nr = r + dirs[di][0]
        nc = c + dirs[di][1]
        if not (0 <= nr < n and 0 <= nc < n and lines[nr][nc] == " "):
            di = (di + 1) % 4
            nr = r + dirs[di][0]
            nc = c + dirs[di][1]
        r, c = nr, nc
    return "\n".join("".join(row) for row in lines)

def draw_checkerboard_small():
    return r"""
# # # #
 # # # #
# # # #
 # # # #
# # # #
 # # # #
# # # #
 # # # #
"""

def draw_maze():
    return r"""
+---+---+---+---+
|   |       |   |
+   +---+   +   +
|   |   |   |   |
+   +   +   +   +
|       |   |   |
+---+---+   +   +
|           |   |
+---+---+---+---+
"""

def draw_target(n=5):
    lines = []
    for i in range(n):
        line = " " * i + "* " * (n - i)
        lines.append(line)
    for i in range(n - 2, -1, -1):
        line = " " * i + "* " * (n - i)
        lines.append(line)
    return "\n".join(lines)

def draw_fractal_tree(levels=3):
    def branch(level, width=60):
        if level <= 0:
            return [" " * (width // 2) + "*"]
        sub = branch(level - 1, width)
        result = []
        for s in sub:
            result.append(s)
        line = ""
        for i in range(width):
            if i == width // 2:
                line += "|"
            else:
                line += " "
        result.append(line)
        return result
    tree = branch(levels)
    return "\n".join(tree)

def draw_flower_garden():
    return r"""
  @   @   @   @
 @@@ @@@ @@@ @@@
@@@@@@@@@@@@@@@@
  |   |   |   |
  |   |   |   |
 \|/ \|/ \|/ \|/
  |   |   |   |
 @   @   @   @
@@@ @@@ @@@ @@@
@@@@@@@@@@@@@@@@
  |   |   |   |
  |   |   |   |
"""

def draw_cross():
    return r"""
     *
     *
     *
     *
*********
     *
     *
     *
     *
"""

def draw_fence(n=5):
    lines = []
    for i in range(n * 2):
        if i % 2 == 0:
            lines.append("|" + "-" * (n * 3) + "|")
        else:
            gap = " " * (n // 2)
            lines.append("|" + gap + "|" + gap + "|" + gap + "|")
    return "\n".join(lines)

def draw_railroad():
    return r"""
===== ===== =====
|   | |   | |   |
|   | |   | |   |
===== ===== =====
"""

def draw_tunnel():
    return r"""
     .-.
    /   \
   /     \
  /       \
 /         \
/           \
|  |     |  |
|  |     |  |
|  |     |  |
|  |     |  |
|  |     |  |
|  |     |  |
|  |     |  |
"""

def draw_lighthouse():
    return r"""
    /\
   /  \
  /    \
 /      \
/   __   \
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |__|  |
|       |
 \_____/
   | |
   | |
   | |
  /   \
 /_____\
"""

def draw_rocket():
    return r"""
    /\
   /  \
  /    \
 /      \
/   __   \
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |__|  |
|       |
 \_____/
   | |
   | |
  /| |\
 / | | \
/__|_|__\
   | |
   | |
  /   \
 /_____\
"""

def draw_submarine():
    return r"""
    ___
   /   \__________
  |   o    o    o |
  |   ____________|
  |  /
  | /
  |/
  |
"""

def draw_helicopter():
    return r"""
   ____
  /    \
 | o  o |
 |  __  |
 | |  | |
 |_|  |_|
   ||
  /||\
 / || \
   ||
  /  \
 /    \
"""

def draw_airplane():
    return r"""
      ____
     /   /
 ___/   /
|______/
|      |
|______|
   ||
  /||\
 / || \
"""

def draw_bicycle():
    return r"""
   ___
  /   \
 | o o |
 |  _  |
  \_/_/
   | |
  /   \
 /_____\
"""

def draw_umbrella():
    return r"""
    .-.
   /   \
  /  .  \
 /  / \  \
/ /     \ \
\/_______/
    |||
   /||\
  / || \
"""

def draw_compass():
    return r"""
      N
      |
   W--+--E
      |
      S
      |
      *
     * *
    *   *
   *     *
    *   *
     * *
      *
"""

def draw_snowflake(n=5):
    lines = []
    for i in range(-n, n + 1):
        line = ""
        for j in range(-n, n + 1):
            if abs(i) == abs(j) or i == 0 or j == 0:
                line += "*"
            else:
                line += " "
        lines.append(line)
    return "\n".join(lines)

def draw_web():
    lines = []
    for i in range(-8, 9):
        line = ""
        for j in range(-8, 9):
            dist = math.sqrt(i*i + j*j)
            angle = math.atan2(i, j)
            if dist < 8 and abs(math.sin(angle * 8)) < 0.3:
                line += "*"
            elif abs(dist - 4) < 0.5 or abs(dist - 8) < 0.5:
                line += "."
            else:
                line += " "
        lines.append(line)
    return "\n".join(lines)

def draw_bridge():
    return r"""
     ___===___
    /         \
   /  _     _  \
  |  | |   | |  |
  |  |_|   |_|  |
  |             |
   \    ___    /
    |  |   |  |
    |  |   |  |
    |  |   |  |
"""

def draw_castle_tower():
    return r"""
   .-.
  /   \
 |  _  |
 | | | |
 | | | |
 | | | |
 | | | |
 |_| |_|
  |___|
   | |
   | |
  /   \
 /_____\
"""

def draw_sword():
    return r"""
    /\
   /  \
  /    \
 /  __  \
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |__|  |
|        |
\________/
    ||
   /||\
  / || \
"""

def draw_shield():
    return r"""
   .===.
  /     \
 |  .-.  |
 |  | |  |
 |  | |  |
 |  | |  |
 |  '-'  |
  \     /
   '==='
    | |
   /   \
  /     \
"""

def draw_anchor():
    return r"""
     _
    | |
    | |
   /   \
  /     \
  |  _  |
  | | | |
  |_| |_|
    | |
    | |
   /   \
  /     \
 /       \
/         \
"""

def draw_crown_king():
    return r"""
   .-""-.
  / .--. \
 / /    \ \
/_/      \_\
|  \    /  |
|   \__/   |
|          |
|  |    |  |
|__|____|__|
"""

def draw_throne():
    return r"""
    .-.
   /   \
  |  |  |
  |  |  |
  |_____|
  |     |
  |     |
  |_____|
  |  |  |
  |  |  |
  |  |  |
"""
