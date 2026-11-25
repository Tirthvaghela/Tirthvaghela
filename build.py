"""Generates the light/dark SVG cards used by README.md.

Run:  python build.py      (writes into ./assets)
Edit the DATA section below, re-run, and commit the assets folder.
"""
from pathlib import Path
from html import escape

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

THEMES = {
    "light": dict(ink="#111111", body="#4A4A4A", muted="#8A8A8A", rule="#E4E4E4",
                  card="#FAFAF8", accent="#FF4F00", node="#FFFFFF"),
    "dark":  dict(ink="#F0F0F0", body="#B4BCC4", muted="#7D8590", rule="#2A3038",
                  card="#11161D", accent="#FF5A1F", node="#0D1117"),
}

SERIF = "Georgia, 'Times New Roman', 'Iowan Old Style', serif"
SANS = "'Helvetica Neue', 'Segoe UI', Arial, sans-serif"
MONO = "'SF Mono', 'Cascadia Code', Consolas, 'Courier New', monospace"

# ----------------------------------------------------------------- DATA
LINKS = ["Portfolio", "LinkedIn", "GitHub", "Email"]

FACTS = [("BASED IN", "Ahmedabad, India"), ("STUDYING", "Int. M.Sc IT · Year 5"),
         ("FOCUS", "Vision · LLMs · Voice"), ("BUILDING", "VoiceForm AI")]

PIPELINE = ["Paper / PDF", "OCR", "LLM dialogue", "Speech EN·HI·GU", "Filled form"]

PROJECTS = [
    ("Urban Signal", "TRAFFIC AI",
     ["Retimes signals from live congestion and", "gives emergency vehicles instant priority."],
     "Next.js · Flask · YOLOv4 · OpenCV"),
    ("RIGS", "ROAD SAFETY",
     ["Spots riders without helmets, reads the", "plate with OCR and issues an e-challan."],
     "React · Node.js · YOLOv8 · OCR"),
    ("Wedding Face Finder", "IMAGE SEARCH",
     ["Finds every photo of one person across a", "huge unsorted collection in under a second."],
     "Flask · DeepFace · ArcFace"),
    ("Electrox", "VOTING PLATFORM",
     ["Web + mobile elections end to end, with", "role-based access and a live dashboard."],
     "Flutter · React · Node.js · Flask · MongoDB"),
    ("Vois", "SOCIAL MEDIA",
     ["Real-time feed with follows, a personalised", "stream and JWT-secured auth."],
     "React · FastAPI · MongoDB"),
    ("EventEase", "COLLEGE EVENTS",
     ["Event registration with capacity limits and", "automatic confirmation emails."],
     "Django · REST · SQLite"),
    ("FreshVault", "E-COMMERCE",
     ["Local grocery store with accounts, cart,", "wishlist and admin-managed inventory."],
     "PHP · MySQL · Tailwind"),
]

TOOLKIT = [
    ("LANGUAGES", "Python   JavaScript   TypeScript   SQL   Dart   PHP"),
    ("FRONTEND", "React   Next.js   Tailwind   Flutter   HTML / CSS"),
    ("BACKEND", "Django   Flask   FastAPI   Node.js   REST   JWT"),
    ("DATA", "MongoDB   MySQL   SQLite"),
    ("AI / VISION", "YOLOv8   YOLOv4   OpenCV   DeepFace   ArcFace   OCR   LLMs"),
    ("TOOLS", "Git   GitHub   Vercel"),
]

EXPERIENCE = dict(
    when="FEB 2026", where="REMOTE", role="Full-Stack Web Development Intern",
    org="Prodigy InfoTech",
    points=["Built modular, responsive frontends in semantic HTML / CSS.",
            "Wrote backend routes and REST integrations that cut payload size and render time.",
            "Added token-based auth middleware to secure user data and API endpoints."],
)
# ----------------------------------------------------------------- HELPERS


def t(x, y, s, size, color, font=SANS, weight=400, anchor="start", spacing=0, italic=False):
    style = f"font-family:{font};font-size:{size}px;font-weight:{weight};letter-spacing:{spacing}px"
    if italic:
        style += ";font-style:italic"
    return (f'<text x="{x}" y="{y}" fill="{color}" text-anchor="{anchor}" '
            f'style="{style}">{escape(s)}</text>')


