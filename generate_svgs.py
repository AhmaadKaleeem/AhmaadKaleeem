import os
import requests
import math

# Portfolio Theme (Soft Fluffy Dark Pastel)
THEME_VOID = "#18181B"
THEME_SIGNAL = "#FAFAFA"
THEME_ALLOW = "#F472B6" # Pink
THEME_ESCALATE = "#A78BFA" # Soft Purple
FONT_FAMILY = "Nunito, sans-serif"
FONT_URL = "https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;800&display=swap"
BOX_BG = "#27272A" # Soft zinc box background

# GitHub GraphQL Setup
GH_TOKEN = os.getenv('GH_TOKEN')
HEADERS = {"Authorization": f"Bearer {GH_TOKEN}"} if GH_TOKEN else {}
GRAPHQL_URL = "https://api.github.com/graphql"

def fetch_github_stats():
    if not GH_TOKEN:
        return {
            "name": "Ahmad Kaleem Bhatti",
            "login": "AhmaadKaleeem",
            "followers": 15,
            "total_commits": 342,
            "total_prs": 12,
            "total_issues": 5
        }
    
    query = """
    query {
      viewer {
        name
        login
        followers { totalCount }
        contributionsCollection {
          totalCommitContributions
          totalPullRequestContributions
          totalIssueContributions
        }
      }
    }
    """
    response = requests.post(GRAPHQL_URL, json={'query': query}, headers=HEADERS)
    if response.status_code == 200:
        data = response.json().get('data', {}).get('viewer', {})
        contribs = data.get('contributionsCollection', {})
        return {
            "name": data.get("name"),
            "login": data.get("login"),
            "followers": data.get("followers", {}).get("totalCount", 0),
            "total_commits": contribs.get("totalCommitContributions", 0),
            "total_prs": contribs.get("totalPullRequestContributions", 0),
            "total_issues": contribs.get("totalIssueContributions", 0),
        }
    else:
        print(f"Failed to fetch data: {response.text}")
        return None

def generate_header_svg(title, filename):
    svg = f"""<svg width="800" height="120" viewBox="0 0 800 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <style>
        @import url('{FONT_URL}');
        .title {{
            font-family: '{FONT_FAMILY}'; font-weight: 800; font-size: 42px; fill: {THEME_SIGNAL};
            opacity: 0; animation: textReveal 1.5s cubic-bezier(0.2, 0.8, 0.2, 1) forwards 0.3s;
        }}
        .glow {{ fill: {THEME_ESCALATE}; filter: blur(8px); opacity: 0.4; animation: pulseGlow 3s infinite alternate; }}
        .dot {{ fill: {THEME_ESCALATE}; animation: pulse 2s infinite; }}
        .line {{ stroke: {THEME_ALLOW}; stroke-width: 3; stroke-linecap: round; stroke-dasharray: 800; stroke-dashoffset: 800; animation: drawLine 1.2s cubic-bezier(0.8, 0, 0.2, 1) forwards; }}
        .accent-box {{ fill: {THEME_ESCALATE}; opacity: 0; animation: boxReveal 0.5s ease-out forwards 0.8s; rx: 4; }}
        @keyframes textReveal {{ 0% {{ opacity: 0; transform: translateX(-20px); filter: blur(4px); }} 100% {{ opacity: 1; transform: translateX(0); filter: blur(0px); }} }}
        @keyframes drawLine {{ to {{ stroke-dashoffset: 0; }} }}
        @keyframes pulseGlow {{ 0% {{ opacity: 0.2; transform: scale(0.98); }} 100% {{ opacity: 0.6; transform: scale(1.02); }} }}
        @keyframes boxReveal {{ to {{ opacity: 1; transform: scaleX(1); }} }}
        @keyframes pulse {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.3; }} }}
    </style>
    <rect width="800" height="120" fill="transparent" />
    <rect x="20" y="60" width="100" height="40" class="glow" />
    <text x="50" y="75" class="title">{title}</text>
    <rect x="20" y="45" width="8" height="35" class="accent-box" transform-origin="20 45" transform="scaleX(0)" />
    <line x1="20" y1="95" x2="780" y2="95" class="line" />
    <circle cx="780" cy="95" r="5" class="dot" />
</svg>"""
    with open(filename, 'w', encoding='utf-8') as f: f.write(svg)

