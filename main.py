from datetime import datetime
from jotform import fetch_submissions
from notion import sync_submission
from config import CUTOFF_DATE_STR
def main():
    print("Running sync job...")
    cutoff = datetime.strptime(CUTOFF_DATE_STR, "%Y-%m-%d")
    submissions = fetch_submissions()
    for submission in submissions:
        sid = submission.get("id")
        created = submission.get("created_at")
        if not created:
            continue
        dt = datetime.strptime(created, "%Y-%m-%d %H:%M:%S")
        if dt < cutoff:
            continue
        answers = submission.get("answers", {})
        from parse import parse_submission  
        parsed = parse_submission(answers)
        sync_submission(sid, created, parsed)
if __name__ == "__main__":
    main()