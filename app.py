"""thee plug trading website"""

import os
import datetime
from flask import Flask, render_template, session
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