def generate_name_svg():
    svg = f"""<svg width="800" height="60" viewBox="0 0 800 60" fill="none" xmlns="http://www.w3.org/2000/svg">
    <style>
        @import url('{FONT_URL}');
        .name {{ font-family: '{FONT_FAMILY}'; font-weight: 800; font-size: 24px; fill: {THEME_SIGNAL}; opacity: 0; animation: textReveal 1.5s cubic-bezier(0.2, 0.8, 0.2, 1) forwards 0.2s; }}
        .badge-text {{ font-family: '{FONT_FAMILY}'; font-size: 11px; font-weight: 700; fill: {THEME_SIGNAL}; }}
        .line {{ stroke: {THEME_ESCALATE}; stroke-width: 3; stroke-linecap: round; }}
        @keyframes textReveal {{ 0% {{ opacity: 0; transform: translateX(-20px); filter: blur(4px); }} 100% {{ opacity: 1; transform: translateX(0); filter: blur(0px); }} }}
    </style>
    <rect width="800" height="60" fill="transparent" />
    <a href="https://www.ahmadkaleem.tech" target="_blank">
        <line x1="10" y1="30" x2="80" y2="30" class="line" />
        <text x="100" y="38" class="name">Ahmad Kaleem Bhatti</text>
    </a>
    <text x="420" y="36" font-family="{FONT_FAMILY}" font-size="28px" fill="#555">|</text>
    <g transform="translate(705, 18)">
        <a href="https://www.ahmadkaleem.tech" target="_blank">
            <rect x="0" y="0" width="75" height="24" fill="{THEME_ALLOW}" rx="12" />
            <text x="37.5" y="16" class="badge-text" text-anchor="middle">Portfolio</text>
        </a>
    </g>
</svg>"""
    with open("name.svg", 'w', encoding='utf-8') as f: f.write(svg)

def generate_terminal_svg():
    svg = f"""<svg width="800" height="200" viewBox="0 0 800 200" fill="none" xmlns="http://www.w3.org/2000/svg">
    <style>
        @import url('{FONT_URL}');
        .bg {{ fill: {THEME_VOID}; }}
        .border {{ stroke: {THEME_ESCALATE}; stroke-width: 2; stroke-opacity: 0.3; }}
        .text {{ font-family: '{FONT_FAMILY}'; font-size: 18px; fill: {THEME_SIGNAL}; font-weight: 700; }}
        .prompt {{ fill: {THEME_ESCALATE}; font-weight: 800; }}
        .highlight {{ fill: {THEME_ALLOW}; font-weight: 800; }}
        .cursor {{ fill: {THEME_ALLOW}; animation: blink 0.8s step-end infinite; }}
        .line1 {{ opacity: 0; animation: fadeIn 0.1s forwards 0.5s; }}
        .line2 {{ opacity: 0; animation: fadeIn 0.1s forwards 1.2s; }}
        .line3 {{ opacity: 0; animation: fadeIn 0.1s forwards 2.0s; }}
        .line4 {{ opacity: 0; animation: fadeIn 0.1s forwards 2.8s; }}
        .line5 {{ opacity: 0; animation: fadeIn 0.1s forwards 3.6s; }}
        @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
        @keyframes fadeIn {{ to {{ opacity: 1; }} }}
    </style>
    <rect x="5" y="5" width="790" height="190" rx="16" class="bg border" />
    <rect x="5" y="5" width="790" height="35" rx="16" fill="{BOX_BG}" class="border" />
    <circle cx="25" cy="22" r="7" fill="#F43F5E" />
    <circle cx="45" cy="22" r="7" fill="#FBBF24" />
    <circle cx="65" cy="22" r="7" fill="#34D399" />
    <text x="360" y="24" class="text" style="font-size: 15px; opacity: 0.7;">🌸 ahmad ✨</text>
    <g transform="translate(25, 75)">
        <g class="line1"><text y="0" class="text"><tspan class="prompt">👋 Hello! I am</tspan></text></g>
        <g class="line2"><text y="30" class="text highlight">Ahmad Kaleem Bhatti | AI Engineer &amp; Backend Developer</text></g>
        <g class="line3"><text y="60" class="text"><tspan class="prompt">🎯 Current Mission</tspan></text></g>
        <g class="line4"><text y="90" class="text highlight">Building deterministic security infrastructure for AI agents.</text></g>
        <g class="line5">
            <text y="120" class="text"><tspan class="prompt">✨</tspan></text>
            <rect x="35" y="105" width="10" height="18" class="cursor" rx="4" />
        </g>
    </g>
</svg>"""
    with open("terminal.svg", 'w', encoding='utf-8') as f: f.write(svg)

