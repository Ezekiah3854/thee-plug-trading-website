"""masterplanfx investments website"""

import os
import datetime
from werkzeug.security import check_password_hash, generate_password_hash
import psycopg2
from flask import Flask, render_template, session, request, redirect, url_for, flash
from dotenv import load_dotenv
from functions import get_user_by_email, insert_user, verify_password

# load environment variables
load_dotenv(".env")

app = Flask(__name__)

# get location token from env
location_token = os.getenv("LOCATION_TOKEN")

# config sessions
app.secret_key = os.urandom(24)  #Secret key for session encryption
app.permanent_session_lifetime = datetime.timedelta(minutes=45)


@app.get("/")
def home():
    """landing page"""
    return render_template("home.html", location_token=location_token)


@app.get("/schedule-class")
def schedule_class():
    """schedule class page"""
    if session.get('email') is None:
        flash("Login to access the page.")
        return redirect(url_for('login'))
    return render_template("class.html")


@app.get("/brokers")
def get_broker():
    """brokers page"""
    if session.get('email') is None:
        flash("Login to access the page.")
        return redirect(url_for('login'))
    return render_template("brokers.html")


@app.get("/available-bots")
def available_bots():
    """available bots page"""
    if session.get('email') is None:
        flash("Login to access the page.")
        return redirect(url_for('login'))
    return render_template("available_bots.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    """login page"""
    if request.method == "POST":
        # get the form data
        email = request.form["email"]
        password = request.form["password"]

        user = get_user_by_email(email)
        if user and verify_password(user[3], password):
            session['username'] = user[2]
            session['email'] = user[1]
            session.permanent = True
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid email or password.", "error")
    return render_template("login.html")

@app.route("/register", methods=["POST", "GET"])
def user_registration():
    """register page"""
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        try:
            insert_user(email, username, password)
            flash("Registration successful. Please login.", "success")
            return redirect(url_for("login"))
        except Exception as e:
            flash(f"Error: {e}", "error")
    return render_template("register.html",), 200

@app.get("/profile")
def profile():
    """user profile page"""
    if session.get('email') is None:
        flash("Login to access the page.")
        return redirect(url_for('login'))
    return render_template("profile.html")

@app.get("/logout")
def logout() -> None:
    """logout user"""
    session.clear()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)