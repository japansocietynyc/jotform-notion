import requests
from config import JOTFORM_API_KEY, JOTFORM_ID
def fetch_submissions(limit=1000):
    url = f"https://api.jotform.com/form/{JOTFORM_ID}/submissions?apiKey={JOTFORM_API_KEY}&limit={limit}"
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception(f"Failed to fetch: {res.status_code}")
    return res.json().get("content", [])