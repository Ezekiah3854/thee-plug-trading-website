"""thee plug trading website"""

import os
import datetime
from flask import Flask, render_template, session, request
from dotenv import load_dotenv

# load environment variables
load_dotenv(".env")

app = Flask(__name__)

# config sessions
app.secret_key = os.getenv("SECRET")
app.permanent_session_lifetime = datetime.timedelta(minutes=30)


@app.get("/")
def home():
    """landing page"""
    return render_template("home.html"), 200


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

@app.route("/register", methods=['GET', 'POST'])
def user_registration():
    """register a user"""
    if request.method == "POST":
        # do something
        pass
    return render_template('register.html')
