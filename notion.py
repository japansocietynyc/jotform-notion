import requests
from datetime import datetime
import ast
from config import DATABASE_ID, NOTION_API_KEY

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}
def iso_date(date_str):
    if not date_str or date_str.lower() == "none":
        return None
    for fmt in ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d"]:
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except:
            continue
    return None
def find_page(submission_id):
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    payload = {
        "filter": {
            "property": "Submission ID",
            "rich_text": {"equals": submission_id}
        }
    }
    res = requests.post(url, headers=HEADERS, json=payload)
    return res.json().get("results", [])
def sync_submission(submission_id, submission_date, data):
    from notion_schema import build_notion_properties  
    props = build_notion_properties(data, submission_id, submission_date)
    existing = find_page(submission_id)
    if existing:
        page_id = existing[0]["id"]
        res = requests.patch(f"https://api.notion.com/v1/pages/{page_id}", headers=HEADERS, json={"properties": props})
        print(f"Updated: {submission_id}")
    else:
        payload = {"parent": {"database_id": DATABASE_ID}, "properties": props}
        res = requests.post("https://api.notion.com/v1/pages", headers=HEADERS, json=payload)
        print(f"Created: {submission_id}")
    if res.status_code not in [200, 201]:
        print(f"Error for {submission_id}: {res.text}")