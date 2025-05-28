import os 
import requests
from dotenv import load_dotenv

load_dotenv()

NOTION_API_KEY= os.getenv("NOTION_API_KEY")
DATABASE_ID= os.getenv("DATABASE_ID")

headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
response = requests.post(url, headers=headers)

if response.status_code == 200:
    print("Success")
    data = response.json()
    for page in data.get("results", []):
        title = page.get("properties", {}).get("Name", {}).get("title", [])
        if title:
            print("Found entry:", title[0]["text"]["content"])
else:
    print({response.status_code})
    print(response.text)

