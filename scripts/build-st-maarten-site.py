#!/usr/bin/env python3
"""Generate St Maarten Shore Excursion static site files."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://stmaartenshoreexcursion.com"
SITE = "St Maarten Shore Excursion"
DATE = "2026-09-04"
FONTS = (
    "https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700"
    "&family=Source+Sans+3:wght@400;500;600;700&display=swap"
)
HERO_GRADIENT = (
    "linear-gradient(135deg, rgba(79, 70, 229, 0.75) 0%, "
    "rgba(192, 38, 211, 0.65) 50%, rgba(49, 46, 129, 0.55) 100%)"
)
ACCENT = "text-fuchsia-300"

HOME_HERO = "images/hero-st-maarten.png"
HOME_HERO_ALT = "Aerial view of Philipsburg bay and turquoise waters in St Maarten"
BEST_IMG = "images/best-st-maarten-excursions.png"
BEST_ALT = "Best St Maarten shore excursions including beaches sailing and island tours"
PORT_IMG = "images/st-maarten-cruise-port.png"
PORT_ALT = "Cruise ships visiting Philipsburg St Maarten cruise port"
ONE_DAY_IMG = "images/one-day-st-maarten.png"
ONE_DAY_ALT = "One day in St Maarten for cruise passengers"
MAHO_IMG = "images/maho-beach-hero.png"
MAHO_ALT = "Aircraft landing over Maho Beach in St Maarten"
ORIENT_IMG = "images/orient-beach-hero.png"
ORIENT_ALT = "Orient Beach in St Martin and St Maarten"
SNORKEL_IMG = "images/st-maarten-snorkelling.png"
SNORKEL_ALT = "Snorkelling excursion in St Maarten Caribbean waters"
ISLAND_IMG = "images/st-maarten-island-tours.png"
ISLAND_ALT = "Island sightseeing tour in St Maarten"
ATV_IMG = "images/st-maarten-atv-buggy.png"
ATV_ALT = "ATV excursion exploring St Maarten"
DUTCH_FRENCH_IMG = "images/dutch-french-side.png"
DUTCH_FRENCH_ALT = "Tour of the Dutch and French sides of St Maarten"
CATAMARAN_IMG = "images/catamaran-sailing.png"
CATAMARAN_ALT = "Catamaran sailing excursion in St Maarten"
PRIVATE_IMG = "images/st-maarten-private-tours.png"
PRIVATE_ALT = "Private St Maarten shore excursion"
FAMILY_IMG = "images/st-maarten-family.png"
FAMILY_ALT = "Family friendly shore excursion in St Maarten"
BEACHES_IMG = "images/st-maarten-beaches.png"
BEACHES_ALT = "Best beaches in St Maarten for cruise passengers"
FAQ_IMG = "images/st-maarten-faq.png"
FAQ_ALT = "Cruise passengers exploring Philipsburg St Maarten"
INTRO_IMG = "images/st-maarten-intro.png"
INTRO_ALT = (
    "St Maarten island sightseeing with Maho Beach aircraft landings, "
    "Orient Beach and Philipsburg cruise port"
)


def page_shell(
    *,
    title: str,
    description: str,
    keywords: str,
    canonical_path: str,
    data_page: str,
    hero: str,
    content: str,
    preload: str = HOME_HERO,
    schema: dict | None = None,
    trust: bool = True,
) -> str:
    canon = f"{DOMAIN}/" if not canonical_path else f"{DOMAIN}/{canonical_path}"
    schema_block = ""
    if schema:
        schema_block = (
            f'  <script type="application/ld+json">\n'
            f"{json.dumps(schema, indent=2)}\n"
            f"  </script>\n"
        )
    trust_attr = '\n  data-trust-strip="partials/trust-strip.html"' if trust else ""
    content_file = content if content.startswith("content/") else f"content/{content}"
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="keywords" content="{keywords}" />
  <link rel="canonical" href="{canon}" />
  <link rel="preload" as="image" href="{preload}" fetchpriority="high" />

  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{DOMAIN}/{preload}" />
  <meta property="og:site_name" content="{SITE}" />
  <meta name="twitter:card" content="summary_large_image" />

{schema_block}
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="js/tailwind-config.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{FONTS}" rel="stylesheet" />
  <link rel="stylesheet" href="css/site.css" />
</head>
<body
  class="bg-white text-gray-800 antialiased"
  data-page="{data_page}"
  data-base=""
  data-hero="{hero}"
  data-content="{content_file}"{trust_attr}
>

  <div id="site-nav"></div>
  <div id="page-hero"></div>
  <div id="page-trust-strip"></div>
  <main id="page-content"></main>
  <div id="site-footer"></div>

  <script src="js/site.js"></script>
</body>
</html>
"""


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"  wrote {path}")


def cruise_snapshot(
    *,
    time_in_port: str,
    best_for: str,
    activity_level: str,
    family: str,
    return_ship: str,
    popular: str,
) -> str:
    return f"""<aside class="cruise-snapshot mb-10 px-4 sm:px-0" aria-label="Cruise passenger snapshot">
  <h3 class="font-display font-bold text-lg text-gray-900 mb-4">Cruise Passenger Snapshot</h3>
  <dl class="cruise-snapshot__grid">
    <div class="cruise-snapshot__item"><dt>Typical Time In Port</dt><dd>{time_in_port}</dd></div>
    <div class="cruise-snapshot__item"><dt>Best For</dt><dd>{best_for}</dd></div>
    <div class="cruise-snapshot__item"><dt>Activity Level</dt><dd>{activity_level}</dd></div>
    <div class="cruise-snapshot__item"><dt>Family Friendly</dt><dd>{family}</dd></div>
    <div class="cruise-snapshot__item"><dt>Return To Ship Friendly</dt><dd>{return_ship}</dd></div>
    <div class="cruise-snapshot__item"><dt>Popular Excursion Types</dt><dd>{popular}</dd></div>
  </dl>
</aside>"""


def _hero_wave() -> str:
    return '<div class="absolute bottom-0 left-0 right-0"><svg viewBox="0 0 1440 48" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" class="site-hero__wave" aria-hidden="true"><path d="M0 24 C360 48 1080 0 1440 24 L1440 48 L0 48 Z" fill="white"/></svg></div>'


def _hero_inner(
    eyebrow: str,
    title: str,
    lead: str,
    image: str,
    aria: str,
    breadcrumb: str = "",
    cta: tuple[str, str] | None = None,
    tags: list[str] | None = None,
) -> str:
    bc = ""
    if breadcrumb:
        bc = f"""<nav class="site-hero__breadcrumb flex items-center gap-2 mb-4 text-xs text-white/60" aria-label="Breadcrumb">
        <a href="index.html" class="hover:text-white transition-colors">Home</a>
        <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
        <span class="text-white/80">{breadcrumb}</span>
      </nav>"""
    cta_html = ""
    if cta:
        cta_html = f'<a href="{cta[0]}" class="btn-ocean inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">{cta[1]}</a>'
    tags_html = ""
    if tags:
        tags_html = '<div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">' + "".join(
            f'<span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">{t}</span>'
            for t in tags
        ) + "</div>"
    return f"""<section class="site-hero">
  <div class="absolute inset-0 hero-bg-custom" style="background-image: {HERO_GRADIENT}, url('{image}');" role="img" aria-label="{aria}"></div>
  <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl">
      {bc}
      <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
        <span class="w-2 h-2 rounded-full bg-fuchsia-400 animate-pulse"></span>
        <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">{eyebrow}</span>
      </div>
      <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">{title}</h1>
      <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">{lead}</p>
      <div class="site-hero__actions flex flex-col sm:flex-row gap-3">{cta_html}</div>
      {tags_html}
    </div>
  </div>
  {_hero_wave()}
</section>"""


