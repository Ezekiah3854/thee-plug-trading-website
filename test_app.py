"""unittests"""
import os
import unittest
import requests
from dotenv import load_dotenv
from functions import connect_db, validate_user_data

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
    
    def test_user_registration(self):
        """user registration"""
        res = requests.get("http://127.0.0.1:5000/register", timeout=10)
        self.assertEqual(200, res.status_code)
    
    def test_user_login(self):
        """user login"""
        res = requests.get("http://127.0.0.1:5000/login", timeout=10)
        self.assertEqual(200, res.status_code)
    
    def test_schedule_class(self):
        """access schedule class"""
        res = requests.get("http://127.0.0.1:5000/schedule-class", timeout=10)
        self.assertEqual(200, res.status_code)

class TestFunctions(unittest.TestCase):
    """test helper functions"""
    # with correct config
    def test_connect_db(self):
        """test connect db"""
        conn = connect_db()
        self.assertNotEqual(type(conn), str)

    # with incorrect password
    # def test_incorrect_db(self):
    #     """incorrect credential"""
    #     conn = connect_db(database="incorrect")
    #     self.assertEqual(type(conn), str)

    # test validation with correct credentials
    def test_validate_user_data(self):
        """correct credentials"""
        result = validate_user_data(
            "t@gmail.com",
            "t@Gmail.1",
            "t@Gmail.1",
            "Erick",
            "Onguso",
            "KE"
        )
        self.assertEqual(result, None)
    
    # test wrong email
    def test_validate_user_email(self):
        """wrong email"""
        result = validate_user_data(
            "tgmailcom",
            "t@Gmail.1",
            "t@Gmail.1",
            "Erick",
            "Onguso",
            "KE"
        )
        self.assertEqual(result, "Email must contain an '@' and '.'")

# -------running the test----------
# python -m unittest -v
# ---------------------------------
