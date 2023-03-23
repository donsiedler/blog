import requests
from flask import Flask, render_template, request

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


@app.route("/post/<int:post_id>")
def view_post(post_id):
    response = requests.get(FAKE_POSTS_URL)
    response.raise_for_status()
    all_posts = response.json()

    for post in all_posts:
        if post["id"] == post_id:
            blog_post = post
    return render_template("post.html", post=blog_post)


@app.route("/form-entry", methods=["POST"])
def receive_contact_form_data():
    data = request.form
    name = data["name"]
    email = data["email"]
    phone = data["phone"]
    message = data["message"]
    print(name, email, phone, message)
    return "<h1>Successfully sent your message</h1>"


if __name__ == "__main__":
    app.run()
