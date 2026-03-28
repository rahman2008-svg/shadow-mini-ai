from flask import Flask, request, jsonify, render_template
from memory import add_to_memory
from brain import get_answer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/teach')
def teach_page():
    return render_template('teach.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_msg = data.get('message')
    user_id = data.get('user_id', 'default')
    
    answer = get_answer(user_msg)
    if answer:
        reply = answer
    else:
        reply = "আমি এখনো এটা শিখিনি 😅"
    return jsonify({"reply": reply})

@app.route('/teach', methods=['POST'])
def teach():
    data = request.get_json()
    question = data.get('question')
    answer = data.get('answer')
    if not question or not answer:
        return jsonify({"message": "প্রশ্ন এবং উত্তর দিতে হবে!"}), 400

    add_to_memory(question, answer)
    return jsonify({"message": f"AI শিখেছে: {question} → {answer}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
