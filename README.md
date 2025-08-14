[![Sync JotForm to Notion](https://github.com/japansocietynyc/jotform-notion/actions/workflows/sync.yml/badge.svg)](https://github.com/japansocietynyc/jotform-notion/actions/workflows/sync.yml)

# Jotform -> Notion Sync

This project syncs form submissions from Jotform to a Notion Database. 

## Features

- Parses Jotform answers and pushes them into Notion Database Rows
- Updates existing Form Submissions in Notion
- Automatically runs every 4 hours using Github Actions

# Setup 

1. Create `.env` file. (Don't commit to Repo)

DATABASE_ID
NOTION_API_KEY
JOTFORM_ID
JOTFORM_API_KEY

2. Install Dependancies:

pip install -r requirements.txt

3. Run python main.py

## Automation Frequency

This runs every 15 minutes using Github Actions