def svg(w, h, body, pad=6):
    # small side padding so glyph overhangs (italics, serif capitals) are not clipped
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w + 2 * pad}" height="{h}" '
            f'viewBox="{-pad} 0 {w + 2 * pad} {h}">{body}</svg>\n')


def header(c, num, label, right=None, dot=False):
    out = [f'<line x1="0" y1="0.5" x2="1200" y2="0.5" stroke="{c["rule"]}"/>',
           t(0, 40, num, 15, c["accent"], MONO, 600, spacing=2),
           t(40, 40, label, 15, c["muted"], MONO, 500, spacing=3)]
    if right:
        out.append(t(1200, 40, right, 15, c["muted"], MONO, 500, "end", 3))
        if dot:
            w = len(right) * 12
            out.append(f'<circle cx="{1200 - w - 14}" cy="35" r="4" fill="{c["accent"]}"/>')
    return "".join(out)


def write(name, theme, content):
    (OUT / f"{name}-{theme}.svg").write_text(content, encoding="utf-8")

# ----------------------------------------------------------------- SECTIONS


def links(c):
    for label in LINKS:
        w = 150
        body = (t(0, 26, label.upper(), 14, c["ink"], MONO, 600, spacing=2.5) +
                t(w - 6, 26, "↗", 16, c["accent"], SANS, 600, "end") +
                f'<line x1="0" y1="40" x2="{w}" y2="40" stroke="{c["ink"]}" stroke-width="1.5"/>')
        yield label.lower(), svg(w, 44, body)


def about(c):
    b = [header(c, "01", "ABOUT")]
    lines = ["Full-stack developer & AI/ML engineer.",
             "I take AI out of the notebook and into"]
    b.append(t(0, 110, lines[0], 38, c["ink"], SERIF, spacing=-0.5))
    b.append(t(0, 158, lines[1], 38, c["muted"], SERIF, spacing=-0.5, italic=True))
    b.append(t(0, 206, "products people actually use.", 38, c["muted"], SERIF, spacing=-0.5, italic=True))
    b.append(t(0, 262, "Computer-vision pipelines that run on live video, LLM systems that talk instead of just chat,",
               18, c["body"]))
    b.append(t(0, 290, "and the full-stack plumbing that holds it all together.", 18, c["body"]))
    y0, colw = 330, 300
    for i, (k, v) in enumerate(FACTS):
        x = i * colw
        b.append(f'<line x1="{x}" y1="{y0}" x2="{x + colw - 24}" y2="{y0}" stroke="{c["rule"]}"/>')
        b.append(t(x, y0 + 30, k, 12, c["muted"], MONO, 500, spacing=2.5))
        b.append(t(x, y0 + 60, v, 19, c["ink"], SANS, 500))
    return svg(1200, 410, "".join(b))


def now(c):
    b = [header(c, "02", "NOW BUILDING", "IN PROGRESS", dot=True)]
    b.append(t(0, 128, "VoiceForm AI", 64, c["ink"], SERIF, spacing=-2))
    b.append(t(0, 176, "Fill any form just by talking. It reads a paper or PDF form, turns it into a spoken",
               19, c["body"]))
    b.append(t(0, 204, "conversation in English, Hindi or Gujarati, and writes the answers back onto the original layout.",
               19, c["body"]))
    n, gap = len(PIPELINE), 28
    w = (1200 - gap * (n - 1)) / n
    y = 250
    for i, label in enumerate(PIPELINE):
        x = i * (w + gap)
        hot = i == 2
        stroke = c["accent"] if hot else c["rule"]
        b.append(f'<rect x="{x + 0.5}" y="{y}" width="{w - 1}" height="74" rx="8" '
                 f'fill="{c["node"]}" stroke="{stroke}" stroke-width="{1.5 if hot else 1}"/>')
        b.append(t(x + 18, y + 28, f"{i + 1:02d}", 12, c["accent"] if hot else c["muted"], MONO, 600, spacing=2))
        b.append(t(x + 18, y + 54, label, 18, c["ink"], SANS, 500))
        if i < n - 1:
            ax = x + w + 6
            b.append(f'<path d="M{ax} {y + 37}h{gap - 12}m-5 -4l5 4l-5 4" fill="none" '
                     f'stroke="{c["muted"]}" stroke-width="1.5"/>')
    return svg(1200, 340, "".join(b))


def simple_header(c, num, label, right=None):
    return svg(1200, 64, header(c, num, label, right))


