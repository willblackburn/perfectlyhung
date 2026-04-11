"""Generate West London location pages from marylebone.html (split + replace).

Run from repo root: python scripts/generate_west_london_locations.py

Then register each new file in vite.config.js and public/sitemap.xml.
"""
from __future__ import annotations

from pathlib import Path

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


def head_html_west(slug: str, display: str, title: str, desc: str, og: str) -> str:
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
        'Precision placement for homes, flats, and commercial spaces across West London."',
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


def L(
    slug: str,
    display: str,
    title: str,
    desc: str,
    og: str,
    span: str,
    mail_q: str,
    faq1: str,
    intro: str,
    btn: str,
    h2: str,
    h2_p: str,
    bullets: tuple[str, str, str, str],
    h3: str,
    p1: str,
    p2: str,
    img_alt: str,
) -> dict:
    return {
        "slug": slug,
        "display": display,
        "title": title,
        "desc": desc,
        "og": og,
        "faq1": faq1,
        "loc": location_section(
            display,
            span,
            f"Picture Hanging Services in {display}",
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
        ),
    }


AREAS = [
    L(
        "chelsea",
        "Chelsea",
        "Picture Hanging Service Chelsea, London SW3 | Perfectly Hung",
        "Professional picture hanging &amp; art installation in Chelsea, London SW3. Perfect alignment for artwork, mirrors &amp; gallery walls across SW3 &amp; SW10.",
        "gallery-006.webp",
        "Chelsea, London SW3",
        "Request%20a%20Chelsea%20Install",
        """                <p class="font-clamp-p2">
                  We cover Chelsea from Sloane Square and Kings Road through to Chelsea Embankment and World's End, including SW3 and SW10 Chelsea streets. We
                  also work South Kensington, Fulham, and Battersea edges when your building is quickest for our Chelsea team.
                </p>""",
        """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Chelsea. From stucco townhouses and
              garden squares to river-facing apartments and basement galleries, we install artwork, mirrors, and gallery walls with laser-precise alignment. We
              choose fixings for marble chimneypieces, silk walls, and modern lightweight partitions. We also offer
              <a href="/curtain-fitting.html">curtain and blind fitting</a> for Chelsea homes.""",
        "Request a Chelsea Install",
        "Trusted installers for SW3 &amp; SW10",
        """We work with homeowners, interior designers, and galleries throughout Chelsea. Whether you are refreshing a family house off the Kings Road or
              dressing a pied-à-terre, every installation is measured, levelled, and finished to a high standard.""",
        (
            "Laser-level picture hanging and gallery walls for Chelsea drawing rooms, bedrooms, and basement cinemas",
            "Secure mirror and heavy artwork installation on period plaster, brick, and feature stone",
            "Discreet service for concierge buildings and private mews with tight access",
            "Coverage from Sloane Square and Duke of York Square through to Lots Road and the Embankment",
        ),
        "River-side &amp; garden-square installs",
        """Chelsea mixes heritage architecture with contemporary new-builds. We protect stone floors and stair runners, coordinate loading where streets are busy,
              and keep communication clear from survey to walk-through. Our <a href="/picture-hanging.html">picture hanging</a> covers salon walls, photography
              collections, and mirrors in en-suites.""",
        """Planning a full hang after a refurbishment? We advise on height, spacing, and lighting. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Chelsea property.""",
        "Picture hanging service in a Chelsea London property",
    ),
    L(
        "kensington",
        "Kensington",
        "Picture Hanging Service Kensington, London W8 | Perfectly Hung",
        "Professional picture hanging &amp; art installation in Kensington, London W8. Perfect alignment for artwork, mirrors &amp; gallery walls across W8 &amp; W14 edges.",
        "gallery-017.webp",
        "Kensington, London W8",
        "Request%20a%20Kensington%20Install",
        """                <p class="font-clamp-p2">
                  We cover Kensington from Kensington High Street and Kensington Gardens through to Olympia edges, including the W8 core and nearby W14 streets
                  that read as Kensington. We also work Notting Hill, Holland Park, and Chelsea boundaries when access suits a Kensington crew.
                </p>""",
        """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Kensington. From white-stucco villas and
              mansion flats to modern apartments, we install artwork, mirrors, and gallery walls with laser-precise alignment. We survey lath-and-plaster,
              brick, and stud walls carefully. We also offer <a href="/curtain-fitting.html">curtain and blind fitting</a> for Kensington properties.""",
        "Request a Kensington Install",
        "Trusted installers for W8 &amp; nearby W14",
        """We work with families, landlords, and design studios across Kensington. Whether you are hanging a single statement piece or a full collection, every
              job is measured, levelled, and finished with care.""",
        (
            "Laser-level picture hanging and gallery walls for double-height halls and formal reception rooms",
            "Secure mirror and heavy artwork installation suited to cornicing and picture rails",
            "Careful protection of parquet, rugs, and listed interior details",
            "Coverage from High Street Kensington through to Phillimore Gardens and Palace-adjacent streets",
        ),
        "Palace-side &amp; High Street installs",
        """Kensington combines embassies, museums, and some of London's finest residential stock. We align with building managers where needed and use fixings
              matched to your wall build-up. Our <a href="/picture-hanging.html">picture hanging</a> covers libraries, dining rooms, and children's spaces.""",
        """Need help sequencing a multi-room project? We advise on visual rhythm along corridors. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Kensington home.""",
        "Picture hanging service in a Kensington London property",
    ),
    L(
        "south-kensington",
        "South Kensington",
        "Picture Hanging Service South Kensington, London SW7 | Perfectly Hung",
        "Professional picture hanging &amp; art installation in South Kensington, London SW7. Perfect alignment for artwork, mirrors &amp; gallery walls across SW7.",
        "gallery-018.webp",
        "South Kensington, London SW7",
        "Request%20a%20South%20Kensington%20Install",
        """                <p class="font-clamp-p2">
                  We cover South Kensington from Exhibition Road and Brompton Oratory through to Onslow Square and Gloucester Road, including the SW7 postcode
                  area. We also work Knightsbridge, Chelsea, and Earl's Court fringes when your address sits on our South Kensington routes.
                </p>""",
        """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across South Kensington. From museum-adjacent
              apartments to stucco terraces and mansion blocks, we install artwork, mirrors, and gallery walls with laser-precise alignment. We are used to
              basement conversions and tall period ceilings. We also offer <a href="/curtain-fitting.html">curtain and blind fitting</a> for South Kensington
              homes.""",
        "Request a South Kensington Install",
        "Trusted installers for SW7",
        """We work with residents, academics, and international tenants across South Kensington. Whether you are dressing a rental between lets or fitting out a
              long-term home, every installation is measured, levelled, and finished to a high standard.""",
        (
            "Laser-level picture hanging and gallery walls for SW7 flats, duplexes, and family houses",
            "Secure mirror and heavy artwork installation on party walls and chimney breasts",
            "Quiet working practices suited to mansion-block neighbours",
            "Coverage around South Ken station, Old Brompton Road, and the streets toward Cromwell Road",
        ),
        "Museum quarter &amp; mansion blocks",
        """South Kensington is dense with period stock and busy pavements. We plan access through service entrances where available and protect common parts. Our
              <a href="/picture-hanging.html">picture hanging</a> covers prints, oils, and large mirrors in compact bathrooms.""",
        """Planning a hang before tenants arrive? We can align with inventory clerks. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your South Kensington property.""",
        "Picture hanging service in a South Kensington London property",
    ),
    L(
        "knightsbridge",
        "Knightsbridge",
        "Picture Hanging Service Knightsbridge, London SW1 &amp; SW7 | Perfectly Hung",
        "Professional picture hanging &amp; art installation in Knightsbridge, London. Perfect alignment for artwork, mirrors &amp; gallery walls across SW1X &amp; SW7.",
        "gallery-019.webp",
        "Knightsbridge, London SW1 &amp; SW7",
        "Request%20a%20Knightsbridge%20Install",
        """                <p class="font-clamp-p2">
                  We cover Knightsbridge from Hyde Park Corner and Brompton Road through to Montpelier Street and Lowndes Square, including SW1X and the SW7
                  Brompton edges. We also work Belgravia, South Kensington, and Mayfair-adjacent blocks when access routes suit our Knightsbridge team.
                </p>""",
        """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Knightsbridge. From penthouses above
              Brompton Road to mews houses and discreet apartments, we install artwork, mirrors, and gallery walls with laser-precise alignment. We understand
              luxury finishes and concierge protocols. We also offer <a href="/curtain-fitting.html">curtain and blind fitting</a> for Knightsbridge homes.""",
        "Request a Knightsbridge Install",
        "Trusted installers for SW1X &amp; SW7 Brompton",
        """We work with homeowners, art consultants, and estate teams across Knightsbridge. Whether you are curating a full reception wall or installing a
              single heavy mirror, every job is measured, levelled, and finished with care.""",
        (
            "Laser-level picture hanging and gallery walls for formal reception rooms and private galleries",
            "Secure mirror and heavy artwork installation on marble, stone, and high-spec dry lining",
            "White-glove handling for valuable pieces and bespoke frames",
            "Coverage along Brompton Road, Sloane Street approaches, and the squares behind Harrods",
        ),
        "Luxury retail &amp; residential SW7",
        """Knightsbridge demands flawless presentation. We coordinate with security, protect stone floors, and select fixings for tall ceilings. Our
              <a href="/picture-hanging.html">picture hanging</a> covers seasonal rotations and permanent salon layouts.""",
        """Need advice on sight lines from seating? We help balance weight across a room. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Knightsbridge property.""",
        "Picture hanging service in a Knightsbridge London property",
    ),
    L(
        "belgravia",
        "Belgravia",
        "Picture Hanging Service Belgravia, London SW1 | Perfectly Hung",
        "Professional picture hanging &amp; art installation in Belgravia, London SW1. Perfect alignment for artwork, mirrors &amp; gallery walls across SW1W.",
        "gallery-020.webp",
        "Belgravia, London SW1",
        "Request%20a%20Belgravia%20Install",
        """                <p class="font-clamp-p2">
                  We cover Belgravia from Eaton Square and Chester Square through to Elizabeth Street and Motcomb Street, including the SW1W postcode area. We
                  also work Victoria, Knightsbridge, and Westminster-adjacent streets when your site is closest to our Belgravia coverage.
                </p>""",
        """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Belgravia. From white-stucco terraces to
              mews houses and lateral apartments, we install artwork, mirrors, and gallery walls with laser-precise alignment. We respect listed interiors and
              discreet fixings. We also offer <a href="/curtain-fitting.html">curtain and blind fitting</a> for Belgravia properties.""",
        "Request a Belgravia Install",
        "Trusted installers for SW1W",
        """We work with homeowners, interior designers, and estate managers throughout Belgravia. Whether you are refreshing a drawing room or fitting out after
              a move, every installation is measured, levelled, and finished to a high standard.""",
        (
            "Laser-level picture hanging and gallery walls for Belgravia reception rooms and principal suites",
            "Secure mirror and heavy artwork installation on period plaster and chimney breasts",
            "Careful coordination with concierges and access windows",
            "Coverage across Eaton Square, Wilton Crescent, and the streets linking Victoria to Sloane Street",
        ),
        "Squares &amp; mews installs",
        """Belgravia combines grand architecture with quiet residential streets. We protect stair carpets, use shoe covers, and keep dust to a minimum. Our
              <a href="/picture-hanging.html">picture hanging</a> covers boardrooms, libraries, and family sitting rooms.""",
        """Planning a seasonal art rotation? We advise on spacing and lighting. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Belgravia property.""",
        "Picture hanging service in a Belgravia London property",
    ),
    L(
        "notting-hill",
        "Notting Hill",
        "Picture Hanging Service Notting Hill, London W11 | Perfectly Hung",
        "Professional picture hanging &amp; art installation in Notting Hill, London W11. Perfect alignment for artwork, mirrors &amp; gallery walls across W11.",
        "gallery-021.webp",
        "Notting Hill, London W11",
        "Request%20a%20Notting%20Hill%20Install",
        """                <p class="font-clamp-p2">
                  We cover Notting Hill from Portobello Road and Westbourne Grove through to Ladbroke Grove and Holland Park Avenue edges, including the W11
                  postcode area. We also work Holland Park, Shepherd's Bush, and Kensington boundaries when access suits our Notting Hill routes.
                </p>""",
        """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Notting Hill. From pastel townhouses and
              stucco conversions to compact flats above shops, we install artwork, mirrors, and gallery walls with laser-precise alignment. We plan for narrow
              stairs and busy market weekends. We also offer <a href="/curtain-fitting.html">curtain and blind fitting</a> for Notting Hill homes.""",
        "Request a Notting Hill Install",
        "Trusted installers for W11",
        """We work with residents, landlords, and creative studios across Notting Hill. Whether you are dressing a single feature wall or a full house, every
              installation is measured, levelled, and finished with care.""",
        (
            "Laser-level picture hanging and gallery walls for Ladbroke Grove terraces and Golborne Road flats",
            "Secure mirror and heavy artwork installation on party walls and Victorian brick",
            "Saturday-aware scheduling near Portobello where pavements are busiest",
            "Coverage across Westbourne Grove, Clarendon Road, and the streets toward Holland Park",
        ),
        "Colourful W11 streets",
        """Notting Hill mixes vibrant retail with tight residential grain. We protect hallways, coordinate with neighbours where needed, and keep noise low. Our
              <a href="/picture-hanging.html">picture hanging</a> covers photography walls, children's art, and mirrors in compact bathrooms.""",
        """Need a fast turnaround between tenancies? We can align with cleaners. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Notting Hill property.""",
        "Picture hanging service in a Notting Hill London property",
    ),
    L(
        "holland-park",
        "Holland Park",
        "Picture Hanging Service Holland Park, London W11 &amp; W14 | Perfectly Hung",
        "Professional picture hanging &amp; art installation in Holland Park, London. Perfect alignment for artwork, mirrors &amp; gallery walls across W11 &amp; W14.",
        "gallery-022.webp",
        "Holland Park, London W11 &amp; W14",
        "Request%20a%20Holland%20Park%20Install",
        """                <p class="font-clamp-p2">
                  We cover Holland Park from the park itself through to Abbotsbury Road, Addison Road, and the Phillimore Estate edges, spanning W11 and W14
                  addresses that sit around the park. We also work Notting Hill, Shepherd's Bush, and Kensington when your home is closest to our Holland Park
                  routes.
                </p>""",
        """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Holland Park. From double-fronted villas to
              lateral apartments with park views, we install artwork, mirrors, and gallery walls with laser-precise alignment. We choose fixings for tall
              ceilings and ornate cornicing. We also offer <a href="/curtain-fitting.html">curtain and blind fitting</a> for Holland Park homes.""",
        "Request a Holland Park Install",
        "Trusted installers for W11 &amp; W14",
        """We work with homeowners and design teams around Holland Park. Whether you are hanging a collection above a fireplace or fitting mirrors through a
              principal suite, every installation is measured, levelled, and finished to a high standard.""",
        (
            "Laser-level picture hanging and gallery walls for large reception rooms and garden-level spaces",
            "Secure mirror and heavy artwork installation on period plaster and stone chimney breasts",
            "Discreet service for private roads and gated mews",
            "Coverage from Holland Park itself through to Shepherd's Bush green and Olympia approaches",
        ),
        "Park-side villas &amp; apartments",
        """Holland Park is one of London's most sought-after enclaves. We coordinate loading on quiet streets, protect wide staircases, and communicate clearly
              with house managers. Our <a href="/picture-hanging.html">picture hanging</a> covers formal dining rooms, studies, and cinema snug walls.""",
        """Planning a hang after a basement dig or extension? We advise on new plaster curing times. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Holland Park property.""",
        "Picture hanging service in a Holland Park London property",
    ),
    L(
        "earls-court",
        "Earl's Court",
        "Picture Hanging Service Earl's Court, London SW5 | Perfectly Hung",
        "Professional picture hanging &amp; art installation in Earl's Court, London SW5. Perfect alignment for artwork, mirrors &amp; gallery walls across SW5.",
        "gallery-023.webp",
        "Earl's Court, London SW5",
        "Request%20a%20Earl%27s%20Court%20Install",
        """                <p class="font-clamp-p2">
                  We cover Earl's Court from the station and Earl's Court Road through to Kempsford Gardens and Philbeach Gardens, including the SW5 postcode
                  area. We also work South Kensington, West Brompton, and Fulham edges when your building sits on our Earl's Court routes.
                </p>""",
        """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Earl's Court. From mansion flats and
              stucco terraces to modern developments, we install artwork, mirrors, and gallery walls with laser-precise alignment. We survey Victorian brick,
              stud partitions, and refurbished cores. We also offer <a href="/curtain-fitting.html">curtain and blind fitting</a> for Earl's Court properties.""",
        "Request an Earl's Court Install",
        "Trusted installers for SW5",
        """We work with residents, sharers, and landlords across Earl's Court. Whether you are refreshing a rental or settling into a long-term home, every
              installation is measured, levelled, and finished with care.""",
        (
            "Laser-level picture hanging and gallery walls for SW5 flats, duplexes, and garden apartments",
            "Secure mirror and heavy artwork installation on party walls and chimney breasts",
            "Practical scheduling around station-side traffic and narrow hallways",
            "Coverage along Earl's Court Road, Warwick Road, and the streets toward West Brompton",
        ),
        "SW5 conversions &amp; mansion flats",
        """Earl's Court mixes Victorian stock with newer schemes. We protect common parts, use dust sheets, and keep communication clear. Our
              <a href="/picture-hanging.html">picture hanging</a> covers single pieces, rental-friendly layouts, and mirror installs in bathrooms.""",
        """Need a quick turnaround between tenancies? We can align with agents. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Earl's Court property.""",
        "Picture hanging service in an Earl's Court London property",
    ),
    L(
        "fulham",
        "Fulham",
        "Picture Hanging Service Fulham, London SW6 | Perfectly Hung",
        "Professional picture hanging &amp; art installation in Fulham, London SW6. Perfect alignment for artwork, mirrors &amp; gallery walls across SW6.",
        "gallery-014.webp",
        "Fulham, London SW6",
        "Request%20a%20Fulham%20Install",
        """                <p class="font-clamp-p2">
                  We cover Fulham from Fulham Road and Parsons Green through to Wandsworth Bridge and the river paths, including the SW6 postcode area. We also
                  work Chelsea, Hammersmith, and Putney fringes when your address is closest to our Fulham routes.
                </p>""",
        """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Fulham. From Victorian terraces and cottage
              rows to riverside apartments, we install artwork, mirrors, and gallery walls with laser-precise alignment. We choose fixings for cavity walls and
              refurbished interiors. We also offer <a href="/curtain-fitting.html">curtain and blind fitting</a> for Fulham homes.""",
        "Request a Fulham Install",
        "Trusted installers for SW6",
        """We work with families, young professionals, and landlords across Fulham. Whether you are dressing a family kitchen-diner or a basement cinema, every
              installation is measured, levelled, and finished to a high standard.""",
        (
            "Laser-level picture hanging and gallery walls for Fulham terraces, maisonettes, and new-builds",
            "Secure mirror and heavy artwork installation on brick, block, and stud-lined extensions",
            "River-side access awareness for mansion blocks and Thames Path adjacency",
            "Coverage from Parsons Green and Munster Village through to Sands End and Imperial Wharf approaches",
        ),
        "Parsons Green to riverside",
        """Fulham combines village-style streets with busy main roads. We plan parking and loading realistically, protect hall carpets, and keep sites tidy. Our
              <a href="/picture-hanging.html">picture hanging</a> covers children's rooms, open-plan living, and compact hall galleries.""",
        """Planning a hang after a loft conversion? We advise on new stud walls. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Fulham property.""",
        "Picture hanging service in a Fulham London property",
    ),
    L(
        "hammersmith",
        "Hammersmith",
        "Picture Hanging Service Hammersmith, London W6 | Perfectly Hung",
        "Professional picture hanging &amp; art installation in Hammersmith, London W6. Perfect alignment for artwork, mirrors &amp; gallery walls across W6.",
        "gallery-015.webp",
        "Hammersmith, London W6",
        "Request%20a%20Hammersmith%20Install",
        """                <p class="font-clamp-p2">
                  We cover Hammersmith from the Broadway and King Street through to Brook Green and the river at Hammersmith Bridge approaches, including the W6
                  postcode area. We also work Shepherd's Bush, Chiswick, and Fulham edges when your building sits on our Hammersmith routes.
                </p>""",
        """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Hammersmith. From mansion flats and period
              conversions to modern apartments, we install artwork, mirrors, and gallery walls with laser-precise alignment. We are used to busy high streets and
              service lifts. We also offer <a href="/curtain-fitting.html">curtain and blind fitting</a> for Hammersmith homes and offices.""",
        "Request a Hammersmith Install",
        "Trusted installers for W6",
        """We work with residents, landlords, and small businesses across Hammersmith. Whether you are refreshing a rental or fitting out a home office, every
              installation is measured, levelled, and finished with care.""",
        (
            "Laser-level picture hanging and gallery walls for W6 flats, duplexes, and live-work spaces",
            "Secure mirror and TV-adjacent art layouts for open-plan living",
            "Practical scheduling around Broadway traffic and bridge closures when announced",
            "Coverage from Ravenscourt Park through to Brook Green and the riverfront",
        ),
        "Brook Green &amp; Broadway",
        """Hammersmith mixes offices with dense residential streets. We protect lifts and lobbies, communicate with concierges where present, and keep noise
              reasonable. Our <a href="/picture-hanging.html">picture hanging</a> covers reception areas, bedrooms, and compact hall galleries.""",
        """Need evening access after work? We can discuss slots. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Hammersmith property.""",
        "Picture hanging service in a Hammersmith London property",
    ),
    L(
        "chiswick",
        "Chiswick",
        "Picture Hanging Service Chiswick, London W4 | Perfectly Hung",
        "Professional picture hanging &amp; art installation in Chiswick, London W4. Perfect alignment for artwork, mirrors &amp; gallery walls across W4.",
        "gallery-016.webp",
        "Chiswick, London W4",
        "Request%20a%20Chiswick%20Install",
        """                <p class="font-clamp-p2">
                  We cover Chiswick from Chiswick High Road and Turnham Green through to Bedford Park and the river at Chiswick Mall, including the W4 postcode
                  area. We also work Hammersmith, Acton, and Barnes edges when your home is closest to our Chiswick routes.
                </p>""",
        """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Chiswick. From Arts-and-Crafts houses and
              Bedford Park villas to family terraces and modern apartments, we install artwork, mirrors, and gallery walls with laser-precise alignment. We
              respect period joinery and picture rails. We also offer <a href="/curtain-fitting.html">curtain and blind fitting</a> for Chiswick homes.""",
        "Request a Chiswick Install",
        "Trusted installers for W4",
        """We work with families and design-led homeowners across Chiswick. Whether you are hanging a collection in a double-height hall or a single mirror in a
              boot room, every installation is measured, levelled, and finished to a high standard.""",
        (
            "Laser-level picture hanging and gallery walls for Chiswick family rooms, studies, and garden studios",
            "Secure mirror and heavy artwork installation on brick, lath-and-plaster, and modern extensions",
            "Careful protection of timber floors and original doors in Bedford Park stock",
            "Coverage from Turnham Green through to Strand-on-the-Green and Gunnersbury approaches",
        ),
        "Bedford Park &amp; riverside W4",
        """Chiswick combines village atmosphere with strong schools and commuter links. We plan realistic parking, use dust sheets, and keep communication clear.
              Our <a href="/picture-hanging.html">picture hanging</a> covers stair galleries, dining rooms, and children's spaces.""",
        """Planning a hang after a side return? We advise on new wall lines. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Chiswick property.""",
        "Picture hanging service in a Chiswick London property",
    ),
    L(
        "barnes",
        "Barnes",
        "Picture Hanging Service Barnes, London SW13 | Perfectly Hung",
        "Professional picture hanging &amp; art installation in Barnes, London SW13. Perfect alignment for artwork, mirrors &amp; gallery walls across SW13.",
        "gallery-024.webp",
        "Barnes, London SW13",
        "Request%20a%20Barnes%20Install",
        """                <p class="font-clamp-p2">
                  We cover Barnes from Barnes High Street and the village pond through to Castelnau and the river paths, including the SW13 postcode area. We also
                  work Mortlake, Putney, and Richmond edges when your address is closest to our Barnes routes.
                </p>""",
        """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Barnes. From Victorian cottages and family
              houses to riverside apartments, we install artwork, mirrors, and gallery walls with laser-precise alignment. We plan for narrow village lanes and
              tight parking. We also offer <a href="/curtain-fitting.html">curtain and blind fitting</a> for Barnes homes.""",
        "Request a Barnes Install",
        "Trusted installers for SW13",
        """We work with families and downsizers across Barnes. Whether you are dressing a new extension or refreshing a whole house, every installation is
              measured, levelled, and finished with care.""",
        (
            "Laser-level picture hanging and gallery walls for Barnes village houses and modern riverside flats",
            "Secure mirror and heavy artwork installation on chimney breasts and feature walls",
            "Village-aware access planning on Castelnau and White Hart Lane",
            "Coverage around the pond, Church Road, and the streets toward Olympic Studios",
        ),
        "Village &amp; riverside SW13",
        """Barnes mixes quiet residential streets with busy weekend traffic. We protect hallways, coordinate with neighbours where drives are shared, and keep
              sites tidy. Our <a href="/picture-hanging.html">picture hanging</a> covers family galleries, kitchen feature walls, and mirrors in cloakrooms.""",
        """Need help sequencing a move-in week? We can align with removers. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Barnes property.""",
        "Picture hanging service in a Barnes London property",
    ),
    L(
        "richmond",
        "Richmond",
        "Picture Hanging Service Richmond, London TW9 &amp; TW10 | Perfectly Hung",
        "Professional picture hanging &amp; art installation in Richmond, London. Perfect alignment for artwork, mirrors &amp; gallery walls across TW9 &amp; TW10.",
        "gallery-025.webp",
        "Richmond, London TW9 &amp; TW10",
        "Request%20a%20Richmond%20Install",
        """                <p class="font-clamp-p2">
                  We cover Richmond from Richmond Hill and the town centre through to North Sheen, Kew Bridge approaches, and Ham pockets within TW10, including
                  core TW9 and TW10 Richmond addresses. We also work Barnes, Twickenham, and Putney edges when your home is closest to our Richmond routes.
                </p>""",
        """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Richmond. From Georgian and Victorian family
              homes to modern apartments near the river, we install artwork, mirrors, and gallery walls with laser-precise alignment. We respect cornicing and
              picture rails common in TW stock. We also offer <a href="/curtain-fitting.html">curtain and blind fitting</a> for Richmond properties.""",
        "Request a Richmond Install",
        "Trusted installers for TW9 &amp; TW10",
        """We work with families, professionals, and landlords across Richmond. Whether you are hanging a collection with a view of the river or dressing a
              garden-facing study, every installation is measured, levelled, and finished to a high standard.""",
        (
            "Laser-level picture hanging and gallery walls for Richmond Hill houses and town-centre apartments",
            "Secure mirror and heavy artwork installation on period plaster and modern dry-lined extensions",
            "Hill-aware access planning where pavements are steep and parking is tight",
            "Coverage from Richmond Green through to Petersham and Sheen approaches",
        ),
        "Hill, Green &amp; riverside",
        """Richmond combines parkland with dense family streets. We plan realistic arrival times, protect stair runners, and keep communication clear. Our
              <a href="/picture-hanging.html">picture hanging</a> covers dining rooms, studies, and cinema rooms.""",
        """Planning a hang after a loft or basement project? We advise on fixing into new builds. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Richmond property.""",
        "Picture hanging service in a Richmond London property",
    ),
    L(
        "putney",
        "Putney",
        "Picture Hanging Service Putney, London SW15 | Perfectly Hung",
        "Professional picture hanging &amp; art installation in Putney, London SW15. Perfect alignment for artwork, mirrors &amp; gallery walls across SW15.",
        "gallery-002.webp",
        "Putney, London SW15",
        "Request%20a%20Putney%20Install",
        """                <p class="font-clamp-p2">
                  We cover Putney from Putney High Street and the river bridges through to Roehampton Lane approaches and West Putney streets, including the SW15
                  postcode area. We also work Wandsworth, Barnes, and Fulham edges when your address sits on our Putney routes.
                </p>""",
        """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Putney. From Victorian semis and Edwardian
              terraces to mansion flats and new-builds, we install artwork, mirrors, and gallery walls with laser-precise alignment. We survey party walls and
              chimney breasts carefully. We also offer <a href="/curtain-fitting.html">curtain and blind fitting</a> for Putney homes.""",
        "Request a Putney Install",
        "Trusted installers for SW15",
        """We work with families, sharers, and landlords across Putney. Whether you are refreshing a rental near the station or settling a long-term home by the
              river, every installation is measured, levelled, and finished with care.""",
        (
            "Laser-level picture hanging and gallery walls for Putney family houses, maisonettes, and apartments",
            "Secure mirror and heavy artwork installation on brick and modern lightweight partitions",
            "Bridge-aware scheduling when central London access is part of your day",
            "Coverage from Putney Bridge through to East Putney and Putney Heath edges",
        ),
        "High Street to heath",
        """Putney combines strong schools with busy commuting streets. We protect hall carpets, use dust sheets, and keep noise reasonable. Our
              <a href="/picture-hanging.html">picture hanging</a> covers stair galleries, open-plan kitchens, and compact flats.""",
        """Need a Saturday slot after rugby traffic? We can discuss timing. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Putney property.""",
        "Picture hanging service in a Putney London property",
    ),
    L(
        "wandsworth",
        "Wandsworth",
        "Picture Hanging Service Wandsworth, London SW18 | Perfectly Hung",
        "Professional picture hanging &amp; art installation in Wandsworth, London SW18. Perfect alignment for artwork, mirrors &amp; gallery walls across SW18.",
        "gallery-026.webp",
        "Wandsworth, London SW18",
        "Request%20a%20Wandsworth%20Install",
        """                <p class="font-clamp-p2">
                  We cover Wandsworth from Old York Road and Wandsworth Town through to Southfields and Earlsfield approaches within SW18. We also work Battersea,
                  Putney, and Clapham fringes when your building is closest to our Wandsworth routes.
                </p>""",
        """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Wandsworth. From Victorian terraces and
              Tonsleys-style streets to new developments near the town centre, we install artwork, mirrors, and gallery walls with laser-precise alignment. We
              choose fixings for cavity walls and refurbished cores. We also offer <a href="/curtain-fitting.html">curtain and blind fitting</a> for Wandsworth
              homes.""",
        "Request a Wandsworth Install",
        "Trusted installers for SW18",
        """We work with young families, professionals, and landlords across Wandsworth. Whether you are dressing a compact flat or a full house, every
              installation is measured, levelled, and finished to a high standard.""",
        (
            "Laser-level picture hanging and gallery walls for Wandsworth terraces, duplexes, and apartments",
            "Secure mirror and heavy artwork installation on party walls and chimney breasts",
            "Town-centre access awareness near the station and Southside shopping",
            "Coverage from Wandsworth Common edges through to Garratt Lane and Tooting borders",
        ),
        "Town centre &amp; commonside",
        """Wandsworth mixes busy retail with residential streets. We plan parking realistically, protect lifts, and keep sites tidy. Our
              <a href="/picture-hanging.html">picture hanging</a> covers family walls, rental refreshes, and home office niches.""",
        """Planning a hang after an extension? We advise on new stud lines. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Wandsworth property.""",
        "Picture hanging service in a Wandsworth London property",
    ),
    L(
        "battersea",
        "Battersea",
        "Picture Hanging Service Battersea, London SW11 | Perfectly Hung",
        "Professional picture hanging &amp; art installation in Battersea, London SW11. Perfect alignment for artwork, mirrors &amp; gallery walls across SW11.",
        "gallery-027.webp",
        "Battersea, London SW11",
        "Request%20a%20Battersea%20Install",
        """                <p class="font-clamp-p2">
                  We cover Battersea from Battersea Park and Albert Bridge through to Nine Elms and Clapham Junction approaches, including the SW11 postcode area.
                  We also work Chelsea, Wandsworth, and Clapham edges when your address is closest to our Battersea routes.
                </p>""",
        """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Battersea. From mansion blocks and riverside
              apartments to new towers and Victorian streets, we install artwork, mirrors, and gallery walls with laser-precise alignment. We understand
              concierge logistics and high-level glazing. We also offer <a href="/curtain-fitting.html">curtain and blind fitting</a> for Battersea homes.""",
        "Request a Battersea Install",
        "Trusted installers for SW11",
        """We work with owners, tenants, and design teams across Battersea. Whether you are dressing a compact flat or a lateral with river views, every
              installation is measured, levelled, and finished with care.""",
        (
            "Laser-level picture hanging and gallery walls for Battersea park-side homes and Nine Elms apartments",
            "Secure mirror and heavy artwork installation on dry-lined cores and feature concrete",
            "High-rise access coordination with site teams where required",
            "Coverage from Queenstown Road through to Lavender Hill approaches and the park perimeter",
        ),
        "Park, bridge &amp; Nine Elms",
        """Battersea is changing fast with new towers alongside period streets. We plan fixings for tall ceilings, protect stone floors, and keep communication
              clear. Our <a href="/picture-hanging.html">picture hanging</a> covers open-plan living walls and bedroom suites.""",
        """Need a hang aligned with furniture deliveries? We can sequence with your schedule. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Battersea property.""",
        "Picture hanging service in a Battersea London property",
    ),
    L(
        "clapham",
        "Clapham",
        "Picture Hanging Service Clapham, London SW4 | Perfectly Hung",
        "Professional picture hanging &amp; art installation in Clapham, London SW4. Perfect alignment for artwork, mirrors &amp; gallery walls across SW4.",
        "gallery-028.webp",
        "Clapham, London SW4",
        "Request%20a%20Clapham%20Install",
        """                <p class="font-clamp-p2">
                  We cover Clapham from Clapham Common North and South sides through to Northcote Road, Abbeville Village, and Clapham High Street, including the
                  SW4 postcode area. We also work Battersea, Brixton, and Balham edges when your home sits on our Clapham routes.
                </p>""",
        """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Clapham. From Victorian terraces and
              conversions to mansion flats and new-builds, we install artwork, mirrors, and gallery walls with laser-precise alignment. We plan for busy common
              weekends and narrow hallways. We also offer <a href="/curtain-fitting.html">curtain and blind fitting</a> for Clapham homes.""",
        "Request a Clapham Install",
        "Trusted installers for SW4",
        """We work with sharers, families, and landlords across Clapham. Whether you are refreshing a rental between lets or settling a long-term home, every
              installation is measured, levelled, and finished to a high standard.""",
        (
            "Laser-level picture hanging and gallery walls for Clapham period houses, garden flats, and duplexes",
            "Secure mirror and heavy artwork installation on party walls and chimney breasts",
            "Common-aware scheduling where pavements and parking are busiest",
            "Coverage around the Old Town, Northcote Road, and the streets toward Stockwell",
        ),
        "Common-side &amp; Old Town",
        """Clapham combines vibrant nightlife with family streets. We protect stair carpets, keep evening noise reasonable where asked, and communicate clearly.
              Our <a href="/picture-hanging.html">picture hanging</a> covers stair galleries, kitchen feature walls, and compact flats.""",
        """Need a fast turnaround for a listing shoot? We can prioritise key walls. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Clapham property.""",
        "Picture hanging service in a Clapham London property",
    ),
    L(
        "shepherds-bush",
        "Shepherd's Bush",
        "Picture Hanging Service Shepherd's Bush, London W12 | Perfectly Hung",
        "Professional picture hanging &amp; art installation in Shepherd's Bush, London W12. Perfect alignment for artwork, mirrors &amp; gallery walls across W12.",
        "gallery-006.webp",
        "Shepherd's Bush, London W12",
        "Request%20a%20Shepherd%27s%20Bush%20Install",
        """                <p class="font-clamp-p2">
                  We cover Shepherd's Bush from Westfield and the Uxbridge Road through to Askew Road, Wood Lane, and White City edges, including the W12 postcode
                  area. We also work Holland Park, Hammersmith, and Notting Hill fringes when your address is closest to our Shepherd's Bush routes.
                </p>""",
        """Perfectly Hung provides professional <a href="/picture-hanging.html">picture hanging services</a> across Shepherd's Bush. From Victorian terraces and
              mansion flats to new developments around White City, we install artwork, mirrors, and gallery walls with laser-precise alignment. We plan for busy
              retail weekends and compact access. We also offer <a href="/curtain-fitting.html">curtain and blind fitting</a> for Shepherd's Bush homes.""",
        "Request a Shepherd's Bush Install",
        "Trusted installers for W12",
        """We work with residents, landlords, and creatives across Shepherd's Bush. Whether you are dressing a single feature wall or a full flat, every
              installation is measured, levelled, and finished with care.""",
        (
            "Laser-level picture hanging and gallery walls for W12 flats, maisonettes, and townhouses",
            "Secure mirror and heavy artwork installation on brick, block, and stud-lined retrofits",
            "Retail-adjacent scheduling awareness near Westfield and Uxbridge Road",
            "Coverage from Goldhawk Road through to Wood Lane and the streets toward Brook Green",
        ),
        "W12 terraces &amp; White City",
        """Shepherd's Bush mixes dense housing with major retail and media campuses. We protect lifts and lobbies, coordinate loading sensibly, and keep sites
              tidy. Our <a href="/picture-hanging.html">picture hanging</a> covers compact hall galleries, open-plan living, and home offices.""",
        """Need evening access after the commute? We can discuss slots. For windows, our
              <a href="/curtain-fitting.html">curtain and blind fitting services</a> complete the look across your Shepherd's Bush property.""",
        "Picture hanging service in a Shepherd's Bush London property",
    ),
]


def main() -> None:
    for cfg in AREAS:
        slug = cfg["slug"]
        display = cfg["display"]
        head = head_html_west(slug, display, cfg["title"], cfg["desc"], cfg["og"])
        body = head + marker_loc + cfg["loc"] + suffix
        body = body.replace(OLD_FAQ1, cfg["faq1"])
        body = body.replace("Marylebone Picture Hanging FAQs", f"{display} Picture Hanging FAQs")
        body = body.replace("Which parts of Marylebone do you cover?", f"Which parts of {display} do you cover?")
        body = body.replace(
            "Professional picture hanging and art installation services across Marylebone and Central London.",
            f"Professional picture hanging and art installation services across {display} and West London.",
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
