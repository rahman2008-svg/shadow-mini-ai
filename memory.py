import json
import os

MEMORY_FILE = "memory.json"

if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump({"qa_data": [], "qa": {}}, f, ensure_ascii=False, indent=4)

def load_memory():
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return {"qa_data": [], "qa": {}}

def save_memory(data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_to_memory(question, answer, user_id="admin", language="bangla"):
    memory = load_memory()
    qa_id = str(len(memory["qa"]) + 1)
    memory["qa"][qa_id] = {
        "question": question,
        "answer": answer,
        "language": language,
        "added_by": user_id
    }
    memory["qa_data"].append({"question": question, "answer": answer, "language": language, "added_by": user_id})
    save_memory(memory)
