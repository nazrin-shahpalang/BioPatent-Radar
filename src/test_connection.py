import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("LENS_API_KEY")

url = "https://api.lens.org/patent/search"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
body = {
    "query": {
        "match": {
            "title": "bio-based adhesive"
        }
    },
    "size": 5,
    "include": ["lens_id", "biblio.invention_title", "abstract", "date_published"]
}

response = requests.post(url, headers=headers, json=body)

print("Status code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print("Total results found:", data.get("total"))
    print("\nFirst results:\n")
    for record in data.get("data", []):
        title_info = record.get("biblio", {}).get("invention_title")
        if isinstance(title_info, list):
            title = title_info[0].get("text") if title_info else "N/A"
        elif isinstance(title_info, dict):
            title = title_info.get("text")
        else:
            title = title_info
        print("-", title, "|", record.get("date_published"))
else:
    print("Error:", response.text)