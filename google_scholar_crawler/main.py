from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os
import re

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}

def _to_int(value):
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return int(value)
    digits = re.sub(r"\D", "", str(value))
    return int(digits) if digits else None

raw_citedby = author.get('citedby')
citedby = _to_int(raw_citedby)
pub_citedby = sum((_to_int(v.get('num_citations')) or 0) for v in author['publications'].values())

if isinstance(raw_citedby, str) and '+' in raw_citedby:
    # Scholar may return "1000+" for profile-level citations; use publication sums when available.
    if pub_citedby > 0:
        citedby = pub_citedby
elif citedby is None and pub_citedby > 0:
    citedby = pub_citedby

author['citedby'] = str(citedby) if citedby is not None else raw_citedby

print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
