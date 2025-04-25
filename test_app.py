"""unittests"""

import unittest
import requests


class TESTROUTES(unittest.TestCase):
    """test app routes"""

    def test_home(self):
        """home route"""
        res = requests.get("http://127.0.0.1:5000/", timeout=10)
        self.assertEqual(200, res.status_code)


# -------running the test----------
# python -m unittest -v
# ---------------------------------
