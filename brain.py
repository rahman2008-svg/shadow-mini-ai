from memory import load_memory
from rapidfuzz import process, fuzz

def get_answer(user_question):
    memory = load_memory()
    questions = [q["question"] for q in memory["qa_data"]]
    if not questions:
        return None
    best_match = process.extractOne(user_question, questions, scorer=fuzz.token_sort_ratio)
    if best_match and best_match[1] > 70:
        idx = questions.index(best_match[0])
        return memory["qa_data"][idx]["answer"]
    return None
