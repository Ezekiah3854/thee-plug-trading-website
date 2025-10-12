import psycopg2
import os
from werkzeug.security import generate_password_hash, check_password_hash

def get_db_connection():
    """Create and return a new database connection."""
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn


def insert_user(email, username, password):
    """Insert a new user with hashed password."""
    conn = get_db_connection()
    cur = conn.cursor()
    hashed_pw = generate_password_hash(password)
    cur.execute("INSERT INTO users (email, username, password_hash) VALUES (%s, %s, %s)", (email, username, hashed_pw))
    conn.commit()
    cur.close()
    conn.close()


def get_user_by_email(email):
    """Fetch a user by email."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user


def verify_password(stored_password, provided_password):
    """Check if provided password matches stored hash."""
    return check_password_hash(stored_password, provided_password)
