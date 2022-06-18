
from collections import UserString
from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.static_folder = 'static'


def chatbot_response(msg):
    output = requests.get("http://127.0.0.1:8000/answer", params={'question': msg, 'retriever' : 'Embedding', 'article_number' : 2})
    return output.json()['answer']


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)


if __name__ == "__main__":
    app.run(debug=True)
