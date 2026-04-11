"""Generate North London and North West London location pages from marylebone.html.

Run: python scripts/generate_north_london_locations.py
Then entries are already expected in vite.config.js and sitemap.xml (update after run if you add rows).
"""
from __future__ import annotations

from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
BASE = (ROOT / "public" / "locations" / "marylebone.html").read_text(encoding="utf-8")

marker_loc = "<!-- Location Content -->\n"
marker_faq = "\n\n    <!-- FAQ & Footer Section -->"

if marker_loc not in BASE or marker_faq not in BASE:
    raise SystemExit("markers not found in marylebone.html")

a, rest = BASE.split(marker_loc, 1)
b, suffix = rest.split(marker_faq, 1)
suffix = marker_faq + suffix

OLD_FAQ1 = """                <p class="font-clamp-p2">
                  We cover all of Marylebone, including Marylebone High Street, Baker Street, Harley Street, Wimpole Street, Portland Place, Chiltern Street, and
                  the W1U, W1G, and NW1 postcodes that fall within the area. We also work in neighbouring Fitzrovia, Mayfair, Paddington, and St John's Wood
                  when projects sit on the boundary.
                </p>"""

# Only files that exist under public/img/gallery/
OG_ROTATE = (
    "gallery-006.webp",
    "gallery-014.webp",
    "gallery-015.webp",
    "gallery-016.webp",
    "gallery-017.webp",
    "gallery-018.webp",
    "gallery-019.webp",
    "gallery-020.webp",
    "gallery-021.webp",
    "gallery-022.webp",
    "gallery-023.webp",
    "gallery-024.webp",
    "gallery-025.webp",
    "gallery-026.webp",
    "gallery-027.webp",
    "gallery-028.webp",
    "gallery-002.webp",
)


def head_html(slug: str, display: str, title: str, desc: str, og: str, region: str) -> str:
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
        f'Precision placement for homes, flats, and commercial spaces across {region}."',
    )
    h = h.replace("Picture Hanging Services Marylebone London | Perfectly Hung", f"Picture Hanging Services {display} London | Perfectly Hung")
    h = h.replace("https://perfectlyhung.uk/img/gallery/gallery-016.webp", f"https://perfectlyhung.uk/img/gallery/{og}")
    h = h.replace("Picture hanging service in a Marylebone London home", f"Picture hanging service in a {display} London home")
    return h


