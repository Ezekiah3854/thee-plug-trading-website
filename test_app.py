"""unittests"""
import os
import unittest
import requests
from dotenv import load_dotenv
from functions import connect_db

load_dotenv('.env')

# environment variables
DATABASE = os.getenv("DATABASE")
USER = os.getenv("USER")
HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD")

class TestRoutes(unittest.TestCase):
    """test app routes"""
    def test_home(self):
        """home route"""
        res = requests.get("http://127.0.0.1:5000/", timeout=10)
        self.assertEqual(200, res.status_code)

class TestFunctions(unittest.TestCase):
    """test helper functions"""
    # with correct config
    def test_connect_db(self):
        """test connect db"""
        conn = connect_db()
        self.assertNotEqual(type(conn), str)

    # with incorrect password
    def test_incorrect_db(self):
        """incorrect credential"""
        conn = connect_db(database="incorrect")
        self.assertEqual(type(conn), str)

# -------running the test----------
# python -m unittest -v
# ---------------------------------
