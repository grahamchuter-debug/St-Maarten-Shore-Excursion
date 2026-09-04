#!/usr/bin/env python3
"""World 2.0 content extensions for St Maarten Shore Excursion.

Runs after build-st-maarten-site.py. Rewrites homepage decision architecture,
decision pages, legal pages, nav/footer, softens unsupported claims, and
merges schedule sitemap fragments. Does not modify Cozumel, Aruba, or Grand Cayman.
"""
from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://stmaartenshoreexcursion.com"
SITE = "St Maarten Shore Excursion"
DATE = "2026-09-04"

_spec = importlib.util.spec_from_file_location(
    "build_sxm", ROOT / "scripts" / "build-st-maarten-site.py"
)
_build = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_build)

page_shell = _build.page_shell
cruise_snapshot = _build.cruise_snapshot
_hero_inner = _build._hero_inner
write = _build.write
HOME_HERO = _build.HOME_HERO
HOME_HERO_ALT = _build.HOME_HERO_ALT
MAHO_IMG = _build.MAHO_IMG
MAHO_ALT = _build.MAHO_ALT
ORIENT_IMG = _build.ORIENT_IMG
ORIENT_ALT = _build.ORIENT_ALT
ISLAND_IMG = _build.ISLAND_IMG
ISLAND_ALT = _build.ISLAND_ALT
DUTCH_FRENCH_IMG = _build.DUTCH_FRENCH_IMG
DUTCH_FRENCH_ALT = _build.DUTCH_FRENCH_ALT
PORT_IMG = _build.PORT_IMG
PORT_ALT = _build.PORT_ALT
INTRO_IMG = _build.INTRO_IMG
INTRO_ALT = _build.INTRO_ALT
CATAMARAN_IMG = _build.CATAMARAN_IMG
CATAMARAN_ALT = _build.CATAMARAN_ALT
ONE_DAY_IMG = _build.ONE_DAY_IMG
ONE_DAY_ALT = _build.ONE_DAY_ALT
ACCENT = _build.ACCENT
HERO_GRADIENT = _build.HERO_GRADIENT
_hero_wave = _build._hero_wave


def soft_claims_in_text(html: str) -> str:
    replacements = [
        (
            r"Operators usually allow 60[–-]90 min buffer",
            "Build your own buffer; confirm operator return plan",
        ),
        (
            r"Ship tours guarantee the vessel waits if the operator is late\. Reputable St Maarten operators plan returns with buffer — confirm policies and read reviews before booking ashore\.",
            "Ship-sold tours often include a wait-if-late policy from the cruise line. Independent operators typically plan a return window — confirm policies, build your own buffer, and do not cut it fine.",
        ),
        (
            r"Ship tours guarantee wait-if-late; reputable locals plan buffer returns\.",
            "Ship-sold tours often include wait-if-late; confirm independent operator policies and build your own buffer.",
        ),
        (
            r"and a fixed return to Philipsburg pier",
            "and a timed return window to Philipsburg pier — confirm details with the operator",
        ),
        (
            r"and a fixed return to the pier",
            "and a timed return window to the pier — confirm details with the operator",
        ),
        (
            r"Allow margin before published all-aboard\.",
            "Build your own buffer before published all-aboard — confirm times with your ship and operator.",
        ),
        (
            r"plan returns with buffer before all aboard",
            "plan returns with enough time before all aboard — confirm with the operator",
        ),
        (
            r"understand all-aboard deadlines",
            "usually plan around all-aboard — still confirm return timing in writing",
        ),
        (
            r"fits comfortably with return buffer",
            "can fit when you leave a sensible return window",
        ),
        (
            r"Maho Beach is 15–20 minutes west; Orient Beach on the French side is 25–35 minutes by taxi or organised transfer\.",
            "Maho Beach is typically about 15–25 minutes west by road — traffic varies. Orient Beach on the French side is often 25–45 minutes depending on congestion and your pickup point.",
        ),
    ]
    out = html
    for pat, repl in replacements:
        out = re.sub(pat, repl, out)
    return out


