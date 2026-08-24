import os
import requests

# Portfolio Theme
THEME_VOID = "#000000"
THEME_SIGNAL = "#FFFFFF"
THEME_ALLOW = "#059D00"
THEME_ESCALATE = "#DF6513"
FONT_FAMILY = "Courier Prime, monospace"
FONT_URL = "https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400;1,700&amp;display=swap"

# GitHub GraphQL Setup
GH_TOKEN = os.getenv('GH_TOKEN')
HEADERS = {"Authorization": f"Bearer {GH_TOKEN}"} if GH_TOKEN else {}
GRAPHQL_URL = "https://api.github.com/graphql"

def fetch_github_stats():
    """Fetch user stats from GitHub GraphQL API"""
    if not GH_TOKEN:
        # Return mock data for testing locally if no token is provided
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
        followers {
          totalCount
        }
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
    """Generates an animated, glowing SVG header to amaze recruiters"""
    svg = f"""<svg width="800" height="120" viewBox="0 0 800 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <style>
        @import url('{FONT_URL}');
        .title {{
            font-family: '{FONT_FAMILY}';
            font-weight: 700;
            font-size: 42px;
            fill: #000000;
            opacity: 0;
            animation: textReveal 1.5s cubic-bezier(0.2, 0.8, 0.2, 1) forwards 0.3s;
        }}
        @media (prefers-color-scheme: dark) {{
            .title {{ fill: #FFFFFF; }}
        }}
        .glow {{
            fill: {THEME_ESCALATE};
            filter: blur(8px);
            opacity: 0.4;
            animation: pulseGlow 3s infinite alternate;
        }}
        .dot {{
            fill: {THEME_ESCALATE};
            animation: pulse 2s infinite;
        }}
        .line {{
            stroke: {THEME_ALLOW};
            stroke-width: 2;
            stroke-dasharray: 800;
            stroke-dashoffset: 800;
            animation: drawLine 1.2s cubic-bezier(0.8, 0, 0.2, 1) forwards;
        }}
        .accent-box {{
            fill: {THEME_ESCALATE};
            opacity: 0;
            animation: boxReveal 0.5s ease-out forwards 0.8s;
        }}
        
        @keyframes textReveal {{
            0% {{ opacity: 0; transform: translateX(-20px); letter-spacing: -5px; filter: blur(4px); }}
            100% {{ opacity: 1; transform: translateX(0); letter-spacing: 0px; filter: blur(0px); }}
        }}
        @keyframes drawLine {{
            to {{ stroke-dashoffset: 0; }}
        }}
        @keyframes pulseGlow {{
            0% {{ opacity: 0.2; transform: scale(0.98); }}
            100% {{ opacity: 0.6; transform: scale(1.02); }}
        }}
        @keyframes boxReveal {{
            to {{ opacity: 1; transform: scaleX(1); }}
        }}
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.3; }}
        }}
    </style>
    <rect width="800" height="120" fill="transparent" />
    
    <!-- Background Glow -->
    <rect x="20" y="60" width="100" height="40" class="glow" />
    
    <!-- Title -->
    <text x="50" y="75" class="title">{title}</text>
    <rect x="20" y="45" width="8" height="35" class="accent-box" transform-origin="20 45" transform="scaleX(0)" />
    
    <!-- Decorative Line -->
    <line x1="20" y1="95" x2="780" y2="95" class="line" />
    <circle cx="780" cy="95" r="4" class="dot" />
</svg>"""
    with open(filename, 'w') as f:
        f.write(svg)
    print(f"Generated {filename}")

