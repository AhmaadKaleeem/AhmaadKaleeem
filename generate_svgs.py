"""
Generate all custom SVGs for Ahmad Kaleem Bhatti's GitHub profile README.
Palette:  #0A0A0A (void)  #FFFFFF (signal)  #FF6B00 (action/orange)  #22C55E (verified/green)
"""

import math
import os

VOID    = "#0A0A0A"
SIGNAL  = "#FFFFFF"
ACTION  = "#FF6B00"
VERIFIED= "#22C55E"
MUTED   = "#1E1E1E"
DIMMED  = "#A3A3A3"

OUT = "assets"
os.makedirs(OUT, exist_ok=True)

def w(name, content):
    path = f"{OUT}/{name}"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  wrote {path}")

# ── 1. HERO BANNER: Centered header with responsive styling ──────────────────

def generate_banner(is_dark=True):
    W, H = 850, 260
    bg_color = "#0D1117" if is_dark else "#F6F8FA"
    name_color = "#FFFFFF" if is_dark else "#0A0A0A"
    sub_color = "#A3A3A3" if is_dark else "#555555"
    grid_color = "#161B22" if is_dark else "#E1E4E8"
    
    # Background
    bg = f'<rect width="{W}" height="{H}" fill="{bg_color}" rx="8"/>'
    
    # Grid pattern
    grid = ""
    for x in range(0, W, 40):
        grid += f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="{grid_color}" stroke-width="1"/>'
    for y in range(0, H, 40):
        grid += f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{grid_color}" stroke-width="1"/>'
        
    # Subtle nodes in background
    nodes = [
        (150, 80, VERIFIED), (700, 60, ACTION),
        (200, 200, ACTION), (750, 200, VERIFIED),
        (80, 150, VERIFIED), (800, 120, ACTION)
    ]
    node_svg = ""
    for nx, ny, color in nodes:
        node_svg += f'<circle cx="{nx}" cy="{ny}" r="4" fill="{color}" opacity="0.6"/>'
        node_svg += f'<line x1="{nx}" y1="{ny}" x2="{nx+50}" y2="{ny}" stroke="{color}" stroke-width="1" opacity="0.3"/>'
        node_svg += f'<line x1="{nx}" y1="{ny}" x2="{nx}" y2="{ny+50}" stroke="{color}" stroke-width="1" opacity="0.3"/>'
        
    # Text
    y_center = H // 2 - 10
    name_svg = f'<text x="{W//2}" y="{y_center}" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, Roboto, sans-serif" font-size="48" font-weight="800" fill="{name_color}" letter-spacing="-0.5">Ahmad Kaleem Bhatti</text>'
    
    sub_svg = f'<text x="{W//2}" y="{y_center + 40}" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, Roboto, sans-serif" font-size="16" fill="{sub_color}" letter-spacing="0.5">I build software that has to actually work.</text>'
    
    # Accent line
    line_svg = f'<rect x="{W//2 - 30}" y="{y_center + 70}" width="60" height="3" fill="{ACTION}" rx="1"/>'
    
    svg = f'''<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
  {bg}
  {grid}
  {node_svg}
  {name_svg}
  {sub_svg}
  {line_svg}
</svg>'''
    
    fname = "banner-dark.svg" if is_dark else "banner-light.svg"
    w(fname, svg)

# ── 2. DIVIDER: thin horizontal rule with orange accent ───────────────────────

def divider():
    svg = f'''<svg width="800" height="1" viewBox="0 0 800 1"
     xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="1" fill="{MUTED}"/>
  <rect width="48" height="1" fill="{ACTION}"/>
</svg>'''
    w("divider.svg", svg)

# ── 3. STATUS BADGE: shipped (green) or building (orange) ────────────────────

def status_badge(name, label, color):
    svg = f'''<svg width="100" height="22" viewBox="0 0 100 22"
     xmlns="http://www.w3.org/2000/svg">
  <rect width="100" height="22" fill="{VOID}" rx="2"/>
  <rect width="3" height="22" fill="{color}" rx="1"/>
  <text x="12" y="15" font-family="monospace" font-size="9"
        fill="{color}" letter-spacing="1.5">{label}</text>
</svg>'''
    w(name, svg)

# ── MAIN ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Generating SVGs...")
    generate_banner(True)
    generate_banner(False)
    divider()
    status_badge("badge-shipped.svg",  "● SHIPPED",  VERIFIED)
    status_badge("badge-building.svg", "● BUILDING", ACTION)
    print("Done.")
