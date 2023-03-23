import os
import requests
import smtplib
from flask import Flask, render_template, request

app = Flask(__name__)

FAKE_POSTS_URL = "https://api.npoint.io/c790b4d5cab58020d391"
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

@app.route("/")
def home():
    response = requests.get(FAKE_POSTS_URL)
    response.raise_for_status()
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        name = data["name"]
        email = data["email"]
        phone = data["phone"]
        message = data["message"]

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject: New contact form message\n\n"
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"Phone: {phone}\n"
                    f"Message: {message}"
            )

        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


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


if __name__ == "__main__":
    app.run()
