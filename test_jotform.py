import os
import requests
from dotenv import load_dotenv

load_dotenv()

JOTFORM_API_KEY= os.getenv("JOTFORM_API_KEY")
JOTFORM_ID = os.getenv("JOTFORM_ID")

url = f"https://api.jotform.com/form/{JOTFORM_ID}/questions?apiKey={JOTFORM_API_KEY}"
response = requests.get(url)

if response.status_code == 200:
    print("Success")
    data = response.json().get("content", {})
    for qid, details in data.items():
        label = details.get("text", "")
        qtype = details.get("text", "")
        print(f"ID: {qid} | Label: {label} | Type: {qtype}")
else:
    print({response.status_code})
    print(response.text)