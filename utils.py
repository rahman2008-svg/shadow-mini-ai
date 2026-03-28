from memory import add_to_memory
from brain import get_answer

def teach_ai(question, answer, user_id="admin", language="bangla"):
    add_to_memory(question, answer, user_id, language)
    return f"শিখানো হয়েছে: {question} -> {answer}"
