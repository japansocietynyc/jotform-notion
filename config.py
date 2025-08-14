import os
from dotenv import load_dotenv

# In GitHub Actions, secrets are automatically available as environment variables
if os.path.exists('.env'):
    load_dotenv()

# Environment variables
JOTFORM_API_KEY = os.getenv("JOTFORM_API_KEY")
JOTFORM_ID = os.getenv("JOTFORM_ID")
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("DATABASE_ID")
CUTOFF_DATE_STR = os.getenv("CUTOFF_DATE", "2025-04-02")

# For Validation 
required_vars = {
    "JOTFORM_API_KEY": JOTFORM_API_KEY,
    "JOTFORM_ID": JOTFORM_ID,
    "NOTION_API_KEY": NOTION_API_KEY,
    "DATABASE_ID": DATABASE_ID
}

missing_vars = [name for name, value in required_vars.items() if not value]
if missing_vars:
    raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")