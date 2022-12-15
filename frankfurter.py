
from api import call_get


class Frankfurter:
    """
    Class that manages API calls to Frankfurter. It will be used to store the URLS to the relevant endpoints. It will also automatically call the Currencies endpoint and store the return list of available currency codes.

    Attributes
    ----------
    base_url : str
        Base url to Frankfurter API
    currencies_url : str
        Frankfurter endpoint for extracting currencies list
    historical_url : str
        Frankfurter endpoint for extracting historical currencies conversion rates
    currencies: list
        List of available currency codes
    """
         
      
    def __init__(self):
        
        self.base_url = 'https://api.frankfurter.app/'
        self.currencies_url = 'https://api.frankfurter.app/currencies'

    def get_currencies_list(self):
        """
        Method that will get the list of available currencies and returns it as a Python list.
        ----------
        Pseudo-code
        ----------
        Restore the class attribute 'self.currencies_url' as a new obeject called currencies_url

        apply function call_get().json() by use input 'urrencies_url' , and as a new obeject called currencies

        return 'currencies'
        ----------
        """

        currencies_url = self.currencies_url
         
        currencies = call_get(currencies_url).json()
         
        return  currencies
         
    


         
    def check_currency(self, currency):
        """
        Method that will check if a provided currency code is valid and return True if that is the case.
        Otherwise it will return False.      
        ----------
        Pseudo-code
        ----------
        class the object 'currencies_list' as a Frankfurter class and apply a function .get_currencies_list() to return a dictionary list

        get the key of the the dictionary 'currencies_list' and save as a new object call 'currencies_keys'


        if input argument 'currency' is not a subset of 'currencies_keys'
            then return False
        else
            return True
        ----------
        """
        
        
         
        currencies_list = Frankfurter().get_currencies_list()
        currencies_keys = currencies_list.keys()
        if currency not in currencies_keys:
            
            return False
        else :
            return True


    def get_historical_rate(self, from_currency, to_currency, from_date, amount=1):
        """
        Method that will call the historical API endpoint in order to get the conversion rate for a given dates and currencies. It will return an requests.models.Response object.  
        ----------
        Pseudo-code
        ----------
        Build a string use the values of the input arguments and mannual setting as a obeject names 'historical_url'

        Use 'historical_url' and 'rates' as input arguments to apply the function call_get().json().get() to extract the list of rate, and save as a new object names 'historical_rate_list'
       
        Use the input argument 'to_currency' to get the rate of the country you want by apply funtion 'historical_rate_list.get', and save as a new object names 'historical_rate'

        return 'historical_rate'
        ----------
        """
        
        
        historical_url = f'{self.base_url}{from_date}?from={from_currency}'
        historical_rate_list = call_get(historical_url).json().get('rates')
        historical_rate = historical_rate_list.get(to_currency)
        
        return historical_rate

      