def generate_name_svg():
    """Generates a dynamic name SVG logo at the top with inline badges"""
    svg = f"""<svg width="800" height="60" viewBox="0 0 800 60" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <style>
        @import url('{FONT_URL}');
        .name {{
            font-family: '{FONT_FAMILY}';
            font-weight: 700;
            font-size: 24px;
            fill: #000000;
            opacity: 0;
            animation: textReveal 1.5s cubic-bezier(0.2, 0.8, 0.2, 1) forwards 0.2s;
        }}
        .badge-text {{
            font-family: 'Verdana, Geneva, sans-serif';
            font-size: 11px;
            font-weight: normal;
            fill: #FFFFFF;
        }}
        @media (prefers-color-scheme: dark) {{
            .name {{ fill: #FFFFFF; }}
        }}
        .line {{
            stroke: {THEME_ESCALATE};
            stroke-width: 2;
        }}
        
        @keyframes textReveal {{
            0% {{ opacity: 0; transform: translateX(-20px); filter: blur(4px); }}
            100% {{ opacity: 1; transform: translateX(0); filter: blur(0px); }}
        }}
    </style>
    
    <rect width="800" height="60" fill="transparent" />
    
    <!-- Left Side: Dash, Name, Pipe -->
    <a href="https://www.ahmadkaleem.tech" target="_blank">
        <line x1="10" y1="30" x2="80" y2="30" class="line" />
        <text x="100" y="38" class="name">Ahmad Kaleem Bhatti</text>
    </a>
    <text x="420" y="36" font-family="{FONT_FAMILY}" font-size="28px" fill="#555">|</text>
    
    <!-- Right Side: Badges -->
    <g transform="translate(705, 18)">
        <!-- Portfolio Badge -->
        <a href="https://www.ahmadkaleem.tech" target="_blank">
            <rect x="0" y="0" width="75" height="24" fill="#000000" rx="0" />
            <text x="37.5" y="16" class="badge-text" text-anchor="middle">Portfolio</text>
        </a>
    </g>
</svg>"""
    with open("name.svg", 'w') as f:
        f.write(svg)
    print("Generated name.svg")

def generate_terminal_svg():
    """Generates a highly animated terminal intro"""
    svg = f"""<svg width="800" height="200" viewBox="0 0 800 200" fill="none" xmlns="http://www.w3.org/2000/svg">
    <style>
        @import url('{FONT_URL}');
        .bg {{ fill: {THEME_VOID}; }}
        .border {{ stroke: {THEME_ESCALATE}; stroke-width: 1; stroke-opacity: 0.5; }}
        .text {{ font-family: '{FONT_FAMILY}'; font-size: 18px; fill: {THEME_SIGNAL}; }}
        .prompt {{ fill: {THEME_ESCALATE}; font-weight: 700; }}
        .highlight {{ fill: {THEME_ALLOW}; font-weight: 700; }}
        .cursor {{ fill: {THEME_ALLOW}; animation: blink 0.8s step-end infinite; }}
        
        /* Typing animation effects */
        .type-line {{ overflow: hidden; white-space: nowrap; }}
        
        .line1 {{ opacity: 0; animation: fadeIn 0.1s forwards 0.5s; }}
        .line2 {{ opacity: 0; animation: fadeIn 0.1s forwards 1.2s; }}
        .line3 {{ opacity: 0; animation: fadeIn 0.1s forwards 2.0s; }}
        .line4 {{ opacity: 0; animation: fadeIn 0.1s forwards 2.8s; }}
        .line5 {{ opacity: 0; animation: fadeIn 0.1s forwards 3.6s; }}
        
        @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
        @keyframes fadeIn {{ to {{ opacity: 1; }} }}
    </style>
    
    <!-- Window -->
    <rect x="5" y="5" width="790" height="190" rx="6" class="bg border" />
    <!-- Top Bar -->
    <rect x="5" y="5" width="790" height="30" rx="6" fill="#111" class="border" />
    <circle cx="20" cy="20" r="6" fill="#FF5F56" />
    <circle cx="40" cy="20" r="6" fill="#FFBD2E" />
    <circle cx="60" cy="20" r="6" fill="#27C93F" />
    <text x="350" y="22" class="text" style="font-size: 14px; opacity: 0.5;">bash - ahmad - 80x24</text>

    <!-- Terminal Content -->
    <g transform="translate(20, 65)">
        <g class="line1">
            <text y="0" class="text"><tspan class="prompt">ahmad@Actsurance ~$</tspan> whoami</text>
        </g>
        
        <g class="line2">
            <text y="30" class="text highlight">Ahmad Kaleem Bhatti | AI Engineer &amp; Backend Developer</text>
        </g>
        
        <g class="line3">
            <text y="60" class="text"><tspan class="prompt">ahmad@Actsurance ~$</tspan> cat current_mission.txt</text>
        </g>
        
        <g class="line4">
            <text y="90" class="text highlight">Building deterministic security infrastructure for AI agents.</text>
        </g>

        <g class="line5">
            <text y="120" class="text"><tspan class="prompt">ahmad@Actsurance ~$</tspan></text>
            <rect x="195" y="105" width="10" height="18" class="cursor" />
        </g>
    </g>
</svg>"""
    with open("terminal.svg", 'w') as f:
        f.write(svg)
    print("Generated terminal.svg")

import math

