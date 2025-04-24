"""thee plug trading website"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/')
def home():
    """landing page"""
    message = "thee plug trading website in development."
    return jsonify(message), 200
