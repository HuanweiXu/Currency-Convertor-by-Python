import unittest
from currency import CurrencyConverter

class TestCurrencyConverterInstantiation(unittest.TestCase):
    """
    Class used for testing the instanciation of the CurrencyConverter class from currency.py
    """
    
    

    def test_instaiation_from(self):
        expected = 'USD'
        result = CurrencyConverter("USD",'AUD','2020-09-01')
        self.assertEqual(expected,result.from_currency)

    def test_instaiation_to(self):
        expected = 'AUD'
        result = CurrencyConverter("USD",'AUD','2020-09-01')
        self.assertEqual(expected,result.to_currency)

    def test_instaiation_date(self):
        expected = '2020-09-01'
        result = CurrencyConverter("USD",'AUD','2020-09-01')
        self.assertEqual(expected,result.date)

class TestCurrencyCheck(unittest.TestCase): 
    """
    Class used for testing the CurrencyConverter.check_currencies() method from currency.py
    """
   
   

    def test_fromTrue_toTrue(self):
        expected = True
        result = CurrencyConverter("USD",'AUD','2020-09-01').check_currencies()
        self.assertEqual(expected,result)

    def test_fromFalse(self):
        with self.assertRaises(SystemExit) as cm:
           result = CurrencyConverter("AAA",'AUD','2020-09-01').check_currencies()
        self.assertEqual(cm.exception.code, 0)

    def test_toFalse(self):
        with self.assertRaises(SystemExit) as cm:
           result = CurrencyConverter("USD",'AAA','2020-09-01').check_currencies()
        self.assertEqual(cm.exception.code, 0)

    def test_from_to_bothFalse(self):
        with self.assertRaises(SystemExit) as cm:
           result = CurrencyConverter("AAA",'BBB','2020-09-01').check_currencies()
        self.assertEqual(cm.exception.code, 0)
           

class TestReverseRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.reverse_rate() method from currency.py
    """
    
    def test_reverse_rate(self):
        expected = 0.738
        result = CurrencyConverter("USD",'AUD','2020-09-01').reverse_rate()
        self.assertEqual(expected,result)
    
class TestRoundRate(unittest.TestCase): 
    """
    Class used for testing the CurrencyConverter.round_rate() method from currency.py
    """
    
    def test_round_success(self):
        expected = 1.124
        result = CurrencyConverter("USD",'AUD','2020-09-01').round_rate(1.12395)
        self.assertEqual(expected,result)

    def test_round_fail(self):
        result = CurrencyConverter("USD",'AUD','2020-09-01').round_rate("USD")
        self.assertFalse(result)

class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the CurrencyConverter.get_historical_rate() method from currency.py
    """
    
    def test_historical_rate_sucess(self):
        
        with self.assertRaises(SystemExit) as cm:
           result = CurrencyConverter("USD",'AUD','2020-09-01').get_historical_rate()
        self.assertEqual(cm.exception.code, 0)
        

    
   
    
if __name__ == '__main__':
    unittest.main()