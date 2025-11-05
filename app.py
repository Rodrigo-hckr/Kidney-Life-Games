
from flask import Flask, render_template
from games.trivia import get_random_question

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/trivia")
def trivia():
    question = get_random_question()
    return render_template("trivia.html", question=question)

if __name__ == "__main__":
    app.run(debug=True)

