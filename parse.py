import ast
field_mapping = {
    "60": "project_title",
    "53": "name",
    "56": "email",
    "72": "marketing_channels",
    "95": "target_live_date",
    "120": "send_date",
    "111": "delivery_date",
    "152": "video_release_date",
    "112": "assets",
    "126": "program_dedicated_send_date",
    "127": "membership_send_date",
    "128": "exclusive_invite_send_date",
    "130": "program_delivery_date",
    "68": "event_date",
    "85": "dept_code",
    "61": "description",
    "84": "additional_notes"
}
def parse_submission(answers):
    data = {field: "" for field in field_mapping.values()}
    for question_id, answer_data in answers.items():
        field = field_mapping.get(question_id)
        if not field:
            continue
        answer = answer_data.get("answer")
        if isinstance(answer, dict):
            data[field] = f"{answer.get('first', '')} {answer.get('last', '')}".strip()
        elif isinstance(answer, list):
            data[field] = answer
        elif isinstance(answer, str) and answer.startswith("[") and answer.endswith("]"):
            try:
                data[field] = ast.literal_eval(answer)
            except:
                data[field] = [answer.strip("[]")]
        else:
            data[field] = answer or ""
    return data