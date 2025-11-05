# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load word list
with open("testList.txt", encoding="utf-8") as f:
    word_list = [line.strip() for line in f.readlines()]

# Hardcoded hidden word
hidden_word = "تونس"

def get_color(word):
    if word not in word_list:
        return "black"
    idx = word_list.index(word)
    max_idx = len(word_list) - 1
    # closer to top = greener, farther = redder
    ratio = 1 - idx / max_idx  # 1 = top, 0 = bottom
    green = int(ratio * 255)
    red = int((1 - ratio) * 255)
    return f"rgb({red},{green},0)"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    word = request.json.get("word", "").strip()
    color = get_color(word)
    return jsonify({"word": word, "color": color})

if __name__ == "__main__":
    app.run(debug=True)
