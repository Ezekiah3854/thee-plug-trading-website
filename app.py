"""thee plug trading website"""

import os
import datetime
from flask import Flask, render_template, session, request, redirect, url_for, flash
from dotenv import load_dotenv
from functions import connect_db, validate_user_data

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
    db = connect_db()
    cursor = db.cursor()
    try:
        if request.method == "POST":
            # get the form data
            email = request.form["email"]
            password = request.form["password"]

            # validate inputs
            result = validate_user_data(email=email, password=password)

            if result is not None:
                flash(result)
                return redirect(url_for("login"))

            query = "SELECT password, lname FROM users WHERE email = %s"
            cursor.execute(query, [email])
            user = cursor.fetchone()

            if user is None:
                flash("User does not exit.")
                return render_template("login.html")

            # encrypt password: TODO
            if password != user[0]:
                flash("Incorrect password")
                return render_template("login.html")

            session.clear()
            session["lname"] = user[1]
            cursor.close()
            db.close()
            return redirect(url_for("home"))
        return render_template("login.html"), 200
    except Exception as e:
        cursor.close()
        db.close()
        return e


@app.route("/register", methods=["POST", "GET"])
def user_registration():
    """register page"""
    db = connect_db()
    cursor = db.cursor()
    try:
        if request.method == "POST":
            fname = request.form.get("fname")
            lname = request.form.get("lname")
            email = request.form.get("email")
            password = request.form.get("password")
            confirm_password = request.form.get("confirm_password")
            location = request.form.get("location")

            # validate inputs
            result = validate_user_data(
                email, password, confirm_password, fname, lname, location
            )

            if result is not None:
                flash(result)
                return render_template("register.html"), 200

            # store user in db
            query = "INSERT INTO users(fname, lname, email, password, country)VALUES(%s, %s, %s, %s, %s)"
            cursor.execute(query, [fname, lname, email, password, location])
            db.commit()
            cursor.close()
            db.close()
            print("user created in db")
            return redirect(url_for("login")), 200
        return render_template("register.html", location_token=location_token), 200
    except TypeError as e:
        cursor.close()
        db.close()
        return e
