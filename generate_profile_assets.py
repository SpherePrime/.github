# -*- coding: utf-8 -*-
"""
SpherePrime GitHub Profile SVG Generator
Generates high-precision dark industrial aesthetic vector graphics
matching LilKALINOV and dwertyfa288 styles for the SpherePrime organization.
"""

import os
import shutil

OUTPUT_DIR = "profile/assets"
ROOT_ASSETS_DIR = "assets"

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(ROOT_ASSETS_DIR, exist_ok=True)

# Common SVG Style Block
COMMON_STYLE = """
text { font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, 'Helvetica Neue', Arial, sans-serif; }
.mono { font-family: 'Cascadia Mono', 'JetBrains Mono', Consolas, 'SF Mono', Menlo, monospace; }
.fb { transform-box: fill-box; transform-origin: center; }
.fbl { transform-box: fill-box; transform-origin: left center; }
.fbb { transform-box: fill-box; transform-origin: center bottom; }

@keyframes reveal { from { transform: translateY(105%); } to { transform: none; } }
@keyframes rise { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: none; } }
@keyframes fade { from { opacity: 0; } to { opacity: 1; } }
@keyframes blink { 0%, 49% { opacity: 1; } 50%, 100% { opacity: 0; } }
@keyframes pulse { 0%, 100% { opacity: 0.3; } 50% { opacity: 1; } }
@keyframes spin { to { transform: rotate(360deg); } }
@keyframes ripple { 0% { transform: scale(0.7); opacity: 0; } 20% { opacity: 0.8; } 100% { transform: scale(2.2); opacity: 0; } }
@keyframes register { 0% { transform: translateX(0); } 100% { transform: translateX(var(--run)); } }
@keyframes nudge { 0%, 70%, 100% { transform: translate(0, 0); } 80% { transform: translate(4px, -4px); } }
@keyframes bob { 0%, 100% { transform: translateY(-3px); } 50% { transform: translateY(4px); } }
@keyframes scan { 0% { transform: translateY(0); opacity: 0; } 8% { opacity: 1; } 92% { opacity: 1; } 100% { transform: translateY(220px); opacity: 0; } }
@keyframes grow { from { transform: scaleX(0); } to { transform: scaleX(1); } }

.reveal { animation: reveal 1.1s cubic-bezier(.77,0,.18,1) both; }
.rise { animation: rise .9s cubic-bezier(.19,1,.22,1) both; }
.fade { animation: fade 1.2s ease both; }
.blink { animation: blink 1.1s steps(1,end) infinite; }
.pulse { animation: pulse 2.6s ease-in-out infinite; }
.spin { animation: spin 30s linear infinite; }
.ripple { animation: ripple 3.2s cubic-bezier(.2,.6,.3,1) infinite; }
.register { animation: register 9s cubic-bezier(.77,0,.18,1) infinite alternate; }
.nudge { animation: nudge 3.6s ease-in-out infinite; }
.bob { animation: bob 2.2s ease-in-out infinite; }
.scan { animation: scan 5.2s cubic-bezier(.45,0,.55,1) infinite; }
.grow { animation: grow 1.4s cubic-bezier(.77,0,.18,1) both; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
"""

COMMON_DEFS = """
<defs>
 <clipPath id="clip"><rect width="1100" height="590" rx="6"/></clipPath>
 <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
  <path d="M0 .5H2M.5 0V2" stroke="#ecebe5" stroke-opacity=".14"/>
 </pattern>
</defs>
"""