def generate_radar_svg():
    skills = [
        ("Python & FastAPI", 95), ("AI Agents", 90), ("Go Backend", 85),
        ("Security (OPA)", 88), ("PostgreSQL", 85), ("React/TS", 80),
        ("Flutter", 75), ("Docker", 70)
    ]
    cx, cy, max_radius = 400, 200, 120
    num_sides = len(skills)
    angle_step = 2 * math.pi / num_sides
    points, labels = [], ""
    for i, (name, value) in enumerate(skills):
        angle = i * angle_step - math.pi / 2
        r = max_radius * (value / 100)
        x, y = cx + r * math.cos(angle), cy + r * math.sin(angle)
        points.append(f"{x},{y}")
        lx, ly = cx + (max_radius + 45) * math.cos(angle), cy + (max_radius + 25) * math.sin(angle)
        text_anchor = "middle"
        if math.cos(angle) > 0.1: text_anchor = "start"
        elif math.cos(angle) < -0.1: text_anchor = "end"
        labels += f'<text x="{lx}" y="{ly}" class="label" text-anchor="{text_anchor}">{name}</text>\n'
    poly_points = " ".join(points)
    
    svg = f"""<svg width="800" height="400" viewBox="0 0 800 400" fill="none" xmlns="http://www.w3.org/2000/svg">
    <style>
        @import url('{FONT_URL}');
        .radar-bg {{ fill: {THEME_VOID}; rx: 16px; }}
        .grid-line {{ stroke: {THEME_ESCALATE}; stroke-width: 1; fill: none; opacity: 0.2; }}
        .axis-line {{ stroke: {THEME_ESCALATE}; stroke-width: 1; opacity: 0.3; }}
        .radar-poly {{ fill: {THEME_ALLOW}; fill-opacity: 0.2; stroke: {THEME_ALLOW}; stroke-width: 3; animation: radarPulse 3s infinite alternate; stroke-linejoin: round; }}
        .node {{ fill: {THEME_ALLOW}; }}
        .label {{ font-family: '{FONT_FAMILY}'; font-size: 14px; fill: {THEME_SIGNAL}; font-weight: 800; }}
        .title {{ font-family: '{FONT_FAMILY}'; font-size: 24px; font-weight: 800; fill: {THEME_ESCALATE}; }}
        @keyframes radarPulse {{ 0% {{ filter: drop-shadow(0 0 5px {THEME_ALLOW}); transform: scale(1); transform-origin: 400px 200px; }} 100% {{ filter: drop-shadow(0 0 15px {THEME_ALLOW}); transform: scale(1.02); transform-origin: 400px 200px; }} }}
        .axis-group {{ opacity: 0; animation: fadeIn 1s forwards 0.5s; }}
        .radar-poly {{ stroke-dasharray: 1000; stroke-dashoffset: 1000; animation: drawRadar 1.5s forwards 1s, radarPulse 3s infinite alternate 2.5s; }}
        @keyframes drawRadar {{ to {{ stroke-dashoffset: 0; }} }}
        @keyframes fadeIn {{ to {{ opacity: 1; }} }}
    </style>
    <rect width="800" height="400" class="radar-bg" />
    <text x="40" y="45" class="title">🌟 My Skill Radar 🌟</text>
    <g class="axis-group">
"""
    for level in range(1, 5):
        r = max_radius * (level / 4)
        grid_pts = []
        for i in range(num_sides):
            angle = i * angle_step - math.pi / 2
            gx, gy = cx + r * math.cos(angle), cy + r * math.sin(angle)
            grid_pts.append(f"{gx},{gy}")
        svg += f'        <polygon points="{" ".join(grid_pts)}" class="grid-line" />\n'
    for i in range(num_sides):
        angle = i * angle_step - math.pi / 2
        ax, ay = cx + max_radius * math.cos(angle), cy + max_radius * math.sin(angle)
        svg += f'        <line x1="{cx}" y1="{cy}" x2="{ax}" y2="{ay}" class="axis-line" />\n'
    svg += f"""{labels}</g><polygon points="{poly_points}" class="radar-poly" />"""
    for pt in points:
        x, y = pt.split(",")
        svg += f'<circle cx="{x}" cy="{y}" r="5" class="node" />\n'
    svg += "</svg>"
    with open("radar.svg", 'w', encoding='utf-8') as f: f.write(svg)

