from notion import iso_date  
def build_notion_properties(data, submission_id, submission_date):
    props = {
        "Project Title": {"title": [{"text": {"content": data.get("project_title") or "Untitled"}}]},
        "Name": {"rich_text": [{"text": {"content": data.get("name", "")}}]},
        "Email": {"email": data.get("email", "")},
        "Marketing Channels": {
            "multi_select": [{"name": ch.strip()} for ch in data.get("marketing_channels", [])]
            if isinstance(data.get("marketing_channels"), list) else []
        },
        "Assets": {"rich_text": [{"text": {"content": data.get("assets", "")}}]},
        "Dept & Project Code": {"rich_text": [{"text": {"content": data.get("dept_code", "")}}]},
        "Project Description": {"rich_text": [{"text": {"content": data.get("description", "")}}]},
        "Additional Notes": {"rich_text": [{"text": {"content": data.get("additional_notes", "")}}]},
        "Submission ID": {"rich_text": [{"text": {"content": submission_id}}]}
    }
    date_fields = {
        "Event Date": data.get("event_date"),
        "Target Live Date": data.get("target_live_date"),
        "Send Date": data.get("send_date"),
        "Delivery Date": data.get("delivery_date"),
        "Video Release Date": data.get("video_release_date"),
        "Program Dedicated Send Date": data.get("program_dedicated_send_date"),
        "Membership Send Date": data.get("membership_send_date"),
        "Exclusive Invite Send Date": data.get("exclusive_invite_send_date"),
        "Program Delivery Date": data.get("program_delivery_date"),
        "Submission Date": submission_date
    }
    for key, value in date_fields.items():
        parsed = iso_date(value)
        if parsed:
            props[key] = {"date": {"start": parsed}}
    return props