def _internal_links() -> str:
    return """<nav class="mt-10 pt-8 border-t border-gray-100" aria-label="Related St Maarten guides">
  <p class="text-sm font-semibold text-gray-900 mb-3">Plan your port day</p>
  <div class="flex flex-wrap gap-3 text-sm">
    <a href="st-maarten-cruise-port-guide.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Port Guide</a>
    <span class="text-gray-300">·</span>
    <a href="best-st-maarten-shore-excursions.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Best Excursions</a>
    <span class="text-gray-300">·</span>
    <a href="maho-beach-plane-spotting-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Maho Beach</a>
    <span class="text-gray-300">·</span>
    <a href="orient-beach-excursions.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Orient Beach</a>
    <span class="text-gray-300">·</span>
    <a href="st-maarten-snorkelling-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Snorkelling</a>
    <span class="text-gray-300">·</span>
    <a href="st-maarten-island-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Island Tours</a>
    <span class="text-gray-300">·</span>
    <a href="catamaran-sailing-excursions.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Catamaran Sailing</a>
    <span class="text-gray-300">·</span>
    <a href="st-maarten-private-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Private Tours</a>
    <span class="text-gray-300">·</span>
    <a href="st-maarten-faq.html" class="text-ocean-600 hover:text-ocean-800 font-medium">FAQ</a>
  </div>
</nav>"""


def _comparison_section() -> str:
    rows = [
        ("Maho Beach", "2–4 hrs", "Aircraft landings &amp; beach", "Low to moderate", "maho-beach-plane-spotting-tours.html"),
        ("Orient Beach", "4–6 hrs", "French-side beach club vibe", "Low — beach time", "orient-beach-excursions.html"),
        ("Snorkelling", "3–4 hrs", "Reef &amp; turquoise bays", "Moderate — swim", "st-maarten-snorkelling-tours.html"),
        ("Island Tour", "4–5 hrs", "Dutch &amp; French highlights", "Low to moderate", "st-maarten-island-tours.html"),
        ("Catamaran Cruise", "3–5 hrs", "Sail, snorkel &amp; swim stops", "Low to moderate", "catamaran-sailing-excursions.html"),
        ("ATV Adventure", "3–4 hrs", "Hills, coastline &amp; viewpoints", "Moderate to high", "st-maarten-atv-buggy-tours.html"),
        ("Private Tour", "4–6 hrs", "Custom pacing for groups", "Varies", "st-maarten-private-tours.html"),
    ]
    body = ""
    for name, dur, best, activity, link in rows:
        body += f"""<tr class="border-b border-sxm-50 hover:bg-sand-50/80">
      <td class="py-4 pr-4 font-semibold text-gray-900"><a href="{link}" class="text-ocean-600 hover:text-ocean-800">{name}</a></td>
      <td class="py-4 px-3 text-gray-600">{dur}</td>
      <td class="py-4 px-3 text-gray-600">{best}</td>
      <td class="py-4 px-3 text-gray-600">{activity}</td>
      <td class="py-4 pl-3"><a href="{link}" class="text-fuchsia-600 font-medium text-xs whitespace-nowrap">Guide →</a></td>
    </tr>"""
    return f"""<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 text-center mb-4">Which St Maarten Excursion Is Right for Me?</h2>
  <p class="text-center text-gray-600 text-sm max-w-2xl mx-auto mb-10">Match your Philipsburg port day to Maho plane spotting, Orient Beach, catamaran sails, snorkel reefs or island drives — all timed for typical cruise schedules.</p>
  <div class="overflow-x-auto rounded-3xl border border-sxm-100 shadow-sm">
    <table class="w-full text-sm text-left min-w-[720px]">
      <thead class="bg-ocean-800 text-white">
        <tr>
          <th class="py-4 px-4 font-semibold rounded-tl-3xl">Excursion</th>
          <th class="py-4 px-3 font-semibold">Duration</th>
          <th class="py-4 px-3 font-semibold">Best For</th>
          <th class="py-4 px-3 font-semibold">Activity Level</th>
          <th class="py-4 px-4 font-semibold rounded-tr-3xl">Details</th>
        </tr>
      </thead>
      <tbody class="bg-white">{body}</tbody>
    </table>
  </div>
</div></section>"""


def _card_grid(cards: list[tuple]) -> str:
    items = []
    for img, alt, title, desc, link, label in cards:
        items.append(f"""<div class="card-hover bg-white rounded-3xl overflow-hidden shadow-md border border-sxm-50 flex flex-col">
      <div class="card-media h-44 relative overflow-hidden">
        <img src="{img}" alt="{alt}" width="600" height="352" loading="lazy" decoding="async" />
      </div>
      <div class="p-6 flex flex-col flex-1">
        <h3 class="text-lg font-display font-semibold text-gray-900 mb-2">{title}</h3>
        <p class="text-sm text-gray-500 leading-relaxed flex-1">{desc}</p>
        <a href="{link}" class="mt-5 btn-ocean inline-flex items-center justify-center text-white text-xs font-semibold px-5 py-2.5 rounded-full">{label}</a>
      </div>
    </div>""")
    return '<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">' + "".join(items) + "</div>"


def _snapshot_default(**overrides: str) -> str:
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


