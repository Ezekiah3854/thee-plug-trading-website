"""thee plug trading website"""

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

print("location token: ", location_token)

# config sessions
app.secret_key = os.getenv("SECRET")
app.permanent_session_lifetime = datetime.timedelta(minutes=45)


@app.get("/")
def home():
    """landing page"""
    return render_template("home.html", location_token=location_token)


@app.get("/schedule-class")
def schedule_class():
    """schedule class page"""
    if session.get('lname') is None:
        flash("Login to access the page.")
        return redirect(url_for('login'))
    return render_template("class.html")


@app.get("/brokers")
def get_broker():
    """brokers page"""
    if session.get('lname') is None:
        flash("Login to access the page.")
        return redirect(url_for('login'))
    return render_template("brokers.html")


@app.get("/available-bots")
def available_bots():
    """available bots page"""
    if session.get('lname') is None:
        flash("Login to access the page.")
        return redirect(url_for('login'))
    return render_template("available_bots.html")


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

            query = "SELECT password, lname FROM crypto_plug_users WHERE email = %s"
            cursor.execute(query, [email])
            user = cursor.fetchone()

            if user is None:
                flash("User does not exit.")
                return render_template("login.html")

            db_password = user[0]

            if not check_password_hash(db_password, password):
                flash("Incorrect password")
                return render_template("login.html")
            print("ok upto password check")

            # assign session
            session.clear()
            session["lname"] = user[1]
            cursor.close()
            db.close()
            return redirect(url_for("home"))
        return render_template("login.html")
    except TypeError:
        cursor.close()
        db.close()
        flash("Server failure. Retry")
        return render_template("register.html", location_token=location_token)


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
                return render_template("register.html", location_token=location_token)

            # encryp password
            password = generate_password_hash(password)

            # store user in db
            query = "INSERT INTO crypto_plug_users(fname, lname, email, password, country)VALUES(%s, %s, %s, %s, %s)"
            cursor.execute(query, [fname, lname, email, password, location])
            db.commit()
            cursor.close()
            db.close()
            print("user created in db")
            return redirect(url_for("login"))
        return render_template("register.html", location_token=location_token), 200
    except TypeError as e:
        cursor.close()
        db.close()
        flash("Server failed. Retry.")
        return f"Registration failed {e}"
    except psycopg2.IntegrityError:
        cursor.close()
        db.close()
        flash("User email already exists.")
        return render_template("register.html", location_token=location_token)


@app.get("/logout")
def logout() -> None:
    """logout user"""
    session.clear()
    return redirect(url_for('home'))