def generate_radar_svg():
    """Generates an animated SVG Radar Chart for Skills"""
    skills = [
        ("Python & FastAPI", 95),
        ("AI Agents & Tooling", 90),
        ("Go & Backend", 85),
        ("Security (OPA, mTLS)", 88),
        ("PostgreSQL & Redis", 85),
        ("React & TypeScript", 80),
        ("Flutter", 75),
        ("DevOps & Docker", 70)
    ]
    
    cx, cy = 400, 200
    max_radius = 120
    num_sides = len(skills)
    angle_step = 2 * math.pi / num_sides
    
    # Calculate polygon points
    points = []
    labels = ""
    for i, (name, value) in enumerate(skills):
        angle = i * angle_step - math.pi / 2
        r = max_radius * (value / 100)
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        points.append(f"{x},{y}")
        
        # Label coordinates
        lx = cx + (max_radius + 40) * math.cos(angle)
        ly = cy + (max_radius + 20) * math.sin(angle)
        text_anchor = "middle"
        if math.cos(angle) > 0.1: text_anchor = "start"
        elif math.cos(angle) < -0.1: text_anchor = "end"
        
        labels += f'<text x="{lx}" y="{ly}" class="label" text-anchor="{text_anchor}">{name}</text>\n'
        
    poly_points = " ".join(points)
    
    svg = f"""<svg width="800" height="400" viewBox="0 0 800 400" fill="none" xmlns="http://www.w3.org/2000/svg">
    <style>
        @import url('{FONT_URL}');
        .radar-bg {{ fill: {THEME_VOID}; }}
        .grid-line {{ stroke: rgba(255, 255, 255, 0.1); stroke-width: 1; fill: none; }}
        .axis-line {{ stroke: rgba(255, 255, 255, 0.2); stroke-width: 1; }}
        .radar-poly {{
            fill: rgba(5, 157, 0, 0.3);
            stroke: {THEME_ALLOW};
            stroke-width: 2;
            animation: radarPulse 3s infinite alternate;
        }}
        .node {{ fill: {THEME_ALLOW}; }}
        .label {{ font-family: '{FONT_FAMILY}'; font-size: 13px; fill: {THEME_SIGNAL}; font-weight: bold; }}
        .title {{ font-family: '{FONT_FAMILY}'; font-size: 20px; font-weight: bold; fill: {THEME_ESCALATE}; }}
        
        @keyframes radarPulse {{
            0% {{ filter: drop-shadow(0 0 5px {THEME_ALLOW}); transform: scale(1); transform-origin: 400px 200px; }}
            100% {{ filter: drop-shadow(0 0 15px {THEME_ALLOW}); transform: scale(1.02); transform-origin: 400px 200px; }}
        }}
        
        .axis-group {{ opacity: 0; animation: fadeIn 1s forwards 0.5s; }}
        .radar-poly {{ stroke-dasharray: 1000; stroke-dashoffset: 1000; animation: drawRadar 1.5s forwards 1s, radarPulse 3s infinite alternate 2.5s; }}
        
        @keyframes drawRadar {{ to {{ stroke-dashoffset: 0; }} }}
        @keyframes fadeIn {{ to {{ opacity: 1; }} }}
    </style>
    
    <rect width="800" height="400" class="radar-bg" />
    <text x="30" y="40" class="title">&gt; SKILL_RADAR.exe</text>
    
    <!-- Grid -->
    <g class="axis-group">
"""
    
    # Draw concentric grid polygons
    for level in range(1, 5):
        r = max_radius * (level / 4)
        grid_pts = []
        for i in range(num_sides):
            angle = i * angle_step - math.pi / 2
            gx = cx + r * math.cos(angle)
            gy = cy + r * math.sin(angle)
            grid_pts.append(f"{gx},{gy}")
        svg += f'        <polygon points="{" ".join(grid_pts)}" class="grid-line" />\n'
        
    # Draw axis lines
    for i in range(num_sides):
        angle = i * angle_step - math.pi / 2
        ax = cx + max_radius * math.cos(angle)
        ay = cy + max_radius * math.sin(angle)
        svg += f'        <line x1="{cx}" y1="{cy}" x2="{ax}" y2="{ay}" class="axis-line" />\n'
        
    svg += f"""
        {labels}
    </g>
    
    <!-- Data Polygon -->
    <polygon points="{poly_points}" class="radar-poly" />
    
    <!-- Nodes -->
"""
    for pt in points:
        x, y = pt.split(",")
        svg += f'    <circle cx="{x}" cy="{y}" r="4" class="node" />\n'
        
    svg += "</svg>"
    
    with open("radar.svg", 'w') as f:
        f.write(svg)
    print("Generated radar.svg")