def _content_excursion_page(
    intro: str,
    bullets: list[str],
    snapshot_kwargs: dict,
    img: str,
    alt: str,
) -> str:
    bl = "".join(
        f'<li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span>{b}</li>'
        for b in bullets
    )
    snap = _snapshot_default(**snapshot_kwargs)
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
      <div>
        <p class="text-gray-600 leading-relaxed mb-6">{intro}</p>
        <ul class="space-y-3 mb-6">{bl}</ul>
      </div>
      <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
        <img src="{img}" alt="{alt}" width="600" height="450" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{_internal_links()}</div></section>"""


def _hero_home() -> str:
    return f"""  <section class="site-hero">
    <div class="absolute inset-0 hero-bg" style="background-image: {HERO_GRADIENT}, url('{HOME_HERO}');" role="img" aria-label="{HOME_HERO_ALT}"></div>
    <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl">
        <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
          <span class="w-2 h-2 rounded-full bg-fuchsia-400 animate-pulse"></span>
          <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">Philipsburg · Dutch &amp; French Island</span>
        </div>
        <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">
          St Maarten Shore<br/><span class="{ACCENT}">Excursions</span><br/>from the Cruise Port
        </h1>
        <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">
          Maho Beach plane spotting, Orient Beach, catamaran sailing, snorkelling and island sightseeing — the experiences cruise passengers book most in St Maarten.
        </p>
        <div class="site-hero__actions flex flex-col sm:flex-row gap-3">
          <a href="best-st-maarten-shore-excursions.html" class="btn-primary inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Compare Excursions</a>
          <a href="maho-beach-plane-spotting-tours.html" class="btn-outline inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm">Maho Beach</a>
        </div>
        <div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Maho Beach</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Aircraft Landings</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Caribbean Water</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Cruise Passengers</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Island Sightseeing</span>
        </div>
      </div>
    </div>
    {_hero_wave()}
  </section>"""


def _content_home() -> str:
    cards = _card_grid([
        (MAHO_IMG, MAHO_ALT, "Maho Beach", "Watch jets land metres overhead on Maho Beach — St Maarten's most famous shore experience.", "maho-beach-plane-spotting-tours.html", "Maho Beach"),
        (ORIENT_IMG, ORIENT_ALT, "Orient Beach", "French-side beach clubs, turquoise water and relaxed lunch stops east of Philipsburg.", "orient-beach-excursions.html", "Orient Beach"),
        (CATAMARAN_IMG, CATAMARAN_ALT, "Catamaran Sailing", "Sail the leeward coast with snorkel stops, open bar and swim time built for port schedules.", "catamaran-sailing-excursions.html", "Catamaran"),
        (ISLAND_IMG, ISLAND_ALT, "Island Tours", "Philipsburg, Marigot, viewpoints and both sides of the island in one air-conditioned loop.", "st-maarten-island-tours.html", "Island Tour"),
    ])
    snap = _snapshot_default()
    return f"""<section class="pt-8 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
      <div>
        <div class="inline-flex items-center gap-2 text-ocean-600 text-xs font-semibold tracking-widest uppercase mb-3"><div class="w-8 h-px bg-ocean-400"></div>Philipsburg Cruise Port</div>
        <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-5">Why Cruise Guests<br/><span class="text-ocean-600">Choose St Maarten</span></h2>
        <p class="text-gray-600 leading-relaxed mb-5">St Maarten pairs Dutch-side duty-free shopping with French-side beaches — Maho Beach, Orient Beach, catamaran sails and dual-nation island tours fit a typical <strong>8–10 hour</strong> Philipsburg call.</p>
        <a href="best-st-maarten-shore-excursions.html" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">Browse All Excursions</a>
      </div>
      <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
        <img src="{INTRO_IMG}" alt="{INTRO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12"><h2 class="text-3xl font-display font-bold text-gray-900">Top St Maarten Experiences</h2></div>
      {cards}
    </div></section>
    {_comparison_section()}
    <section class="py-16 cta-gradient"><div class="max-w-3xl mx-auto px-4 text-center">
      <h2 class="text-3xl font-display font-bold text-white mb-4">Plan Your St Maarten Port Day</h2>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <a href="st-maarten-cruise-port-guide.html" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Port Guide</a>
        <a href="st-maarten-faq.html" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">FAQ</a>
      </div>
    </div></section>"""


def _content_best() -> str:
    cards = _card_grid([
        (MAHO_IMG, MAHO_ALT, "Maho Beach", "Plane-spotting transfers with timed returns for cruise schedules.", "maho-beach-plane-spotting-tours.html", "Maho Beach"),
        (ORIENT_IMG, ORIENT_ALT, "Orient Beach", "French-side beach day with transport and chair options.", "orient-beach-excursions.html", "Orient Beach"),
        (SNORKEL_IMG, SNORKEL_ALT, "Snorkelling", "Reef sites and clear bays with gear included.", "st-maarten-snorkelling-tours.html", "Snorkel"),
        (PRIVATE_IMG, PRIVATE_ALT, "Private Tours", "Custom island routes for your group.", "st-maarten-private-tours.html", "Private"),
    ])
    snap = _snapshot_default(best_for="Comparing all excursion types", popular="See comparison table below")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Best St Maarten Shore Excursions</h2>
      <p class="text-gray-600 leading-relaxed text-sm">Operators meet at <strong>Philipsburg cruise terminals</strong> and typically plan a return window before all aboard — confirm details and build your own buffer.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    {_comparison_section()}
    <section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Excursion Guides</h2>
      {cards}
      <div class="mt-12 max-w-3xl mx-auto">{_internal_links()}</div>
    </div></section>"""


