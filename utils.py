from memory import add_to_memory

def teach_ai(question, answer, language="bangla"):
    add_to_memory(question, answer, language)
    return f"শিখানো হয়েছে: {question} -> {answer}"
