"""thee plug trading website"""

import os
import datetime
from flask import Flask, render_template, session, request, redirect, url_for, flash
from dotenv import load_dotenv

# load environment variables
load_dotenv(".env")

app = Flask(__name__)

# get location token from env
location_token = os.getenv("LOCATION_TOKEN")

print("location token: ", location_token)

# config sessions
app.secret_key = os.getenv("SECRET")
app.permanent_session_lifetime = datetime.timedelta(minutes=30)


@app.get("/")
def home():
    """landing page"""
    return render_template("home.html", location_token=location_token), 200


@app.get("/schedule-class")
def schedule_class():
    """schedule class page"""
    return render_template("class.html"), 200

@app.get("/brokers")
def get_broker():
    """brokers page"""
    return render_template("brokers.html"), 200

@app.get("/available-bots")
def available_bots():
    """available bots page"""
    return render_template("available_bots.html"), 200

@app.route("/login", methods=["POST", "GET"])
def login():
    """login page"""
    if request.method == "POST":
        # get the form data
        email = request.form["email"]
        password = request.form["password"]

        # check if the user is valid
        if email == "nyagwayaezekiah@gmail.com" and password == "zack3854?":
            session["user"] = email
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password")
            # return to the login page with an error message
            return render_template("login.html"), 401

    return render_template("login.html"), 200

@app.route("/register", methods=["POST", "GET"])
def register():
    """register page"""
    if request.method == "POST":
        """register the user"""

    return render_template("register.html", location_token=location_token), 200
