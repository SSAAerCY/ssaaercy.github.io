#!/usr/bin/env python3
"""Import a validated, dated ADS snapshot for this site's publications.

This offline step reads an existing snapshot. It never requests an API token or
contacts ADS, and leaves the last valid website data intact if validation fails.
"""

import argparse
from datetime import date
import json
import os
from pathlib import Path
import re
import tempfile
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SNAPSHOT = ROOT.parent / "CV/CV_YuanChen/ads_metrics/citations.json"
OUTPUT = ROOT / "_data/citation_metrics.json"
ADS_HOSTS = {"scixplorer.org", "ui.adsabs.harvard.edu"}
BIBCODE = re.compile(r"[A-Za-z0-9&.]{19}")
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


class ImportError(ValueError):
    """Snapshot data cannot safely be displayed on the website."""


def integer(value, label):
    if type(value) is not int or value < 0:
        raise ImportError(f"{label} must be a nonnegative integer.")
    return value


def ads_bibcode(url, label):
    if not isinstance(url, str):
        raise ImportError(f"{label} must be an ADS/SciX URL.")
    parsed = urlsplit(url)
    parts = unquote(parsed.path).strip("/").split("/")
    if (parsed.scheme != "https" or parsed.hostname not in ADS_HOSTS
            or parsed.username or parsed.password or parsed.query or parsed.fragment
            or len(parts) not in {2, 3} or parts[0] != "abs"
            or (len(parts) == 3 and parts[2] != "abstract")
            or not BIBCODE.fullmatch(parts[1])):
        raise ImportError(f"{label} must identify a valid ADS/SciX bibcode.")
    return parts[1]


def frontmatter_string(lines, field, filename):
    matches = [line.split(":", 1)[1].strip() for line in lines
               if re.match(r"^" + re.escape(field) + r"\s*:", line)]
    if len(matches) != 1:
        raise ImportError(f"{filename} needs exactly one {field} field.")
    value = matches[0]
    if value.startswith('"'):
        try:
            value, end = json.JSONDecoder().raw_decode(value)
        except json.JSONDecodeError as exc:
            raise ImportError(f"Invalid {field} in {filename}.") from exc
        remainder = matches[0][end:].strip()
        if remainder and not remainder.startswith("#"):
            raise ImportError(f"Unsupported {field} value in {filename}.")
    elif value.startswith("'"):
        match = re.fullmatch(r"'((?:[^']|'')*)'\s*(?:#.*)?", value)
        if not match:
            raise ImportError(f"Invalid {field} in {filename}.")
        value = match[1].replace("''", "'")
    else:
        value = re.split(r"\s+#", value, maxsplit=1)[0].strip()
    if not isinstance(value, str) or not value or any(c.isspace() for c in value):
        raise ImportError(f"{field} in {filename} must be a single nonempty string.")
    return value


def site_publications():
    publications = {}
    codes = set()
    files = sorted(path for path in (ROOT / "_publications").iterdir()
                   if path.is_file() and path.suffix in {".md", ".markdown", ".html"})
    for path in files:
        lines = path.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0] != "---" or "---" not in lines[1:]:
            raise ImportError(f"Missing front matter in {path.name}.")
        fields = lines[1:lines.index("---", 1)]
        key = frontmatter_string(fields, "bibkey", path.name)
        code = ads_bibcode(frontmatter_string(fields, "adsurl", path.name), path.name)
        if key in publications or code in codes:
            raise ImportError("Website publications contain a duplicate bibkey or ADS bibcode.")
        publications[key] = code
        codes.add(code)
    if not publications:
        raise ImportError("No website publications found.")
    return publications


