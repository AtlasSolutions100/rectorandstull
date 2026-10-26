#!/usr/bin/env python3
"""Builds rectorandstull.com: a handful of static pages from shared chrome.
Run `python3 build.py`; commit the output. GitHub Pages serves the repo root."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://rectorandstull.com"
EMAIL = "hello@rectorandstull.com"
ADDRESS = "Rector &amp; Stull LLC &middot; 30 N Gould St Ste R, Sheridan, WY 82801"

NAV = """<a class="skip" href="#main">Skip to content</a>
<header class="nav"><div class="wrap">
  <a class="brand" href="/">Rector <em>&amp;</em> Stull</a>
  <nav aria-label="Site"><a href="/#work">Work</a><a href="/#how">How we launch</a><a href="/#who">Who</a><a href="/#contact">Contact</a></nav>
</div></header>"""

FOOTER = f"""<footer><div class="wrap">
  <div>&copy; <span class="yr">2026</span> {ADDRESS}</div>
  <div><a href="/privacy.html">Privacy</a><a href="https://themorningupgrades.com" rel="noopener">The Morning Upgrade</a><a href="https://crowdcut.studio" rel="noopener">Crowdcut</a></div>
</div></footer>
<script>document.querySelectorAll('.yr').forEach(function(e){{e.textContent=new Date().getFullYear()}})</script>"""


def page(title, desc, body, fn, noindex=False):
    canonical = SITE + ("/" if fn == "index.html" else "/" + fn)
    robots = '<meta name="robots" content="noindex,follow">' if noindex else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
{robots}
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">
<meta property="og:image" content="{SITE}/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,300..600,0..100,0..1;1,9..144,300..600,0..100,0..1&family=Inter+Tight:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"Rector & Stull LLC","url":"{SITE}","email":"{EMAIL}","address":{{"@type":"PostalAddress","streetAddress":"30 N Gould St Ste R","addressLocality":"Sheridan","addressRegion":"WY","postalCode":"82801","addressCountry":"US"}},"brand":[{{"@type":"Brand","name":"The Morning Upgrade","url":"https://themorningupgrades.com"}},{{"@type":"Brand","name":"Crowdcut","url":"https://crowdcut.studio"}}]}}</script>
</head>
<body>
{NAV}
<main id="main">
{body}
</main>
{FOOTER}
</body>
</html>
"""


