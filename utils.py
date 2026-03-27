from tinydb import TinyDB, Query

db = TinyDB('memory.json')
qa_table = db.table('qa')
Question = Query()

def add_to_memory(question, answer):
    existing = qa_table.search(Question.question == question)
    if existing:
        qa_table.update({'answer': answer}, Question.question == question)
    else:
        qa_table.insert({'question': question, 'answer': answer})

def get_best_answer(user_question):
    all_qas = qa_table.all()
    if not all_qas:
        return "আমি এখনো এটি শিখিনি।"

    for qa in all_qas:
        if qa['question'].lower() == user_question.lower():
            return qa['answer']

    # Auto-learn: নতুন প্রশ্ন সেভ হবে "আমি এখনো এটি শিখিনি।"
    add_to_memory(user_question, "আমি এখনো এটি শিখিনি।")
    return "আমি এখনো এটি শিখিনি।"
