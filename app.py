from flask import Flask, render_template, request, jsonify
from utils import add_to_memory, get_best_answer

app = Flask(__name__)

# -------------------
# Home Page (Chat)
# -------------------
@app.route('/')
def home():
    return render_template("index.html")  # Chat পেজ

# -------------------
# Teach Page
# -------------------
@app.route('/teach')
def teach():
    return render_template("teach.html")  # Teach AI পেজ

# -------------------
# Ask AI (Chat) Route
# -------------------
@app.route('/ask', methods=['POST'])
def ask_ai():
    data = request.get_json()
    question = data.get('question')
    if not question:
        return jsonify({"answer": "প্রশ্ন পাঠানো হয়নি!"})
    
    answer = get_best_answer(question)
    return jsonify({"answer": answer})

# -------------------
# Teach AI Route
# -------------------
@app.route('/teach_ai', methods=['POST'])
def teach_ai():
    data = request.get_json()
    question = data.get('question')
    answer = data.get('answer')
    
    if not question or not answer:
        return jsonify({"status": "error", "message": "প্রশ্ন বা উত্তর পাঠানো হয়নি"})
    
    add_to_memory(question, answer)
    return jsonify({"status": "success", "message": "AI শেখানো হয়েছে!"})

# -------------------
# Run Server
# -------------------
if __name__ == "__main__":
    # মোবাইল বা Termux এ চলার জন্য host 0.0.0.0
    app.run(host='0.0.0.0', port=8000, debug=True)