HOME = f"""
<div class="hero"><div class="wrap">
  <h1 class="amp" aria-label="Rector and Stull">
    <span class="n r" aria-hidden="true">Rector</span><span class="a" aria-hidden="true">&amp;</span><span class="n s" aria-hidden="true">Stull</span>
  </h1>
  <p class="lede">We build consumer brands, and the software that sells them.</p>
  <p class="sub">A two-partner firm. We run our own brands first, so every method we use has been paid for with our own money before anyone else's.</p>
  <div class="row"><a class="btn" href="#work">See what we run</a><a class="btn quiet" href="mailto:{EMAIL}">Write to us</a></div>
</div></div>

<section id="work"><div class="wrap">
  <div class="sect-h"><h2>Two things we run every day.</h2><p>Not client work. Our own brands, with our own money on the line. They are the proof of the method.</p></div>
  <div class="cases">
    <a class="case" href="https://themorningupgrades.com" rel="noopener">
      <div class="shot"><img src="/img/tmu.jpg" width="2160" height="1350" alt="The Morning Upgrade storefront: One scoop. No 2 PM crash." loading="lazy"></div>
      <div class="body">
        <h3>The Morning Upgrade</h3>
        <p class="what">A direct-to-consumer coffee brand. Storefront, subscription checkout, email flows, and a library of AI-produced video ads, built and launched in under a month.</p>
        <ul><li>Brand &amp; storefront</li><li>AI video creative</li><li>Subscriptions</li><li>Email flows</li><li>Paid social</li></ul>
        <div class="go">themorningupgrades.com</div>
      </div>
    </a>
    <a class="case" href="https://crowdcut.studio" rel="noopener">
      <div class="shot"><img src="/img/crowdcut.jpg" width="2160" height="1350" alt="Crowdcut: The crowd marks the moment. We cut the clip." loading="lazy"></div>
      <div class="body">
        <h3>Crowdcut</h3>
        <p class="what">Software for streamers and clippers. It finds the moments a community reacted to, cuts them vertical with captions and hooks, and posts them. Our own distribution engine, sold as a product.</p>
        <ul><li>Product &amp; engineering</li><li>Short-form distribution</li><li>Creator referrals</li><li>Self-serve billing</li></ul>
        <div class="go">crowdcut.studio</div>
      </div>
    </a>
  </div>
</div></section>

<section id="how"><div class="wrap">
  <div class="sect-h"><h2>How a launch goes.</h2><p>The same four moves, in the same order, for a coffee or a piece of software.</p></div>
  <div class="steps">
    <div><div class="k">1</div><h3>Creative</h3><p>Video ads, hosts and product films produced with AI, in volume, so we can test twenty angles instead of two.</p></div>
    <div><div class="k">2</div><h3>Distribution</h3><p>Short-form first: clipped, captioned and posted daily. Paid social turns up what already works organically.</p></div>
    <div><div class="k">3</div><h3>Storefront</h3><p>A fast site, a checkout that takes subscriptions, and email that follows up without anyone remembering to.</p></div>
    <div><div class="k">4</div><h3>Measure, repeat</h3><p>Cost to acquire, retention, payback. The numbers decide what gets more budget next week.</p></div>
  </div>
</div></section>

<section id="who"><div class="wrap">
  <div class="sect-h"><h2>Two partners, two states.</h2><p>Rector &amp; Stull LLC, registered in Wyoming.</p></div>
  <div class="who">
    <div><h3>Rector</h3><p class="where">Idaho</p><p>Has reached the top of two direct-sales companies. Knows how a product gets sold person to person, and what has to be true for that to scale online.</p></div>
    <div><h3>Stull</h3><p class="where">Texas</p><p>Builds the software and ran national sales teams. Writes the systems that make the selling repeatable, from the storefront to the clip pipeline.</p></div>
  </div>
</div></section>

<section id="contact"><div class="wrap">
  <div class="contact">
    <div><h2>Working on something?</h2><p style="color:var(--grey);margin:14px 0 22px">We take on a small number of brands whose problem looks like one we have already solved for ourselves.</p><a class="big" href="mailto:{EMAIL}">{EMAIL}</a></div>
    <address>Rector &amp; Stull LLC<br>30 N Gould St Ste R<br>Sheridan, WY 82801</address>
  </div>
</div></section>
"""

PRIVACY = f"""
<div class="wrap legal">
  <h1>Privacy</h1>
  <p>This site, rectorandstull.com, is a brochure for Rector &amp; Stull LLC. It has no accounts, no forms and no shopping cart.</p>
  <h2>What we collect</h2>
  <p>Nothing through this site. We don't run analytics or advertising pixels here. If you email us, we keep the email so we can answer it.</p>
  <h2>Our brands</h2>
  <p>The Morning Upgrade (themorningupgrades.com) and Crowdcut (crowdcut.studio) are run by Rector &amp; Stull LLC and each has its own privacy policy covering what those sites collect.</p>
  <h2>Hosting</h2>
  <p>The site is served by GitHub Pages, which logs requests (IP address, page, time) to operate the service. See GitHub's privacy statement for details.</p>
  <h2>Contact</h2>
  <p><a href="mailto:{EMAIL}">{EMAIL}</a><br>{ADDRESS}</p>
</div>
"""

NOTFOUND = """
<div class="wrap legal">
  <h1>That page isn't here.</h1>
  <p>Try the <a href="/">home page</a>, or write to us and we'll point you the right way.</p>
</div>
"""

PAGES = {
    "index.html": ("Rector & Stull — brands, and the software that sells them",
                   "A two-partner firm that builds consumer brands and the software behind them. The Morning Upgrade and Crowdcut are ours.", HOME, False),
    "privacy.html": ("Privacy — Rector & Stull", "What rectorandstull.com collects (nothing) and how to reach us.", PRIVACY, False),
    "404.html": ("Not found — Rector & Stull", "That page isn't here.", NOTFOUND, True),
}

for fn, (title, desc, body, noindex) in PAGES.items():
    with open(os.path.join(HERE, fn), "w", encoding="utf-8") as f:
        f.write(page(title, desc, body, fn, noindex))

with open(os.path.join(HERE, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "".join(f"  <url><loc>{SITE}/{'' if fn == 'index.html' else fn}</loc></url>\n" for fn in PAGES if fn != "404.html")
            + "</urlset>\n")
with open(os.path.join(HERE, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
with open(os.path.join(HERE, "CNAME"), "w", encoding="utf-8") as f:
    f.write("rectorandstull.com\n")
print("built", ", ".join(PAGES))