def _content_port() -> str:
    snap = _snapshot_default(
        activity_level="Low at terminal; moderate on tours",
        popular="Walk-on port, taxis, tour pickups",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <p class="text-gray-600 leading-relaxed text-sm">Ships dock at <strong>Philipsburg</strong> on the Dutch side — waterfront shopping, beaches and tour pickups are minutes away on a typical <strong>8–10 hour</strong> call.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Where Ships Arrive</h2>
      <div class="info-image rounded-3xl aspect-[21/9] shadow-xl overflow-hidden mb-8 max-w-5xl mx-auto">
        <img src="{PORT_IMG}" alt="{PORT_ALT}" width="1200" height="514" loading="lazy" decoding="async" />
      </div>
      <div class="grid lg:grid-cols-2 gap-6 text-sm">
        <div class="bg-white rounded-3xl p-6 border border-sxm-100"><h3 class="font-display font-bold text-lg mb-2">Philipsburg Terminals</h3><p class="text-gray-600">Dr. A.C. Wathey Cruise &amp; Cargo Facilities place you steps from Front Street duty-free shops, taxis and shore-excursion desks.</p></div>
        <div class="bg-white rounded-3xl p-6 border border-sxm-100"><h3 class="font-display font-bold text-lg mb-2">Getting To Beaches</h3><p class="text-gray-600">Maho Beach is typically about 15–25 minutes west by road — traffic varies. Orient Beach on the French side is often 25–45 minutes depending on congestion and your pickup point.</p></div>
      </div>
    </div></section>
    <section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4">
      <div class="grid sm:grid-cols-3 gap-6 text-sm">
        <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Currency</strong><p class="mt-2 text-gray-600">Netherlands Antillean guilder (ANG) on Dutch side; euros in French St Martin. <strong>US dollars</strong> widely accepted.</p></div>
        <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Language</strong><p class="mt-2 text-gray-600">Dutch and English on Dutch side; French in Marigot. English common in tourism and at the port.</p></div>
        <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Getting Around</strong><p class="mt-2 text-gray-600">Taxis at the pier; island tours and catamarans include port or marina pickup.</p></div>
      </div>
      <p class="text-center mt-8"><a href="one-day-in-st-maarten.html" class="text-ocean-600 font-semibold text-sm">One-day itinerary →</a></p>
      <div class="mt-10 max-w-3xl mx-auto">{_internal_links()}</div>
    </div></section>"""


def _content_one_day() -> str:
    snap = _snapshot_default(best_for="Maho morning + Orient or catamaran afternoon")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <p class="text-gray-600 text-sm">Sample timeline for an <strong>8–10 hour</strong> Philipsburg call. Adjust for your ship's actual times.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Classic St Maarten Port Day</h2>
      <ol class="space-y-4 text-sm">
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-sxm-100"><span class="font-bold text-ocean-600 shrink-0">08:00</span><div><strong>Depart pier</strong><p class="text-gray-600 mt-1">Meet Maho transfer or catamaran — morning slots beat afternoon crowds at Maho Beach.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-sxm-100"><span class="font-bold text-ocean-600 shrink-0">09:30</span><div><strong>Maho Beach or catamaran sail</strong><p class="text-gray-600 mt-1">Choose plane spotting or a half-day sail with snorkel — both are cruise favourites.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-sxm-100"><span class="font-bold text-ocean-600 shrink-0">13:00</span><div><strong>Orient Beach or island tour</strong><p class="text-gray-600 mt-1">French-side beach lunch or Dutch &amp; French highlights drive if energy allows.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-sxm-100"><span class="font-bold text-ocean-600 shrink-0">15:30</span><div><strong>Philipsburg stroll</strong><p class="text-gray-600 mt-1">Front Street shopping and waterfront cafés near the pier before return buffer.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-sxm-100"><span class="font-bold text-ocean-600 shrink-0">17:00</span><div><strong>Back at ship</strong><p class="text-gray-600 mt-1">Build your own buffer before published all-aboard — confirm times with your ship and operator.</p></div></li>
      </ol>
      <div class="mt-10">{_internal_links()}</div>
    </div></section>"""


def _content_maho() -> str:
    return _content_excursion_page(
        "Maho Beach sits at the end of Princess Juliana International Airport runway — when aircraft are moving, landings can pass metres overhead. Cruise excursions usually include transport, beach time and a timed return window to Philipsburg pier — confirm details with the operator. Aircraft movements vary by day; treat plane sightings as possible, not a guaranteed show.",
        [
            "Flight activity changes with airline schedules, weather and airport operations — do not plan the day around a specific landing time.",
            "Stay behind fence lines and follow crew safety briefings near the runway.",
            "Sunset Bar area offers food and drinks with runway views.",
            "Pair with afternoon Orient Beach only on long port calls, with your own return buffer.",
        ],
        dict(
            best_for="Plane spotters and bucket-list beach fans",
            activity_level="Low to moderate — beach and viewing",
            popular="Maho Beach transfers, plane-spotting tours",
        ),
        MAHO_IMG,
        MAHO_ALT,
    )


def _content_orient() -> str:
    return _content_excursion_page(
        "Orient Beach on the French side offers turquoise water, beach clubs and a relaxed lunch atmosphere east of Philipsburg. Organised excursions include transport, often chair rental and cruise-timed returns.",
        [
            "French-side beach clubs may charge for chairs — confirm inclusions.",
            "Calmer morning water suits families before afternoon breeze.",
            "Combine with Marigot market stop on island tour combos.",
            "Reef-safe sunscreen and shade recommended.",
        ],
        dict(
            best_for="Beach lovers wanting French-side atmosphere",
            activity_level="Low — swimming and walking",
            popular="Orient Beach transfers, beach club packages",
        ),
        ORIENT_IMG,
        ORIENT_ALT,
    )


def _content_snorkelling() -> str:
    return _content_excursion_page(
        "St Maarten's leeward coast and offshore cays offer clear snorkelling over reef patches, turtles and tropical fish. Tours supply masks, fins and guides; many catamaran sails include a snorkel stop on the same trip.",
        [
            "Half-day trips fit most 8–10 hour port schedules.",
            "Beginners welcome — flotation aids often available.",
            "Use reef-safe sunscreen or a rash guard.",
            "See our catamaran guide for sail-and-snorkel combos.",
        ],
        dict(
            best_for="Reef swimmers and wildlife watchers",
            activity_level="Moderate — boat and snorkelling",
            popular="Reef snorkel, catamaran snorkel sails",
        ),
        SNORKEL_IMG,
        SNORKEL_ALT,
    )


def _content_island() -> str:
    return _content_excursion_page(
        "Island sightseeing tours cover both nations on one island — Philipsburg shopping, Marigot waterfront, hilltop viewpoints and photo stops at the Dutch–French border. Air-conditioned vans suit guests who want culture between beach days.",
        [
            "4–5 hour loops fit standard port calls.",
            "Marigot market suits morning stops on French-side routes.",
            "Less physically demanding than ATV trails.",
            "Private options let you prioritise Marigot vs Maho Beach.",
        ],
        dict(
            best_for="Sightseers and first-time visitors",
            activity_level="Low to moderate — van and short walks",
            popular="Dual-nation drives, Philipsburg &amp; Marigot tours",
        ),
        ISLAND_IMG,
        ISLAND_ALT,
    )


def _content_atv() -> str:
    return _content_excursion_page(
        "ATV and buggy adventures explore St Maarten's hills, coastal lookouts and back roads — dusty trails, ridge viewpoints and hidden bays. Operators provide helmets, briefing and cruise-timed returns from Philipsburg pickups.",
        [
            "Drivers typically need a valid licence — check operator rules.",
            "Wear closed-toe shoes, sunglasses and dust-friendly clothing.",
            "Not ideal for guests with serious back or mobility limits.",
            "Book morning slots to leave afternoon beach time.",
        ],
        dict(
            best_for="Adventure seekers and active groups",
            activity_level="Moderate to high — off-road driving",
            popular="ATV coastline tours, buggy hill rides",
        ),
        ATV_IMG,
        ATV_ALT,
    )


def _content_dutch_french() -> str:
    return _content_excursion_page(
        "Dutch and French side tours highlight St Maarten's split personality — duty-free Philipsburg, colourful Marigot, border monuments and beaches on both coasts. Guides explain currency, language and everyday differences as you move between sides. For ordinary day movement the land border is typically open and low-friction — do not invent passport drama for a standard cruise excursion.",
        [
            "Day sightseeing between Dutch St Maarten and French St Martin is usually straightforward for cruise visitors; carry ID if your operator asks.",
            "Marigot offers French cafés and market shopping.",
            "Philipsburg suits quick pier-side shopping on return.",
            "Often combined with Maho or Orient Beach photo stops.",
        ],
        dict(
            best_for="Culture curious and first-time visitors",
            activity_level="Low to moderate — van touring",
            popular="Dutch &amp; French combo drives, border tours",
        ),
        DUTCH_FRENCH_IMG,
        DUTCH_FRENCH_ALT,
    )


def _content_catamaran() -> str:
    return _content_excursion_page(
        "Catamaran sailing excursions cruise the leeward coast with trade-wind sailing, snorkel stops, open bars and swim time at calm bays. Half-day and sunset departures are built around Philipsburg cruise schedules.",
        [
            "Morning sails return in time for afternoon island touring.",
            "Sunset cruises suit late-departure ship days.",
            "Snorkel gear usually included — bring a towel from the ship.",
            "Motion-sensitive guests should take medication early.",
        ],
        dict(
            best_for="Sail lovers and relaxed groups",
            activity_level="Low to moderate — boat and optional swim",
            popular="Half-day catamarans, snorkel sails",
        ),
        CATAMARAN_IMG,
        CATAMARAN_ALT,
    )


def _content_private() -> str:
    return _content_excursion_page(
        "Private SUVs, vans and charter boats let your group set the pace — Maho Beach first, Orient lunch, snorkel bay and Marigot market in one custom loop. Drivers serving cruise guests usually plan around all-aboard — still confirm return timing in writing.",
        [
            "Split cost across families to rival per-person coach pricing.",
            "Share priorities when booking — routes are flexible.",
            "Ideal for mixed mobility within one group.",
            "Confirm return time in writing before payment and build your own buffer.",
        ],
        dict(
            best_for="Groups wanting custom pacing",
            activity_level="Low to moderate — varies by itinerary",
            popular="Private island tours, custom snorkel charters",
        ),
        PRIVATE_IMG,
        PRIVATE_ALT,
    )


def _content_family() -> str:
    return _content_excursion_page(
        "Family excursions in St Maarten favour calm Orient Beach time, gentle catamaran sails, short island drives and supervised Maho Beach viewing with clear safety rules. Two well-paced stops beat three rushed attractions with children.",
        [
            "Orient Beach suits school-age kids with shade breaks.",
            "ATV tours publish age and height rules — verify when booking.",
            "Private vans simplify nap timing and snack stops.",
            "Catamaran operators often offer junior snorkel gear.",
        ],
        dict(
            best_for="Kids, parents and multi-generational groups",
            family="Excellent with age-appropriate tour choice",
            popular="Beach transfers, family island tours",
        ),
        FAMILY_IMG,
        FAMILY_ALT,
    )


def _content_beaches() -> str:
    snap = _snapshot_default(
        best_for="Choosing Maho vs Orient vs Great Bay",
        popular="Maho Beach, Orient Beach, Great Bay",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
      <div>
        <p class="text-gray-600 leading-relaxed mb-6">St Maarten beaches range from runway plane spotting to French-side clubs — <strong>Maho Beach</strong> for aircraft overhead, <strong>Orient Beach</strong> for turquoise swim and lunch, and <strong>Great Bay</strong> steps from Philipsburg pier on short port days.</p>
        <ul class="space-y-3 mb-6">
          <li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span><strong>Maho Beach</strong> — jet landings, Sunset Bar, cruise-friendly transfers.</li>
          <li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span><strong>Orient Beach</strong> — French-side clubs, water sports, lunch spots.</li>
          <li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span><strong>Great Bay</strong> — walkable from Philipsburg cruise port.</li>
        </ul>
        <a href="maho-beach-plane-spotting-tours.html" class="text-ocean-600 font-semibold text-sm">Maho Beach excursions →</a>
      </div>
      <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
        <img src="{BEACHES_IMG}" alt="{BEACHES_ALT}" width="600" height="450" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{_internal_links()}</div></section>"""


def _content_faq() -> str:
    snap = _snapshot_default(best_for="Quick planning answers", popular="See FAQ topics below")
    return f"""<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-8 bg-white"><div class="max-w-3xl mx-auto px-4 space-y-4">
      <details class="faq-item rounded-2xl border border-sxm-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How long do cruise ships stay in Philipsburg?</summary>
        <p class="mt-4 text-sm text-gray-500">Most Philipsburg calls are 8 to 10 hours. A Maho Beach morning plus Orient Beach or catamaran sail can fit when you leave a sensible return window — confirm your ship’s times.</p></details>
      <details class="faq-item rounded-2xl border border-sxm-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Is Maho Beach safe for cruise passengers?</summary>
        <p class="mt-4 text-sm text-gray-500">Yes when you stay behind marked barriers and follow operator briefings. Jet blast from departing aircraft is dangerous — never stand on the fence line during takeoffs. Aircraft timing is not promised.</p></details>
      <details class="faq-item rounded-2xl border border-sxm-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">What is the difference between the Dutch and French sides?</summary>
        <p class="mt-4 text-sm text-gray-500">Dutch St Maarten uses the guilder and English widely; French St Martin uses euros and French. For ordinary day movement the land border is typically open, so island tours can cover both in one port day without inventing heavy border-control theatre.</p></details>
      <details class="faq-item rounded-2xl border border-sxm-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Orient Beach or Maho Beach for a port day?</summary>
        <p class="mt-4 text-sm text-gray-500">Maho Beach is iconic for possible aircraft landings and a shorter visit; Orient Beach suits a longer swim-and-lunch French-side day. Many guests do Maho in the morning and Orient or a catamaran later — flight activity still varies.</p></details>
      <details class="faq-item rounded-2xl border border-sxm-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Ship excursion or book independently?</summary>
        <p class="mt-4 text-sm text-gray-500">Ship-sold tours often include a wait-if-late policy from the cruise line. Independent operators typically plan a return window — confirm policies, build your own buffer, and do not cut it fine.</p></details>
      {_internal_links()}
    </div></section>"""


def _faq_schema() -> dict:
    qa = [
        (
            "How long do cruise ships stay in Philipsburg?",
            "Most Philipsburg calls are 8 to 10 hours.",
        ),
        (
            "Is Maho Beach safe for cruise passengers?",
            "Yes when you stay behind marked barriers and follow operator briefings.",
        ),
        (
            "What is the difference between the Dutch and French sides?",
            "Dutch St Maarten uses guilders; French St Martin uses euros — island tours cover both.",
        ),
        (
            "Orient Beach or Maho Beach for a port day?",
            "Maho for plane spotting; Orient for a longer French-side beach day.",
        ),
        (
            "Ship excursion or book independently?",
            "Ship-sold tours often include wait-if-late; confirm independent operator policies and build your own buffer.",
        ),
    ]
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in qa
        ],
    }


def main() -> None:
    print("Building St Maarten Shore Excursion site…")

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
        <a href="st-maarten-snorkelling-tours.html" data-nav="snorkelling" class="text-gray-600 hover:text-ocean-600 transition-colors">Snorkelling</a>
        <a href="st-maarten-island-tours.html" data-nav="island" class="text-gray-600 hover:text-ocean-600 transition-colors">Island Tours</a>
        <a href="st-maarten-cruise-port-guide.html" data-nav="port" class="text-gray-600 hover:text-ocean-600 transition-colors">Port Guide</a>
      </div>
      <a href="best-st-maarten-shore-excursions.html" class="hidden md:inline-flex items-center gap-2 btn-ocean text-white text-sm font-semibold px-4 py-2 rounded-full shadow-md">
        Compare Tours
      </a>
      <button type="button" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-sand-50" aria-label="Open menu">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </div>
</nav>
""",
    )

    write(
        "partials/footer.html",
        f"""  <footer class="bg-gray-900 text-gray-400 py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
        <div class="sm:col-span-2 lg:col-span-1">
          <a href="index.html" class="font-display font-semibold text-white text-lg">{SITE}</a>
          <p class="mt-3 text-sm leading-relaxed">Planning guide for cruise visitors to St Maarten from Philipsburg port. Not affiliated with any cruise line.</p>
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
            <li><a href="st-maarten-private-tours.html" class="hover:text-white transition-colors">Private Tours</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Resources</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="st-maarten-cruise-port-guide.html" class="hover:text-white transition-colors">Port Guide</a></li>
            <li><a href="one-day-in-st-maarten.html" class="hover:text-white transition-colors">One Day in St Maarten</a></li>
            <li><a href="dutch-and-french-side-tours.html" class="hover:text-white transition-colors">Dutch &amp; French Side</a></li>
            <li><a href="best-beaches-in-st-maarten.html" class="hover:text-white transition-colors">Best Beaches</a></li>
            <li><a href="st-maarten-family-excursions.html" class="hover:text-white transition-colors">Family Excursions</a></li>
            <li><a href="st-maarten-faq.html" class="hover:text-white transition-colors">FAQ</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-gray-800 pt-8 text-xs text-center sm:text-left">
        <p>&copy; 2026 {SITE}. Verify times and prices with operators before booking.</p>
      </div>
    </div>
  </footer>
""",
    )

    write(
        "partials/trust-strip.html",
        f"""<section class="trust-strip" aria-label="St Maarten shore excursion highlights">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <ul class="trust-strip__list">
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Maho Beach</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Orient Beach</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Catamaran Sailing</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Cruise-Friendly Returns</li>
    </ul>
  </div>
</section>
""",
    )

    heroes = {
        "hero-home.html": _hero_home(),
        "hero-excursions.html": _hero_inner(
            "Philipsburg · Dutch & French Island",
            f"Best St Maarten<br/><span class=\"{ACCENT}\">Shore Excursions</span>",
            "Compare Maho Beach, Orient Beach, catamaran sailing, snorkelling, island tours, ATV adventures and private options for your ship schedule.",
            BEST_IMG,
            BEST_ALT,
            breadcrumb="Best Excursions",
        ),
        "hero-port-guide.html": _hero_inner(
            "Cruise Passenger Guide",
            f"St Maarten<br/><span class=\"{ACCENT}\">Cruise Port Guide</span>",
            "Philipsburg terminals, taxis, currency and how to plan shore time ashore on both sides of the island.",
            PORT_IMG,
            PORT_ALT,
            breadcrumb="Port Guide",
            cta=("best-st-maarten-shore-excursions.html", "View Shore Excursions →"),
            tags=["🚢 Philipsburg", "✈️ Maho Beach", "🏖️ Orient Beach", "⛵ Catamaran"],
        ),
        "hero-one-day.html": _hero_inner(
            "Port Day Timeline",
            f"One Day in<br/><span class=\"{ACCENT}\">St Maarten</span>",
            "Hour-by-hour plan from gangway to departure — Maho Beach, Orient Beach or catamaran with return buffer.",
            ONE_DAY_IMG,
            ONE_DAY_ALT,
            breadcrumb="One Day in St Maarten",
        ),
        "hero-maho-beach.html": _hero_inner(
            "Princess Juliana Airport",
            f"Maho Beach<br/><span class=\"{ACCENT}\">Plane Spotting</span>",
            "Watch aircraft land metres overhead on Maho Beach — St Maarten's signature shore experience for cruise guests.",
            MAHO_IMG,
            MAHO_ALT,
            breadcrumb="Maho Beach",
        ),
        "hero-orient-beach.html": _hero_inner(
            "French Side · St Martin",
            f"Orient Beach<br/><span class=\"{ACCENT}\">Excursions</span>",
            "Turquoise water, beach clubs and relaxed French-side atmosphere east of Philipsburg.",
            ORIENT_IMG,
            ORIENT_ALT,
            breadcrumb="Orient Beach",
        ),
        "hero-snorkelling.html": _hero_inner(
            "Leeward Coast · St Maarten",
            f"St Maarten<br/><span class=\"{ACCENT}\">Snorkelling</span> Tours",
            "Clear Caribbean water, reef patches and tropical fish — boat trips with gear from Philipsburg.",
            SNORKEL_IMG,
            SNORKEL_ALT,
            breadcrumb="Snorkelling Tours",
        ),
        "hero-island.html": _hero_inner(
            "Sightseeing · St Maarten",
            f"St Maarten<br/><span class=\"{ACCENT}\">Island Tours</span>",
            "Philipsburg, Marigot, viewpoints and both sides of the island by air-conditioned van.",
            ISLAND_IMG,
            ISLAND_ALT,
            breadcrumb="Island Tours",
        ),
        "hero-atv.html": _hero_inner(
            "Off-Road Adventure",
            f"St Maarten ATV &amp;<br/><span class=\"{ACCENT}\">Buggy Tours</span>",
            "Explore hills, coastline and back roads — high-energy shore excursions from the cruise port.",
            ATV_IMG,
            ATV_ALT,
            breadcrumb="ATV & Buggy",
        ),
        "hero-dutch-french.html": _hero_inner(
            "Two Nations · One Island",
            f"Dutch &amp; French Side<br/><span class=\"{ACCENT}\">Tours</span>",
            "Cross the open border — Philipsburg duty-free, Marigot waterfront and dual-culture highlights.",
            DUTCH_FRENCH_IMG,
            DUTCH_FRENCH_ALT,
            breadcrumb="Dutch & French Side",
        ),
        "hero-catamaran.html": _hero_inner(
            "Leeward Sailing",
            f"Catamaran<br/><span class=\"{ACCENT}\">Sailing Excursions</span>",
            "Trade-wind sailing with snorkel stops, swim time and open bar — timed for cruise port days.",
            CATAMARAN_IMG,
            CATAMARAN_ALT,
            breadcrumb="Catamaran Sailing",
        ),
        "hero-private.html": _hero_inner(
            "Custom Shore Trips",
            f"St Maarten<br/><span class=\"{ACCENT}\">Private Tours</span>",
            "Private vans and charters at your group's pace — Maho Beach, Orient Beach and custom island routes.",
            PRIVATE_IMG,
            PRIVATE_ALT,
            breadcrumb="Private Tours",
        ),
        "hero-family.html": _hero_inner(
            "All Ages Welcome",
            f"St Maarten<br/><span class=\"{ACCENT}\">Family</span> Excursions",
            "Calm beaches, gentle catamaran sails and relaxed island drives for every generation.",
            FAMILY_IMG,
            FAMILY_ALT,
            breadcrumb="Family Excursions",
        ),
        "hero-beaches.html": _hero_inner(
            "Beach Guide · St Maarten",
            f"Best Beaches<br/><span class=\"{ACCENT}\">in St Maarten</span>",
            "Maho Beach, Orient Beach and Great Bay — choose the right sand for your Philipsburg port day.",
            BEACHES_IMG,
            BEACHES_ALT,
            breadcrumb="Best Beaches",
        ),
        "hero-faq.html": _hero_inner(
            "Cruise Planning Answers",
            f"St Maarten<br/><span class=\"{ACCENT}\">Excursions FAQ</span>",
            "Philipsburg port hours, Maho Beach safety, Dutch vs French sides and booking independent vs ship tours.",
            FAQ_IMG,
            FAQ_ALT,
            breadcrumb="FAQ",
        ),
    }
    for name, html in heroes.items():
        write(f"partials/{name}", html)

    contents = {
        "home.html": _content_home(),
        "best-st-maarten-shore-excursions.html": _content_best(),
        "st-maarten-cruise-port-guide.html": _content_port(),
        "one-day-in-st-maarten.html": _content_one_day(),
        "maho-beach-plane-spotting-tours.html": _content_maho(),
        "orient-beach-excursions.html": _content_orient(),
        "st-maarten-snorkelling-tours.html": _content_snorkelling(),
        "st-maarten-island-tours.html": _content_island(),
        "st-maarten-atv-buggy-tours.html": _content_atv(),
        "dutch-and-french-side-tours.html": _content_dutch_french(),
        "catamaran-sailing-excursions.html": _content_catamaran(),
        "st-maarten-private-tours.html": _content_private(),
        "st-maarten-family-excursions.html": _content_family(),
        "best-beaches-in-st-maarten.html": _content_beaches(),
        "st-maarten-faq.html": _content_faq(),
    }
    for name, html in contents.items():
        write(f"content/{name}", html)

    pages = [
        dict(
            file="index.html",
            title=f"{SITE} | Maho Beach, Catamaran &amp; Island Tours from Philipsburg",
            description="Plan St Maarten shore excursions for cruise passengers — Maho Beach plane spotting, Orient Beach, catamaran sailing, snorkelling, island tours and private trips from Philipsburg cruise port.",
            keywords="St Maarten shore excursions, St Maarten cruise excursions, Maho Beach cruise tour, Philipsburg cruise port tours, Orient Beach excursion",
            path="",
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
        dict(
            file="best-st-maarten-shore-excursions.html",
            title="Best St Maarten Shore Excursions | Compare Philipsburg Cruise Tours",
            description="Compare the best St Maarten shore excursions — Maho Beach, Orient Beach, catamaran sailing, snorkelling, island tours, ATV adventures and private options with cruise timing.",
            keywords="best St Maarten shore excursions, St Maarten cruise port tours, compare St Maarten excursions, Philipsburg shore trips",
            path="best-st-maarten-shore-excursions.html",
            data_page="excursions",
            hero="partials/hero-excursions.html",
            content="best-st-maarten-shore-excursions.html",
            preload=BEST_IMG,
            schema={
                "@context": "https://schema.org",
                "@type": "WebPage",
                "name": "Best St Maarten Shore Excursions",
                "url": f"{DOMAIN}/best-st-maarten-shore-excursions.html",
            },
        ),
        dict(
            file="st-maarten-cruise-port-guide.html",
            title="St Maarten Cruise Port Guide | Philipsburg for Cruise Passengers",
            description="St Maarten cruise port guide — Philipsburg terminals, taxis, ANG and USD, Dutch and French sides, and top shore excursions timed for your ship's schedule.",
            keywords="St Maarten cruise port guide, Philipsburg cruise port, St Maarten port day, cruise passenger guide St Maarten",
            path="st-maarten-cruise-port-guide.html",
            data_page="port",
            hero="partials/hero-port-guide.html",
            content="st-maarten-cruise-port-guide.html",
            preload=PORT_IMG,
            schema={
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": "St Maarten Cruise Port Guide",
                "url": f"{DOMAIN}/st-maarten-cruise-port-guide.html",
            },
        ),
        dict(
            file="one-day-in-st-maarten.html",
            title="One Day in St Maarten from a Cruise Ship | Port Itinerary",
            description="How to spend one day in St Maarten on a cruise stop — Maho Beach, Orient Beach and catamaran sample timeline with return-to-ship buffer.",
            keywords="one day in St Maarten cruise, St Maarten port day itinerary, Philipsburg cruise stop planning",
            path="one-day-in-st-maarten.html",
            data_page="port",
            hero="partials/hero-one-day.html",
            content="one-day-in-st-maarten.html",
            preload=ONE_DAY_IMG,
        ),
        dict(
            file="maho-beach-plane-spotting-tours.html",
            title="Maho Beach Plane Spotting Tours | St Maarten Cruise Excursions",
            description="Maho Beach plane spotting excursions from Philipsburg — aircraft landings overhead, beach time and cruise-friendly returns.",
            keywords="Maho Beach excursion St Maarten, Maho Beach cruise port, plane spotting St Maarten shore excursion",
            path="maho-beach-plane-spotting-tours.html",
            data_page="maho",
            hero="partials/hero-maho-beach.html",
            content="maho-beach-plane-spotting-tours.html",
            preload=MAHO_IMG,
        ),
        dict(
            file="orient-beach-excursions.html",
            title="Orient Beach Excursions | French Side St Maarten Cruise Tours",
            description="Orient Beach excursions from Philipsburg — French-side beach clubs, turquoise water and cruise-friendly returns.",
            keywords="Orient Beach excursion St Maarten, Orient Beach cruise port, French side beach day St Maarten",
            path="orient-beach-excursions.html",
            data_page="orient",
            hero="partials/hero-orient-beach.html",
            content="orient-beach-excursions.html",
            preload=ORIENT_IMG,
        ),
        dict(
            file="st-maarten-snorkelling-tours.html",
            title="St Maarten Snorkelling Tours | Reef Cruise Excursions from Philipsburg",
            description="St Maarten snorkelling tours on the leeward coast — reef sites, turtles and clear water with cruise-friendly returns; catamaran combos available.",
            keywords="St Maarten snorkelling tours, reef snorkel cruise St Maarten, Philipsburg snorkel excursion",
            path="st-maarten-snorkelling-tours.html",
            data_page="snorkelling",
            hero="partials/hero-snorkelling.html",
            content="st-maarten-snorkelling-tours.html",
            preload=SNORKEL_IMG,
        ),
        dict(
            file="st-maarten-island-tours.html",
            title="St Maarten Island Tours | Sightseeing from Philipsburg Cruise Port",
            description="St Maarten island tours for cruise passengers — Philipsburg, Marigot, viewpoints and Dutch and French side highlights.",
            keywords="St Maarten island tour cruise, sightseeing St Maarten shore excursion, Philipsburg island drive",
            path="st-maarten-island-tours.html",
            data_page="island",
            hero="partials/hero-island.html",
            content="st-maarten-island-tours.html",
            preload=ISLAND_IMG,
        ),
        dict(
            file="st-maarten-atv-buggy-tours.html",
            title="St Maarten ATV &amp; Buggy Tours | Off-Road Cruise Excursions",
            description="St Maarten ATV and buggy adventures from the cruise port — hills, coastline and back roads with cruise-friendly timing.",
            keywords="St Maarten ATV tour cruise, buggy excursion St Maarten, off road shore excursion Philipsburg",
            path="st-maarten-atv-buggy-tours.html",
            data_page="atv",
            hero="partials/hero-atv.html",
            content="st-maarten-atv-buggy-tours.html",
            preload=ATV_IMG,
        ),
        dict(
            file="dutch-and-french-side-tours.html",
            title="Dutch &amp; French Side Tours | St Maarten Dual-Nation Excursions",
            description="Dutch and French side tours from Philipsburg — Philipsburg, Marigot, open border crossings and both cultures in one port day.",
            keywords="Dutch French side tour St Maarten, Marigot Philipsburg tour, St Maarten border excursion cruise",
            path="dutch-and-french-side-tours.html",
            data_page="island",
            hero="partials/hero-dutch-french.html",
            content="dutch-and-french-side-tours.html",
            preload=DUTCH_FRENCH_IMG,
        ),
        dict(
            file="catamaran-sailing-excursions.html",
            title="Catamaran Sailing Excursions | St Maarten Cruise Port Sails",
            description="Catamaran sailing excursions from Philipsburg — snorkel stops, swim time and trade-wind cruising timed for cruise schedules.",
            keywords="catamaran St Maarten cruise, sailing excursion Philipsburg, snorkel catamaran St Maarten",
            path="catamaran-sailing-excursions.html",
            data_page="sailing",
            hero="partials/hero-catamaran.html",
            content="catamaran-sailing-excursions.html",
            preload=CATAMARAN_IMG,
        ),
        dict(
            file="st-maarten-private-tours.html",
            title="St Maarten Private Tours | Custom Cruise Shore Excursions",
            description="Private St Maarten tours for cruise passengers — custom vans and charters with flexible Maho Beach, Orient Beach and island itineraries.",
            keywords="St Maarten private tours cruise, private shore excursion St Maarten, custom Philipsburg tour",
            path="st-maarten-private-tours.html",
            data_page="private",
            hero="partials/hero-private.html",
            content="st-maarten-private-tours.html",
            preload=PRIVATE_IMG,
        ),
        dict(
            file="st-maarten-family-excursions.html",
            title="St Maarten Family Excursions | Kid-Friendly Philipsburg Cruise Tours",
            description="Family-friendly St Maarten excursions — Orient Beach, gentle catamaran sails and relaxed island tours for cruise guests with children.",
            keywords="St Maarten family excursions, kid friendly St Maarten cruise tours, family shore excursion St Maarten",
            path="st-maarten-family-excursions.html",
            data_page="beaches",
            hero="partials/hero-family.html",
            content="st-maarten-family-excursions.html",
            preload=FAMILY_IMG,
        ),
        dict(
            file="best-beaches-in-st-maarten.html",
            title="Best Beaches in St Maarten | Maho &amp; Orient for Cruise Passengers",
            description="Best beaches in St Maarten for cruise visitors — Maho Beach, Orient Beach and Great Bay near Philipsburg on a port day.",
            keywords="best beaches St Maarten cruise, Maho Beach Orient Beach, beach guide St Maarten port day",
            path="best-beaches-in-st-maarten.html",
            data_page="beaches",
            hero="partials/hero-beaches.html",
            content="best-beaches-in-st-maarten.html",
            preload=BEACHES_IMG,
        ),
        dict(
            file="st-maarten-faq.html",
            title="St Maarten Shore Excursions FAQ | Philipsburg Cruise Planning",
            description="FAQ for St Maarten shore excursions — Philipsburg port hours, Maho Beach safety, Dutch vs French sides, Orient vs Maho and independent vs ship booking.",
            keywords="St Maarten shore excursions FAQ, St Maarten cruise port questions, Maho Beach FAQ cruise",
            path="st-maarten-faq.html",
            data_page="port",
            hero="partials/hero-faq.html",
            content="st-maarten-faq.html",
            preload=FAQ_IMG,
            schema=_faq_schema(),
        ),
    ]

    for p in pages:
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
                schema=p.get("schema"),
            ),
        )

    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")

    urls = [
        ("", "1.0", "weekly"),
        ("best-st-maarten-shore-excursions.html", "0.9", "monthly"),
        ("st-maarten-cruise-port-guide.html", "0.8", "monthly"),
        ("one-day-in-st-maarten.html", "0.8", "monthly"),
        ("maho-beach-plane-spotting-tours.html", "0.9", "monthly"),
        ("orient-beach-excursions.html", "0.9", "monthly"),
        ("st-maarten-snorkelling-tours.html", "0.8", "monthly"),
        ("st-maarten-island-tours.html", "0.8", "monthly"),
        ("st-maarten-atv-buggy-tours.html", "0.8", "monthly"),
        ("dutch-and-french-side-tours.html", "0.8", "monthly"),
        ("catamaran-sailing-excursions.html", "0.8", "monthly"),
        ("st-maarten-private-tours.html", "0.8", "monthly"),
        ("st-maarten-family-excursions.html", "0.8", "monthly"),
        ("best-beaches-in-st-maarten.html", "0.8", "monthly"),
        ("st-maarten-faq.html", "0.7", "monthly"),
    ]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, priority, freq in urls:
        url = f"{DOMAIN}/{loc}" if loc else f"{DOMAIN}/"
        lines += [
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{DATE}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{priority}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    write("sitemap.xml", "\n".join(lines) + "\n")

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

    # Domain may already be attached in Cloudflare; prefer workers_dev for local hygiene.
    write(
        "wrangler.jsonc",
        """{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "st-maarten-shore-excursion",
  "compatibility_date": "2026-06-04",
  "observability": { "enabled": true },
  "assets": { "directory": "." },
  "workers_dev": true
}
""",
    )

    write(
        "deploy.sh",
        f"""#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -f node_modules/.bin/wrangler ]]; then
  npm install
fi

echo "Deploying {SITE} to Cloudflare..."
npx wrangler deploy

echo "Done. Check {DOMAIN}/ shortly."
""",
    )

    (ROOT / "deploy.sh").chmod(0o755)

    images_dir = ROOT / "images"
    images_dir.mkdir(exist_ok=True)
    placeholders = [
        HOME_HERO,
        BEST_IMG,
        PORT_IMG,
        ONE_DAY_IMG,
        MAHO_IMG,
        ORIENT_IMG,
        SNORKEL_IMG,
        ISLAND_IMG,
        ATV_IMG,
        DUTCH_FRENCH_IMG,
        CATAMARAN_IMG,
        PRIVATE_IMG,
        FAMILY_IMG,
        BEACHES_IMG,
        FAQ_IMG,
        INTRO_IMG,
    ]
    for img in placeholders:
        p = ROOT / img
        if p.exists() and p.stat().st_size > 5000:
            continue
        if not p.exists() or p.stat().st_size <= 5000:
            p.write_bytes(
                b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01"
                b"\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89"
                b"\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n"
                b"\xdb\x00\x00\x00\x00IEND\xaeB`\x82"
            )

    print("Done.")


if __name__ == "__main__":
    main()
