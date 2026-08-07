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
    """Generates an animated SVG header"""
    svg = f"""<svg width="800" height="120" viewBox="0 0 800 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <style>
        @import url('{FONT_URL}');
        .title {{
            font-family: '{FONT_FAMILY}';
            font-weight: 700;
            font-size: 48px;
            fill: {THEME_SIGNAL};
            animation: fadeIn 1.5s ease-in-out forwards;
            opacity: 0;
        }}
        .dot {{
            fill: {THEME_ESCALATE};
            animation: pulse 2s infinite;
        }}
        .line {{
            stroke: {THEME_ESCALATE};
            stroke-width: 2;
            stroke-dasharray: 800;
            stroke-dashoffset: 800;
            animation: drawLine 1s ease-out 0.5s forwards;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        @keyframes drawLine {{
            to {{ stroke-dashoffset: 0; }}
        }}
        @keyframes pulse {{
            0% {{ opacity: 0.5; }}
            50% {{ opacity: 1; }}
            100% {{ opacity: 0.5; }}
        }}
    </style>
    <rect width="800" height="120" fill="{THEME_VOID}" />
    
    <!-- Title -->
    <text x="40" y="75" class="title">{title}</text>
    <circle cx="20" cy="62" r="6" class="dot" />
    
    <!-- Decorative Line -->
    <line x1="40" y1="95" x2="760" y2="95" class="line" />
</svg>"""
    with open(filename, 'w') as f:
        f.write(svg)
    print(f"Generated {filename}")

def generate_terminal_svg():
    """Generates an animated terminal intro"""
    svg = f"""<svg width="800" height="200" viewBox="0 0 800 200" fill="none" xmlns="http://www.w3.org/2000/svg">
    <style>
        @import url('{FONT_URL}');
        .bg {{ fill: {THEME_VOID}; }}
        .border {{ stroke: {THEME_ESCALATE}; stroke-width: 1; stroke-opacity: 0.5; }}
        .text {{ font-family: '{FONT_FAMILY}'; font-size: 18px; fill: {THEME_SIGNAL}; }}
        .prompt {{ fill: {THEME_ESCALATE}; font-weight: 700; }}
        .cursor {{ fill: {THEME_ALLOW}; animation: blink 1s step-end infinite; }}
        .typing1 {{ stroke: transparent; animation: typing1 2s steps(40, end) forwards; white-space: nowrap; overflow: hidden; display: inline-block; width: 0; }}
        
        @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
        @keyframes typing1 {{ from {{ width: 0; }} to {{ width: 100%; }} }}
    </style>
    
    <!-- Window -->
    <rect x="5" y="5" width="790" height="190" rx="6" class="bg border" />
    <!-- Top Bar -->
    <rect x="5" y="5" width="790" height="30" rx="6" fill="#111" class="border" />
    <circle cx="20" cy="20" r="6" fill="#FF5F56" />
    <circle cx="40" cy="20" r="6" fill="#FFBD2E" />
    <circle cx="60" cy="20" r="6" fill="#27C93F" />
    <text x="350" y="22" class="text" style="font-size: 14px; opacity: 0.5;">bash - actsurance</text>

    <!-- Terminal Content -->
    <g transform="translate(20, 65)">
        <text y="0" class="text">
            <tspan class="prompt">ahmad@secure-node:~$</tspan> whoami
        </text>
        <text y="30" class="text" style="fill: {THEME_ALLOW};">Ahmad Kaleem Bhatti | AI Security Engineer</text>
        <text y="70" class="text">
            <tspan class="prompt">ahmad@secure-node:~$</tspan> cat current_mission.txt
        </text>
        <text y="100" class="text" style="fill: {THEME_ALLOW};">Building deterministic control layers for autonomous agents.</text>
        <rect x="540" y="85" width="10" height="18" class="cursor" />
    </g>
</svg>"""
    with open("terminal.svg", 'w') as f:
        f.write(svg)
    print("Generated terminal.svg")

def generate_stats_svg(stats):
    """Generates an SVG for GitHub Stats"""
    if not stats:
        print("No stats data available.")
        return

    # Draw stats with Actsurance premium theme
    svg = f"""<svg width="800" height="250" viewBox="0 0 800 250" fill="none" xmlns="http://www.w3.org/2000/svg">
    <style>
        @import url('{FONT_URL}');
        .container {{
            fill: {THEME_VOID};
        }}
        .border {{
            stroke: {THEME_ESCALATE};
            stroke-width: 1;
            stroke-opacity: 0.5;
        }}
        .header {{
            font-family: '{FONT_FAMILY}';
            font-size: 24px;
            font-weight: 700;
            fill: {THEME_ESCALATE};
        }}
        .label {{
            font-family: '{FONT_FAMILY}';
            font-size: 16px;
            fill: {THEME_SIGNAL};
            opacity: 0.8;
        }}
        .value {{
            font-family: '{FONT_FAMILY}';
            font-size: 28px;
            font-weight: 700;
            fill: {THEME_ALLOW};
        }}
        .card {{
            animation: fadeIn 1s ease-in-out forwards;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}
    </style>
    
    <!-- Background & Border -->
    <rect x="5" y="5" width="790" height="240" rx="8" class="container border" />
    
    <g class="card">
        <!-- Title -->
        <text x="40" y="45" class="header">&gt; SYSTEM_STATS: {stats['login']}</text>
        <line x1="40" y1="60" x2="760" y2="60" class="border" />
        
        <!-- Stat: Commits -->
        <rect x="40" y="80" width="220" height="120" rx="4" fill="#0A080C" class="border" />
        <text x="60" y="115" class="label">Total Commits</text>
        <text x="60" y="165" class="value">{stats['total_commits']}</text>
        
        <!-- Stat: PRs -->
        <rect x="290" y="80" width="220" height="120" rx="4" fill="#0A080C" class="border" />
        <text x="310" y="115" class="label">Pull Requests</text>
        <text x="310" y="165" class="value">{stats['total_prs']}</text>
        
        <!-- Stat: Issues -->
        <rect x="540" y="80" width="220" height="120" rx="4" fill="#0A080C" class="border" />
        <text x="560" y="115" class="label">Issues</text>
        <text x="560" y="165" class="value">{stats['total_issues']}</text>
    </g>
</svg>"""
    
    with open("stats.svg", 'w') as f:
        f.write(svg)
    print("Generated stats.svg")

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

if __name__ == "__main__":
    main()