def location_section(
    display: str,
    span: str,
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

            <h1>Picture Hanging Services in {display}</h1>
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


# (slug, display, region, postcode_bit_for_desc, faq_para_lines (2), span, h2_title, h3_title, bullet4)
# faq: (line1, line2) without <p> wrapper — we wrap
RAW: list[tuple] = [
    (
        "hampstead",
        "Hampstead",
        "North London",
        "NW3",
        (
            "We cover Hampstead from Heath Street, Flask Walk, and Frognal through to South End Green and the NW3 streets around the Heath.",
            "We also work Swiss Cottage, Highgate borders, and West Hampstead edges when your address is quickest for our Hampstead team.",
        ),
        "Hampstead, London NW3",
        "Trusted installers for NW3",
        "Heath-side &amp; village homes",
        "Coverage across Fitzjohn's Avenue, Willow Road, and the approaches toward Swiss Cottage",
    ),
    (
        "hampstead-heath",
        "Hampstead Heath",
        "North London",
        "NW3",
        (
            "We cover Hampstead Heath-side addresses in NW3 from Parliament Hill and Gospel Oak approaches through to East Heath Road and Spaniards Inn edges.",
            "We also work Highgate, Dartmouth Park, and Hampstead village streets when your home sits on our Heath-side routes.",
        ),
        "Hampstead Heath, London NW3",
        "Trusted installers for Heath-side NW3",
        "Park-adjacent terraces &amp; apartments",
        "Coverage around Parliament Hill, South End Green, and the streets linking Gospel Oak to Highgate",
    ),
    (
        "highgate",
        "Highgate",
        "North London",
        "N6",
        (
            "We cover Highgate from Highgate Village and Highgate Hill through to Archway Road and the Pond Square area, including core N6 streets.",
            "We also work Crouch End, Muswell Hill, and Hampstead borders when access suits our Highgate crew.",
        ),
        "Highgate, London N6",
        "Trusted installers for N6",
        "Village lanes &amp; hilltop homes",
        "Coverage along Swains Lane, Southwood Lane, and the streets toward Archway and Waterlow Park",
    ),
    (
        "primrose-hill",
        "Primrose Hill",
        "North London",
        "NW1",
        (
            "We cover Primrose Hill from Regent's Park Road and Chalcot Square through to Gloucester Avenue and Albert Terrace, including NW1 Primrose streets.",
            "We also work Camden Town, Swiss Cottage, and St John's Wood fringes when your building is on our Primrose Hill routes.",
        ),
        "Primrose Hill, London NW1",
        "Trusted installers for NW1",
        "Regent's Park views &amp; pastel terraces",
        "Coverage around Primrose Hill Park, Chalk Farm, and the approaches toward Camden Lock",
    ),
    (
        "camden",
        "Camden",
        "North London",
        "NW1",
        (
            "We cover Camden from Camden High Street and Camden Lock through to Mornington Crescent and parts of Kentish Town borders within NW1.",
            "We also work Primrose Hill, King's Cross edges, and Regent's Canal-adjacent blocks when your site is closest to our Camden routes.",
        ),
        "Camden, London NW1",
        "Trusted installers for NW1",
        "Canal-side &amp; High Street installs",
        "Coverage along Parkway, Albert Street, and the streets toward Mornington Crescent",
    ),
    (
        "st-johns-wood",
        "St John's Wood",
        "North London",
        "NW8",
        (
            "We cover St John's Wood from Abbey Road and Hamilton Terrace through to Wellington Road and the NW8 streets around Regent's Park.",
            "We also work Maida Vale, Swiss Cottage, and Lisson Grove edges when your address sits on our St John's Wood routes.",
        ),
        "St John's Wood, London NW8",
        "Trusted installers for NW8",
        "Regent's Park &amp; villa streets",
        "Coverage along Circus Road, Grove End Road, and the approaches toward Lord's and Maida Vale",
    ),
    (
        "swiss-cottage",
        "Swiss Cottage",
        "North London",
        "NW3",
        (
            "We cover Swiss Cottage from Finchley Road and the O2 Centre through to Adelaide Road and Eton Avenue, including the NW3 Swiss Cottage core.",
            "We also work Hampstead, St John's Wood, and South Hampstead edges when access is quickest for our Swiss Cottage team.",
        ),
        "Swiss Cottage, London NW3",
        "Trusted installers for NW3",
        "Finchley Road &amp; mansion blocks",
        "Coverage around Fellows Road, Belsize Park approaches, and the streets toward South Hampstead",
    ),
    (
        "kentish-town",
        "Kentish Town",
        "North London",
        "NW5",
        (
            "We cover Kentish Town from Kentish Town Road and Fortress Road through to Gaisford Street and the NW5 core around the station.",
            "We also work Camden, Tufnell Park, and Gospel Oak edges when your building is on our Kentish Town routes.",
        ),
        "Kentish Town, London NW5",
        "Trusted installers for NW5",
        "Victorian terraces &amp; conversions",
        "Coverage along Brecknock Road, Leverton Street, and the streets toward Tufnell Park",
    ),
    (
        "islington",
        "Islington",
        "North London",
        "N1",
        (
            "We cover Islington from Upper Street and Essex Road through to Highbury Fields and Barnsbury squares, including the N1 postcode core.",
            "We also work Angel, Canonbury, and De Beauvoir Town edges when your address is closest to our Islington routes.",
        ),
        "Islington, London N1",
        "Trusted installers for N1",
        "Squares &amp; Victorian stock",
        "Coverage along Liverpool Road, Barnsbury Street, and the streets toward Highbury Corner",
    ),
    (
        "angel",
        "Angel",
        "North London",
        "N1",
        (
            "We cover the Angel from Upper Street and Islington Green through to City Road and Pentonville Road approaches within N1.",
            "We also work Clerkenwell edges, King's Cross fringes, and deeper Islington when your site suits an Angel-based crew.",
        ),
        "Angel, London N1",
        "Trusted installers for N1",
        "Upper Street &amp; period conversions",
        "Coverage around Duncan Terrace, Colebrooke Row, and the streets toward Essex Road",
    ),
    (
        "stoke-newington",
        "Stoke Newington",
        "North London",
        "N16",
        (
            "We cover Stoke Newington from Church Street and Stoke Newington High Street through to Clissold Park and Stamford Hill approaches within N16.",
            "We also work Dalston, Newington Green, and Stamford Hill edges when your address is on our Stoke Newington routes.",
        ),
        "Stoke Newington, London N16",
        "Trusted installers for N16",
        "Church Street &amp; park-side homes",
        "Coverage along Albion Road, Defoe Road, and the streets toward Manor House",
    ),
    (
        "crouch-end",
        "Crouch End",
        "North London",
        "N8",
        (
            "We cover Crouch End from Broadway and Topsfield Parade through to Hornsey Rise and the N8 streets around the clock tower.",
            "We also work Stroud Green, Highgate borders, and Harringay edges when your home sits on our Crouch End routes.",
        ),
        "Crouch End, London N8",
        "Trusted installers for N8",
        "Clock tower &amp; ladder roads",
        "Coverage along Park Road, Cecile Park, and the streets toward Finsbury Park",
    ),
    (
        "muswell-hill",
        "Muswell Hill",
        "North London",
        "N10",
        (
            "We cover Muswell Hill from Muswell Hill Broadway and Fortis Green through to Queens Avenue and Alexandra Park edges within N10.",
            "We also work East Finchley, Crouch End, and Bounds Green approaches when your address is closest to our Muswell Hill team.",
        ),
        "Muswell Hill, London N10",
        "Trusted installers for N10",
        "Broadway &amp; Alexandra views",
        "Coverage along Colney Hatch Lane, Pages Lane, and the streets toward Highgate Wood",
    ),
    (
        "finchley",
        "Finchley",
        "North London",
        "N2 &amp; N3",
        (
            "We cover Finchley from Finchley Central and North Finchley through to East Finchley and Ballards Lane within N2 and N3.",
            "We also work Golders Green, Hendon borders, and Muswell Hill approaches when your building is on our Finchley routes.",
        ),
        "Finchley, London N2 &amp; N3",
        "Trusted installers for N2 &amp; N3",
        "Suburban family streets",
        "Coverage along Regents Park Road, Woodside Park, and the streets toward Mill Hill borders",
    ),
    (
        "golders-green",
        "Golders Green",
        "North London",
        "NW11",
        (
            "We cover Golders Green from Golders Green Road and Finchley Road through to Brent Cross approaches and Hampstead Garden Suburb edges within NW11.",
            "We also work Hampstead, Hendon, and Childs Hill fringes when your address suits our Golders Green routes.",
        ),
        "Golders Green, London NW11",
        "Trusted installers for NW11",
        "Finchley Road &amp; suburban villas",
        "Coverage along North End Road, Woodstock Avenue, and the streets toward Hampstead Heath Extension",
    ),
    (
        "barnet",
        "Barnet",
        "North London",
        "EN5 &amp; NW7",
        (
            "We cover Chipping Barnet and High Barnet from Wood Street and Barnet High Street through to Hadley Green and the EN5 town centre.",
            "We also work Totteridge, Whetstone, and Mill Hill edges when your home is closest to our Barnet routes.",
        ),
        "Barnet, London EN5 &amp; NW7",
        "Trusted installers for EN5 &amp; NW7",
        "High Barnet &amp; Totteridge lanes",
        "Coverage along Barnet Hill, Mays Lane, and the streets toward Hadley Common",
    ),
    (
        "maida-vale",
        "Maida Vale",
        "North West London",
        "W9",
        (
            "We cover Maida Vale from Maida Avenue and Randolph Avenue through to Shirland Road and Little Venice approaches within W9.",
            "We also work St John's Wood, Queen's Park, and Paddington edges when your address is on our Maida Vale routes.",
        ),
        "Maida Vale, London W9",
        "Trusted installers for W9",
        "Canal-side mansion flats",
        "Coverage along Elgin Avenue, Lauderdale Road, and the streets toward Warwick Avenue",
    ),
    (
        "little-venice",
        "Little Venice",
        "North West London",
        "W9",
        (
            "We cover Little Venice from Browning's Pool and the Regents Canal towpath through to Warwick Avenue and Clifton Gardens within W9.",
            "We also work Maida Vale, Paddington, and Notting Hill borders when your mooring-side or mansion flat sits on our Little Venice routes.",
        ),
        "Little Venice, London W9",
        "Trusted installers for W9",
        "Regent's Canal &amp; stucco terraces",
        "Coverage along Formosa Street, Randolph Mews, and the streets toward Paddington Basin",
    ),
    (
        "kilburn",
        "Kilburn",
        "North West London",
        "NW6",
        (
            "We cover Kilburn from Kilburn High Road and Quex Road through to Brondesbury and West Hampstead borders within NW6.",
            "We also work Queen's Park, Maida Vale fringes, and Cricklewood edges when your building is closest to our Kilburn routes.",
        ),
        "Kilburn, London NW6",
        "Trusted installers for NW6",
        "High Road &amp; period conversions",
        "Coverage along Grange Park, Mazenod Avenue, and the streets toward Brondesbury Park",
    ),
    (
        "queens-park",
        "Queen's Park",
        "North West London",
        "NW6",
        (
            "We cover Queen's Park from Salusbury Road and Lonsdale Road through to the park perimeter and Kensal Rise approaches within NW6.",
            "We also work Kilburn, Maida Vale edges, and Notting Hill borders when your address suits our Queen's Park routes.",
        ),
        "Queen's Park, London NW6",
        "Trusted installers for NW6",
        "Salusbury Road &amp; park-side",
        "Coverage along Chevening Road, Ilbert Street, and the streets toward Kensal Green",
    ),
    (
        "willesden",
        "Willesden",
        "North West London",
        "NW10",
        (
            "We cover Willesden from Willesden High Road and Dollis Hill through to Harlesden borders and Neasden edges within NW10.",
            "We also work Queen's Park, Kensal Green, and Cricklewood fringes when your site is on our Willesden routes.",
        ),
        "Willesden, London NW10",
        "Trusted installers for NW10",
        "High Road &amp; family houses",
        "Coverage along Dudden Hill Lane, Roundwood Road, and the streets toward Neasden",
    ),
    (
        "harrow",
        "Harrow",
        "North West London",
        "HA1 &amp; HA2",
        (
            "We cover Harrow from Harrow on the Hill and Station Road through to North Harrow and South Harrow centres within HA1 and HA2.",
            "We also work Pinner, Stanmore, and Wembley edges when your address is closest to our Harrow routes.",
        ),
        "Harrow, Greater London HA1 &amp; HA2",
        "Trusted installers for HA1 &amp; HA2",
        "Hill village &amp; suburban streets",
        "Coverage along Roxeth Hill, Kenton Road, and the streets toward Northwick Park",
    ),
    (
        "wembley",
        "Wembley",
        "North West London",
        "HA9",
        (
            "We cover Wembley from Wembley High Road and Empire Way through to Alperton and Sudbury approaches within HA9.",
            "We also work Brent, Harrow borders, and Neasden edges when your building sits on our Wembley routes.",
        ),
        "Wembley, London HA9",
        "Trusted installers for HA9",
        "Stadium quarter &amp; suburban homes",
        "Coverage along Forty Avenue, Ealing Road, and the streets toward Stonebridge Park",
    ),
    (
        "brent",
        "Brent",
        "North West London",
        "NW &amp; HA",
        (
            "We cover Brent borough addresses from Kilburn and Queens Park through to Wembley, Harlesden, and Neasden within our Brent-wide NW and HA coverage.",
            "We also work Camden, Westminster, and Barnet fringes when your site is quickest for a Brent-based crew.",
        ),
        "Brent, North West London",
        "Trusted installers across Brent",
        "Borough-wide residential &amp; commercial",
        "Coverage linking Kilburn High Road, Harrow Road, and the approaches toward Wembley Park",
    ),
]


def faq_html(line1: str, line2: str) -> str:
    return f"""                <p class="font-clamp-p2">
                  {line1}
                  {line2}
                </p>"""


def build_area(row: tuple, og: str) -> dict:
    slug, display, region, pc, (l1, l2), span, h2, h3, b4 = row
    if slug == "harrow":
        title = f"Picture Hanging Service {display}, Greater London | Perfectly Hung"
    elif slug == "barnet":
        title = f"Picture Hanging Service {display}, Greater London | Perfectly Hung"
    else:
        title = f"Picture Hanging Service {display}, London | Perfectly Hung"
    desc = (
        f"Professional picture hanging &amp; art installation in {display}, London. "
        f"Perfect alignment for artwork, mirrors &amp; gallery walls across {pc}."
    )
    mail_q = quote(f"Request a {display} Install", safe="")
    btn = f"Request a {display} Install"
    intro = f"""Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across {display}. From Victorian terraces and
              mansion conversions to modern apartments and family houses, we install artwork, mirrors, and gallery walls with laser-precise alignment. We survey
              wall types and select fixings suited to period plaster, brick, and stud partitions typical of homes across {region}. We also offer
              <a href="/curtain-fitting.html">curtain and blind fitting</a> for {display} properties."""
    h2_p = f"""We work with homeowners, landlords, interior designers, and small businesses across {display}. Whether you are refreshing a single room or
              dressing a whole property, every installation is measured, levelled, and finished to a high standard."""
    bullets = (
        f"Laser-level picture hanging and gallery walls for {display} homes, flats, and reception rooms",
        f"Secure mirror and heavy artwork installation on brick, lath-and-plaster, and stud walls typical of {region} properties",
        "Discreet fixings, careful hallway protection, and tidy working practices in multi-occupancy buildings",
        b4,
    )
    p1 = f"""{display} combines dense Victorian and Edwardian stock with busy high streets and strong transport links. We coordinate access, protect stair
              carpets, and keep communication clear from survey to walk-through. Our <a href="/picture-hanging.html">picture hanging</a> covers salon walls,
              single statement pieces, and mirrors in bathrooms and dressing areas."""
    p2 = f"""Planning a hang after refurbishment or between tenancies? We advise on layout and lighting. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your {display} property."""
    img_alt = f"Picture hanging service in a {display} London property"
    loc = location_section(
        display,
        span,
        intro,
        mail_q,
        btn,
        h2,
        h2_p,
        bullets,
        h3,
        p1,
        p2,
        img_alt,
    )
    return {
        "slug": slug,
        "display": display,
        "region": region,
        "title": title,
        "desc": desc,
        "og": og,
        "faq1": faq_html(l1, l2),
        "loc": loc,
    }


def main() -> None:
    for i, row in enumerate(RAW):
        cfg = build_area(row, OG_ROTATE[i % len(OG_ROTATE)])
        slug = cfg["slug"]
        display = cfg["display"]
        region = cfg["region"]
        head = head_html(slug, display, cfg["title"], cfg["desc"], cfg["og"], region)
        body = head + marker_loc + cfg["loc"] + suffix
        body = body.replace(OLD_FAQ1, cfg["faq1"])
        body = body.replace("Marylebone Picture Hanging FAQs", f"{display} Picture Hanging FAQs")
        body = body.replace("Which parts of Marylebone do you cover?", f"Which parts of {display} do you cover?")
        body = body.replace(
            "Professional picture hanging and art installation services across Marylebone and Central London.",
            f"Professional picture hanging and art installation services across {display} and {region}.",
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
