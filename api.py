import requests
import sys

def call_get(url: str) -> requests.models.Response:
    """
    Function that will call the API endpoint (input parameter) and return its response as a requests.models.Response object
    In case of an error, the program will exit and display the relevant message provided in the assignment brief
    ----------
    Pseudo-code
    ----------
    Apply function requests.get() to get response, save the response name 'resp'

    if 'resp.status_code' is equal 200
      then return 'resp'
    
    Print There is an error with Frankfurter API
    and exit the programme
    ----------
    """
    
    # => To be filled by student
    resp = requests.get(url)
    if resp.status_code == 200:
     return resp 
    
    print('There is an error with Frankfurter API')
    sys.exit(0)