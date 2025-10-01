"""helper functions"""

import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import psycopg2

load_dotenv(".env")

# environment variables
DATABASE_URL = os.getenv("DATABASE_URL")


def connect_db():
    """connect database"""
    result = urlparse(DATABASE_URL)
    try:
        connection = psycopg2.connect(
            host=result.hostname,
            port=result.port,
            dbname=result.path[1:],
            user=result.username,
            password=result.password,
        )
        print("db connected")
        return connection
    except (
        psycopg2.InterfaceError,
        psycopg2.ProgrammingError,
        psycopg2.DatabaseError
    ) as e:
        return f"Connection Failed: {e}"


def validate_user_data(
    email: str = None,
    password: str = None,
    confirm_password: str = None,
    fname: str = None,
    lname: str = None,
    location: str = None,
):
    """validate user inputs upon registration and login"""
    message = None
    try:
        while message is None:
            # password mismatch
            if confirm_password is not None and password != confirm_password:
                message = "Passwords do not match!"
                break

            # include uppercase letters
            if not any(char.isupper() for char in password):
                message = "Password must contain a uppercase letter."
                break

            # include a digit
            if not any(char.isdigit() for char in password):
                message = "Password must contain a numeric digit."
                break

            # include a special char
            if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password):
                message = "Password must contain a special character."
                break

            # valid email
            if email is not None and ("@" not in email or "." not in email):
                message = "Email must contain an '@' and '.'"
                break

            if (fname is not None and len(fname) > 16) or (
                lname is not None and len(lname) > 16
            ):
                message = "Name exceeded limit."
                break
            if location is not None and len(location) > 16:
                message = "Location exceeded limit."
                break
            break
        return message
    except TypeError as e:
        return f"Registration failed. {e}"