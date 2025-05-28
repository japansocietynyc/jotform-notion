import os
from dotenv import load_dotenv
load_dotenv()
JOTFORM_API_KEY = os.getenv("JOTFORM_API_KEY")
JOTFORM_ID = os.getenv("JOTFORM_ID")
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("DATABASE_ID")
CUTOFF_DATE_STR = os.getenv("CUTOFF_DATE", "2025-04-02")