"""Import BibTeX into Academic Pages without overwriting existing paper pages."""
import argparse
from datetime import date as calendar_date
import json
import re
import shutil
from pathlib import Path
from urllib.parse import urlsplit

import bibtexparser
from bibtexparser.bparser import BibTexParser
from pylatexenc.latex2text import LatexNodes2Text

ROOT = Path(__file__).resolve().parents[1]
JOURNALS = {r"\aap": "Astronomy & Astrophysics", r"\apjl": "The Astrophysical Journal Letters", r"\apj": "The Astrophysical Journal", r"\apjs": "The Astrophysical Journal Supplement Series"}
MONTHS = {name: index for index, name in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split(), 1)}
MONTHS.update({name: index for index, name in enumerate("january february march april may june july august september october november december".split(), 1)})


def text(value):
    return " ".join(LatexNodes2Text().latex_to_text(value).split())


def yaml_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    return json.dumps(value, ensure_ascii=False)


def publication_date(entry):
    """Return a validated sorting date and the precision supplied by BibTeX."""
    source_date = str(entry.get("date") or entry.get("year") or "").strip()
    if not re.fullmatch(r"\d{4}(?:-\d{2}(?:-\d{2})?)?", source_date):
        raise ValueError("Expected a year, YYYY-MM, or YYYY-MM-DD.")
    precision = {4: "year", 7: "month", 10: "day"}[len(source_date)]
    if precision == "year":
        month = str(entry.get("month") or "").strip().lower()
        if month:
            month_number = MONTHS.get(month)
            if month_number is None and month.isdigit():
                month_number = int(month)
            if month_number is None or not 1 <= month_number <= 12:
                raise ValueError(f"Invalid publication month: {month!r}.")
            source_date += f"-{month_number:02d}"
            precision = "month"
    # Jan 1 / day 1 are sorting anchors only; precision records the source.
    complete_date = source_date + ("-01-01" if precision == "year" else "-01" if precision == "month" else "")
    calendar_date.fromisoformat(complete_date)
    return complete_date, precision


def publisher_pdf(entry):
    """Use publisher PDF metadata; local files and arXiv are separate resources."""
    for candidate in (entry.get("pdfurl", ""), entry.get("url", "")):
        parsed = urlsplit(candidate)
        if (parsed.scheme in {"https", "http"}
                and parsed.hostname
                and parsed.hostname not in {"arxiv.org", "www.arxiv.org", "ui.adsabs.harvard.edu"}
                and parsed.path.endswith((".pdf", "/pdf"))):
            return candidate
    doi = entry.get("doi", "")
    if doi.startswith("10.1051/0004-6361/"):
        return "https://www.aanda.org/" + doi + "/pdf"
    if doi.startswith("10.3847/"):
        return "https://iopscience.iop.org/article/" + doi + "/pdf"
    return None


def main():
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument("bibfile", nargs="?", type=Path, default=ROOT / "_bibliography/publications.bib")
    args.add_argument("--replace", action="store_true", help="Replace imported pages, including manual changes")
    options = args.parse_args()
    parser = BibTexParser(common_strings=True)
    database = bibtexparser.loads(options.bibfile.read_text(encoding="utf-8"), parser=parser)
    if not database.entries:
        raise SystemExit("No bibliography entries found.")
    created = skipped = 0
    for entry in database.entries:
        key = entry["ID"]
        # BibTeX keys determine stable filenames and URLs.
        slug = re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")
        destination = ROOT / "_publications" / (slug + ".md")
        if destination.exists() and not options.replace:
            skipped += 1
            continue
        try:
            date, precision = publication_date(entry)
        except ValueError as error:
            raise SystemExit(f"Missing or invalid publication date for {key}: {error}") from error
        year = date[:4]
        authors = [text(author) for author in re.split(r"\s+and\s+", entry.get("author", ""))]
        first_author = bool(authors and re.match(r"Chen,\s*(Yuan|Y\.)", authors[0]))
        title = text(entry["title"])
        if key == "Chen2026":
            title = r"Probing the Ubiquity of Complex Ices in Protostars with JWST: The First Systematic Quantification of Weak Ice Bands between $\mathdefault{6.8}$ and $\mathdefault{7.9\,\mu m}$"
        if key == "Nazari2026":
            title = r"JOYS+: Analyses of $\mathdefault{OCN^{-}}$, $\mathdefault{N_{2}O}$, NO, and complex cyanides in ices: Thermal processing results in a modest increase of $\mathdefault{OCN^{-}}$ ice"
        metadata = {
            "title": title, "bibkey": key, "date": date, "date_precision": precision,
            "venue": JOURNALS.get(entry.get("journal", ""), text(entry.get("journal", ""))),
            "authors": "; ".join(authors), "first_author": first_author,
            "featured": first_author,
        }
        for field, source in [("volume", "volume"), ("article_number", "eid"), ("doi", "doi"), ("arxiv", "eprint"), ("adsurl", "adsurl"), ("status", "status")]:
            if entry.get(source): metadata[field] = entry[source]
        if not metadata.get("article_number") and entry.get("pages"):
            metadata["article_number"] = entry["pages"]
        paperurl = publisher_pdf(entry)
        if paperurl: metadata["paperurl"] = paperurl
        lines = ["---"] + [f"{field}: {yaml_value(value)}" for field, value in metadata.items()] + ["---", "", "{% include publication-authors.html authors=page.authors %}", "", f"*{metadata['venue']}* · {year}" + (f", {metadata['volume']}" if metadata.get('volume') else '') + (f", {metadata['article_number']}" if metadata.get('article_number') else ''), "", "{% include publication-links.html paper=page %}", ""]
        destination.write_text("\n".join(lines), encoding="utf-8")
        created += 1
    shutil.copy2(options.bibfile, ROOT / "files/publications.bib")
    print(f"Imported {created} paper pages; retained {skipped} existing pages.")


if __name__ == "__main__":
    main()