def validated_data(snapshot, publications):
    if not isinstance(snapshot, dict) or type(snapshot.get("schema_version")) is not int or snapshot["schema_version"] != 1:
        raise ImportError("Unsupported snapshot schema.")
    if snapshot.get("source") not in {"NASA ADS / SciX", "NASA ADS/SciX"}:
        raise ImportError("The snapshot must come from NASA ADS/SciX.")
    if snapshot.get("self_citations") != "Included. No self-citation exclusion is applied.":
        raise ImportError("The snapshot must explicitly include self-citations.")
    as_of = snapshot.get("as_of")
    if not isinstance(as_of, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", as_of):
        raise ImportError("The snapshot needs an ISO as_of date.")
    try:
        observed = date.fromisoformat(as_of)
    except ValueError as exc:
        raise ImportError("Invalid snapshot as_of date.") from exc
    source_papers = snapshot.get("papers")
    if not isinstance(source_papers, list) or not source_papers:
        raise ImportError("The snapshot must contain all website publications.")
    papers = {}
    codes = set()
    for paper in source_papers:
        if not isinstance(paper, dict):
            raise ImportError("Invalid paper record in snapshot.")
        key = paper.get("key")
        code = paper.get("bibcode")
        if not isinstance(key, str) or not key or any(c.isspace() for c in key):
            raise ImportError("Invalid paper bibkey in snapshot.")
        if not isinstance(code, str) or not BIBCODE.fullmatch(code):
            raise ImportError(f"Invalid ADS bibcode for {key}.")
        if key in papers or code in codes:
            raise ImportError("Snapshot contains a duplicate bibkey or ADS bibcode.")
        count = integer(paper.get("citation_count"), f"Citation count for {key}")
        if paper.get("refereed") is not True:
            raise ImportError(f"{key} is not marked as a refereed publication in the ADS snapshot.")
        if ads_bibcode(paper.get("ads_url"), f"ADS URL for {key}") != code:
            raise ImportError(f"ADS URL does not match the bibcode for {key}.")
        papers[key] = {"citation_count": count, "bibcode": code, "ads_url": paper["ads_url"]}
        codes.add(code)
    if papers.keys() != publications.keys():
        raise ImportError("Snapshot bibkeys do not exactly match the website publications. Update the snapshot first.")
    if any(papers[key]["bibcode"] != code for key, code in publications.items()):
        raise ImportError("Snapshot ADS bibcodes do not match the website publications.")
    counts = sorted((paper["citation_count"] for paper in papers.values()), reverse=True)
    summary = {"paper_count": len(papers), "total_citations": sum(counts),
               "h_index": max((i for i, count in enumerate(counts, 1) if count >= i), default=0)}
    source_summary = snapshot.get("summary")
    source_summary = source_summary.get("all") if isinstance(source_summary, dict) else None
    if not isinstance(source_summary, dict):
        raise ImportError("The snapshot needs its all-publications summary.")
    for field, value in summary.items():
        if integer(source_summary.get(field), f"Summary {field}") != value:
            raise ImportError(f"Snapshot summary {field} does not match its paper records.")
    return {"schema_version": 1, "source": "NASA ADS/SciX",
            "source_url": "https://adsabs.github.io/help/actions/analyze",
            "as_of": as_of,
            "date_label": f"{MONTHS[observed.month - 1]} {observed.year}",
            "scope": "Refereed publications listed on this site; self-citations included.",
            "summary": summary, "papers": dict(sorted(papers.items()))}


def write_data(data):
    output_text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    temporary = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=OUTPUT.parent,
                                         prefix=".citation-metrics-", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(output_text)
        os.replace(temporary, OUTPUT)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", nargs="?", type=Path, default=DEFAULT_SNAPSHOT,
                        help="Existing ADS snapshot JSON; defaults to the local CV snapshot")
    args = parser.parse_args()
    try:
        snapshot = json.loads(args.snapshot.read_text(encoding="utf-8"))
        data = validated_data(snapshot, site_publications())
        write_data(data)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Citation import failed: {exc}\nPrevious website data was left unchanged.\n")
    summary = data["summary"]
    print(f"Imported {summary['paper_count']} publications: {summary['total_citations']} citations, "
          f"h-index {summary['h_index']} ({data['source']}, {data['date_label']}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
