from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='template')

@app.route('/')
def root():
    return render_template("redirection_page.html", code=302)

@app.route("/profile")
def profile():
    return render_template("profile.html", random_number=random.random())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
