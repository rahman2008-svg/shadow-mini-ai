import json
import os

CONTEXT_FILE = "context.json"

if not os.path.exists(CONTEXT_FILE):
    with open(CONTEXT_FILE, "w", encoding="utf-8") as f:
        json.dump({}, f, ensure_ascii=False, indent=4)

def save_context(user_id, message):
    with open(CONTEXT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    if user_id not in data:
        data[user_id] = []
    data[user_id].append(message)
    if len(data[user_id]) > 50:  # Keep last 50 messages
        data[user_id] = data[user_id][-50:]
    with open(CONTEXT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_context(user_id):
    with open(CONTEXT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get(user_id, [])