def save_svg(filename, content):
    p1 = os.path.join(OUTPUT_DIR, filename)
    p2 = os.path.join(ROOT_ASSETS_DIR, filename)
    with open(p1, "w", encoding="utf-8") as f:
        f.write(content.strip())
    with open(p2, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated: {filename}")

# ==============================================================================
# 1. HERO BANNER (1100 x 590)
# ==============================================================================
def make_hero():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="590" viewBox="0 0 1100 590" role="img" aria-labelledby="t">
<title id="t">SpherePrime — организация и экосистема агентных инструментов, десктопных воркспейсов, AI и сетевых продуктов.</title>
{COMMON_DEFS}
<style>
{COMMON_STYLE}
@keyframes ticker {{
  0.00%, 14.28% {{ transform: translateY(0px); }}
  16.66%, 30.95% {{ transform: translateY(-40px); }}
  33.33%, 47.61% {{ transform: translateY(-80px); }}
  50.00%, 64.28% {{ transform: translateY(-120px); }}
  66.66%, 80.95% {{ transform: translateY(-160px); }}
  83.33%, 97.61% {{ transform: translateY(-200px); }}
  100% {{ transform: translateY(-240px); }}
}}
.ticker {{ animation: ticker 14s cubic-bezier(.77,0,.18,1) infinite; }}
</style>
<rect width="1100" height="590" rx="6" fill="#121211"/>
<rect width="1100" height="590" fill="url(#grid)" clip-path="url(#clip)"/>
<path d="M12 22V12H22M12 568V578H22M1088 22V12H1078M1088 568V578H1078" fill="none" stroke="#57554f" stroke-width="1.2"/>
<path d="M28 50H1072" stroke="#2d2c29"/>
<g style="--run:988px"><rect class="register" style="animation-delay:0.00s" x="28" y="49" width="56" height="2" fill="#ff5b14"/></g>

<!-- Top bar labels -->
<text x="28.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">SPHEREPRIME / ECOSYSTEM</text>
<text x="1072.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" text-anchor="end" letter-spacing="1.6" class="mono">FOUNDERS: LILKALINOV &amp; DWERTYFA — REV. 11.2026</text>
<rect x=".5" y=".5" width="1099" height="589" rx="6" fill="none" stroke="#2d2c29"/>

<!-- Giant Title -->
<clipPath id="name-clip"><rect x="20" y="60" width="760" height="170"/></clipPath>
<g clip-path="url(#name-clip)">
  <g class="reveal" style="animation-delay:0.10s">
    <text x="24" y="195" font-size="118" font-weight="800" letter-spacing="-4" fill="#ecebe5">SpherePrime<tspan fill="#ff5b14">.</tspan></text>
  </g>
</g>

<!-- Subtitle -->
<g class="rise" style="animation-delay:0.50s">
  <text x="28.0" y="246.0" font-size="18.5" fill="#8d8b85">Агентные инструменты, десктопные воркспейсы, сетевые протоколы и AI-решения.</text>
  <text x="28.0" y="274.0" font-size="15" fill="#57554f" class="mono">Prime CLI · Prime Desktop · PrimeBoost · PrimeProxy · PrimeAi · Astra Plugins</text>
</g>

<!-- Telemetry Plate on Right -->
<g class="fade" style="animation-delay:0.35s">
  <rect x="760" y="74" width="312" height="212" fill="#0e0e0d" stroke="#2d2c29"/>
  <rect x="760" y="74" width="312" height="212" fill="url(#grid)"/>
  <path d="M760 106H1072" stroke="#2d2c29"/>
  <text x="776.0" y="95.0" font-size="10.5" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">SYS.STATUS / NODES</text>
  <circle cx="1046" cy="91" r="4" fill="#ff5b14" class="pulse"/>
  <text x="1034.0" y="95.0" font-size="10" fill="#ff5b14" font-weight="700" text-anchor="end" class="mono">ONLINE</text>

  <!-- Waveform monitor -->
  <path d="M776 150H1056" stroke="#2d2c29" stroke-dasharray="2 3"/>
  <path d="M776 150 L800 150 L812 135 L824 165 L836 142 L848 150 L870 150 L882 120 L894 180 L906 130 L918 160 L930 150 L960 150 L972 138 L984 158 L996 150 L1056 150"
        fill="none" stroke="#ff5b14" stroke-width="1.8" stroke-linejoin="round">
    <animate attributeName="d" dur="3.6s" repeatCount="indefinite"
             values="M776 150 L800 150 L812 135 L824 165 L836 142 L848 150 L870 150 L882 120 L894 180 L906 130 L918 160 L930 150 L960 150 L972 138 L984 158 L996 150 L1056 150;
                     M776 150 L790 150 L802 125 L814 175 L826 138 L838 150 L860 150 L872 140 L884 160 L900 150 L920 120 L932 170 L944 140 L956 150 L980 150 L992 135 L1056 150;
                     M776 150 L800 150 L812 135 L824 165 L836 142 L848 150 L870 150 L882 120 L894 180 L906 130 L918 160 L930 150 L960 150 L972 138 L984 158 L996 150 L1056 150"/>
  </path>

  <!-- Node telemetry metrics -->
  <text x="776.0" y="200.0" font-size="11" fill="#57554f" class="mono">CORE</text>
  <text x="820.0" y="200.0" font-size="11.5" fill="#ecebe5" font-weight="600" class="mono">Prime V2 / Go &amp; Rust</text>

  <text x="776.0" y="224.0" font-size="11" fill="#57554f" class="mono">AUTH</text>
  <text x="820.0" y="224.0" font-size="11.5" fill="#ecebe5" font-weight="600" class="mono">LilKALINOV &amp; dwertyfa</text>

  <text x="776.0" y="248.0" font-size="11" fill="#57554f" class="mono">NET</text>
  <text x="820.0" y="248.0" font-size="11.5" fill="#ff5b14" font-weight="600" class="mono">PrimeBoost (ex-RoxyBoost)</text>

  <text x="776.0" y="272.0" font-size="10" fill="#8d8b85" class="mono">REV: 2026.11 · LATENCY: 0.4ms</text>
</g>

<!-- Divider -->
<rect class="fbl grow" style="animation-delay:0.50s" x="28" y="308" width="1044" height="1" fill="#8d8b85"/>
<path d="M366 330V520" stroke="#2d2c29"/>
<path d="M726 330V520" stroke="#2d2c29"/>

<!-- Column 01: Focus / Mission -->
<text x="28.0" y="344.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">01 / МИССИЯ</text>
<text x="28.0" y="366.0" font-size="15" fill="#8d8b85">Разрабатываем</text>
<clipPath id="ticker-clip"><rect x="26" y="368" width="330" height="42"/></clipPath>
<g clip-path="url(#ticker-clip)">
  <g class="ticker">
    <text x="28.0" y="398.0" font-size="27" fill="#ecebe5" font-weight="700" letter-spacing="-0.5">ИИ-агентов для кода</text>
    <text x="28.0" y="438.0" font-size="27" fill="#ecebe5" font-weight="700" letter-spacing="-0.5">десктоп: Tauri &amp; Electron</text>
    <text x="28.0" y="478.0" font-size="27" fill="#ecebe5" font-weight="700" letter-spacing="-0.5">PrimeBoost VPN сеть</text>
    <text x="28.0" y="518.0" font-size="27" fill="#ecebe5" font-weight="700" letter-spacing="-0.5">MTProto WebSocket прокси</text>
    <text x="28.0" y="558.0" font-size="27" fill="#ecebe5" font-weight="700" letter-spacing="-0.5">AI-роутер для Astra</text>
    <text x="28.0" y="598.0" font-size="27" fill="#ecebe5" font-weight="700" letter-spacing="-0.5">открытые инструменты</text>
    <text x="28.0" y="638.0" font-size="27" fill="#ecebe5" font-weight="700" letter-spacing="-0.5">ИИ-агентов для кода</text>
  </g>
</g>
<text x="28.0" y="438.0" font-size="14.5" fill="#8d8b85">Нативные кроссплатформенные</text>
<text x="28.0" y="460.0" font-size="14.5" fill="#8d8b85">решения и независимый софт</text>
<text x="28.0" y="482.0" font-size="14.5" fill="#8d8b85">с бескомпромиссным качеством.</text>

<!-- Column 02: Stack / Systems -->
<text x="392.0" y="344.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">02 / СТЕК И ТЕХНОЛОГИИ</text>
<g class="rise" style="animation-delay:0.75s">
  <text x="406.0" y="376.0" font-size="10" fill="#57554f" class="mono">01</text><text x="428.0" y="376.0" font-size="13" fill="#ecebe5" class="mono">Rust (Core / Proxy / VPN)</text>
  <text x="406.0" y="401.0" font-size="10" fill="#57554f" class="mono">02</text><text x="428.0" y="401.0" font-size="13" fill="#ecebe5" class="mono">Go (Prime CLI Agent)</text>
  <text x="406.0" y="426.0" font-size="10" fill="#57554f" class="mono">03</text><text x="428.0" y="426.0" font-size="13" fill="#ecebe5" class="mono">Tauri v2 &amp; Electron (Desktop)</text>
  <text x="406.0" y="451.0" font-size="10" fill="#57554f" class="mono">04</text><text x="428.0" y="451.0" font-size="13" fill="#ecebe5" class="mono">TypeScript &amp; React (Web UI)</text>
  <text x="406.0" y="476.0" font-size="10" fill="#57554f" class="mono">05</text><text x="428.0" y="476.0" font-size="13" fill="#ecebe5" class="mono">Python (AI / Automation)</text>
  <text x="406.0" y="501.0" font-size="10" fill="#57554f" class="mono">06</text><text x="428.0" y="501.0" font-size="13" fill="#ecebe5" class="mono">MCP &amp; LSP Protocols</text>
</g>

<!-- Column 03: Authors & Governance -->
<text x="752.0" y="344.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">03 / ОСНОВАТЕЛИ</text>
<text x="1072.0" y="344.0" font-size="11" fill="#ff5b14" font-weight="600" text-anchor="end" letter-spacing="1.6" class="mono">CO-FOUNDERS</text>

<g class="rise" style="animation-delay:0.85s">
  <rect x="752" y="366" width="320" height="66" fill="#0e0e0d" stroke="#2d2c29"/>
  <text x="770.0" y="392.0" font-size="16" fill="#ecebe5" font-weight="700">LilKALINOV</text>
  <text x="1054.0" y="392.0" font-size="11" fill="#ff5b14" text-anchor="end" font-weight="600" class="mono">LEAD QA / CO-FOUNDER</text>
  <text x="770.0" y="414.0" font-size="12" fill="#8d8b85">QA Astra, системный софт, Rust, Tauri, ИИ-агенты</text>

  <rect x="752" y="442" width="320" height="66" fill="#0e0e0d" stroke="#2d2c29"/>
  <text x="770.0" y="468.0" font-size="16" fill="#ecebe5" font-weight="700">dwertyfa</text>
  <text x="1054.0" y="468.0" font-size="11" fill="#ff5b14" text-anchor="end" font-weight="600" class="mono">FULL-STACK / CO-FOUNDER</text>
  <text x="770.0" y="490.0" font-size="12" fill="#8d8b85">Веб, PrimeBoost VPN, Three.js, Telegram, Astra плагины</text>
</g>
</svg>"""
    save_svg("hero-sphereprime.svg", svg)

# ==============================================================================
# 2. QUICK LINK BUTTONS (356 x 92)
# ==============================================================================
def make_links():
    # Link 1: Telegram
    l1 = f"""<svg xmlns="http://www.w3.org/2000/svg" width="356" height="92" viewBox="0 0 356 92" role="img" aria-labelledby="t">
<title id="t">Telegram — t.me/SpherePrime</title>
{COMMON_DEFS}
<style>{COMMON_STYLE}</style>
<rect width="356" height="92" rx="6" fill="#121211"/>
<path d="M12 22V12H22M12 70V80H22M344 22V12H334M344 70V80H334" fill="none" stroke="#57554f" stroke-width="1.2"/>
<rect x=".5" y=".5" width="355" height="91" rx="6" fill="none" stroke="#2d2c29"/>
<text x="24.0" y="30.0" font-size="11" fill="#ff5b14" font-weight="600" letter-spacing="1.6" class="mono">01</text>
<text x="24.0" y="58.0" font-size="22" fill="#ecebe5" font-weight="700">Telegram</text>
<rect class="fbl grow" style="animation-delay:0.40s" x="24" y="66" width="93" height="2" fill="#ff5b14"/>
<text x="24.0" y="82.0" font-size="11.5" fill="#8d8b85" class="mono">t.me/SpherePrime</text>
<g transform="translate(320 46.0)">
  <g class="nudge"><path d="M-9 9L9 -9M-3.6 -9H9V3.6" fill="none" stroke="#ecebe5" stroke-width="1.8" stroke-linecap="square"/></g>
</g>
</svg>"""
    save_svg("link-telegram.svg", l1)

    # Link 2: Prime CLI
    l2 = f"""<svg xmlns="http://www.w3.org/2000/svg" width="356" height="92" viewBox="0 0 356 92" role="img" aria-labelledby="t">
<title id="t">Prime CLI — github.com/SpherePrime/CLI</title>
{COMMON_DEFS}
<style>{COMMON_STYLE}</style>
<rect width="356" height="92" rx="6" fill="#121211"/>
<path d="M12 22V12H22M12 70V80H22M344 22V12H334M344 70V80H334" fill="none" stroke="#57554f" stroke-width="1.2"/>
<rect x=".5" y=".5" width="355" height="91" rx="6" fill="none" stroke="#2d2c29"/>
<text x="24.0" y="30.0" font-size="11" fill="#ff5b14" font-weight="600" letter-spacing="1.6" class="mono">02</text>
<text x="24.0" y="58.0" font-size="22" fill="#ecebe5" font-weight="700">Prime CLI</text>
<rect class="fbl grow" style="animation-delay:0.40s" x="24" y="66" width="93" height="2" fill="#ff5b14"/>
<text x="24.0" y="82.0" font-size="11.5" fill="#8d8b85" class="mono">github.com/SpherePrime/CLI</text>
<g transform="translate(320 46.0)">
  <g class="nudge"><path d="M-9 9L9 -9M-3.6 -9H9V3.6" fill="none" stroke="#ecebe5" stroke-width="1.8" stroke-linecap="square"/></g>
</g>
</svg>"""
    save_svg("link-cli.svg", l2)

    # Link 3: PrimeBoost (ex-RoxyBoost)
    l3 = f"""<svg xmlns="http://www.w3.org/2000/svg" width="356" height="92" viewBox="0 0 356 92" role="img" aria-labelledby="t">
<title id="t">PrimeBoost VPN — Бывший RoxyBoost</title>
{COMMON_DEFS}
<style>{COMMON_STYLE}</style>
<rect width="356" height="92" rx="6" fill="#121211"/>
<path d="M12 22V12H22M12 70V80H22M344 22V12H334M344 70V80H334" fill="none" stroke="#57554f" stroke-width="1.2"/>
<rect x=".5" y=".5" width="355" height="91" rx="6" fill="none" stroke="#2d2c29"/>
<text x="24.0" y="30.0" font-size="11" fill="#ff5b14" font-weight="600" letter-spacing="1.6" class="mono">03</text>
<text x="24.0" y="58.0" font-size="22" fill="#ecebe5" font-weight="700">PrimeBoost</text>
<rect class="fbl grow" style="animation-delay:0.40s" x="24" y="66" width="112" height="2" fill="#ff5b14"/>
<text x="24.0" y="82.0" font-size="11.5" fill="#8d8b85" class="mono">VPN · ex-RoxyBoost</text>
<g transform="translate(320 46.0)">
  <g class="nudge"><path d="M-9 9L9 -9M-3.6 -9H9V3.6" fill="none" stroke="#ecebe5" stroke-width="1.8" stroke-linecap="square"/></g>
</g>
</svg>"""
    save_svg("link-primeboost.svg", l3)

# ==============================================================================
# 3. STATS BANNER (1100 x 326)
# ==============================================================================
def make_stats():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="326" viewBox="0 0 1100 326" role="img" aria-labelledby="t">
<title id="t">SpherePrime в цифрах: 40+ репозиториев экосистемы, 8+ языков и систем, 3 десктоп-платформы, 6+ ключевых сервисов.</title>
{COMMON_DEFS}
<style>
{COMMON_STYLE}
@keyframes once {{ from {{ transform: scaleY(0); }} to {{ transform: scaleY(1); }} }}
.eq-once {{ animation: once .5s cubic-bezier(.19,1,.22,1) both; }}
</style>
<rect width="1100" height="326" rx="6" fill="#121211"/>
<rect width="1100" height="326" fill="url(#grid)" clip-path="url(#clip)"/>
<path d="M12 22V12H22M12 304V314H22M1088 22V12H1078M1088 304V314H1078" fill="none" stroke="#57554f" stroke-width="1.2"/>
<path d="M28 50H1072" stroke="#2d2c29"/>
<g style="--run:988px"><rect class="register" style="animation-delay:-3.00s" x="28" y="49" width="56" height="2" fill="#ff5b14"/></g>
<text x="28.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">INDEX / ЭКОСИСТЕМА В ЦИФРАХ</text>
<text x="1072.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" text-anchor="end" letter-spacing="1.6" class="mono">GITHUB · SPHEREPRIME · 2026</text>
<rect x=".5" y=".5" width="1099" height="325" rx="6" fill="none" stroke="#2d2c29"/>

<!-- Stat 1: Repos -->
<g class="rise" style="animation-delay:0.20s">
  <text x="30.0" y="152.0" font-size="74" fill="#ecebe5" font-weight="800">40<tspan fill="#ff5b14">+</tspan></text>
  <text x="30.0" y="184.0" font-size="12" fill="#ecebe5" font-weight="600" letter-spacing="1.6" class="mono">РЕПОЗИТОРИЕВ</text>
  <text x="30.0" y="204.0" font-size="12" fill="#57554f" class="mono">SpherePrime + Founders</text>
</g>
<path d="M260.0 82V212" stroke="#2d2c29"/>

<!-- Stat 2: Languages -->
<g class="rise" style="animation-delay:0.35s">
  <text x="286.0" y="152.0" font-size="74" fill="#ecebe5" font-weight="800">08<tspan fill="#ff5b14">+</tspan></text>
  <text x="286.0" y="184.0" font-size="12" fill="#ecebe5" font-weight="600" letter-spacing="1.6" class="mono">ЯЗЫКОВ И СИСТЕМ</text>
  <text x="286.0" y="204.0" font-size="12" fill="#57554f" class="mono">Rust · Go · TS · Python · C++</text>
</g>
<path d="M530.0 82V212" stroke="#2d2c29"/>

<!-- Stat 3: Platforms -->
<g class="rise" style="animation-delay:0.50s">
  <text x="556.0" y="152.0" font-size="74" fill="#ecebe5" font-weight="800">03</text>
  <text x="556.0" y="184.0" font-size="12" fill="#ecebe5" font-weight="600" letter-spacing="1.6" class="mono">ДЕСКТОП-СРЕДЫ</text>
  <text x="556.0" y="204.0" font-size="12" fill="#57554f" class="mono">Tauri v2 · Electron · CLI</text>
</g>
<path d="M800.0 82V212" stroke="#2d2c29"/>

<!-- Stat 4: Services -->
<g class="rise" style="animation-delay:0.65s">
  <text x="826.0" y="152.0" font-size="74" fill="#ecebe5" font-weight="800">06<tspan fill="#ff5b14">+</tspan></text>
  <text x="826.0" y="184.0" font-size="12" fill="#ecebe5" font-weight="600" letter-spacing="1.6" class="mono">ПРОДУКТОВ И СЕТЕЙ</text>
  <text x="826.0" y="204.0" font-size="12" fill="#57554f" class="mono">CLI · Boost · Proxy · Router</text>
</g>

<!-- Bottom Language Distribution Bar -->
<path d="M28 218H1072" stroke="#2d2c29"/>
<text x="28.0" y="238.0" font-size="10" fill="#57554f" font-weight="600" letter-spacing="1.6" class="mono">РАСПРЕДЕЛЕНИЕ ТЕХНОЛОГИЧЕСКОГО СТЕКА В ЭКОСИСТЕМЕ</text>

<!-- Equalizer Bars for Languages -->
<g transform="translate(0, 10)">
  <!-- Rust (orange) -->
  <rect class="fbb eq-once" style="animation-delay:0.60s" x="28" y="240" width="360" height="18" fill="#ff5b14"/>
  <!-- Go (off-white) -->
  <rect class="fbb eq-once" style="animation-delay:0.75s" x="394" y="240" width="260" height="18" fill="#ecebe5"/>
  <!-- TypeScript (bright gray) -->
  <rect class="fbb eq-once" style="animation-delay:0.90s" x="660" y="240" width="180" height="18" fill="#b9b7b0"/>
  <!-- Python (warm orange) -->
  <rect class="fbb eq-once" style="animation-delay:1.05s" x="846" y="240" width="110" height="18" fill="#ff8040"/>
  <!-- C/C++/Asm/Other (darker) -->
  <rect class="fbb eq-once" style="animation-delay:1.20s" x="962" y="240" width="110" height="18" fill="#595854"/>
</g>

<!-- Legend -->
<rect x="28" y="293" width="9" height="9" fill="#ff5b14"/>
<text x="44.0" y="302.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1" class="mono">RUST (CORE / NETWORK / TAURI)</text>

<rect x="290" y="293" width="9" height="9" fill="#ecebe5"/>
<text x="306.0" y="302.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1" class="mono">GO (PRIME CLI AGENT)</text>

<rect x="520" y="293" width="9" height="9" fill="#b9b7b0"/>
<text x="536.0" y="302.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1" class="mono">TYPESCRIPT (REACT / ELECTRON)</text>

<rect x="800" y="293" width="9" height="9" fill="#ff8040"/>
<text x="816.0" y="302.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1" class="mono">PYTHON</text>

<rect x="910" y="293" width="9" height="9" fill="#595854"/>
<text x="926.0" y="302.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1" class="mono">C/C++ &amp; ASM</text>
</svg>"""
    save_svg("stats.svg", svg)

# ==============================================================================
# 4. SECTION 01 HEADER (Prime Ecosystem)
# ==============================================================================
def make_section_prime():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="150" viewBox="0 0 1100 150" role="img" aria-labelledby="t">
<title id="t">01 — Prime Ecosystem. Агентные инструменты для разработчиков: терминал, десктоп, роутинг, прокси.</title>
{COMMON_DEFS}
<style>{COMMON_STYLE}</style>
<rect width="1100" height="150" rx="6" fill="#121211"/>
<path d="M12 22V12H22M12 128V138H22M1088 22V12H1078M1088 128V138H1078" fill="none" stroke="#57554f" stroke-width="1.2"/>
<path d="M28 50H1072" stroke="#2d2c29"/>
<g style="--run:988px"><rect class="register" style="animation-delay:-5.20s" x="28" y="49" width="56" height="2" fill="#ff5b14"/></g>
<text x="28.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">РАЗДЕЛ 01</text>
<text x="1072.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" text-anchor="end" letter-spacing="1.6" class="mono">PRIME ECOSYSTEM · 04 ПРОЕКТА</text>
<rect x=".5" y=".5" width="1099" height="149" rx="6" fill="none" stroke="#2d2c29"/>

<clipPath id="num"><rect x="20" y="58" width="150" height="86"/></clipPath>
<g clip-path="url(#num)"><g class="reveal"><text x="24.0" y="130.0" font-size="92" fill="#ff5b14" font-weight="800" letter-spacing="-4">01</text></g></g>

<clipPath id="ttl"><rect x="170" y="62" width="900" height="56"/></clipPath>
<g clip-path="url(#ttl)"><g class="reveal" style="animation-delay:0.15s"><text x="176.0" y="106.0" font-size="46" fill="#ecebe5" font-weight="800" letter-spacing="-1.5">Prime Ecosystem</text></g></g>
<g class="rise" style="animation-delay:0.50s"><text x="178.0" y="132.0" font-size="15" fill="#8d8b85">Агентные инструменты нового поколения: терминальный ИИ, десктопный воркспейс, роутинг и прокси.</text></g>
<path d="M168 70V130" stroke="#2d2c29"/>
<g transform="translate(1056 104)"><g class="bob"><path d="M0 -14V12M-8 4L0 12L8 4" fill="none" stroke="#ecebe5" stroke-width="1.8"/></g></g>
<text x="1036.0" y="109.0" font-size="11" fill="#8d8b85" font-weight="600" text-anchor="end" letter-spacing="1.6" class="mono">ПРОЕКТЫ</text>
</svg>"""
    save_svg("section-prime.svg", svg)

# ==============================================================================
# 5. CARD: PRIME CLI (1100 x 430)
# ==============================================================================
def make_card_cli():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="430" viewBox="0 0 1100 430" role="img" aria-labelledby="t">
<title id="t">Prime CLI — агентный AI-ассистент для кода в терминале: любые модели, MCP, LSP. Go. Открыть репозиторий SpherePrime.</title>
{COMMON_DEFS}
<style>
{COMMON_STYLE}
@keyframes cl0 {{ 0%, 12% {{ opacity: 0; transform: translateY(3px); }} 15%, 92% {{ opacity: 1; transform: none; }} 95%, 100% {{ opacity: 0; }} }}
@keyframes cl1 {{ 0%, 24% {{ opacity: 0; transform: translateY(3px); }} 27%, 92% {{ opacity: 1; transform: none; }} 95%, 100% {{ opacity: 0; }} }}
@keyframes cl2 {{ 0%, 36% {{ opacity: 0; transform: translateY(3px); }} 39%, 92% {{ opacity: 1; transform: none; }} 95%, 100% {{ opacity: 0; }} }}
@keyframes cl3 {{ 0%, 48% {{ opacity: 0; transform: translateY(3px); }} 51%, 92% {{ opacity: 1; transform: none; }} 95%, 100% {{ opacity: 0; }} }}
@keyframes cldone {{ 0%, 60% {{ opacity: 0; transform: translateY(3px); }} 63%, 92% {{ opacity: 1; transform: none; }} 95%, 100% {{ opacity: 0; }} }}
.cl0 {{ animation: cl0 12s cubic-bezier(.2,.8,.2,1) infinite; }}
.cl1 {{ animation: cl1 12s cubic-bezier(.2,.8,.2,1) infinite; }}
.cl2 {{ animation: cl2 12s cubic-bezier(.2,.8,.2,1) infinite; }}
.cl3 {{ animation: cl3 12s cubic-bezier(.2,.8,.2,1) infinite; }}
.cldone {{ animation: cldone 12s cubic-bezier(.2,.8,.2,1) infinite; }}

@keyframes mtick {{
  0.00%, 26.00% {{ transform: translateY(0px); }}
  33.33%, 59.33% {{ transform: translateY(-22px); }}
  66.67%, 92.67% {{ transform: translateY(-44px); }}
  100% {{ transform: translateY(-66px); }}
}}
.mtick {{ animation: mtick 7.5s cubic-bezier(.77,0,.18,1) infinite; }}
</style>
<rect width="1100" height="430" rx="6" fill="#121211"/>
<path d="M12 22V12H22M12 408V418H22M1088 22V12H1078M1088 408V418H1078" fill="none" stroke="#57554f" stroke-width="1.2"/>
<path d="M28 50H1072" stroke="#2d2c29"/>
<g style="--run:988px"><rect class="register" style="animation-delay:-6.50s" x="28" y="49" width="56" height="2" fill="#ff5b14"/></g>
<text x="28.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">01 — ФЛАГМАН · GO</text>
<text x="1072.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" text-anchor="end" letter-spacing="1.6" class="mono">GITHUB.COM/SPHEREPRIME/CLI</text>
<rect x=".5" y=".5" width="1099" height="429" rx="6" fill="none" stroke="#2d2c29"/>

<!-- Terminal preview plate -->
<rect x="556" y="66" width="516" height="320" fill="#0e0e0d"/>
<clipPath id="plate"><rect x="556" y="66" width="516" height="320"/></clipPath>
<g clip-path="url(#plate)">
  <rect x="556" y="66" width="516" height="320" fill="url(#grid)"/>
  <path d="M556 106H1072" stroke="#2d2c29"/>
  <text x="576.0" y="91.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">PRIME CLI — ~/SPHEREPRIME</text>
  <clipPath id="mclip"><rect x="912" y="77" width="150" height="19"/></clipPath>
  <g clip-path="url(#mclip)">
    <g class="mtick">
      <text x="1052.0" y="91.0" font-size="12" fill="#ff5b14" font-weight="600" text-anchor="end" class="mono">claude-3-7-sonnet</text>
      <text x="1052.0" y="113.0" font-size="12" fill="#ff5b14" font-weight="600" text-anchor="end" class="mono">gpt-4o / o3</text>
      <text x="1052.0" y="135.0" font-size="12" fill="#ff5b14" font-weight="600" text-anchor="end" class="mono">local / qwen2.5</text>
      <text x="1052.0" y="157.0" font-size="12" fill="#ff5b14" font-weight="600" text-anchor="end" class="mono">claude-3-7-sonnet</text>
    </g>
  </g>
  <text x="580.0" y="140.0" font-size="16" fill="#ff5b14" font-weight="700" class="mono">›</text>
  <clipPath id="cli-type">
    <rect x="600" y="124" width="0" height="24">
      <animate attributeName="width" dur="12s" repeatCount="indefinite" calcMode="discrete"
               values="0;12;24;36;48;60;72;84;96;108;120;132;144;156;168;180;192;204;216;228;240;240;0"
               keyTimes="0.00;0.005;0.01;0.015;0.02;0.025;0.03;0.035;0.04;0.045;0.05;0.055;0.06;0.065;0.07;0.075;0.08;0.085;0.09;0.095;0.10;0.94;1"/>
    </rect>
  </clipPath>
  <g clip-path="url(#cli-type)">
    <text x="600.0" y="140.0" font-size="14" fill="#ecebe5" class="mono">проведи рефакторинг API роутера</text>
  </g>

  <!-- Execution steps -->
  <g class="cl0"><text x="580.0" y="178.0" font-size="11" fill="#57554f" font-weight="700" letter-spacing="1.5" class="mono">EXPLORE</text><text x="656.0" y="178.0" font-size="13" fill="#8d8b85" class="mono">core/router.go &amp; handlers/</text></g>
  <g class="cl1"><text x="580.0" y="206.0" font-size="11" fill="#57554f" font-weight="700" letter-spacing="1.5" class="mono">LSP</text><text x="656.0" y="206.0" font-size="13" fill="#8d8b85" class="mono">8 references · gopls check OK</text></g>
  <g class="cl2"><text x="580.0" y="234.0" font-size="11" fill="#57554f" font-weight="700" letter-spacing="1.5" class="mono">MCP</text><text x="656.0" y="234.0" font-size="13" fill="#8d8b85" class="mono">prime_terminal.exec: go test ./...</text></g>
  <g class="cl3"><text x="580.0" y="262.0" font-size="11" fill="#57554f" font-weight="700" letter-spacing="1.5" class="mono">VERIFY</text><text x="656.0" y="262.0" font-size="13" fill="#8d8b85" class="mono">14/14 tests PASS · 0 warnings</text></g>
  <g class="cldone"><rect x="580" y="282" width="8" height="8" fill="#ff5b14"/><text x="596.0" y="291.0" font-size="13.5" fill="#ecebe5" font-weight="700" class="mono">задача выполнена · PR готов</text></g>

  <path d="M556 342H1072" stroke="#2d2c29"/>
  <text x="580.0" y="369.0" font-size="15" fill="#8d8b85" font-weight="700" class="mono">›</text><rect class="blink" x="598" y="357" width="8" height="15" fill="#ecebe5"/>
  <text x="1052.0" y="368.0" font-size="10" fill="#57554f" font-weight="600" text-anchor="end" letter-spacing="1.6" class="mono">CTRL+P MCP &amp; LSP</text>
</g>
<rect x="556" y="66" width="516" height="320" fill="none" stroke="#2d2c29"/>
<text x="1072.0" y="404.0" font-size="10" fill="#8d8b85" font-weight="600" text-anchor="end" letter-spacing="1.6" class="mono">FIG. 01 — TERMINAL AGENT</text>

<!-- Left description -->
<clipPath id="ttl"><rect x="22" y="112" width="520" height="78"/></clipPath>
<g clip-path="url(#ttl)"><g class="reveal" style="animation-delay:0.15s"><text x="26.0" y="172.0" font-size="60" fill="#ecebe5" font-weight="800" letter-spacing="-1.8">Prime CLI</text></g></g>
<g class="rise" style="animation-delay:0.40s"><text x="28.0" y="214.0" font-size="17" fill="#8d8b85">Агентный AI-ассистент для разработки в терминале.</text></g>
<g class="rise" style="animation-delay:0.50s"><text x="28.0" y="240.0" font-size="17" fill="#8d8b85">Любые LLM-провайдеры, MCP инструменты, LSP контекст,</text></g>
<g class="rise" style="animation-delay:0.60s"><text x="28.0" y="266.0" font-size="17" fill="#8d8b85">полная автономность, сессии и голосовое управление.</text></g>
<path d="M28 300H500" stroke="#2d2c29"/>
<g class="fade" style="animation-delay:0.60s">
  <text x="28.0" y="328.0" font-size="13" fill="#8d8b85" class="mono">Go</text><text x="53.6" y="328.0" font-size="13" fill="#ff5b14" class="mono">/</text>
  <text x="71.4" y="328.0" font-size="13" fill="#8d8b85" class="mono">MCP</text><text x="105.0" y="328.0" font-size="13" fill="#ff5b14" class="mono">/</text>
  <text x="122.8" y="328.0" font-size="13" fill="#8d8b85" class="mono">LSP</text><text x="156.0" y="328.0" font-size="13" fill="#ff5b14" class="mono">/</text>
  <text x="173.8" y="328.0" font-size="13" fill="#8d8b85" class="mono">Multi-Agent</text>
</g>
<g class="rise" style="animation-delay:0.90s">
  <rect x="28" y="348" width="200" height="44" fill="none" stroke="#ecebe5"/>
  <text x="46.0" y="375.0" font-size="12" fill="#ecebe5" font-weight="600" letter-spacing="1.6" class="mono">РЕПОЗИТОРИЙ</text>
  <g transform="translate(208 370)"><path d="M-6 6L6 -6M-2.4 -6H6V2.4" fill="none" stroke="#ff5b14" stroke-width="1.8" stroke-linecap="square"/></g>
</g>
</svg>"""
    save_svg("card-cli.svg", svg)

# ==============================================================================
# 6. CARD: PRIME DESKTOP (1100 x 430)
# ==============================================================================
def make_card_desktop():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="430" viewBox="0 0 1100 430" role="img" aria-labelledby="t">
<title id="t">Prime Desktop — десктоп-воркспейс Prime для Windows и Linux на Tauri v2, Electron и React.</title>
{COMMON_DEFS}
<style>{COMMON_STYLE}</style>
<rect width="1100" height="430" rx="6" fill="#121211"/>
<path d="M12 22V12H22M12 408V418H22M1088 22V12H1078M1088 408V418H1078" fill="none" stroke="#57554f" stroke-width="1.2"/>
<path d="M28 50H1072" stroke="#2d2c29"/>
<g style="--run:988px"><rect class="register" style="animation-delay:-4.20s" x="28" y="49" width="56" height="2" fill="#ff5b14"/></g>
<text x="28.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">02 — ДЕСКТОП-ВОРКСПЕЙС · TAURI V2 &amp; ELECTRON</text>
<text x="1072.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" text-anchor="end" letter-spacing="1.6" class="mono">WINDOWS / LINUX WORKSPACE</text>
<rect x=".5" y=".5" width="1099" height="429" rx="6" fill="none" stroke="#2d2c29"/>

<!-- Desktop Mockup Plate -->
<rect x="556" y="66" width="516" height="320" fill="#0e0e0d"/>
<clipPath id="dplate"><rect x="556" y="66" width="516" height="320"/></clipPath>
<g clip-path="url(#dplate)">
  <rect x="556" y="66" width="516" height="320" fill="url(#grid)"/>
  <!-- Window title bar -->
  <rect x="556" y="66" width="516" height="32" fill="#181816"/>
  <circle cx="574" cy="82" r="5" fill="#ff5b14"/>
  <circle cx="590" cy="82" r="5" fill="#57554f"/>
  <circle cx="606" cy="82" r="5" fill="#57554f"/>
  <text x="814" y="86" font-size="11" fill="#8d8b85" text-anchor="middle" font-weight="600" class="mono">Prime Desktop — Chat &amp; Workspace</text>
  <path d="M556 98H1072" stroke="#2d2c29"/>

  <!-- Left Sidebar (Chats & Projects) -->
  <rect x="556" y="98" width="130" height="288" fill="#121211" stroke="#2d2c29"/>
  <text x="568" y="120" font-size="10" fill="#ff5b14" font-weight="700" class="mono">CHATS</text>
  <rect x="562" y="130" width="118" height="24" fill="#2d2c29" rx="3"/>
  <text x="570" y="146" font-size="10.5" fill="#ecebe5" class="mono"># SpherePrime</text>
  <text x="570" y="174" font-size="10.5" fill="#8d8b85" class="mono"># PrimeBoost</text>
  <text x="570" y="200" font-size="10.5" fill="#8d8b85" class="mono"># Core QA</text>

  <text x="568" y="240" font-size="10" fill="#57554f" font-weight="700" class="mono">TOOLS</text>
  <text x="570" y="262" font-size="10" fill="#8d8b85" class="mono">› Terminals</text>
  <text x="570" y="284" font-size="10" fill="#8d8b85" class="mono">› Browser</text>
  <text x="570" y="306" font-size="10" fill="#8d8b85" class="mono">› Diffs / Git</text>
  <text x="570" y="328" font-size="10" fill="#8d8b85" class="mono">› SSH Remote</text>

  <!-- Center Active Chat / Editor -->
  <rect x="686" y="98" width="386" height="288" fill="#0e0e0d"/>
  <!-- Message 1 -->
  <rect x="702" y="114" width="354" height="60" fill="#181816" rx="4" stroke="#2d2c29"/>
  <text x="716" y="134" font-size="11" fill="#ff5b14" font-weight="700" class="mono">User</text>
  <text x="716" y="154" font-size="12" fill="#ecebe5">Запусти проверку нативных окон и браузерного UI</text>

  <!-- Message 2 (Agent response) -->
  <rect x="702" y="186" width="354" height="130" fill="#121211" rx="4" stroke="#ff5b14" stroke-opacity=".5"/>
  <text x="716" y="208" font-size="11" fill="#ff5b14" font-weight="700" class="mono">Prime Desktop Agent</text>
  <text x="716" y="228" font-size="11.5" fill="#ecebe5">✓ Dev server запущен на localhost:5173</text>
  <text x="716" y="248" font-size="11.5" fill="#8d8b85">✓ browser_run: десктоп 1280px + мобильный 390px</text>
  <text x="716" y="268" font-size="11.5" fill="#8d8b85">✓ Скриншоты сохранены, контраст и фокус проверены</text>
  <text x="716" y="294" font-size="11.5" fill="#ff5b14" font-weight="700">COMPLETION CHECK: ALL VERIFIED</text>
</g>
<rect x="556" y="66" width="516" height="320" fill="none" stroke="#2d2c29"/>
<text x="1072.0" y="404.0" font-size="10" fill="#8d8b85" font-weight="600" text-anchor="end" letter-spacing="1.6" class="mono">FIG. 02 — DESKTOP WORKSPACE</text>

<!-- Left description -->
<clipPath id="dttl"><rect x="22" y="112" width="520" height="78"/></clipPath>
<g clip-path="url(#dttl)"><g class="reveal" style="animation-delay:0.15s"><text x="26.0" y="172.0" font-size="54" fill="#ecebe5" font-weight="800" letter-spacing="-1.8">Prime Desktop</text></g></g>
<g class="rise" style="animation-delay:0.40s"><text x="28.0" y="214.0" font-size="17" fill="#8d8b85">Нативный десктоп-воркспейс для Windows и Linux.</text></g>
<g class="rise" style="animation-delay:0.50s"><text x="28.0" y="240.0" font-size="17" fill="#8d8b85">Tauri v2 для Windows, Electron для Linux, встроенный</text></g>
<g class="rise" style="animation-delay:0.60s"><text x="28.0" y="266.0" font-size="17" fill="#8d8b85">браузер, терминалы, diff-инспектор, SSH и агентный чат.</text></g>
<path d="M28 300H500" stroke="#2d2c29"/>
<g class="fade" style="animation-delay:0.60s">
  <text x="28.0" y="328.0" font-size="13" fill="#8d8b85" class="mono">Rust</text><text x="68" y="328.0" font-size="13" fill="#ff5b14" class="mono">/</text>
  <text x="84" y="328.0" font-size="13" fill="#8d8b85" class="mono">Tauri v2</text><text x="156" y="328.0" font-size="13" fill="#ff5b14" class="mono">/</text>
  <text x="172" y="328.0" font-size="13" fill="#8d8b85" class="mono">Electron</text><text x="246" y="328.0" font-size="13" fill="#ff5b14" class="mono">/</text>
  <text x="262" y="328.0" font-size="13" fill="#8d8b85" class="mono">React</text>
</g>
<g class="rise" style="animation-delay:0.90s">
  <rect x="28" y="348" width="200" height="44" fill="none" stroke="#ecebe5"/>
  <text x="46.0" y="375.0" font-size="12" fill="#ecebe5" font-weight="600" letter-spacing="1.6" class="mono">ИСХОДНИКИ</text>
  <g transform="translate(208 370)"><path d="M-6 6L6 -6M-2.4 -6H6V2.4" fill="none" stroke="#ff5b14" stroke-width="1.8" stroke-linecap="square"/></g>
</g>
</svg>"""
    save_svg("card-desktop.svg", svg)

# ==============================================================================
# 7. CARDS: PRIMEAI (540 x 380) & PRIMEPROXY (540 x 380)
# ==============================================================================
def make_primeai_and_proxy():
    # PrimeAi
    ai = f"""<svg xmlns="http://www.w3.org/2000/svg" width="540" height="380" viewBox="0 0 540 380" role="img" aria-labelledby="t">
<title id="t">PrimeAi — AI-провайдер для Astra с интеллектуальной маршрутизацией через Router API. TypeScript.</title>
{COMMON_DEFS}
<style>{COMMON_STYLE}</style>
<rect width="540" height="380" rx="6" fill="#121211"/>
<path d="M12 22V12H22M12 358V368H22M528 22V12H518M528 358V368H518" fill="none" stroke="#57554f" stroke-width="1.2"/>
<path d="M28 50H512" stroke="#2d2c29"/>
<g style="--run:428px"><rect class="register" style="animation-delay:-2.10s" x="28" y="49" width="56" height="2" fill="#ff5b14"/></g>
<text x="28.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">03 — AI ROUTING · TYPESCRIPT</text>
<text x="488.0" y="36.0" font-size="11" fill="#ff5b14" font-weight="600" text-anchor="end" letter-spacing="1.2" class="mono">AI ROUTER</text>
<rect x=".5" y=".5" width="539" height="379" rx="6" fill="none" stroke="#2d2c29"/>

<g transform="translate(502 32)"><path d="M-7 7L7 -7M-2.8 -7H7V2.8" fill="none" stroke="#ff5b14" stroke-width="1.6" stroke-linecap="square"/></g>

<!-- Content -->
<clipPath id="ait"><rect x="24" y="68" width="480" height="52"/></clipPath>
<g clip-path="url(#ait)"><g class="reveal"><text x="28" y="108" font-size="44" fill="#ecebe5" font-weight="800" letter-spacing="-1.2">PrimeAi</text></g></g>

<g class="rise" style="animation-delay:0.30s">
  <text x="28.0" y="142.0" font-size="15.5" fill="#8d8b85">Интеллектуальный AI-провайдер для голосового</text>
  <text x="28.0" y="166.0" font-size="15.5" fill="#8d8b85">ассистента Astra и агентных сред с авто-маршрутизацией.</text>
</g>

<!-- Graphic box -->
<rect x="28" y="186" width="484" height="124" fill="#0e0e0d" stroke="#2d2c29"/>
<rect x="28" y="186" width="484" height="124" fill="url(#grid)"/>
<text x="44.0" y="212.0" font-size="11" fill="#ff5b14" font-weight="700" class="mono">ROUTER API ENGINE</text>
<text x="44.0" y="238.0" font-size="12.5" fill="#ecebe5" class="mono">Claude 3.7 · GPT-4o · Gemini 2.0 · DeepSeek</text>
<text x="44.0" y="262.0" font-size="12" fill="#8d8b85" class="mono">Автоматический выбор наилучшей модели по задаче</text>
<text x="44.0" y="286.0" font-size="11" fill="#57554f" class="mono">Failover · Token Caching · Stream Responses</text>

<g class="rise" style="animation-delay:0.70s">
  <text x="28.0" y="344.0" font-size="12" fill="#57554f" class="mono">REPO: SpherePrime/PrimeAi · MIT License</text>
</g>
</svg>"""
    save_svg("card-primeai.svg", ai)

    # PrimeProxy
    proxy = f"""<svg xmlns="http://www.w3.org/2000/svg" width="540" height="380" viewBox="0 0 540 380" role="img" aria-labelledby="t">
<title id="t">PrimeProxy — локальный MTProto-прокси для Telegram с WebSocket-транспортом. Rust.</title>
{COMMON_DEFS}
<style>{COMMON_STYLE}</style>
<rect width="540" height="380" rx="6" fill="#121211"/>
<path d="M12 22V12H22M12 358V368H22M528 22V12H518M528 358V368H518" fill="none" stroke="#57554f" stroke-width="1.2"/>
<path d="M28 50H512" stroke="#2d2c29"/>
<g style="--run:428px"><rect class="register" style="animation-delay:-5.60s" x="28" y="49" width="56" height="2" fill="#ff5b14"/></g>
<text x="28.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">04 — PROXY · RUST</text>
<text x="488.0" y="36.0" font-size="11" fill="#ff5b14" font-weight="600" text-anchor="end" letter-spacing="1.2" class="mono">MTPROTO</text>
<rect x=".5" y=".5" width="539" height="379" rx="6" fill="none" stroke="#2d2c29"/>

<g transform="translate(502 32)"><path d="M-7 7L7 -7M-2.8 -7H7V2.8" fill="none" stroke="#ff5b14" stroke-width="1.6" stroke-linecap="square"/></g>

<!-- Content -->
<clipPath id="prt"><rect x="24" y="68" width="480" height="52"/></clipPath>
<g clip-path="url(#prt)"><g class="reveal"><text x="28" y="108" font-size="44" fill="#ecebe5" font-weight="800" letter-spacing="-1.2">PrimeProxy</text></g></g>

<g class="rise" style="animation-delay:0.30s">
  <text x="28.0" y="142.0" font-size="15.5" fill="#8d8b85">Локальный высокопроизводительный MTProto-прокси</text>
  <text x="28.0" y="166.0" font-size="15.5" fill="#8d8b85">для Telegram с быстрым WebSocket-транспортом на Rust.</text>
</g>

<!-- Graphic box -->
<rect x="28" y="186" width="484" height="124" fill="#0e0e0d" stroke="#2d2c29"/>
<rect x="28" y="186" width="484" height="124" fill="url(#grid)"/>
<text x="44.0" y="212.0" font-size="11" fill="#ff5b14" font-weight="700" class="mono">MTPROTO + WEBSOCKET TUNNEL</text>
<text x="44.0" y="238.0" font-size="12.5" fill="#ecebe5" class="mono">Zero-copy I/O · Tokio Async Runtime · Low-latency</text>
<text x="44.0" y="262.0" font-size="12" fill="#8d8b85" class="mono">Прямой обход блокировок и стабильное соединение в TG</text>
<text x="44.0" y="286.0" font-size="11" fill="#57554f" class="mono">Автоконфигурация · Встроенный DNS криптографический слой</text>

<g class="rise" style="animation-delay:0.70s">
  <text x="28.0" y="344.0" font-size="12" fill="#57554f" class="mono">REPO: SpherePrime/PrimeProxy · Rust Core</text>
</g>
</svg>"""
    save_svg("card-primeproxy.svg", proxy)

# ==============================================================================
# 8. SECTION 02 HEADER (PrimeBoost & Network)
# ==============================================================================
def make_section_boost():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="150" viewBox="0 0 1100 150" role="img" aria-labelledby="t">
<title id="t">02 — PrimeBoost &amp; Network. Сетевые продукты, защита приватности и системные расширения.</title>
{COMMON_DEFS}
<style>{COMMON_STYLE}</style>
<rect width="1100" height="150" rx="6" fill="#121211"/>
<path d="M12 22V12H22M12 128V138H22M1088 22V12H1078M1088 128V138H1078" fill="none" stroke="#57554f" stroke-width="1.2"/>
<path d="M28 50H1072" stroke="#2d2c29"/>
<g style="--run:988px"><rect class="register" style="animation-delay:-8.20s" x="28" y="49" width="56" height="2" fill="#ff5b14"/></g>
<text x="28.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">РАЗДЕЛ 02</text>
<text x="1072.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" text-anchor="end" letter-spacing="1.6" class="mono">NETWORK &amp; SECURITY · 03 СИСТЕМЫ</text>
<rect x=".5" y=".5" width="1099" height="149" rx="6" fill="none" stroke="#2d2c29"/>

<clipPath id="num2"><rect x="20" y="58" width="150" height="86"/></clipPath>
<g clip-path="url(#num2)"><g class="reveal"><text x="24.0" y="130.0" font-size="92" fill="#ff5b14" font-weight="800" letter-spacing="-4">02</text></g></g>

<clipPath id="ttl2"><rect x="170" y="62" width="900" height="56"/></clipPath>
<g clip-path="url(#ttl2)"><g class="reveal" style="animation-delay:0.15s"><text x="176.0" y="106.0" font-size="46" fill="#ecebe5" font-weight="800" letter-spacing="-1.5">PrimeBoost &amp; Network</text></g></g>
<g class="rise" style="animation-delay:0.50s"><text x="178.0" y="132.0" font-size="15" fill="#8d8b85">Защищённая сетевая инфраструктура (RoxyBoost → PrimeBoost), прокси-серверы и плагины.</text></g>
<path d="M168 70V130" stroke="#2d2c29"/>
<g transform="translate(1056 104)"><g class="bob"><path d="M0 -14V12M-8 4L0 12L8 4" fill="none" stroke="#ecebe5" stroke-width="1.8"/></g></g>
<text x="1036.0" y="109.0" font-size="11" fill="#8d8b85" font-weight="600" text-anchor="end" letter-spacing="1.6" class="mono">СЕТЬ &amp; VPN</text>
</svg>"""
    save_svg("section-boost.svg", svg)

# ==============================================================================
# 9. CARD: PRIMEBOOST (EX-ROXYBOOST) (1100 x 430)
# ==============================================================================
def make_card_primeboost():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="430" viewBox="0 0 1100 430" role="img" aria-labelledby="t">
<title id="t">PrimeBoost (ex-RoxyBoost) — VPN-продукт и скоростной сетевой протокол: инфраструктура, приложения, сайт. Rust ядро.</title>
{COMMON_DEFS}
<style>
{COMMON_STYLE}
@keyframes pulse-ring {{
  0% {{ r: 24px; opacity: 0.8; }}
  100% {{ r: 68px; opacity: 0; }}
}}
.pulse-ring {{ animation: pulse-ring 2.8s cubic-bezier(.2,.8,.2,1) infinite; }}
</style>
<rect width="1100" height="430" rx="6" fill="#121211"/>
<path d="M12 22V12H22M12 408V418H22M1088 22V12H1078M1088 408V418H1078" fill="none" stroke="#57554f" stroke-width="1.2"/>
<path d="M28 50H1072" stroke="#2d2c29"/>
<g style="--run:988px"><rect class="register" style="animation-delay:-3.80s" x="28" y="49" width="56" height="2" fill="#ff5b14"/></g>
<text x="28.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">01 — VPN &amp; NETWORK PRODUCT · RUST CORE</text>
<text x="1072.0" y="36.0" font-size="11" fill="#ff5b14" font-weight="600" text-anchor="end" letter-spacing="1.6" class="mono">EX-ROXYBOOST → PRIMEBOOST</text>
<rect x=".5" y=".5" width="1099" height="429" rx="6" fill="none" stroke="#2d2c29"/>

<!-- Network Telemetry Visual Plate -->
<rect x="556" y="66" width="516" height="320" fill="#0e0e0d"/>
<clipPath id="bplate"><rect x="556" y="66" width="516" height="320"/></clipPath>
<g clip-path="url(#bplate)">
  <rect x="556" y="66" width="516" height="320" fill="url(#grid)"/>
  <path d="M556 106H1072" stroke="#2d2c29"/>
  <text x="576.0" y="91.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">PRIMEBOOST GLOBAL NETWORK</text>
  <text x="1052.0" y="91.0" font-size="11" fill="#ff5b14" font-weight="600" text-anchor="end" class="mono">10 GBPS · ZERO-LOGS</text>

  <!-- Network Map & Radar Center -->
  <g transform="translate(814 200)">
    <!-- Concentric radar circles -->
    <circle cx="0" cy="0" r="90" fill="none" stroke="#2d2c29" stroke-width="1.2"/>
    <circle cx="0" cy="0" r="60" fill="none" stroke="#2d2c29" stroke-width="1.2"/>
    <circle cx="0" cy="0" r="30" fill="none" stroke="#2d2c29" stroke-width="1.2"/>
    <circle class="pulse-ring" cx="0" cy="0" r="24" fill="none" stroke="#ff5b14" stroke-width="2"/>
    <circle cx="0" cy="0" r="14" fill="#ff5b14"/>
    <text x="0" y="4" font-size="8" fill="#121211" font-weight="800" text-anchor="middle" class="mono">SEC</text>

    <!-- Nodes around -->
    <circle cx="-55" cy="-35" r="4" fill="#ecebe5"/>
    <text x="-65" y="-32" font-size="9" fill="#8d8b85" text-anchor="end" class="mono">FRA (12ms)</text>

    <circle cx="65" cy="-25" r="4" fill="#ecebe5"/>
    <text x="75" y="-22" font-size="9" fill="#8d8b85" class="mono">AMS (14ms)</text>

    <circle cx="-40" cy="50" r="4" fill="#ecebe5"/>
    <text x="-50" y="53" font-size="9" fill="#8d8b85" text-anchor="end" class="mono">HEL (8ms)</text>

    <circle cx="50" cy="45" r="4" fill="#ecebe5"/>
    <text x="60" y="48" font-size="9" fill="#8d8b85" class="mono">STO (11ms)</text>

    <!-- Connecting rays -->
    <path d="M0 0 L-55 -35 M0 0 L65 -25 M0 0 L-40 50 M0 0 L50 45" stroke="#ff5b14" stroke-dasharray="2 3" opacity=".6"/>
  </g>

  <!-- Status badges at bottom -->
  <path d="M556 320H1072" stroke="#2d2c29"/>
  <text x="576.0" y="348.0" font-size="11" fill="#57554f" class="mono">PROTOCOL</text>
  <text x="650.0" y="348.0" font-size="11.5" fill="#ecebe5" font-weight="600" class="mono">VLESS + XTLS + WS</text>

  <text x="576.0" y="368.0" font-size="11" fill="#57554f" class="mono">CLIENTS</text>
  <text x="650.0" y="368.0" font-size="11.5" fill="#ecebe5" font-weight="600" class="mono">Windows · macOS · Android · iOS</text>
</g>
<rect x="556" y="66" width="516" height="320" fill="none" stroke="#2d2c29"/>
<text x="1072.0" y="404.0" font-size="10" fill="#8d8b85" font-weight="600" text-anchor="end" letter-spacing="1.6" class="mono">FIG. 03 — SECURE NETWORK INFRASTRUCTURE</text>

<!-- Left description -->
<clipPath id="pbttl"><rect x="22" y="112" width="520" height="78"/></clipPath>
<g clip-path="url(#pbttl)"><g class="reveal" style="animation-delay:0.15s"><text x="26.0" y="172.0" font-size="54" fill="#ecebe5" font-weight="800" letter-spacing="-1.8">PrimeBoost</text></g></g>
<g class="rise" style="animation-delay:0.40s"><text x="28.0" y="214.0" font-size="17" fill="#8d8b85">Флагманский VPN-продукт (ранее известный как RoxyBoost).</text></g>
<g class="rise" style="animation-delay:0.50s"><text x="28.0" y="240.0" font-size="17" fill="#8d8b85">Собственная серверная инфраструктура, кроссплатформенные</text></g>
<g class="rise" style="animation-delay:0.60s"><text x="28.0" y="266.0" font-size="17" fill="#8d8b85">приложения, Rust-ядро, zero-logs и мгновенный отклик.</text></g>
<path d="M28 300H500" stroke="#2d2c29"/>
<g class="fade" style="animation-delay:0.60s">
  <text x="28.0" y="328.0" font-size="13" fill="#8d8b85" class="mono">Rust Core</text><text x="96" y="328.0" font-size="13" fill="#ff5b14" class="mono">/</text>
  <text x="112" y="328.0" font-size="13" fill="#8d8b85" class="mono">WireGuard &amp; VLESS</text><text x="250" y="328.0" font-size="13" fill="#ff5b14" class="mono">/</text>
  <text x="266" y="328.0" font-size="13" fill="#8d8b85" class="mono">ex-RoxyBoost</text>
</g>
<g class="rise" style="animation-delay:0.90s">
  <rect x="28" y="348" width="220" height="44" fill="none" stroke="#ecebe5"/>
  <text x="46.0" y="375.0" font-size="12" fill="#ecebe5" font-weight="600" letter-spacing="1.6" class="mono">ПРОЕКТ / САЙТ</text>
  <g transform="translate(228 370)"><path d="M-6 6L6 -6M-2.4 -6H6V2.4" fill="none" stroke="#ff5b14" stroke-width="1.8" stroke-linecap="square"/></g>
</g>
</svg>"""
    save_svg("card-primeboost.svg", svg)

# ==============================================================================
# 10. CARDS: ASTRAPROXY & PRIMEAUTOACCEPT (540 x 380 each)
# ==============================================================================
def make_network_subcards():
    # Astra-PrimeProxy
    p1 = f"""<svg xmlns="http://www.w3.org/2000/svg" width="540" height="380" viewBox="0 0 540 380" role="img" aria-labelledby="t">
<title id="t">Astra-PrimeProxy — защищенный прокси-транспорт для Astra. Rust.</title>
{COMMON_DEFS}
<style>{COMMON_STYLE}</style>
<rect width="540" height="380" rx="6" fill="#121211"/>
<path d="M12 22V12H22M12 358V368H22M528 22V12H518M528 358V368H518" fill="none" stroke="#57554f" stroke-width="1.2"/>
<path d="M28 50H512" stroke="#2d2c29"/>
<g style="--run:428px"><rect class="register" style="animation-delay:-1.20s" x="28" y="49" width="56" height="2" fill="#ff5b14"/></g>
<text x="28.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">02 — ASTRA TRANSPORT · RUST</text>
<text x="488.0" y="36.0" font-size="11" fill="#ff5b14" font-weight="600" text-anchor="end" letter-spacing="1.2" class="mono">PROXY</text>
<rect x=".5" y=".5" width="539" height="379" rx="6" fill="none" stroke="#2d2c29"/>

<g transform="translate(502 32)"><path d="M-7 7L7 -7M-2.8 -7H7V2.8" fill="none" stroke="#ff5b14" stroke-width="1.6" stroke-linecap="square"/></g>

<!-- Content -->
<clipPath id="appr"><rect x="24" y="68" width="480" height="52"/></clipPath>
<g clip-path="url(#appr)"><g class="reveal"><text x="28" y="108" font-size="38" fill="#ecebe5" font-weight="800" letter-spacing="-1.2">Astra-PrimeProxy</text></g></g>

<g class="rise" style="animation-delay:0.30s">
  <text x="28.0" y="142.0" font-size="15.5" fill="#8d8b85">Специализированный защищенный транспорт</text>
  <text x="28.0" y="166.0" font-size="15.5" fill="#8d8b85">для голосового ассистента Astra. Написан на Rust.</text>
</g>

<!-- Graphic box -->
<rect x="28" y="186" width="484" height="124" fill="#0e0e0d" stroke="#2d2c29"/>
<rect x="28" y="186" width="484" height="124" fill="url(#grid)"/>
<text x="44.0" y="212.0" font-size="11" fill="#ff5b14" font-weight="700" class="mono">ENCRYPTED ASSISTANT CHANNEL</text>
<text x="44.0" y="238.0" font-size="12.5" fill="#ecebe5" class="mono">TLS 1.3 · Secure WebSocket · Direct Connect</text>
<text x="44.0" y="262.0" font-size="12" fill="#8d8b85" class="mono">Изолированный канал для голосового и текстового потока</text>
<text x="44.0" y="286.0" font-size="11" fill="#57554f" class="mono">Полная интеграция с плагинной системой Astra</text>

<g class="rise" style="animation-delay:0.70s">
  <text x="28.0" y="344.0" font-size="12" fill="#57554f" class="mono">REPO: SpherePrime/Astra-PrimeProxy · Rust</text>
</g>
</svg>"""
    save_svg("card-astraproxy.svg", p1)

    # PrimeAutoAccept
    p2 = f"""<svg xmlns="http://www.w3.org/2000/svg" width="540" height="380" viewBox="0 0 540 380" role="img" aria-labelledby="t">
<title id="t">PrimeAutoAccept — плагин автопринятия матчей для Astra (LoL, Dota 2, CS2). Rust.</title>
{COMMON_DEFS}
<style>{COMMON_STYLE}</style>
<rect width="540" height="380" rx="6" fill="#121211"/>
<path d="M12 22V12H22M12 358V368H22M528 22V12H518M528 358V368H518" fill="none" stroke="#57554f" stroke-width="1.2"/>
<path d="M28 50H512" stroke="#2d2c29"/>
<g style="--run:428px"><rect class="register" style="animation-delay:-6.70s" x="28" y="49" width="56" height="2" fill="#ff5b14"/></g>
<text x="28.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">03 — GAMING UTILITY · RUST</text>
<text x="488.0" y="36.0" font-size="11" fill="#ff5b14" font-weight="600" text-anchor="end" letter-spacing="1.2" class="mono">HOOK</text>
<rect x=".5" y=".5" width="539" height="379" rx="6" fill="none" stroke="#2d2c29"/>

<g transform="translate(502 32)"><path d="M-7 7L7 -7M-2.8 -7H7V2.8" fill="none" stroke="#ff5b14" stroke-width="1.6" stroke-linecap="square"/></g>

<!-- Content -->
<clipPath id="pttl"><rect x="24" y="68" width="480" height="52"/></clipPath>
<g clip-path="url(#pttl)"><g class="reveal"><text x="28" y="108" font-size="38" fill="#ecebe5" font-weight="800" letter-spacing="-1.2">PrimeAutoAccept</text></g></g>

<g class="rise" style="animation-delay:0.30s">
  <text x="28.0" y="142.0" font-size="15.5" fill="#8d8b85">Плагин для Astra: автоматическое принятие матчей</text>
  <text x="28.0" y="166.0" font-size="15.5" fill="#8d8b85">в соревновательных играх: League of Legends, Dota 2, CS2.</text>
</g>

<!-- Graphic box -->
<rect x="28" y="186" width="484" height="124" fill="#0e0e0d" stroke="#2d2c29"/>
<rect x="28" y="186" width="484" height="124" fill="url(#grid)"/>
<text x="44.0" y="212.0" font-size="11" fill="#ff5b14" font-weight="700" class="mono">REAL-TIME GAME CLIENT HOOK</text>
<text x="44.0" y="238.0" font-size="12.5" fill="#ecebe5" class="mono">Dota 2 GC · LoL LCU API · CS2 Game State</text>
<text x="44.0" y="262.0" font-size="12" fill="#8d8b85" class="mono">Мгновенный детект поиска игры и принятие за 20ms</text>
<text x="44.0" y="286.0" font-size="11" fill="#57554f" class="mono">Звуковое оповещение через Astra TTS</text>

<g class="rise" style="animation-delay:0.70s">
  <text x="28.0" y="344.0" font-size="12" fill="#57554f" class="mono">REPO: SpherePrime/PrimeAutoAccept · Rust</text>
</g>
</svg>"""
    save_svg("card-autoaccept.svg", p2)

# ==============================================================================
# 11. SECTION 03 HEADER (Team & Co-founders)
# ==============================================================================
def make_section_team():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="150" viewBox="0 0 1100 150" role="img" aria-labelledby="t">
<title id="t">03 — Team &amp; Co-founders. Создатели и ключевые разработчики экосистемы SpherePrime.</title>
{COMMON_DEFS}
<style>{COMMON_STYLE}</style>
<rect width="1100" height="150" rx="6" fill="#121211"/>
<path d="M12 22V12H22M12 128V138H22M1088 22V12H1078M1088 128V138H1078" fill="none" stroke="#57554f" stroke-width="1.2"/>
<path d="M28 50H1072" stroke="#2d2c29"/>
<g style="--run:988px"><rect class="register" style="animation-delay:-1.20s" x="28" y="49" width="56" height="2" fill="#ff5b14"/></g>
<text x="28.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">РАЗДЕЛ 03</text>
<text x="1072.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" text-anchor="end" letter-spacing="1.6" class="mono">CO-FOUNDERS &amp; ARCHITECTS</text>
<rect x=".5" y=".5" width="1099" height="149" rx="6" fill="none" stroke="#2d2c29"/>

<clipPath id="num3"><rect x="20" y="58" width="150" height="86"/></clipPath>
<g clip-path="url(#num3)"><g class="reveal"><text x="24.0" y="130.0" font-size="92" fill="#ff5b14" font-weight="800" letter-spacing="-4">03</text></g></g>

<clipPath id="ttl3"><rect x="170" y="62" width="900" height="56"/></clipPath>
<g clip-path="url(#ttl3)"><g class="reveal" style="animation-delay:0.15s"><text x="176.0" y="106.0" font-size="46" fill="#ecebe5" font-weight="800" letter-spacing="-1.5">Команда и Соавторы</text></g></g>
<g class="rise" style="animation-delay:0.50s"><text x="178.0" y="132.0" font-size="15" fill="#8d8b85">Основатели SpherePrime: LilKALINOV и dwertyfa — от ядра до нативных интерфейсов.</text></g>
<path d="M168 70V130" stroke="#2d2c29"/>
<g transform="translate(1056 104)"><g class="bob"><path d="M0 -14V12M-8 4L0 12L8 4" fill="none" stroke="#ecebe5" stroke-width="1.8"/></g></g>
<text x="1036.0" y="109.0" font-size="11" fill="#8d8b85" font-weight="600" text-anchor="end" letter-spacing="1.6" class="mono">АВТОРЫ</text>
</svg>"""
    save_svg("section-team.svg", svg)

# ==============================================================================
# 13. TEAM CARDS: LILKALINOV & DWERTYFA (540 x 400 each)
# ==============================================================================
def make_team_cards():
    # LilKALINOV
    lk = f"""<svg xmlns="http://www.w3.org/2000/svg" width="540" height="400" viewBox="0 0 540 400" role="img" aria-labelledby="t">
<title id="t">LilKALINOV — Co-founder SpherePrime, Lead QA Astra. Профиль и проекты.</title>
{COMMON_DEFS}
<style>{COMMON_STYLE}</style>
<rect width="540" height="400" rx="6" fill="#121211"/>
<path d="M12 22V12H22M12 378V388H22M528 22V12H518M528 378V388H518" fill="none" stroke="#57554f" stroke-width="1.2"/>
<path d="M28 50H512" stroke="#2d2c29"/>
<g style="--run:428px"><rect class="register" style="animation-delay:0.00s" x="28" y="49" width="56" height="2" fill="#ff5b14"/></g>
<text x="28.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.2" class="mono">01 — CO-FOUNDER · LEAD QA</text>
<text x="488.0" y="36.0" font-size="11" fill="#ff5b14" font-weight="600" text-anchor="end" letter-spacing="1.2" class="mono">@LILKALINOV</text>
<rect x=".5" y=".5" width="539" height="399" rx="6" fill="none" stroke="#2d2c29"/>

<g transform="translate(502 32)"><path d="M-7 7L7 -7M-2.8 -7H7V2.8" fill="none" stroke="#ff5b14" stroke-width="1.6" stroke-linecap="square"/></g>

<!-- Name & Role -->
<clipPath id="lkn"><rect x="24" y="68" width="480" height="54"/></clipPath>
<g clip-path="url(#lkn)"><g class="reveal"><text x="28" y="112" font-size="46" fill="#ecebe5" font-weight="800" letter-spacing="-1.2">LilKALINOV<tspan fill="#ff5b14">.</tspan></text></g></g>

<g class="rise" style="animation-delay:0.30s">
  <text x="28.0" y="146.0" font-size="15" fill="#ecebe5" font-weight="600">Со-основатель SpherePrime · Lead QA Astra</text>
  <text x="28.0" y="172.0" font-size="14.5" fill="#8d8b85">Архитектура, тестирование ИИ-агентов, системные утилиты</text>
  <text x="28.0" y="194.0" font-size="14.5" fill="#8d8b85">и голосовые расширения. Открытый код и надёжность.</text>
</g>

<!-- Focus tags -->
<rect x="28" y="214" width="484" height="110" fill="#0e0e0d" stroke="#2d2c29"/>
<rect x="28" y="214" width="484" height="110" fill="url(#grid)"/>

<text x="44.0" y="240.0" font-size="11" fill="#ff5b14" font-weight="700" class="mono">КЛЮЧЕВЫЕ ПРОЕКТЫ И ПЛАГИНЫ</text>
<text x="44.0" y="264.0" font-size="12.5" fill="#ecebe5" class="mono">Prime Desktop · Astra-Google-STT · Astra Silero</text>
<text x="44.0" y="286.0" font-size="12.5" fill="#ecebe5" class="mono">astra-websearch-ddg · Astra-PrimeProxy · fluxer</text>
<text x="44.0" y="308.0" font-size="11" fill="#57554f" class="mono">Стек: Rust · Python · Go · Tauri · C/C++ · Qt</text>

<!-- Button -->
<g class="rise" style="animation-delay:0.75s">
  <rect x="28" y="340" width="200" height="38" fill="none" stroke="#ecebe5"/>
  <text x="46.0" y="364.0" font-size="11.5" fill="#ecebe5" font-weight="600" letter-spacing="1.4" class="mono">ПРОФИЛЬ АВТОРА</text>
  <g transform="translate(208 359)"><path d="M-5 5L5 -5M-2 -5H5V2" fill="none" stroke="#ff5b14" stroke-width="1.6" stroke-linecap="square"/></g>
</g>
</svg>"""
    save_svg("card-lilkalinov.svg", lk)

    # dwertyfa
    dw = f"""<svg xmlns="http://www.w3.org/2000/svg" width="540" height="400" viewBox="0 0 540 400" role="img" aria-labelledby="t">
<title id="t">dwertyfa — Co-founder SpherePrime, Full-stack инженер. Профиль и проекты.</title>
{COMMON_DEFS}
<style>{COMMON_STYLE}</style>
<rect width="540" height="400" rx="6" fill="#121211"/>
<path d="M12 22V12H22M12 378V388H22M528 22V12H518M528 378V388H518" fill="none" stroke="#57554f" stroke-width="1.2"/>
<path d="M28 50H512" stroke="#2d2c29"/>
<g style="--run:428px"><rect class="register" style="animation-delay:-4.00s" x="28" y="49" width="56" height="2" fill="#ff5b14"/></g>
<text x="28.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.2" class="mono">02 — CO-FOUNDER · FULL-STACK</text>
<text x="488.0" y="36.0" font-size="11" fill="#ff5b14" font-weight="600" text-anchor="end" letter-spacing="1.2" class="mono">@DWERTYFA288</text>
<rect x=".5" y=".5" width="539" height="399" rx="6" fill="none" stroke="#2d2c29"/>

<g transform="translate(502 32)"><path d="M-7 7L7 -7M-2.8 -7H7V2.8" fill="none" stroke="#ff5b14" stroke-width="1.6" stroke-linecap="square"/></g>

<!-- Name & Role -->
<clipPath id="dwn"><rect x="24" y="68" width="480" height="54"/></clipPath>
<g clip-path="url(#dwn)"><g class="reveal"><text x="28" y="112" font-size="46" fill="#ecebe5" font-weight="800" letter-spacing="-1.2">dwertyfa<tspan fill="#ff5b14">.</tspan></text></g></g>

<g class="rise" style="animation-delay:0.30s">
  <text x="28.0" y="146.0" font-size="15" fill="#ecebe5" font-weight="600">Со-основатель SpherePrime · Full-stack Инженер</text>
  <text x="28.0" y="172.0" font-size="14.5" fill="#8d8b85">Веб-платформы, интерактивные 3D-интерфейсы,</text>
  <text x="28.0" y="194.0" font-size="14.5" fill="#8d8b85">PrimeBoost VPN, Telegram Mini Apps и голосовые плагины.</text>
</g>

<!-- Focus tags -->
<rect x="28" y="214" width="484" height="110" fill="#0e0e0d" stroke="#2d2c29"/>
<rect x="28" y="214" width="484" height="110" fill="url(#grid)"/>

<text x="44.0" y="240.0" font-size="11" fill="#ff5b14" font-weight="700" class="mono">КЛЮЧЕВЫЕ ПРОЕКТЫ И ПРОДУКТЫ</text>
<text x="44.0" y="264.0" font-size="12.5" fill="#ecebe5" class="mono">PrimeBoost (RoxyBoost) · dwertyfa-astra-tg</text>
<text x="44.0" y="286.0" font-size="12.5" fill="#ecebe5" class="mono">astra-interject · Мой Дизайнер · 3D Портфолио</text>
<text x="44.0" y="308.0" font-size="11" fill="#57554f" class="mono">Стек: Rust · Next.js · React · Three.js · Python · TS</text>

<!-- Button -->
<g class="rise" style="animation-delay:0.75s">
  <rect x="28" y="340" width="200" height="38" fill="none" stroke="#ecebe5"/>
  <text x="46.0" y="364.0" font-size="11.5" fill="#ecebe5" font-weight="600" letter-spacing="1.4" class="mono">ПРОФИЛЬ АВТОРА</text>
  <g transform="translate(208 359)"><path d="M-5 5L5 -5M-2 -5H5V2" fill="none" stroke="#ff5b14" stroke-width="1.6" stroke-linecap="square"/></g>
</g>
</svg>"""
    save_svg("card-dwertyfa.svg", dw)

# ==============================================================================
# 14. FOOTER BANNER (1100 x 180)
# ==============================================================================
def make_footer():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="180" viewBox="0 0 1100 180" role="img" aria-labelledby="t">
<title id="t">SpherePrime — есть идея или проект? Присоединяйтесь к комьюнити в Telegram.</title>
{COMMON_DEFS}
<style>{COMMON_STYLE}</style>
<rect width="1100" height="180" rx="6" fill="#121211"/>
<path d="M12 22V12H22M12 158V168H22M1088 22V12H1078M1088 158V168H1078" fill="none" stroke="#57554f" stroke-width="1.2"/>
<path d="M28 50H1072" stroke="#2d2c29"/>
<g style="--run:988px"><rect class="register" style="animation-delay:-7.50s" x="28" y="49" width="56" height="2" fill="#ff5b14"/></g>
<text x="28.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" letter-spacing="1.6" class="mono">SPHEREPRIME / CONTACT &amp; COMMUNITY</text>
<text x="1072.0" y="36.0" font-size="11" fill="#8d8b85" font-weight="600" text-anchor="end" letter-spacing="1.6" class="mono">OPEN FOR COLLABORATION</text>
<rect x=".5" y=".5" width="1099" height="179" rx="6" fill="none" stroke="#2d2c29"/>

<text x="28.0" y="98.0" font-size="28" fill="#ecebe5" font-weight="700">Есть идея или задача? Соберём живой продукт вместе.</text>
<text x="28.0" y="128.0" font-size="15" fill="#8d8b85">ИИ-агенты, десктопные оболочки, PrimeBoost VPN, архитектура и системное тестирование.</text>

<g transform="translate(1040 100)">
  <g class="nudge">
    <circle cx="0" cy="0" r="24" fill="#0e0e0d" stroke="#ecebe5" stroke-width="1.6"/>
    <path d="M-6 6L6 -6M-2.4 -6H6V2.4" fill="none" stroke="#ff5b14" stroke-width="2" stroke-linecap="square"/>
  </g>
</g>
<text x="1000.0" y="105.0" font-size="13" fill="#ff5b14" font-weight="700" text-anchor="end" class="mono">t.me/SpherePrime</text>
</svg>"""
    save_svg("footer.svg", svg)

if __name__ == "__main__":
    print("Generating SpherePrime SVG assets...")
    make_hero()
    make_links()
    make_stats()
    make_section_prime()
    make_card_cli()
    make_card_desktop()
    make_primeai_and_proxy()
    make_section_boost()
    make_card_primeboost()
    make_network_subcards()
    make_section_team()
    make_team_cards()
    make_footer()
    print("All assets successfully generated!")