def generate_stats_svg(stats):
    """Generates an incredibly animated SVG for GitHub Stats"""
    if not stats:
        print("No stats data available.")
        return

    # Draw stats with Actsurance premium theme
    svg = f"""<svg width="800" height="250" viewBox="0 0 800 250" fill="none" xmlns="http://www.w3.org/2000/svg">
    <style>
        @import url('{FONT_URL}');
        .container {{ fill: {THEME_VOID}; }}
        .border-glow {{
            stroke: {THEME_ALLOW};
            stroke-width: 2;
            filter: blur(4px);
            animation: pulseGlow 2s infinite alternate;
        }}
        .border-solid {{
            stroke: {THEME_ALLOW};
            stroke-width: 1;
        }}
        .header {{ font-family: '{FONT_FAMILY}'; font-size: 24px; font-weight: 700; fill: {THEME_ESCALATE}; }}
        .label {{ font-family: '{FONT_FAMILY}'; font-size: 16px; fill: {THEME_SIGNAL}; opacity: 0.8; }}
        .value {{ font-family: '{FONT_FAMILY}'; font-size: 32px; font-weight: 700; fill: {THEME_ALLOW}; }}
        
        .stat-box {{ opacity: 0; animation: statReveal 0.8s cubic-bezier(0.2, 0.8, 0.2, 1) forwards; }}
        .box1 {{ animation-delay: 0.5s; }}
        .box2 {{ animation-delay: 0.7s; }}
        .box3 {{ animation-delay: 0.9s; }}
        
        @keyframes statReveal {{
            0% {{ opacity: 0; transform: translateY(20px); }}
            100% {{ opacity: 1; transform: translateY(0); }}
        }}
        @keyframes pulseGlow {{
            0% {{ opacity: 0.3; }}
            100% {{ opacity: 0.8; }}
        }}
    </style>
    
    <!-- Background -->
    <rect x="5" y="5" width="790" height="240" rx="8" class="container border-solid" />
    <rect x="5" y="5" width="790" height="240" rx="8" fill="none" class="border-glow" />
    
    <!-- Title -->
    <text x="40" y="45" class="header">&gt; SYSTEM_STATS {stats.get('login', 'AhmaadKaleeem')}</text>
    <line x1="40" y1="60" x2="760" y2="60" class="border-solid" style="opacity: 0.3;" />
    
    <!-- Stat: Commits -->
    <g class="stat-box box1" transform="translate(0,0)">
        <rect x="40" y="80" width="220" height="120" rx="4" fill="#0A080C" class="border-solid" style="stroke-opacity: 0.5" />
        <text x="60" y="115" class="label">Total Commits</text>
        <text x="60" y="165" class="value">{stats['total_commits']}</text>
    </g>
    
    <!-- Stat: PRs -->
    <g class="stat-box box2" transform="translate(0,0)">
        <rect x="290" y="80" width="220" height="120" rx="4" fill="#0A080C" class="border-solid" style="stroke-opacity: 0.5" />
        <text x="310" y="115" class="label">Pull Requests</text>
        <text x="310" y="165" class="value">{stats['total_prs']}</text>
    </g>
    
    <!-- Stat: Issues -->
    <g class="stat-box box3" transform="translate(0,0)">
        <rect x="540" y="80" width="220" height="120" rx="4" fill="#0A080C" class="border-solid" style="stroke-opacity: 0.5" />
        <text x="560" y="115" class="label">Issues</text>
        <text x="560" y="165" class="value">{stats['total_issues']}</text>
    </g>
</svg>"""
    
    with open("stats.svg", 'w') as f:
        f.write(svg)
    print("Generated stats.svg")

