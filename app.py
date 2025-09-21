import os
from dataclasses import dataclass
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.urandom(24)
load_dotenv()
PASSWORD = os.getenv("PASSWORD")
entries = []


@dataclass
class Entry:
    content: str
    timestamp: datetime = datetime.now()


@app.route("/")
def index():
    return render_template("index.html", entries=entries)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_password = request.form.get("password")
        if user_password == PASSWORD:
            session["logged_in"] = True
            flash("Login successful!", "success")
            return redirect(url_for("index"))
        else:
            flash("Incorrect password. Please try again.", "error")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("Logged out successfully.", "success")
    return redirect(url_for("index"))


@app.route("/add_entry", methods=["POST"])
def add_entry():
    content = request.form.get("content")
    if content:
        entry = Entry(content=content)
        entries.append(entry)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
