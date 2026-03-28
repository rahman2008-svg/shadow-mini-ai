from flask import Flask, render_template, request, jsonify
from utils import teach_ai
from brain import get_answer
from context import save_context, get_context

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/teach")
def teach_page():
    return render_template("teach.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message")
    user_id = data.get("user_id", "default")
    
    save_context(user_id, user_msg)
    context = get_context(user_id)
    answer = get_answer(user_msg)
    
    if answer:
        reply = answer
    else:
        reply = "আমি এখনো এটা শিখিনি 😅"
    
    return jsonify({"reply": reply})

@app.route("/teach", methods=["POST"])
def teach():
    data = request.get_json()
    question = data.get("question")
    answer = data.get("answer")
    user_id = data.get("user_id", "admin")
    response = teach_ai(question, answer, user_id)
    return jsonify({"status": "success", "message": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
