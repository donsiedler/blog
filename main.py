import requests
from flask import Flask, render_template

app = Flask(__name__)

FAKE_POSTS_URL = "https://api.npoint.io/c790b4d5cab58020d391"


@app.route("/")
def home():
    response = requests.get(FAKE_POSTS_URL)
    response.raise_for_status()
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