def project(c, i, p):
    name, cat, desc, stack = p
    w, h = 600, 270
    b = [f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="12" fill="{c["card"]}" stroke="{c["rule"]}"/>',
         t(32, 50, f"{i:02d}", 14, c["accent"], MONO, 600, spacing=2),
         t(w - 32, 50, cat, 13, c["muted"], MONO, 500, "end", 2.5),
         t(32, 116, name, 40, c["ink"], SERIF, spacing=-1)]
    for j, line in enumerate(desc):
        b.append(t(32, 160 + j * 27, line, 18, c["body"]))
    b.append(f'<line x1="32" y1="{h - 58}" x2="{w - 32}" y2="{h - 58}" stroke="{c["rule"]}"/>')
    b.append(t(32, h - 26, stack, 13, c["muted"], MONO, 500, spacing=0.5))
    b.append(t(w - 32, h - 26, "↗", 18, c["muted"], SANS, 500, "end"))
    return svg(w, h, "".join(b))


def more(c):
    w, h = 600, 270
    b = [f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="12" fill="none" '
         f'stroke="{c["rule"]}" stroke-dasharray="6 6"/>',
         t(32, 50, "+", 18, c["accent"], MONO, 600),
         t(32, 116, "More on GitHub", 40, c["ink"], SERIF, spacing=-1, italic=True),
         t(32, 160, "Assignments, experiments, prototypes", 18, c["body"]),
         t(32, 187, "and everything in between.", 18, c["body"]),
         t(w - 32, h - 26, "↗", 18, c["accent"], SANS, 600, "end")]
    return svg(w, h, "".join(b))


def toolkit(c):
    b = [header(c, "04", "TOOLKIT")]
    for i, (k, v) in enumerate(TOOLKIT):
        y = 90 + i * 52
        b.append(t(0, y + 24, k, 13, c["muted"], MONO, 500, spacing=2.5))
        b.append(t(240, y + 25, v.replace("   ", "  ·  "), 21, c["ink"], SANS))
        b.append(f'<line x1="0" y1="{y + 44}" x2="1200" y2="{y + 44}" stroke="{c["rule"]}"/>')
    return svg(1200, 90 + len(TOOLKIT) * 52 + 10, "".join(b))


def experience(c):
    e = EXPERIENCE
    b = [header(c, "05", "EXPERIENCE"),
         t(0, 104, e["when"], 14, c["ink"], MONO, 600, spacing=2.5),
         t(0, 128, e["where"], 13, c["muted"], MONO, 500, spacing=2.5),
         t(240, 108, e["role"], 34, c["ink"], SERIF, spacing=-0.5),
         t(240, 140, e["org"], 18, c["muted"], SANS, italic=True)]
    for i, p in enumerate(e["points"]):
        y = 190 + i * 34
        b.append(f'<line x1="240" y1="{y - 6}" x2="256" y2="{y - 6}" stroke="{c["accent"]}" stroke-width="2"/>')
        b.append(t(272, y, p, 18, c["body"]))
    return svg(1200, 190 + len(e["points"]) * 34 + 10, "".join(b))


def footer(c):
    b = [f'<line x1="0" y1="0.5" x2="1200" y2="0.5" stroke="{c["rule"]}"/>',
         t(0, 56, "Off the keyboard — video editing, drawing, guitar, and music while coding.",
           20, c["body"], SERIF, italic=True),
         t(1200, 56, "TIRTH VAGHELA", 13, c["muted"], MONO, 500, "end", 3)]
    return svg(1200, 84, "".join(b))


for theme, c in THEMES.items():
    for name, content in links(c):
        write(f"link-{name}", theme, content)
    write("about", theme, about(c))
    write("now", theme, now(c))
    write("work", theme, simple_header(c, "03", "SELECTED WORK", f"{len(PROJECTS):02d} PROJECTS"))
    for i, p in enumerate(PROJECTS, 1):
        write(f"project-{i:02d}", theme, project(c, i, p))
    write("project-more", theme, more(c))
    write("toolkit", theme, toolkit(c))
    write("experience", theme, experience(c))
    write("activity", theme, simple_header(c, "06", "ACTIVITY", "LAST 31 DAYS"))
    write("footer", theme, footer(c))

print("wrote", len(list(OUT.glob("*.svg"))), "files to", OUT)
