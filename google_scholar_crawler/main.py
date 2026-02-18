from scholarly import scholarly, ProxyGenerator
import json
from datetime import datetime
import os
import re
import urllib.request


def _to_int(value):
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return int(value)
    digits = re.sub(r"\D", "", str(value))
    return int(digits) if digits else None


def _fetch_citations_from_mirror(scholar_id):
    if not scholar_id:
        return None
    profile_url = f"https://scholar.google.com/citations?user={scholar_id}&hl=en"
    mirror_url = "https://r.jina.ai/http://scholar.google.com/citations?user={}&hl=en".format(scholar_id)
    try:
        with urllib.request.urlopen(mirror_url, timeout=20) as resp:
            text = resp.read().decode("utf-8", errors="ignore")
        m = re.search(r"Citations\s+([0-9,]+)", text, flags=re.IGNORECASE)
        if not m:
            return None
        return _to_int(m.group(1))
    except Exception:
        return None


scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID")
author = {}
scholarly_error = None

try:
    pg = ProxyGenerator()
    pg.FreeProxies()
    scholarly.use_proxy(pg)

    author = scholarly.search_author_id(scholar_id)
    scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
except Exception as e:
    scholarly_error = str(e)
    author = {}

author["updated"] = str(datetime.now())
publications = author.get("publications", [])
if isinstance(publications, list):
    author["publications"] = {v.get("author_pub_id", str(i)): v for i, v in enumerate(publications)}
elif isinstance(publications, dict):
    author["publications"] = publications
else:
    author["publications"] = {}

raw_citedby = author.get("citedby")
citedby = _to_int(raw_citedby)
pub_citedby = sum((_to_int(v.get("num_citations")) or 0) for v in author["publications"].values())

if isinstance(raw_citedby, str) and "+" in raw_citedby:
    if pub_citedby > 0:
        citedby = pub_citedby
elif citedby is None and pub_citedby > 0:
    citedby = pub_citedby

if citedby is None:
    mirror_citedby = _fetch_citations_from_mirror(scholar_id)
    if mirror_citedby is not None:
        citedby = mirror_citedby

if citedby is not None:
    author["citedby"] = str(citedby)
elif raw_citedby is not None:
    author["citedby"] = str(raw_citedby)
else:
    author["citedby"] = "N/A"

if scholarly_error:
    author["crawler_error"] = scholarly_error

print(json.dumps(author, indent=2))
os.makedirs("results", exist_ok=True)
with open("results/gs_data.json", "w") as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author['citedby']}",
    "color": "9cf",
}
with open("results/gs_data_shieldsio.json", "w") as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
