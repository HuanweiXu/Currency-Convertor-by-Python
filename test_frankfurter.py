import unittest
from frankfurter import Frankfurter

class TestUrl(unittest.TestCase):
    """
    Class used for testing the url attributes of the Frankfurter class from checks.py
    """
    # => To be filled by student
    
    def test_base_url(self) :
        expected = 'https://api.frankfurter.app/'

        result = Frankfurter().base_url
        self.assertEqual(result,expected)
        
    def test_curencies_url(self) :
        expected = 'https://api.frankfurter.app/currencies'
        result = Frankfurter().currencies_url
        self.assertEqual(result,expected)
     
class TestCurrenciesList(unittest.TestCase):
    """
    Class used for testing the currencies attribute of the Frankfurter class from checks.py
    """
    # => To be filled by student
    def test_currency_list (self):
            expected = {"AUD":"Australian Dollar","BGN":"Bulgarian Lev","BRL":"Brazilian Real","CAD":"Canadian Dollar","CHF":"Swiss Franc","CNY":"Chinese Renminbi Yuan","CZK":"Czech Koruna","DKK":"Danish Krone","EUR":"Euro","GBP":"British Pound","HKD":"Hong Kong Dollar","HRK":"Croatian Kuna","HUF":"Hungarian Forint","IDR":"Indonesian Rupiah","ILS":"Israeli New Sheqel","INR":"Indian Rupee","ISK":"Icelandic Króna","JPY":"Japanese Yen","KRW":"South Korean Won","MXN":"Mexican Peso","MYR":"Malaysian Ringgit","NOK":"Norwegian Krone","NZD":"New Zealand Dollar","PHP":"Philippine Peso","PLN":"Polish Złoty","RON":"Romanian Leu","SEK":"Swedish Krona","SGD":"Singapore Dollar","THB":"Thai Baht","TRY":"Turkish Lira","USD":"United States Dollar","ZAR":"South African Rand"}
            
            currency_list = Frankfurter()
            result = currency_list.get_currencies_list()
            self.assertEqual(expected,result)
            


class TestCheckCurrency(unittest.TestCase):
    """
    Class used for testing the Frankfurter.check_currency() method from frankfurter.py
    """
    # => To be filled by student
    def test_check_currency_false (self):
        expected = False
        false_code = 'USA'
        result = Frankfurter().check_currency(false_code)
        self.assertEqual(expected,result)

    def test_check_currency_True (self):
        expected = True
        True_code = 'USD'
        result = Frankfurter().check_currency(True_code)
        self.assertEqual(expected,result)
    

class TestHistoricalRate(unittest.TestCase):
    """
    Class used for testing the Frankfurter.get_historical_rate() method from frankfurter.py
    """
    # => To be filled by student
    #def setup(self):
       # self.from_currency = 'USD'
        #self.to_currency = 'EUR'
       # self.date = '2022-09-06'

    #def test_historical_url(self):
       # expect = ''
       # result = Frankfurter().get_historical_rate(self.from_currency,self.to_currency,self.date)
    def test_rate_true(self):
        expected = 1.355
        result = Frankfurter().get_historical_rate('USD','AUD','2020-09-01')
        self.assertEqual(expected,result)

if __name__ == '__main__':
    unittest.main()