def generate_stats_svg(stats):
    if not stats: return
    svg = f"""<svg width="495" height="195" viewBox="0 0 495 195" fill="none" xmlns="http://www.w3.org/2000/svg">
    <style>
        @import url('{FONT_URL}');
        .container {{ fill: {THEME_VOID}; }}
        .border-glow {{ stroke: {THEME_ALLOW}; stroke-width: 2; filter: blur(6px); animation: pulseGlow 2s infinite alternate; }}
        .border-solid {{ stroke: {THEME_ALLOW}; stroke-width: 2; }}
        .header {{ font-family: '{FONT_FAMILY}'; font-size: 20px; font-weight: 800; fill: {THEME_ESCALATE}; }}
        .label {{ font-family: '{FONT_FAMILY}'; font-size: 14px; fill: {THEME_SIGNAL}; opacity: 0.9; font-weight: 700; }}
        .value {{ font-family: '{FONT_FAMILY}'; font-size: 32px; font-weight: 800; fill: {THEME_ALLOW}; }}
        .stat-box {{ opacity: 0; animation: statReveal 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) forwards; }}
        .box1 {{ animation-delay: 0.5s; }} .box2 {{ animation-delay: 0.7s; }} .box3 {{ animation-delay: 0.9s; }}
        @keyframes statReveal {{ 0% {{ opacity: 0; transform: translateY(15px); }} 100% {{ opacity: 1; transform: translateY(0); }} }}
        @keyframes pulseGlow {{ 0% {{ opacity: 0.3; }} 100% {{ opacity: 0.8; }} }}
    </style>
    <rect x="2" y="2" width="491" height="191" rx="16" class="container border-solid" />
    <rect x="2" y="2" width="491" height="191" rx="16" fill="none" class="border-glow" />
    <text x="25" y="40" class="header">✨ {stats.get('login', 'AhmaadKaleeem')}'s Stats ✨</text>
    <line x1="25" y1="55" x2="470" y2="55" class="border-solid" style="opacity: 0.2; stroke-width: 1;" />
    
    <g class="stat-box box1" transform="translate(0,0)">
        <rect x="25" y="70" width="135" height="100" rx="12" fill="{BOX_BG}" />
        <text x="92.5" y="105" class="label" text-anchor="middle">Commits</text>
        <text x="92.5" y="150" class="value" text-anchor="middle">{stats['total_commits']}</text>
    </g>
    <g class="stat-box box2" transform="translate(0,0)">
        <rect x="180" y="70" width="135" height="100" rx="12" fill="{BOX_BG}" />
        <text x="247.5" y="105" class="label" text-anchor="middle">PRs</text>
        <text x="247.5" y="150" class="value" text-anchor="middle">{stats['total_prs']}</text>
    </g>
    <g class="stat-box box3" transform="translate(0,0)">
        <rect x="335" y="70" width="135" height="100" rx="12" fill="{BOX_BG}" />
        <text x="402.5" y="105" class="label" text-anchor="middle">Issues</text>
        <text x="402.5" y="150" class="value" text-anchor="middle">{stats['total_issues']}</text>
    </g>
</svg>"""
    with open("stats.svg", 'w', encoding='utf-8') as f: f.write(svg)

