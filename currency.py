
import sys
from frankfurter import Frankfurter

class CurrencyConverter:
    """
    Class that represents a Currency conversion object. It will be used to store the input arguments (currency codes, date) and also other information required (amount, rate, inverse rate, instantiation of Frankfurter class).

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    api : Frankfurter
        Instance of Frankfurter class
    """
    def __init__(self, from_currency, to_currency, date):
        
        
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.date = date
        self.api = Frankfurter()
        self.amount = None
        self.rate = None
        self.inverse_rate = None
        

    def check_currencies(self):
        """
        Method that will check if currency codes stored in the class attributes are valid.
        Otherwise the program will exit and display the relevant message provided in the assignment brief
        ----------
        Pseudo-code
        ----------
        Apply function Frankfurter().check_currency with a input argument 'self.from_currency' to get a True or False response to reflect the input argument whether is in the currency list, and names the return as 'check_from_currency'
        Apply function Frankfurter().check_currency with a input argument 'self.to_currency' to get a True or False response to reflect the input argument whether is in the currency list, and names the return as 'check_to_currency'


        if 'check_from_currency' is equal to False
            if 'check_to_currency' is equal to False
                then print those 2 input arguments both not valid currency codes'
                return False
                and exit the program
            else
            print the input argument from_currency is not a valid currency code
        elif check_from_currency is equal to True
            if 'check_to_currency' is equal to False
                then print the input argument to_currency is not a valid currency code
                return False
                and exit the program
            else
                return True
        ----------
        """
      
        check_from_currency = Frankfurter().check_currency(self.from_currency)
        check_to_currency = Frankfurter().check_currency(self.to_currency)

        if check_from_currency == False :
            if check_to_currency == False :
             print(f'{self.from_currency} and {self.to_currency} are not valid currency codes')
             
             sys.exit(0) 
            else :
             print(f'{self.from_currency} is not a valid currency code')
             
             sys.exit(0)
             
        elif check_from_currency == True:
            if check_to_currency  == False:
             print(f'{self.to_currency} is not a valid currency code')
             
             sys.exit(0)
             
        
        return True

       
    def reverse_rate(self):
        """
        Method that will calculate the inverse rate from the value stored in the class attribute, round it to 4 decimal places and save it back in the class attribute inverse_rate.
        ----------
        Pseudo-code
        ----------
        if the class attribute 'self.rate' is equal to None
            Apply the function Frankfurter().get_historical_rate() with input arguments :'self.from_currency', 'self.to_currency', 'self.date' to extract the conversion rate, and store the return as 'self.rate', which upgraded the class attribute
        
        apply the function round() with input arguments: take the multiplicative inverse of 'self.rate' and 4, to extract the inverse currency rate, save as 'self.inverse_rate' to ungrade the attribute of class
        return attribute 'self.inverse_rate'
        ----------
        """
        
        if self.rate == None:
         self.rate = Frankfurter().get_historical_rate(self.from_currency,self.to_currency,self.date)
        self.inverse_rate = round(1/self.rate,4)
        return self.inverse_rate
        
    def round_rate(self, rate:float):
        """
        Method that will round an input argument to 4 decimals places.

        
        ----------
        Pseudo-code
        ----------
       if the input argument 'rate' is a float type 
            apply around() with input argument: rate and 4, to round the value into 4 digitals, and save as object names 'rate_4_decimal'
            return 'rate_4_decimal'
       else
            print rate is not a float.
        ----------
        """
        if type(rate) == float:
            rate_4_decimal = round(rate,4) 
            return rate_4_decimal
        else:
          print(f'{rate} is not a float.')
            
         
        


    def get_historical_rate(self):
        """
        Method that will call the Frankfurter API and get the historical conversion rate for the currencies (rounded to 4 decimals) and date stored in the class attributes.
        Then it will calculate the inverse rate and will exit by displaying the relevant message provided in the assignment brief

        ----------
        Pseudo-code
        ----------
        Apply the function Frankfurter().get_historical_rate() with input arguments :'self.from_currency', 'self.to_currency', 'self.date' to extract the conversion rate, and store the return as 'self.rate', which upgraded the class attribute
        Apply the fcuntion self.reverse_rate() to extract the inverse rate and save as self.inverse_rate to upgrade the attribute
        print the coversion rate and reverse rate by the input currency codes
        exit the program
        
        -------
       
        """

       
       
        #self.rate = self.api.get_historical_rate(self.from_currency, self.from_currency, self.date)
    
        self.rate = Frankfurter().get_historical_rate(self.from_currency,self.to_currency,self.date)
        self.inverse_rate = self.reverse_rate()
        print(f'The conversion rate on {self.date} from {self.from_currency} to {self.to_currency} was {self.rate}. The inverse rate was {self.inverse_rate}')
        sys.exit(0)
        
       
        
       