from distutils.log import error
import unittest
from api import call_get
import requests

class TestAPI(unittest.TestCase):
    """
    Class used for testing the call_get() function in api.py
    """
    
    def test_API_TypeOfReturn_Sucess(self):
        expected = type(requests.get('https://api.frankfurter.app/currencies'))
        result = type(call_get('https://api.frankfurter.app/currencies'))
        msg = 'call_get is not instance of requests.get'
        self.assertIsInstance(result,type(expected),msg)





if __name__ == '__main__':
    unittest.main()
