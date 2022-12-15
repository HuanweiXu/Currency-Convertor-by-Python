import datetime
import sys

def check_arguments(args):
    """
    Function that will check if there are enough input arguments provided (ie exactly 3) and will return the input arguments if it is the case.
    Otherwise the program will exit and display the relevant message provided in the assignment brief
    ----------
    Pseudo-code
    ----------
    if the length of input argument is equal to 3
      then return the input arguments
    else 
      print "You need to provide 3 arguments in the following order: <date> <currency1> <currency2>"
      and exit the program
    ----------
    """

    
    if len(args) == 3:
        return args           
    else:
        print("You need to provide 3 arguments in the following order: <date> <currency1> <currency2>")
        sys.exit(0)
    
    

def check_date(date):
    
    """
    Function that will check if the provided date is valid and will return the value True if that is the case. 
    Otherwise the program will exit and display the relevant message provided in the assignment brief
    ----------
    Pseudo-code
    ----------
    if length of input argument is not qual to 10, or the 4th and 7th elements of input argument are both not equal to '-'
      then print 'Provided date is invalid and exit the program'
    

    split the input argument via '-' as date store names 'year','month', and 'day' orderly

    Store a Logic value 'True' and names 'isValidDate'

    Try
     the year, month, and day we store before is a valid datetime
    exception
      when the try is error
         the 'isValidDate' change the logic into 'False'

    if 'isValidDate' is True
        then print 'Provided date is True'
        and return a value 'True'
    else
        print "Provided date is invalid"
        and exit the program
    ----------  
    """

    if len(date) != 10 or date[4] and date[7] != '-':
        print("Provided date is invalid")
        sys.exit(0)

    year, month, day = date.split('-')

    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False
    if(isValidDate):
        print("Provided date is True ")
        return True 
    else:
        print("Provided date is invalid")
        sys.exit(0)
  



   



