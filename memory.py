import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'w') as f:
            json.dump([], f)
    with open(MEMORY_FILE, 'r') as f:
        return json.load(f)

def add_to_memory(question, answer):
    memory = load_memory()
    memory.append({"question": question, "answer": answer})
    with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)
