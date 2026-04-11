"""Generate Central London location pages from marylebone.html (split + replace)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = (ROOT / "public" / "locations" / "marylebone.html").read_text(encoding="utf-8")

marker_loc = "<!-- Location Content -->\n"
marker_faq = "\n\n    <!-- FAQ & Footer Section -->"

if marker_loc not in BASE or marker_faq not in BASE:
    raise SystemExit("markers not found in marylebone.html")

a, rest = BASE.split(marker_loc, 1)
b, suffix = rest.split(marker_faq, 1)
suffix = marker_faq + suffix  # restore marker

OLD_FAQ1 = """                <p class="font-clamp-p2">
                  We cover all of Marylebone, including Marylebone High Street, Baker Street, Harley Street, Wimpole Street, Portland Place, Chiltern Street, and
                  the W1U, W1G, and NW1 postcodes that fall within the area. We also work in neighbouring Fitzrovia, Mayfair, Paddington, and St John's Wood
                  when projects sit on the boundary.
                </p>"""


def head_html(slug: str, display: str, title: str, desc: str, og: str) -> str:
    h = a
    h = h.replace("marylebone.html", f"{slug}.html")
    h = h.replace(
        "<title>Picture Hanging Service Marylebone, London NW1 &amp; W1 | Perfectly Hung</title>",
        f"<title>{title}</title>",
    )
    h = h.replace(
        "content=\"Professional picture hanging &amp; art installation in Marylebone, London. "
        "Perfect alignment for artwork, mirrors &amp; gallery walls across W1U, W1G &amp; NW1.\"",
        f'content="{desc}"',
    )
    h = h.replace(
        "content=\"Professional picture hanging, mirror installation, and gallery wall design across Marylebone. "
        "Trusted installers for period homes, apartments, and professional spaces.\"",
        f'content="Professional picture hanging, mirror installation, and gallery wall design across {display}. '
        "Trusted installers for period homes, apartments, and professional spaces.\"",
    )
    h = h.replace(
        "content=\"Expert art installation and picture hanging in Marylebone, London. "
        "Precision placement for townhouses, mansion flats, and galleries near Regent's Park.\"",
        f'content="Expert art installation and picture hanging in {display}, London. '
        'Precision placement for homes, flats, and commercial spaces across Central London."',
    )
    h = h.replace("Picture Hanging Services Marylebone London | Perfectly Hung", f"Picture Hanging Services {display} London | Perfectly Hung")
    h = h.replace("https://perfectlyhung.uk/img/gallery/gallery-016.webp", f"https://perfectlyhung.uk/img/gallery/{og}")
    h = h.replace("Picture hanging service in a Marylebone London home", f"Picture hanging service in a {display} London home")
    return h


def location_section(
    display: str,
    span: str,
    h1_line: str,
    intro: str,
    mail_q: str,
    btn: str,
    h2: str,
    h2_p: str,
    bullets: tuple[str, str, str, str],
    h3: str,
    p1: str,
    p2: str,
    img_alt: str,
) -> str:
    b0, b1, b2, b3 = bullets
    return f"""    <section class="section location-page">
      <div class="location-container">
        <div class="location-content">
          <div data-aos="fade-up">
            <div class="span-heading">{span}</div>

            <h1>{h1_line}</h1>
            <p>
              {intro}
            </p>
          </div>
          <div class="location-cta" data-aos="fade-up" data-aos-delay="200">
            <a href="mailto:hello@perfectlydone.uk?subject={mail_q}" class="cta btn btn-primary">{btn}</a>
            <a href="tel:07951101683" class="cta btn btn-outline">Call 07951 101683</a>
          </div>

          <div data-aos="fade-up" data-aos-delay="100">
            <div>
              <h2>{h2}</h2>
              <p>
                {h2_p}
              </p>
            </div>
            <br />
            <ul>
              <li class="font-clamp-p2">{b0}</li>
              <li class="font-clamp-p2">{b1}</li>
              <li class="font-clamp-p2">{b2}</li>
              <li class="font-clamp-p2">{b3}</li>
            </ul>
          </div>

          <div data-aos="fade-up" data-aos-delay="150">
            <h3>{h3}</h3>
            <p>
              {p1}
            </p>
            <p>
              {p2}
            </p>
          </div>
        </div>

        <div class="location-image-wrapper" data-aos="fade-left" data-aos-delay="150">
          <div class="location-image">
            <img src="../img/locations.webp" alt="{img_alt}" width="720" height="960" loading="lazy" />
          </div>
        </div>
      </div>
    </section>