def soft_all_content() -> None:
    content_dir = ROOT / "content"
    for path in content_dir.glob("*.html"):
        original = path.read_text(encoding="utf-8")
        updated = soft_claims_in_text(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(f"  softened claims in content/{path.name}")


def internal_links() -> str:
    return """<nav class="mt-10 pt-8 border-t border-gray-100" aria-label="Related St Maarten guides">
  <p class="text-sm font-semibold text-gray-900 mb-3">Plan your Philipsburg port day</p>
  <div class="flex flex-wrap gap-3 text-sm">
    <a href="st-maarten-cruise-port-guide.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Port Guide</a>
    <span class="text-gray-300">·</span>
    <a href="best-st-maarten-shore-excursions.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Best Excursions</a>
    <span class="text-gray-300">·</span>
    <a href="dutch-side-vs-french-side.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Dutch vs French</a>
    <span class="text-gray-300">·</span>
    <a href="maho-vs-orient-bay.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Maho vs Orient</a>
    <span class="text-gray-300">·</span>
    <a href="ship-schedule/" class="text-ocean-600 hover:text-ocean-800 font-medium">Ship Schedule</a>
    <span class="text-gray-300">·</span>
    <a href="st-maarten-faq.html" class="text-ocean-600 hover:text-ocean-800 font-medium">FAQ</a>
  </div>
</nav>"""


def concierge_panel() -> str:
    return """<section class="py-14 bg-white" id="concierge" aria-labelledby="concierge-heading">
  <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="concierge-panel">
      <h2 id="concierge-heading" class="font-display font-bold text-2xl sm:text-3xl mb-3">Need help shaping your St Maarten day?</h2>
      <p class="text-white/90 text-sm sm:text-base leading-relaxed mb-4">
        Tell us your ship, call date, and whether you lean Maho plane spotting, Orient Beach, a dual-nation island circuit, or a catamaran sail.
        We are an independent planning resource — not the cruise line and not a ticket marketplace.
      </p>
      <p class="text-white/80 text-sm leading-relaxed mb-5">
        Email <a href="mailto:hello@stmaartenshoreexcursion.com">hello@stmaartenshoreexcursion.com</a> with your ship, date and preferences.
        We do not promise instant replies or 24/7 staffing.
      </p>
      <div class="flex flex-col sm:flex-row gap-3">
        <a href="mailto:hello@stmaartenshoreexcursion.com" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-6 py-3 rounded-full text-sm no-underline">Email the St Maarten concierge</a>
        <a href="best-st-maarten-shore-excursions.html" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-6 py-3 rounded-full text-sm no-underline">Compare excursion types</a>
      </div>
    </div>
  </div>
</section>"""


def snapshot(**overrides: str) -> str:
    defaults = dict(
        time_in_port="8–10 hours (typical)",
        best_for="Maho Beach, Orient Beach, sailing, island tours",
        activity_level="Varies — see comparison",
        family="Excellent with age-appropriate picks",
        return_ship="Build your own buffer; confirm operator return plan",
        popular="Maho Beach, Orient Beach, catamaran, island drive",
    )
    defaults.update(overrides)
    return cruise_snapshot(**defaults)


def write_nav() -> None:
    write(
        "partials/nav.html",
        f"""<nav class="fixed top-0 left-0 right-0 z-50 bg-white/90 border-b border-sxm-100 shadow-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-12">
      <a href="index.html" class="flex items-center gap-2">
        <div class="w-7 h-7 rounded-full btn-ocean flex items-center justify-center">
          <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/>
          </svg>
        </div>
        <span class="font-display font-semibold text-ocean-800 text-base leading-tight">St Maarten<br/><span class="text-[10px] font-body font-normal text-fuchsia-600 tracking-widest uppercase">Shore Excursion</span></span>
      </a>
      <div class="hidden lg:flex items-center gap-5 text-sm font-medium">
        <a href="index.html" data-nav="home" class="text-gray-600 hover:text-ocean-600 transition-colors">Home</a>
        <a href="best-st-maarten-shore-excursions.html" data-nav="excursions" class="text-gray-600 hover:text-ocean-600 transition-colors">Excursions</a>
        <a href="maho-beach-plane-spotting-tours.html" data-nav="maho" class="text-gray-600 hover:text-ocean-600 transition-colors">Maho Beach</a>
        <a href="orient-beach-excursions.html" data-nav="orient" class="text-gray-600 hover:text-ocean-600 transition-colors">Orient Beach</a>
        <a href="ship-schedule/" data-nav="schedule" class="text-gray-600 hover:text-ocean-600 transition-colors">Ship Schedule</a>
        <a href="st-maarten-cruise-port-guide.html" data-nav="port" class="text-gray-600 hover:text-ocean-600 transition-colors">Port Guide</a>
      </div>
      <a href="contact.html" class="hidden md:inline-flex items-center gap-2 btn-ocean text-white text-sm font-semibold px-4 py-2 rounded-full shadow-md">
        Contact concierge
      </a>
      <button type="button" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-sand-50" aria-label="Open menu">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </div>
</nav>
""",
    )


def write_footer() -> None:
    write(
        "partials/footer.html",
        f"""  <footer class="bg-gray-900 text-gray-400 py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
        <div class="sm:col-span-2 lg:col-span-1">
          <a href="index.html" class="font-display font-semibold text-white text-lg">{SITE}</a>
          <p class="mt-3 text-sm leading-relaxed">Independent planning guide for cruise visitors docking at Philipsburg. Not affiliated with any cruise line.</p>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Excursions</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="best-st-maarten-shore-excursions.html" class="hover:text-white transition-colors">Best Excursions</a></li>
            <li><a href="maho-beach-plane-spotting-tours.html" class="hover:text-white transition-colors">Maho Beach</a></li>
            <li><a href="orient-beach-excursions.html" class="hover:text-white transition-colors">Orient Beach</a></li>
            <li><a href="st-maarten-snorkelling-tours.html" class="hover:text-white transition-colors">Snorkelling</a></li>
            <li><a href="st-maarten-island-tours.html" class="hover:text-white transition-colors">Island Tours</a></li>
            <li><a href="st-maarten-atv-buggy-tours.html" class="hover:text-white transition-colors">ATV &amp; Buggy</a></li>
            <li><a href="catamaran-sailing-excursions.html" class="hover:text-white transition-colors">Catamaran Sailing</a></li>
            <li><a href="dutch-side-vs-french-side.html" class="hover:text-white transition-colors">Dutch vs French</a></li>
            <li><a href="maho-vs-orient-bay.html" class="hover:text-white transition-colors">Maho vs Orient</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Resources</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="st-maarten-cruise-port-guide.html" class="hover:text-white transition-colors">Port Guide</a></li>
            <li><a href="ship-schedule/" class="hover:text-white transition-colors">Ship Schedule</a></li>
            <li><a href="one-day-in-st-maarten.html" class="hover:text-white transition-colors">One Day in St Maarten</a></li>
            <li><a href="dutch-and-french-side-tours.html" class="hover:text-white transition-colors">Dutch &amp; French Tours</a></li>
            <li><a href="best-beaches-in-st-maarten.html" class="hover:text-white transition-colors">Best Beaches</a></li>
            <li><a href="st-maarten-faq.html" class="hover:text-white transition-colors">FAQ</a></li>
            <li><a href="methodology.html" class="hover:text-white transition-colors">Methodology</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Legal</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="about.html" class="hover:text-white transition-colors">About</a></li>
            <li><a href="contact.html" class="hover:text-white transition-colors">Contact</a></li>
            <li><a href="privacy.html" class="hover:text-white transition-colors">Privacy</a></li>
            <li><a href="terms.html" class="hover:text-white transition-colors">Terms</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-gray-800 pt-8 text-xs text-center sm:text-left">
        <p>&copy; 2026 {SITE}. Confirm times with your cruise line and operators. No fabricated prices or ratings on this site.</p>
      </div>
    </div>
  </footer>
""",
    )


def hero_home() -> str:
    return f"""  <section class="site-hero">
    <div class="absolute inset-0 hero-bg" style="background-image: {HERO_GRADIENT}, url('{HOME_HERO}');" role="img" aria-label="{HOME_HERO_ALT}"></div>
    <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl">
        <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
          <span class="w-2 h-2 rounded-full bg-fuchsia-400 animate-pulse"></span>
          <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">Philipsburg · Two nations · One island</span>
        </div>
        <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">
          St Maarten Shore<br/><span class="{ACCENT}">Excursion</span>
        </h1>
        <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">
          Step off in Philipsburg and choose your St Maarten: Dutch-side duty-free streets, French-side Orient sand, Maho’s runway theatre when planes are moving, or a dual-nation island circuit.
        </p>
        <div class="site-hero__actions flex flex-col sm:flex-row gap-3">
          <a href="maho-vs-orient-bay.html" class="btn-primary inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Maho or Orient?</a>
          <a href="ship-schedule/" class="btn-outline inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm">Find your ship</a>
        </div>
        <div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Philipsburg</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Maho Beach</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Orient Bay</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Dutch &amp; French</span>
        </div>
      </div>
    </div>
    {_hero_wave()}
  </section>"""


def content_home() -> str:
    snap = snapshot()
    return f"""<section class="pt-8 pb-6 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
  <p class="section-label mx-auto">Philipsburg cruise call</p>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">St Maarten is two nations sharing one hillside island</h2>
  <p class="text-gray-600 text-sm sm:text-base leading-relaxed">Ships berth at Philipsburg on the Dutch side. From there you can stay near Front Street, chase Maho’s runway beach when aircraft are active, cross to French-side Orient Bay for a longer swim day, or stitch both cultures into one island circuit — road times vary with traffic.</p>
</div></section>
<section class="pb-10 bg-white"><div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="decision-grid">
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Maho plane spotting</h3><p>Runway-end beach energy when jets are moving — treat landings as possible, not a timed show.</p><a href="maho-beach-plane-spotting-tours.html" class="text-ocean-600 font-semibold text-sm">Maho Beach →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Orient Beach day</h3><p>French-side clubs, turquoise water and lunch pacing east of Philipsburg.</p><a href="orient-beach-excursions.html" class="text-ocean-600 font-semibold text-sm">Orient Beach →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Dutch vs French</h3><p>Currency, language and mood differ — ordinary day movement between sides is usually low-friction.</p><a href="dutch-side-vs-french-side.html" class="text-ocean-600 font-semibold text-sm">Compare sides →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Maho vs Orient</h3><p>Short iconic runway stop versus a longer French-side beach day — honest trade-offs.</p><a href="maho-vs-orient-bay.html" class="text-ocean-600 font-semibold text-sm">Decide →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Island circuit</h3><p>Philipsburg, Marigot, viewpoints and both coasts in one air-conditioned loop.</p><a href="st-maarten-island-tours.html" class="text-ocean-600 font-semibold text-sm">Island tours →</a></div>
    <div class="decision-card"><h3 class="font-display font-bold text-gray-900">Find your ship</h3><p>Search Philipsburg call dates, then leave a sensible return window before all aboard.</p><a href="ship-schedule/" class="text-ocean-600 font-semibold text-sm">Ship schedule →</a></div>
  </div>
</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <p class="section-label">Pier orientation</p>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Philipsburg is a walk-ashore Dutch-side port</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Cruise ships use the Dr. A.C. Wathey facilities on Great Bay. You step into duty-free Front Street, taxis and tour meeting points — then choose how far west (Maho) or east (Orient / Marigot) to travel. Build time for variable traffic rather than assuming a fixed transfer clock.</p>
    <a href="st-maarten-cruise-port-guide.html" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">Port guide</a>
  </div>
  <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
    <img src="{PORT_IMG}" alt="{PORT_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg order-2 lg:order-1">
    <img src="{INTRO_IMG}" alt="{INTRO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
  <div class="order-1 lg:order-2">
    <p class="section-label">Two-nation identity</p>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Dutch streets, French cafés, one hillside island</h2>
    <p class="text-gray-600 leading-relaxed mb-4">St Maarten / Saint Martin is the smallest island shared by two countries. That geography is the story — not invented border theatre. Use it to pick Philipsburg shopping, Marigot markets, Orient sand or a dual-culture van loop.</p>
    <a href="dutch-side-vs-french-side.html" class="text-ocean-600 font-semibold text-sm">Dutch vs French →</a>
    <span class="text-gray-300 mx-2">·</span>
    <a href="dutch-and-french-side-tours.html" class="text-ocean-600 font-semibold text-sm">Combo tours →</a>
  </div>
</div></div></section>
<section class="pb-4 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="text-center mb-10">
    <p class="section-label mx-auto">Signature stops</p>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-3">Four St Maarten experiences cruise guests compare most</h2>
  </div>
  <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
    <div class="bg-white rounded-3xl overflow-hidden shadow-md border border-sxm-50 flex flex-col">
      <div class="card-media h-44"><img src="{MAHO_IMG}" alt="{MAHO_ALT}" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Maho Beach</h3><p class="text-sm text-gray-500 flex-1">Runway-end beach when aircraft are moving — safety briefings first.</p><a href="maho-beach-plane-spotting-tours.html" class="mt-5 text-ocean-600 font-semibold text-sm">Maho Beach →</a></div>
    </div>
    <div class="bg-white rounded-3xl overflow-hidden shadow-md border border-sxm-50 flex flex-col">
      <div class="card-media h-44"><img src="{ORIENT_IMG}" alt="{ORIENT_ALT}" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Orient Beach</h3><p class="text-sm text-gray-500 flex-1">French-side swim-and-lunch pacing east of the pier.</p><a href="orient-beach-excursions.html" class="mt-5 text-ocean-600 font-semibold text-sm">Orient Beach →</a></div>
    </div>
    <div class="bg-white rounded-3xl overflow-hidden shadow-md border border-sxm-50 flex flex-col">
      <div class="card-media h-44"><img src="{CATAMARAN_IMG}" alt="{CATAMARAN_ALT}" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Catamaran sail</h3><p class="text-sm text-gray-500 flex-1">Leeward sailing with optional snorkel stops timed for port days.</p><a href="catamaran-sailing-excursions.html" class="mt-5 text-ocean-600 font-semibold text-sm">Catamaran →</a></div>
    </div>
    <div class="bg-white rounded-3xl overflow-hidden shadow-md border border-sxm-50 flex flex-col">
      <div class="card-media h-44"><img src="{ISLAND_IMG}" alt="{ISLAND_ALT}" width="600" height="352" loading="lazy" decoding="async" /></div>
      <div class="p-6 flex flex-col flex-1"><h3 class="text-lg font-display font-semibold text-gray-900 mb-2">Island circuit</h3><p class="text-sm text-gray-500 flex-1">Both nations, viewpoints and waterfront towns in one loop.</p><a href="st-maarten-island-tours.html" class="mt-5 text-ocean-600 font-semibold text-sm">Island tours →</a></div>
    </div>
  </div>
  <p class="text-center mt-8"><a href="best-st-maarten-shore-excursions.html" class="text-ocean-600 font-semibold text-sm">Full comparison →</a></p>
</div></section>
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
  <div>
    <p class="section-label">Ship planning</p>
    <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Match the day to your Philipsburg call</h2>
    <p class="text-gray-600 leading-relaxed mb-4">Browse arrivals by month, note your all-aboard window, then choose Maho, Orient, sail or island circuit. Schedules can change — treat published times as planning aids and build your own buffer.</p>
    <a href="ship-schedule/" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm">Find your ship schedule</a>
  </div>
  <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{ONE_DAY_IMG}" alt="{ONE_DAY_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div></div></section>
<section class="py-16 cta-gradient"><div class="max-w-3xl mx-auto px-4 text-center">
  <h2 class="text-3xl font-display font-bold text-white mb-4">Still deciding?</h2>
  <p class="text-white/85 text-sm mb-6">Compare Maho versus Orient, or email the St Maarten concierge with your ship and date.</p>
  <div class="flex flex-col sm:flex-row gap-4 justify-center">
    <a href="maho-vs-orient-bay.html" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Maho vs Orient</a>
    <a href="contact.html" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Contact concierge</a>
  </div>
</div></section>
{concierge_panel()}"""


def content_port() -> str:
    snap = snapshot(
        activity_level="Low at terminal; moderate on tours",
        popular="Walk-ashore port, taxis, organised pickups",
        best_for="Orienting at Philipsburg before Maho, Orient or island plans",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
  <p class="text-gray-600 leading-relaxed text-sm">St Maarten is a <strong>pier port</strong> on the Dutch side. Ships berth at <strong>Philipsburg</strong> — Front Street shops, taxis and excursion meeting points are close ashore on a typical <strong>8–10 hour</strong> call.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4">
  <h2 class="text-2xl font-display font-bold text-center mb-8">Where ships arrive</h2>
  <div class="info-image rounded-3xl aspect-[21/9] shadow-xl overflow-hidden mb-8 max-w-5xl mx-auto">
    <img src="{PORT_IMG}" alt="{PORT_ALT}" width="1200" height="514" loading="lazy" decoding="async" />
  </div>
  <div class="grid lg:grid-cols-2 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-sxm-100"><h3 class="font-display font-bold text-lg mb-2">Philipsburg terminals</h3><p class="text-gray-600">Dr. A.C. Wathey Cruise &amp; Cargo Facilities place you steps from Front Street duty-free shops, taxis and shore-excursion desks. Confirm your meeting point — multi-ship days get busy.</p></div>
    <div class="bg-white rounded-3xl p-6 border border-sxm-100"><h3 class="font-display font-bold text-lg mb-2">Getting to beaches</h3><p class="text-gray-600">Maho Beach is typically about 15–25 minutes west by road — traffic varies. Orient Beach on the French side is often 25–45 minutes depending on congestion and your pickup point. Build your own return window.</p></div>
  </div>
</div></section>
<section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4">
  <div class="grid sm:grid-cols-3 gap-6 text-sm">
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Currency</strong><p class="mt-2 text-gray-600">Netherlands Antillean guilder (ANG) on Dutch side; euros in French St Martin. <strong>US dollars</strong> widely accepted.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Language</strong><p class="mt-2 text-gray-600">Dutch and English on Dutch side; French in Marigot. English common in tourism and at the port.</p></div>
    <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Two nations</strong><p class="mt-2 text-gray-600">Ordinary day movement between Dutch and French sides is typically open and low-friction — geography matters more than border theatre.</p></div>
  </div>
  <p class="text-center mt-8"><a href="one-day-in-st-maarten.html" class="text-ocean-600 font-semibold text-sm">One-day itinerary →</a>
  <span class="text-gray-300 mx-2">·</span>
  <a href="ship-schedule/" class="text-ocean-600 font-semibold text-sm">Ship schedule →</a></p>
  <div class="mt-10 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>
{concierge_panel()}"""


def content_dutch_vs_french() -> str:
    snap = snapshot(
        best_for="Understanding Dutch vs French sides before booking",
        activity_level="Low to moderate — van and short walks",
        popular="Philipsburg, Marigot, dual-nation loops",
    )
    return f"""<section class="pt-8 pb-6 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <p class="text-gray-600 leading-relaxed mb-4">St Maarten / Saint Martin is useful geography for cruise guests: <strong>two nations on one small island</strong>. Dutch-side Philipsburg is where ships dock; French-side Marigot and Orient Bay sit across the hills.</p>
  <p class="text-gray-600 leading-relaxed">For ordinary day movement the land border is typically <strong>open and low-friction</strong>. Do not invent significant border-control drama for a standard shore excursion — carry ID if your operator asks, then focus on currency, language and beach mood.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-2xl font-display font-bold text-gray-900 text-center mb-8">Dutch side vs French side</h2>
  <div class="grid md:grid-cols-2 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-sxm-100">
      <div class="card-media rounded-2xl overflow-hidden aspect-[16/10] mb-4">
        <img src="{PORT_IMG}" alt="{PORT_ALT}" width="600" height="375" loading="lazy" decoding="async" />
      </div>
      <h3 class="font-display font-bold text-lg mb-3">Dutch St Maarten</h3>
      <ul class="space-y-2 text-gray-600">
        <li>Philipsburg pier, Front Street duty-free and Great Bay</li>
        <li>Guilder (ANG) officially; US dollars widely used</li>
        <li>English common in tourism; Dutch official</li>
        <li>Maho Beach and Princess Juliana Airport sit on this side</li>
      </ul>
      <p class="mt-4"><a href="st-maarten-cruise-port-guide.html" class="text-ocean-600 font-semibold">Port guide →</a> · <a href="maho-beach-plane-spotting-tours.html" class="text-ocean-600 font-semibold">Maho →</a></p>
    </div>
    <div class="bg-white rounded-3xl p-6 border border-sxm-100">
      <div class="card-media rounded-2xl overflow-hidden aspect-[16/10] mb-4">
        <img src="{ORIENT_IMG}" alt="{ORIENT_ALT}" width="600" height="375" loading="lazy" decoding="async" />
      </div>
      <h3 class="font-display font-bold text-lg mb-3">French St Martin</h3>
      <ul class="space-y-2 text-gray-600">
        <li>Marigot waterfront, markets and café culture</li>
        <li>Euros common; US dollars still accepted in tourist zones</li>
        <li>French language; English still widespread at beaches</li>
        <li>Orient Beach is the signature French-side swim day</li>
      </ul>
      <p class="mt-4"><a href="orient-beach-excursions.html" class="text-ocean-600 font-semibold">Orient Beach →</a> · <a href="dutch-and-french-side-tours.html" class="text-ocean-600 font-semibold">Combo tours →</a></p>
    </div>
  </div>
</div></section>
<section class="py-12 bg-white"><div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="grid lg:grid-cols-2 gap-10 items-center mb-12">
    <div>
      <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Seeing both on one ship day</h2>
      <p class="text-gray-600 leading-relaxed mb-3">Island sightseeing vans routinely cover Philipsburg, Marigot and viewpoints in a single loop. Road times vary with traffic — especially mid-day on multi-ship calls — so leave your own return buffer.</p>
      <p class="text-gray-600 leading-relaxed">Want beach time instead of monuments? Compare <a href="maho-vs-orient-bay.html" class="text-ocean-600 font-semibold">Maho vs Orient</a> and skip the full dual-nation circuit.</p>
      <p class="mt-4"><a href="st-maarten-island-tours.html" class="text-ocean-600 font-semibold">Island tours →</a> · <a href="ship-schedule/" class="text-ocean-600 font-semibold">Ship schedule →</a></p>
    </div>
    <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
      <img src="{DUTCH_FRENCH_IMG}" alt="{DUTCH_FRENCH_ALT}" width="600" height="450" loading="lazy" decoding="async" />
    </div>
  </div>
  <div class="mt-4 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>
{concierge_panel()}"""


def content_maho_vs_orient() -> str:
    snap = snapshot(
        best_for="Choosing plane-spotting energy vs French-side beach day",
        activity_level="Both low–moderate; Maho shorter, Orient longer",
        popular="Maho Beach vs Orient Beach",
    )
    return f"""<section class="pt-8 pb-6 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <p class="text-gray-600 leading-relaxed mb-4">On a Philipsburg call, many guests choose between a <strong>Maho Beach runway stop</strong> and an <strong>Orient Beach French-side day</strong>. Both are excellent. They spend your hours differently.</p>
  <p class="text-gray-600 leading-relaxed">Maho is iconic when aircraft are moving — but flight activity varies with airline schedules, weather and airport operations. Do not over-promise a specific landing time. Orient maximises swim, shade and lunch pacing.</p>
</div></section>
<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
<section class="py-12 bg-sand-50"><div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-2xl font-display font-bold text-gray-900 text-center mb-8">Maho Beach vs Orient Bay</h2>
  <div class="grid md:grid-cols-2 gap-6 text-sm">
    <div class="bg-white rounded-3xl p-6 border border-sxm-100">
      <div class="card-media rounded-2xl overflow-hidden aspect-[16/10] mb-4">
        <img src="{MAHO_IMG}" alt="{MAHO_ALT}" width="600" height="375" loading="lazy" decoding="async" />
      </div>
      <h3 class="font-display font-bold text-lg mb-3">Maho — planes &amp; short visit</h3>
      <ul class="space-y-2 text-gray-600">
        <li>Runway-end beach west of Philipsburg when jets are active</li>
        <li>Better as a focused stop than an all-day lounger plan</li>
        <li>Stay behind barriers; jet blast on takeoff is dangerous</li>
        <li>Treat aircraft sightings as possible, not scheduled entertainment</li>
      </ul>
      <p class="mt-4"><a href="maho-beach-plane-spotting-tours.html" class="text-ocean-600 font-semibold">Maho Beach →</a></p>
    </div>
    <div class="bg-white rounded-3xl p-6 border border-sxm-100">
      <div class="card-media rounded-2xl overflow-hidden aspect-[16/10] mb-4">
        <img src="{ORIENT_IMG}" alt="{ORIENT_ALT}" width="600" height="375" loading="lazy" decoding="async" />
      </div>
      <h3 class="font-display font-bold text-lg mb-3">Orient — beach day</h3>
      <ul class="space-y-2 text-gray-600">
        <li>French-side clubs, turquoise water and longer sand time</li>
        <li>Transfer times vary with traffic — often longer than Maho</li>
        <li>Better when swimming and lunch matter more than runway photos</li>
        <li>Confirm chair inclusions and return window with the operator</li>
      </ul>
      <p class="mt-4"><a href="orient-beach-excursions.html" class="text-ocean-600 font-semibold">Orient Beach →</a></p>
    </div>
  </div>
</div></section>
<section class="py-12 bg-white"><div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="grid lg:grid-cols-2 gap-10 items-center mb-12">
    <div>
      <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Mixing both on a long call</h2>
      <p class="text-gray-600 leading-relaxed mb-3">On a longer Philipsburg day, some guests do a shorter Maho stop and later Orient or a catamaran — two well-paced blocks beat three rushed attractions.</p>
      <p class="text-gray-600 leading-relaxed">Check your ship’s all-aboard time and build your own buffer. Road times between west and east are variable, not exact.</p>
      <p class="mt-4"><a href="one-day-in-st-maarten.html" class="text-ocean-600 font-semibold">One-day paths →</a> · <a href="ship-schedule/" class="text-ocean-600 font-semibold">Ship schedule →</a></p>
    </div>
    <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
      <img src="{ONE_DAY_IMG}" alt="{ONE_DAY_ALT}" width="600" height="450" loading="lazy" decoding="async" />
    </div>
  </div>
  <div class="mt-4 max-w-3xl mx-auto">{internal_links()}</div>
</div></section>
{concierge_panel()}"""


def content_about() -> str:
    return f"""<section class="pt-10 pb-16 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">About St Maarten Shore Excursion</h2>
  <p class="text-gray-600 leading-relaxed mb-4">St Maarten / Saint Martin is one island shared by two nations. Cruise guests usually land on the Dutch side at Philipsburg, then choose Front Street shopping, Maho’s runway theatre when planes are moving, French-side Orient sand, or a dual-nation circuit — traffic and timing can stretch the clock.</p>
  <p class="text-gray-600 leading-relaxed mb-4">We write for that passenger decision set without inventing border drama or guaranteed aircraft flyovers. We are not a cruise line, ticket marketplace or port authority.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Ship schedules here are synced from the Caribbean Shore Excursions authority import for St Maarten only. Confirm final timings with your cruise line.</p>
  <p class="text-gray-600 leading-relaxed mb-8">Network context: <a href="https://caribbeanshoreexcursion.com/" class="text-ocean-600 font-medium">Caribbean Shore Excursions</a>. St Maarten detail lives here.</p>
  {internal_links()}
</div></section>
{concierge_panel()}"""


def content_contact() -> str:
    return f"""<section class="pt-10 pb-8 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Contact</h2>
  <p class="text-gray-600 leading-relaxed mb-4">If you want help narrowing a St Maarten port day, include your ship name, call date, and whether you prefer Maho plane spotting, Orient Beach, a dual-nation island circuit or a catamaran sail.</p>
  <p class="text-gray-600 leading-relaxed mb-6">Email <a class="text-ocean-600 font-semibold" href="mailto:hello@stmaartenshoreexcursion.com">hello@stmaartenshoreexcursion.com</a>. Replies are handled when we can — this is a planning concierge, not a booking desk.</p>
  <ul class="space-y-2 text-sm text-gray-600 mb-8">
    <li><a class="text-ocean-600 font-semibold" href="ship-schedule/">Find your ship schedule</a></li>
    <li><a class="text-ocean-600 font-semibold" href="best-st-maarten-shore-excursions.html">Compare excursion types</a></li>
    <li><a class="text-ocean-600 font-semibold" href="st-maarten-cruise-port-guide.html">Read the port guide</a></li>
    <li><a class="text-ocean-600 font-semibold" href="maho-vs-orient-bay.html">Maho vs Orient decision</a></li>
  </ul>
  {internal_links()}
</div></section>
{concierge_panel()}"""


def content_privacy() -> str:
    return """<section class="pt-10 pb-16 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Privacy</h2>
  <p class="text-gray-600 leading-relaxed mb-4">This is a static planning website. In this phase we do not operate a booking engine, payment system, or passenger account database.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Messages sent to hello@stmaartenshoreexcursion.com are used only to respond about St Maarten port-day planning. We will not sell contact details.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Standard web server and CDN logs may record technical request data (such as IP address, user agent and requested URL) as part of delivering the site securely. We do not add analytics trackers in this build.</p>
  <p class="text-gray-600 leading-relaxed">If our contact or tooling practices change, this page will be updated before those features go live.</p>
</div></section>"""


def content_terms() -> str:
    return """<section class="pt-10 pb-16 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Terms of use</h2>
  <p class="text-gray-600 leading-relaxed mb-4">Content on St Maarten Shore Excursion is provided for general information and planning. It is not a contract of carriage, not travel insurance, and not a guarantee of excursion availability, aircraft sightings, weather or on-time return to your ship.</p>
  <p class="text-gray-600 leading-relaxed mb-4">Cruise schedules, pier operations and excursion details can change. Confirm final arrangements with your cruise line and any operator you choose.</p>
  <p class="text-gray-600 leading-relaxed mb-4">We are independent of cruise lines and of St Maarten / Saint Martin port operators. Mentions of beaches, airports or landmarks are for orientation and do not imply partnership unless we say so explicitly.</p>
  <p class="text-gray-600 leading-relaxed">You are responsible for leaving enough time to reboard, for following local rules near Maho Beach, and for checking any medical or activity requirements before water or adventure activities.</p>
</div></section>"""


def content_methodology() -> str:
    return f"""<section class="pt-10 pb-16 bg-white"><div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">How we assess St Maarten excursions</h2>
  <p class="text-gray-600 leading-relaxed mb-4">We judge options the way a cruise passenger has to: against the length of the Philipsburg call, pier logistics, variable road times, and how much return buffer you need before all aboard.</p>
  <div class="space-y-4 text-sm text-gray-600 mb-8">
    <div class="bg-sand-50 rounded-2xl p-5 border border-sxm-100"><h3 class="font-display font-bold text-gray-900 mb-2">Cruise timing first</h3><p>A brilliant full-island mash-up is the wrong answer on a short call. We favour options that leave a realistic return window.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-5 border border-ocean-100"><h3 class="font-display font-bold text-gray-900 mb-2">Decision clarity</h3><p>Dutch versus French geography, Maho plane spotting versus Orient Beach — passengers need honest trade-offs, not marketplace noise.</p></div>
    <div class="bg-sand-50 rounded-2xl p-5 border border-sxm-100"><h3 class="font-display font-bold text-gray-900 mb-2">No invented proof</h3><p>We do not invent star ratings, review counts, “places left” or fabricated prices. Trust comes from clear planning language and transparent limits — including that aircraft timing at Maho is not promised.</p></div>
    <div class="bg-ocean-50 rounded-2xl p-5 border border-ocean-100"><h3 class="font-display font-bold text-gray-900 mb-2">Schedule integrity</h3><p>Call lists are generated from the Caribbean authority import for St Maarten, then checked for count and record-level match before pages are built.</p></div>
  </div>
  {internal_links()}
</div></section>
{concierge_panel()}"""


NEW_PAGES = [
    dict(
        file="dutch-side-vs-french-side.html",
        title="Dutch Side vs French Side St Maarten | Cruise Decision",
        description="Compare Dutch St Maarten and French St Martin for cruise passengers from Philipsburg — currency, language and beach mood without inventing border drama.",
        keywords="Dutch vs French St Maarten, Philipsburg vs Marigot, St Maarten cruise decision",
        path="dutch-side-vs-french-side.html",
        data_page="excursions",
        hero="partials/hero-dutch-vs-french.html",
        content="dutch-side-vs-french-side.html",
        preload=DUTCH_FRENCH_IMG,
    ),
    dict(
        file="maho-vs-orient-bay.html",
        title="Maho Beach vs Orient Bay | St Maarten Cruise Decision",
        description="Compare Maho Beach plane spotting with Orient Bay beach day on a St Maarten cruise call — honest trade-offs without over-promising aircraft timing.",
        keywords="Maho vs Orient Beach, St Maarten beach decision, Philipsburg cruise Maho Orient",
        path="maho-vs-orient-bay.html",
        data_page="excursions",
        hero="partials/hero-maho-vs-orient.html",
        content="maho-vs-orient-bay.html",
        preload=MAHO_IMG,
    ),
    dict(
        file="about.html",
        title="About St Maarten Shore Excursion | Independent Port Planning",
        description="About St Maarten Shore Excursion — independent planning guidance for cruise passengers calling at Philipsburg.",
        keywords="about St Maarten Shore Excursion, St Maarten cruise planning",
        path="about.html",
        data_page="contact",
        hero="partials/hero-port-guide.html",
        content="about.html",
        preload=PORT_IMG,
    ),
    dict(
        file="contact.html",
        title="Contact St Maarten Shore Excursion | Concierge",
        description="Contact the St Maarten shore excursion concierge at hello@stmaartenshoreexcursion.com for Philipsburg port-day planning help.",
        keywords="contact St Maarten Shore Excursion, St Maarten cruise concierge",
        path="contact.html",
        data_page="contact",
        hero="partials/hero-port-guide.html",
        content="contact.html",
        preload=PORT_IMG,
    ),
    dict(
        file="privacy.html",
        title="Privacy | St Maarten Shore Excursion",
        description="Privacy policy for St Maarten Shore Excursion — static planning site practices.",
        keywords="privacy St Maarten Shore Excursion",
        path="privacy.html",
        data_page="contact",
        hero="partials/hero-port-guide.html",
        content="privacy.html",
        preload=PORT_IMG,
    ),
    dict(
        file="terms.html",
        title="Terms of Use | St Maarten Shore Excursion",
        description="Terms of use for St Maarten Shore Excursion planning content.",
        keywords="terms St Maarten Shore Excursion",
        path="terms.html",
        data_page="contact",
        hero="partials/hero-port-guide.html",
        content="terms.html",
        preload=PORT_IMG,
    ),
    dict(
        file="methodology.html",
        title="How We Assess St Maarten Excursions | Methodology",
        description="How St Maarten Shore Excursion assesses cruise excursion options — timing, honest claims and schedule integrity.",
        keywords="St Maarten excursion methodology, how we choose St Maarten tours",
        path="methodology.html",
        data_page="contact",
        hero="partials/hero-port-guide.html",
        content="methodology.html",
        preload=PORT_IMG,
    ),
]


def merge_sitemap(extra: list[tuple[str, str, str]]) -> None:
    sitemap_path = ROOT / "sitemap.xml"
    existing: list[tuple[str, str, str]] = []
    if sitemap_path.exists():
        text = sitemap_path.read_text(encoding="utf-8")
        locs = re.findall(r"<loc>(.*?)</loc>", text)
        freqs = re.findall(r"<changefreq>(.*?)</changefreq>", text)
        pris = re.findall(r"<priority>(.*?)</priority>", text)
        for i, loc in enumerate(locs):
            path = loc.replace(DOMAIN + "/", "").replace(DOMAIN, "")
            if path == "/":
                path = ""
            freq = freqs[i] if i < len(freqs) else "monthly"
            pri = pris[i] if i < len(pris) else "0.5"
            existing.append((path, pri, freq))

    by_path = {p: (pri, freq) for p, pri, freq in existing}
    for path, pri, freq in extra:
        by_path[path] = (pri, freq)

    frag = ROOT / "data" / "generated" / "schedule-sitemap.json"
    if frag.exists():
        try:
            for path, pri, freq in json.loads(frag.read_text(encoding="utf-8")):
                by_path[path] = (pri, freq)
        except json.JSONDecodeError:
            pass

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for path, (pri, freq) in sorted(by_path.items(), key=lambda x: (x[0] != "", x[0])):
        url = f"{DOMAIN}/{path}" if path else f"{DOMAIN}/"
        lines += [
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{DATE}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{pri}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    write("sitemap.xml", "\n".join(lines) + "\n")


def write_package_json() -> None:
    write(
        "package.json",
        """{
  "name": "st-maarten-shore-excursion",
  "private": true,
  "scripts": {
    "sync:schedules": "node scripts/sync-schedules.mjs",
    "qa:schedules": "node scripts/qa-schedules.mjs",
    "build": "python3.14 scripts/build-st-maarten-site.py && python3.14 scripts/world2_extend_st_maarten.py && python3.14 scripts/generate_schedule_pages.py",
    "build:all": "npm run sync:schedules && npm run qa:schedules && npm run build",
    "images": "python3.14 scripts/fetch-st-maarten-images.py",
    "deploy": "wrangler deploy",
    "preview": "python3.14 -m http.server 8903"
  },
  "devDependencies": {
    "wrangler": "^4.94.0"
  }
}
""",
    )


def ensure_decision_css() -> None:
    css_path = ROOT / "css" / "site.css"
    css = css_path.read_text(encoding="utf-8")
    if ".decision-grid" not in css:
        css += """
.section-label {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: #0d9488;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 0.75rem;
}
.decision-grid {
  display: grid;
  gap: 1rem;
}
@media (min-width: 640px) {
  .decision-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 1024px) {
  .decision-grid { grid-template-columns: repeat(3, 1fr); }
}
.decision-card {
  background: #fff;
  border: 1px solid #fce7f3;
  border-radius: 1.25rem;
  padding: 1.25rem 1.35rem;
}
.decision-card h3 {
  font-size: 1.05rem;
  margin-bottom: 0.4rem;
}
.decision-card p {
  font-size: 0.875rem;
  color: #4b5563;
  line-height: 1.55;
  margin-bottom: 0.75rem;
}
"""
        css_path.write_text(css, encoding="utf-8")
        print("  updated css/site.css with decision styles")


def main() -> None:
    print("World 2.0 extending St Maarten Shore Excursion…")
    ensure_decision_css()
    write_nav()
    write_footer()
    write("partials/hero-home.html", hero_home())
    write(
        "partials/hero-dutch-vs-french.html",
        _hero_inner(
            "Two nations · One island",
            f"Dutch Side vs<br/><span class=\"{ACCENT}\">French Side</span>",
            "Philipsburg duty-free versus Marigot and Orient — geography that helps cruise guests choose without inventing border theatre.",
            DUTCH_FRENCH_IMG,
            DUTCH_FRENCH_ALT,
            breadcrumb="Dutch vs French",
        ),
    )
    write(
        "partials/hero-maho-vs-orient.html",
        _hero_inner(
            "Philipsburg decision",
            f"Maho Beach vs<br/><span class=\"{ACCENT}\">Orient Bay</span>",
            "Plane-spotting energy versus a French-side beach day — honest trade-offs for a St Maarten cruise call.",
            MAHO_IMG,
            MAHO_ALT,
            breadcrumb="Maho vs Orient",
        ),
    )

    write("content/home.html", content_home())
    write("content/st-maarten-cruise-port-guide.html", content_port())
    write("content/dutch-side-vs-french-side.html", content_dutch_vs_french())
    write("content/maho-vs-orient-bay.html", content_maho_vs_orient())
    write("content/about.html", content_about())
    write("content/contact.html", content_contact())
    write("content/privacy.html", content_privacy())
    write("content/terms.html", content_terms())
    write("content/methodology.html", content_methodology())

    soft_all_content()

    for p in NEW_PAGES:
        write(
            p["file"],
            page_shell(
                title=p["title"],
                description=p["description"],
                keywords=p["keywords"],
                canonical_path=p["path"],
                data_page=p["data_page"],
                hero=p["hero"],
                content=p["content"],
                preload=p.get("preload", HOME_HERO),
            ),
        )

    write(
        "index.html",
        page_shell(
            title=f"{SITE} | Philipsburg — Two Nations, Maho &amp; Orient",
            description="Independent St Maarten shore excursion planning from Philipsburg — Maho Beach, Orient Bay, Dutch and French sides, catamaran sails and island circuits for cruise passengers.",
            keywords="St Maarten shore excursions, Philipsburg cruise port, Maho Beach, Orient Beach, Dutch French St Maarten",
            canonical_path="",
            data_page="home",
            hero="partials/hero-home.html",
            content="home.html",
            schema={
                "@context": "https://schema.org",
                "@type": "WebSite",
                "name": SITE,
                "url": f"{DOMAIN}/",
                "description": "Planning guide for St Maarten cruise shore excursions from Philipsburg",
            },
        ),
    )

    extra = [
        ("dutch-side-vs-french-side.html", "0.8", "monthly"),
        ("maho-vs-orient-bay.html", "0.8", "monthly"),
        ("about.html", "0.5", "yearly"),
        ("contact.html", "0.5", "yearly"),
        ("privacy.html", "0.3", "yearly"),
        ("terms.html", "0.3", "yearly"),
        ("methodology.html", "0.5", "yearly"),
    ]
    merge_sitemap(extra)
    write_package_json()
    print("World 2.0 extend done.")


if __name__ == "__main__":
    main()
