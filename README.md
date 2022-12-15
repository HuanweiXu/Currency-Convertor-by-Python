# <Currency Converter>

## Author
Name: <Huanwei Xu>
Student ID: <14090118>

## Description
<What your application does>
<Some of the challenges you faced>
<Some of the features you hope to implement in the future>

## How to Setup
<Provide a step-by-step description of how to get the development environment set and running.>
<Which Python version you used>
<Which packages and version you used>

## How to Run the Program
< 1.Put all the ".py" file into a same folder >
< 2.Open the powershell and change the direction as the folder of the files. The code will obey the form: input 'cd ':/the direction'' >
< 3.Open the main file with 3 arguments: date, the base country, the convert country. The code will obey the form: 'python main.py YYYY-MM-DD USA AUD' >

< 4.The dictionary of the Country code > :

<"AUD":"Australian Dollar","BGN":"Bulgarian Lev","BRL":"Brazilian Real",
"CAD":"Canadian Dollar","CHF":"Swiss Franc","CNY":"Chinese Renminbi Yuan",
"CZK":"Czech Koruna","DKK":"Danish Krone","EUR":"Euro","GBP":"British Pound",
"HKD":"Hong Kong Dollar","HRK":"Croatian Kuna","HUF":"Hungarian Forint",
"IDR":"Indonesian Rupiah","ILS":"Israeli New Sheqel","INR":"Indian Rupee",
ISK":"Icelandic Króna","JPY":"Japanese Yen","KRW":"South Korean Won","MXN":"Mexican Peso",
"MYR":"Malaysian Ringgit","NOK":"Norwegian Krone","NZD":"New Zealand Dollar",
"PHP":"Philippine Peso","PLN":"Polish Złoty","RON":"Romanian Leu","SEK":"Swedish Krona",
"SGD":"Singapore Dollar","THB":"Thai Baht","TRY":"Turkish Lira","USD":"United States Dollar","ZAR":"South African Rand>

## Project Structure

### Meta files 
<main.py: Main logics of the program.>
<api.py: a function that will call the API endpoint (input parameter) and return its response as a requests.models.Response object>
<check.py: containing 2 function, one is for check the length of input argument; the other is for check the validation of the date argument>
<currency.py: A Class that represents a Currency conversion object. It will be used to store the input arguments (currency codes, date) and also other information required (amount, rate, inverse rate, instantiation of Frankfurter class).>
<frankfurter.py: A Class that manages API calls to Frankfurter. It will be used to store the URLS to the relevant endpoints. It will also automatically call the Currencies endpoint and store the return list of available currency codes.>

### Test files
<test_api.py: a test on api.py that test the function whehter work under different given scenarios>
<test_checks.py: a test on checks.py that test the function whehter work under different given scenarios>
<test_frankfurter.py: a test on frankfurter.py that test the function whehter work under different given scenarios>
<test_currency.py: a test on currency.py that test the function whehter work under different given scenarios>

## Citations

<Sara A. Metwalli(2022), < Pseudocode: What It Is and How to Write It > ,https://builtin.com/data-science/pseudocode>
<Pavel Anossov(2013), < Is it possible for a unit test to assert that a method calls sys.exit()? >, 
https://stackoverflow.com/questions/15672151is-it-possible-for-a-unit-test-to-assert-that-a-method-calls-sys-exit>
<CodeVsColor,<How to check if a date is valid or not in python>, https://www.codevscolor.com/date-valid-check-python >


