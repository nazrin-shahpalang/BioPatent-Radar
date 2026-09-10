import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("LENS_API_KEY")
url = "https://api.lens.org/patent/search"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

query = {
    "bool": {
        "must": [
            {
                "bool": {
                    "should": [
                        {"match_phrase": {"title": "bio-based adhesive"}},
                        {"match_phrase": {"title": "bio-adhesive"}},
                        {"match_phrase": {"title": "biobased adhesive"}},
                        {"match_phrase": {"title": "plant-based adhesive"}},
                        {"match_phrase": {"title": "natural adhesive"}}
                    ],
                    "minimum_should_match": 1
                }
            },
            {"prefix": {"class_cpc.symbol": "C09J"}},
            {
                "range": {
                    "date_published": {
                        "gte": "2011-01-01",
                        "lte": "2026-12-31"
                    }
                }
            }
        ]
    }
}

include_fields = [
    "lens_id",
    "biblio.invention_title",
    "abstract",
    "date_published",
    "jurisdiction",
    "biblio.classifications_cpc.classifications.symbol"
]

def get_english_text(field):
    if isinstance(field, list):
        for item in field:
            if item.get("lang") == "en":
                return item.get("text")
        return field[0].get("text") if field else None
    elif isinstance(field, dict):
        return field.get("text")
    return field

all_records = []
page_size = 100
start = 0
total = None

while total is None or start < total:
    body = {
        "query": query,
        "from": start,
        "size": page_size,
        "include": include_fields
    }
    response = requests.post(url, headers=headers, json=body)
    if response.status_code != 200:
        print("Error:", response.text)
        break

    data = response.json()
    total = data.get("total", 0)
    records = data.get("data", [])

    for r in records:
        title = get_english_text(r.get("biblio", {}).get("invention_title"))
        abstract = get_english_text(r.get("abstract"))
        cpc_list = r.get("biblio", {}).get("classifications_cpc", {}).get("classifications", [])
        cpc_symbols = [c.get("symbol") for c in cpc_list]

        all_records.append({
            "lens_id": r.get("lens_id"),
            "title": title,
            "abstract": abstract,
            "date_published": r.get("date_published"),
            "jurisdiction": r.get("jurisdiction"),
            "cpc_codes": "; ".join(cpc_symbols)
        })

    print(f"Fetched {len(records)} records (start={start}, total={total})")
    start += page_size
    time.sleep(6)

df = pd.DataFrame(all_records)
os.makedirs("data", exist_ok=True)
df.to_csv("data/bio_adhesive_patents.csv", index=False)
print(f"\nSaved {len(df)} records to data/bio_adhesive_patents.csv")