"""masterplanfx investments website"""

import os
import datetime
from werkzeug.security import check_password_hash, generate_password_hash
import psycopg2
from flask import Flask, render_template, session, request, redirect, url_for, flash
from dotenv import load_dotenv
from functions import connect_db, validate_user_data

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

        # assign session
        session.clear()
        session['email'] = email
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/register", methods=["POST", "GET"])
def user_registration():
    """register page"""
    if request.method == "POST":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        location = request.form.get("location")

        return redirect(url_for("login"))
    return render_template("register.html",), 200


@app.get("/logout")
def logout() -> None:
    """logout user"""
    session.clear()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