def generate_actsurance_architecture_svg():
    svg = f"""<svg width="800" height="400" viewBox="0 0 800 400" fill="none" xmlns="http://www.w3.org/2000/svg">
    <style>
        @import url('{FONT_URL}');
        text {{ font-family: '{FONT_FAMILY}'; fill: {THEME_SIGNAL}; font-size: 14px; font-weight: 700; }}
        .title {{ font-size: 24px; font-weight: 800; fill: {THEME_ESCALATE}; }}
        .box {{ fill: {BOX_BG}; stroke: {THEME_ALLOW}; stroke-width: 2; rx: 12; }}
        .box-escalate {{ fill: {BOX_BG}; stroke: {THEME_ESCALATE}; stroke-width: 2; rx: 12; }}
        .flow-line {{ stroke: {THEME_ALLOW}; stroke-width: 3; stroke-linecap: round; stroke-dasharray: 8 8; animation: flow 20s linear infinite; opacity: 0.8; }}
        .flow-line-escalate {{ stroke: {THEME_ESCALATE}; stroke-width: 3; stroke-linecap: round; stroke-dasharray: 8 8; animation: flow 20s linear infinite; opacity: 0.8; }}
        @keyframes flow {{ to {{ stroke-dashoffset: -400; }} }}
        .pulse {{ animation: pulseNode 3s infinite alternate; }}
        @keyframes pulseNode {{ 0% {{ filter: drop-shadow(0 0 4px {THEME_ALLOW}); }} 100% {{ filter: drop-shadow(0 0 12px {THEME_ALLOW}); }} }}
    </style>
    <rect width="800" height="400" fill="{THEME_VOID}" rx="16" />
    <text x="35" y="45" class="title">🌸 Actsurance Architecture</text>
    <path d="M 120 120 L 220 120" class="flow-line" />
    <path d="M 340 120 L 440 120" class="flow-line" />
    <path d="M 560 120 L 660 120" class="flow-line" />
    <path d="M 500 140 L 500 240 L 560 240" class="flow-line-escalate" />
    <path d="M 620 280 L 620 320" class="flow-line-escalate" />
    <path d="M 680 240 L 720 240 L 720 140 L 680 140" class="flow-line" style="animation-direction: reverse;" />
    
    <rect x="20" y="90" width="100" height="60" class="box" />
    <text x="35" y="115">AI Agent</text>
    <text x="35" y="135" style="font-size: 11px; opacity: 0.7;">Tool Call</text>
    
    <rect x="220" y="80" width="120" height="150" class="box pulse" />
    <text x="240" y="105" style="fill: {THEME_ESCALATE};">L1 Firewall</text>
    <text x="235" y="130" style="font-size: 12px;">RE2 Regex</text>
    <text x="235" y="150" style="font-size: 12px;">Identity JWT</text>
    <text x="235" y="170" style="font-size: 12px;">Rate Limiter</text>
    <text x="235" y="210" style="font-size: 11px; fill: {THEME_ALLOW};">403 DENY</text>
    
    <rect x="440" y="90" width="120" height="80" class="box" />
    <text x="455" y="115" style="fill: {THEME_ESCALATE};">Splitter</text>
    <text x="455" y="135" style="font-size: 12px;">OPA (RBAC)</text>
    <text x="455" y="155" style="font-size: 12px;">ONNX (Risk)</text>
    
    <rect x="660" y="90" width="120" height="60" class="box" />
    <text x="675" y="115">Fast Path</text>
    <text x="675" y="135" style="font-size: 12px;">Sealed Broker</text>
    
    <rect x="560" y="210" width="120" height="70" class="box-escalate" />
    <text x="575" y="235" style="fill: {THEME_ESCALATE};">Slow Path</text>
    <text x="575" y="255" style="font-size: 12px;">Temporal</text>
    <text x="575" y="270" style="font-size: 12px;">Human Review</text>
    
    <rect x="560" y="320" width="120" height="60" class="box" style="stroke: #555;" />
    <text x="570" y="345">Postgres</text>
    <text x="570" y="365" style="font-size: 12px;">Offline Verifier</text>
</svg>"""
    with open("actsurance-architecture.svg", 'w', encoding='utf-8') as f: f.write(svg)

def main():
    print("Fetching GitHub Stats...")
    stats = fetch_github_stats()
    generate_stats_svg(stats)
    generate_terminal_svg()
    headers = {
        "header-about.svg": "About Me", "header-building.svg": "What I'm Building",
        "header-stack.svg": "Tech Stack", "header-projects.svg": "Projects",
        "header-experience.svg": "Experience", "header-background.svg": "Background",
        "header-certifications.svg": "Certifications", "header-contact.svg": "Contact"
    }
    for filename, title in headers.items(): generate_header_svg(title, filename)
    generate_radar_svg()
    generate_actsurance_architecture_svg()
    generate_name_svg()
    print("All SVGs generated successfully.")

if __name__ == "__main__": main()