"""


AREAS = [
    {
        "slug": "fitzrovia",
        "display": "Fitzrovia",
        "title": "Picture Hanging Service Fitzrovia, London W1 | Perfectly Hung",
        "desc": "Professional picture hanging &amp; art installation in Fitzrovia, London W1. Perfect alignment for artwork, mirrors &amp; gallery walls across W1T.",
        "og": "gallery-018.webp",
        "span": "Fitzrovia, London W1",
        "mail_q": "Request%20a%20Fitzrovia%20Install",
        "faq1": """                <p class="font-clamp-p2">
                  We cover Fitzrovia from Tottenham Court Road and Goodge Street across to Great Portland Street, including Charlotte Street, Cleveland Street,
                  and the W1T postcode area. We also take work that borders Soho, Bloomsbury, and Marylebone when the site is closest to our Fitzrovia coverage.
                </p>""",
        "loc": location_section(
            "Fitzrovia",
            "Fitzrovia, London W1",
            "Picture Hanging Services in Fitzrovia",
            """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Fitzrovia. From creative studios and
              agency offices near Charlotte Street to period conversions and flats above retail on Tottenham Court Road, we install artwork, mirrors, and
              gallery walls with laser-precise alignment. We choose fixings for stud walls, brick, and older plaster typical of W1 conversions. We also offer
              <a href="/curtain-fitting.html">curtain and blind fitting</a> for Fitzrovia homes and workspaces.""",
            "Request%20a%20Fitzrovia%20Install",
            "Request a Fitzrovia Install",
            "Trusted installers for W1T &amp; W1W",
            """We work with homeowners, landlords, and design teams across Fitzrovia. Whether you are fitting out a compact flat, refreshing a mews house, or
              dressing a commercial reception, every installation is measured, levelled, and finished to a high standard.""",
            (
                "Laser-level picture hanging and gallery walls for Fitzrovia flats, offices, and hospitality spaces",
                "Secure mirror and heavy artwork installation on plaster, brick, and stud walls",
                "Neat cable-aware TV and art combinations where living and work spaces overlap",
                "Coverage from Goodge Street and Tottenham Court Road through to the Portland Hospital and Fitzroy Square edges",
            ),
            "Creative quarter installs",
            """Fitzrovia sits between the West End and Bloomsbury, with a mix of restaurants, galleries, and residential streets. We protect floors and
              furnishings, work around busy pavements and access rules, and keep communication clear from first visit to final walk-through. Our
              <a href="/picture-hanging.html">picture hanging</a> covers salon walls, single statement pieces, and mirror installs in bathrooms and bedrooms.""",
            """Planning a full hang after a refurbishment? We advise on height, spacing, and visual balance. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Fitzrovia property.""",
            "Picture hanging service in a Fitzrovia London property",
        ),
    },
    {
        "slug": "bloomsbury",
        "display": "Bloomsbury",
        "title": "Picture Hanging Service Bloomsbury, London WC1 | Perfectly Hung",
        "desc": "Professional picture hanging &amp; art installation in Bloomsbury, London WC1. Perfect alignment for artwork, mirrors &amp; gallery walls across WC1A &amp; WC1B.",
        "og": "gallery-019.webp",
        "span": "Bloomsbury, London WC1",
        "mail_q": "Request%20a%20Bloomsbury%20Install",
        "faq1": """                <p class="font-clamp-p2">
                  We cover Bloomsbury including Russell Square, Bedford Square, Brunswick Square, Great Ormond Street, and the WC1A, WC1B, and WC1E postcode
                  areas. We also work on the edges of Holborn, Covent Garden, and Fitzrovia when your address sits within easy reach of our Bloomsbury routes.
                </p>""",
        "loc": location_section(
            "Bloomsbury",
            "Bloomsbury, London WC1",
            "Picture Hanging Services in Bloomsbury",
            """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Bloomsbury. From Georgian townhouses and
              mansion blocks near Russell Square to student and professional lets and museum-adjacent galleries, we install artwork, mirrors, and gallery walls
              with laser-precise alignment. We respect academic and medical building rules where they apply. We also offer
              <a href="/curtain-fitting.html">curtain and blind fitting</a> for Bloomsbury homes and offices.""",
            "Request%20a%20Bloomsbury%20Install",
            "Request a Bloomsbury Install",
            "Trusted installers for WC1A, WC1B &amp; WC1E",
            """We work with residents, landlords, faculty-adjacent properties, and small galleries throughout Bloomsbury. Whether you are hanging a single
              archive print or a full salon wall, every job is measured, levelled, and finished with care.""",
            (
                "Laser-level picture hanging and gallery layouts for Bloomsbury flats, townhouses, and study spaces",
                "Secure mirror and heavy artwork installation on lath-and-plaster, brick, and modern stud walls",
                "Discreet fixings suitable for listed interiors and sensitive wall finishes",
                "Coverage across Russell Square, Gordon Square, and the streets linking to Kings Cross and Holborn",
            ),
            "Institutions, homes &amp; galleries",
            """Bloomsbury blends residential calm with universities, hospitals, and cultural venues. We coordinate access, protect stairwells and lifts, and
              use fixings matched to your wall build-up. Our <a href="/picture-hanging.html">picture hanging</a> covers libraries, reception areas, and
              domestic rooms alike.""",
            """Need help sequencing a multi-room hang? We advise on layout and lighting sight lines. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Bloomsbury property.""",
            "Picture hanging service in a Bloomsbury London property",
        ),
    },
    {
        "slug": "covent-garden",
        "display": "Covent Garden",
        "title": "Picture Hanging Service Covent Garden, London WC2 | Perfectly Hung",
        "desc": "Professional picture hanging &amp; art installation in Covent Garden, London WC2. Perfect alignment for artwork, mirrors &amp; gallery walls near the Piazza.",
        "og": "gallery-020.webp",
        "span": "Covent Garden, London WC2",
        "mail_q": "Request%20a%20Covent%20Garden%20Install",
        "faq1": """                <p class="font-clamp-p2">
                  We cover Covent Garden from the Piazza and Seven Dials through to the Strand edge and Drury Lane, including the WC2E postcode area and nearby
                  WC2H streets. We also pick up neighbouring Soho, Holborn, and Temple-adjacent jobs when access is quickest from our Covent Garden routes.
                </p>""",
        "loc": location_section(
            "Covent Garden",
            "Covent Garden, London WC2",
            "Picture Hanging Services in Covent Garden",
            """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Covent Garden. From flats above theatres
              and restaurants to boutique offices and retail displays near the market, we install artwork, mirrors, and gallery walls with laser-precise
              alignment. We plan around noise, loading, and night-time access where venues need it. We also offer
              <a href="/curtain-fitting.html">curtain and blind fitting</a> for Covent Garden properties.""",
            "Request%20a%20Covent%20Garden%20Install",
            "Request a Covent Garden Install",
            "Trusted installers for WC2E &amp; WC2H",
            """We work with residents, production offices, hospitality groups, and retail teams across Covent Garden. Whether you are dressing a compact pied-à-terre
              or a full-floor rental, every installation is measured, levelled, and finished to a high standard.""",
            (
                "Laser-level picture hanging and gallery walls for Covent Garden flats, pied-à-terre, and backstage-adjacent spaces",
                "Secure mirror and heavy artwork installation where walls sit above busy retail and basements",
                "Careful protection of finishes in high-traffic buildings and period stock",
                "Coverage around the Piazza, Seven Dials, Long Acre, and the Strand approaches",
            ),
            "Theatreland &amp; market-side installs",
            """Covent Garden mixes world-famous retail with dense residential streets. We coordinate with concierges, stage short on-street load-ins where
              permitted, and keep dust sheets and shoe covers to hand. Our <a href="/picture-hanging.html">picture hanging</a> covers feature walls, poster
              collections, and mirror installs in compact bathrooms.""",
            """Planning a seasonal refresh for a rental portfolio? We advise on layouts that photograph well for listings. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Covent Garden property.""",
            "Picture hanging service in a Covent Garden London property",
        ),
    },
    {
        "slug": "soho",
        "display": "Soho",
        "title": "Picture Hanging Service Soho, London W1 | Perfectly Hung",
        "desc": "Professional picture hanging &amp; art installation in Soho, London W1. Perfect alignment for artwork, mirrors &amp; gallery walls across W1D &amp; W1F.",
        "og": "gallery-021.webp",
        "span": "Soho, London W1",
        "mail_q": "Request%20a%20Soho%20Install",
        "faq1": """                <p class="font-clamp-p2">
                  We cover Soho from Oxford Street south through Old Compton Street and Dean Street, including the W1D and W1F postcode areas. We also work the
                  fringes of Mayfair, Fitzrovia, and Covent Garden when your building sits on a Soho-adjacent block.
                </p>""",
        "loc": location_section(
            "Soho",
            "Soho, London W1",
            "Picture Hanging Services in Soho",
            """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Soho. From compact flats above Dean Street
              to media offices and members' clubs, we install artwork, mirrors, and gallery walls with laser-precise alignment. We are used to tight stairs,
              service lifts, and evening access windows. We also offer <a href="/curtain-fitting.html">curtain and blind fitting</a> for Soho apartments and
              hospitality spaces.""",
            "Request%20a%20Soho%20Install",
            "Request a Soho Install",
            "Trusted installers for W1D &amp; W1F",
            """We work with residents, creatives, and commercial tenants across Soho. Whether you are refreshing a single feature wall or fitting out a new
              studio, every job is measured, levelled, and finished with care.""",
            (
                "Laser-level picture hanging and gallery walls for Soho flats, studios, and compact offices",
                "Secure mirror and heavy artwork installation on party walls, brick, and stud-lined interiors",
                "Quiet, tidy working practices suited to neighbours and night-time venue schedules",
                "Coverage across Dean Street, Wardour Street, Berwick Street, and the streets linking to Oxford Circus",
            ),
            "Dense W1 installs",
            """Soho is one of London's tightest urban grain neighbourhoods. We plan fixings for vibration from venues below, protect narrow hallways, and keep
              noise to a minimum. Our <a href="/picture-hanging.html">picture hanging</a> covers vinyl collections, photography walls, and mirrors in small
              bathrooms.""",
            """Need a fast turnaround between tenancies? We can align with cleaners and inventory clerks. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Soho property.""",
            "Picture hanging service in a Soho London property",
        ),
    },
    {
        "slug": "westminster",
        "display": "Westminster",
        "title": "Picture Hanging Service Westminster, London SW1 | Perfectly Hung",
        "desc": "Professional picture hanging &amp; art installation in Westminster, London SW1. Perfect alignment for artwork, mirrors &amp; gallery walls across SW1 &amp; Victoria.",
        "og": "gallery-023.webp",
        "span": "Westminster, London SW1",
        "mail_q": "Request%20a%20Westminster%20Install",
        "faq1": """                <p class="font-clamp-p2">
                  We cover Westminster from Victoria and St James's Park through to Westminster Abbey and Millbank edges, including SW1A, SW1P, SW1H, and SW1V
                  streets. We also work Pimlico-adjacent and St James's-adjacent blocks when access routes suit a Westminster crew.
                </p>""",
        "loc": location_section(
            "Westminster",
            "Westminster, London SW1",
            "Picture Hanging Services in Westminster",
            """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Westminster. From Whitehall-adjacent
              apartments and Victoria new-builds to stucco terraces near St James's Park, we install artwork, mirrors, and gallery walls with laser-precise
              alignment. We understand concierge protocols and security-conscious buildings. We also offer
              <a href="/curtain-fitting.html">curtain and blind fitting</a> for Westminster homes and offices.""",
            "Request%20a%20Westminster%20Install",
            "Request a Westminster Install",
            "Trusted installers for SW1A, SW1P, SW1H &amp; SW1V",
            """We work with homeowners, diplomats' quarters, corporate apartments, and small galleries throughout Westminster. Whether you are hanging a
              single piece above a fireplace or dressing a full reception, every installation is measured, levelled, and finished to a high standard.""",
            (
                "Laser-level picture hanging and gallery walls for Westminster flats, duplexes, and formal reception rooms",
                "Secure mirror and heavy artwork installation on stone, brick, and modern lightweight partitions",
                "Discreet service suited to security-conscious and concierge-managed buildings",
                "Coverage from Victoria Street and Broadway through Birdcage Walk and the Abbey approaches",
            ),
            "Civic &amp; residential SW1",
            """Westminster combines civic architecture with some of London's most prestigious residential stock. We coordinate with building managers, use
              protection for stone and timber floors, and select fixings for high ceilings and cornicing. Our <a href="/picture-hanging.html">picture hanging</a>
              covers boardrooms, libraries, and private sitting rooms.""",
            """Planning a hang before a diplomatic or corporate move-in? We advise on sight lines from seating. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Westminster property.""",
            "Picture hanging service in a Westminster London property",
        ),
    },
]


def main() -> None:
    for cfg in AREAS:
        slug = cfg["slug"]
        display = cfg["display"]
        head = head_html(slug, display, cfg["title"], cfg["desc"], cfg["og"])
        body = head + marker_loc + cfg["loc"] + suffix
        body = body.replace(OLD_FAQ1, cfg["faq1"])
        body = body.replace("Marylebone Picture Hanging FAQs", f"{display} Picture Hanging FAQs")
        body = body.replace("Which parts of Marylebone do you cover?", f"Which parts of {display} do you cover?")
        body = body.replace(
            "Professional picture hanging and art installation services across Marylebone and Central London.",
            f"Professional picture hanging and art installation services across {display} and Central London.",
        )
        body = body.replace(
            "We regularly coordinate with designers, estate managers, and landlords in Marylebone.",
            f"We regularly coordinate with designers, estate managers, and landlords in {display}.",
        )
        out = ROOT / "public" / "locations" / f"{slug}.html"
        out.write_text(body, encoding="utf-8")
        print("Wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
