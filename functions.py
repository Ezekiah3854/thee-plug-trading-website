"""helper functions"""

import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv(".env")

# environment variables
DATABASE = os.getenv("DATABASE")
USER = os.getenv("USER")
HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD")


def connect_db(user=USER, database=DATABASE, host=HOST, password=PASSWORD):
    """connect database"""
    try:
        conn = mysql.connector.connect(
            user=user, database=database, host=host, password=password
        )
        return conn
    except (
        mysql.connector.InterfaceError,
        mysql.connector.ProgrammingError,
        mysql.connector.DatabaseError
    ) as e:
        return f"Connection Failed: {e}"