def generate_actsurance_architecture_svg():
    """Generates an animated architecture diagram for Actsurance"""
    svg = f"""<svg width="800" height="400" viewBox="0 0 800 400" fill="none" xmlns="http://www.w3.org/2000/svg">
    <style>
        @import url('{FONT_URL}');
        text {{ font-family: '{FONT_FAMILY}'; fill: {THEME_SIGNAL}; font-size: 14px; }}
        .title {{ font-size: 20px; font-weight: bold; fill: {THEME_ESCALATE}; }}
        .box {{ fill: #0A080C; stroke: {THEME_ALLOW}; stroke-width: 1.5; rx: 6; }}
        .box-escalate {{ fill: #0A080C; stroke: {THEME_ESCALATE}; stroke-width: 1.5; rx: 6; }}
        
        /* Flow animations */
        .flow-line {{ stroke: {THEME_ALLOW}; stroke-width: 2; stroke-dasharray: 6 6; animation: flow 20s linear infinite; opacity: 0.6; }}
        .flow-line-escalate {{ stroke: {THEME_ESCALATE}; stroke-width: 2; stroke-dasharray: 6 6; animation: flow 20s linear infinite; opacity: 0.6; }}
        
        @keyframes flow {{ to {{ stroke-dashoffset: -400; }} }}
        
        .pulse {{ animation: pulseNode 3s infinite alternate; }}
        @keyframes pulseNode {{
            0% {{ filter: drop-shadow(0 0 2px {THEME_ALLOW}); }}
            100% {{ filter: drop-shadow(0 0 8px {THEME_ALLOW}); }}
        }}
    </style>
    
    <rect width="800" height="400" fill="{THEME_VOID}" />
    <text x="30" y="40" class="title">Actsurance Architecture</text>
    
    <!-- Flow Lines -->
    <path d="M 120 120 L 220 120" class="flow-line" />
    <path d="M 340 120 L 440 120" class="flow-line" />
    <path d="M 560 120 L 660 120" class="flow-line" />
    <path d="M 500 140 L 500 240 L 560 240" class="flow-line-escalate" />
    <path d="M 620 280 L 620 320" class="flow-line-escalate" />
    <path d="M 680 240 L 720 240 L 720 140 L 680 140" class="flow-line" style="animation-direction: reverse;" />
    
    <!-- Nodes -->
    <!-- Client -->
    <rect x="20" y="90" width="100" height="60" class="box" />
    <text x="35" y="115">AI Agent</text>
    <text x="35" y="135" style="font-size: 10px; opacity: 0.7;">Tool Call</text>
    
    <!-- TIER 1 -->
    <rect x="220" y="80" width="120" height="150" class="box pulse" />
    <text x="240" y="105" style="font-weight: bold; fill: {THEME_ESCALATE};">L1 Firewall</text>
    <text x="235" y="130" style="font-size: 12px;">RE2 Regex</text>
    <text x="235" y="150" style="font-size: 12px;">Identity JWT</text>
    <text x="235" y="170" style="font-size: 12px;">Rate Limiter</text>
    <text x="235" y="210" style="font-size: 10px; fill: #DF6513;">[403 HARD DENY]</text>
    
    <!-- Splitter -->
    <rect x="440" y="90" width="120" height="80" class="box" />
    <text x="455" y="115" style="font-weight: bold; fill: {THEME_ESCALATE};">Splitter</text>
    <text x="455" y="135" style="font-size: 12px;">OPA (RBAC)</text>
    <text x="455" y="155" style="font-size: 12px;">ONNX (Risk)</text>
    
    <!-- Fast Path -->
    <rect x="660" y="90" width="120" height="60" class="box" />
    <text x="675" y="115" style="font-weight: bold;">Fast Path</text>
    <text x="675" y="135" style="font-size: 12px;">Sealed Broker</text>
    
    <!-- Slow Path -->
    <rect x="560" y="210" width="120" height="70" class="box-escalate" />
    <text x="575" y="235" style="font-weight: bold; fill: {THEME_ESCALATE};">Slow Path</text>
    <text x="575" y="255" style="font-size: 12px;">Temporal Workflow</text>
    <text x="575" y="270" style="font-size: 12px;">Human Review</text>
    
    <!-- Verification -->
    <rect x="560" y="320" width="120" height="60" class="box" style="stroke: #555;" />
    <text x="570" y="345">Postgres Audit</text>
    <text x="570" y="365" style="font-size: 12px;">Offline Verifier</text>
</svg>"""
    with open("actsurance-architecture.svg", 'w') as f:
        f.write(svg)
    print("Generated actsurance-architecture.svg")

def main():
    # 1. Fetch Stats
    print("Fetching GitHub Stats...")
    stats = fetch_github_stats()
    
    # 2. Generate Stats SVG
    generate_stats_svg(stats)
    
    # 3. Generate Terminal SVG
    generate_terminal_svg()
    
    # 4. Generate Header SVGs
    headers = {
        "header-about.svg": "About Me",
        "header-building.svg": "What I'm Building",
        "header-stack.svg": "Tech Stack",
        "header-projects.svg": "Projects",
        "header-background.svg": "Background",
        "header-certifications.svg": "Certifications",
        "header-contact.svg": "Contact"
    }
    
    for filename, title in headers.items():
        generate_header_svg(title, filename)
        
    # Generate Radar SVG
    generate_radar_svg()
    
    # Generate Actsurance Architecture SVG
    generate_actsurance_architecture_svg()
    
    # Generate Name SVG
    generate_name_svg()
    
    print("All SVGs generated successfully.")

if __name__ == "__main__":
    main()
