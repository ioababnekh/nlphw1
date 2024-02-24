from flask import Flask, request, render_template

from chatbot import respond

app = Flask(__name__)


@app.route("/respond", methods=["POST"])
def respond_to_query():
    data = request.json
    query = data["query"]
    response, score = respond(query)
    return {"response": response, "score": str(score.max())}


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
