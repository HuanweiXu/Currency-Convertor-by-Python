import unittest
from checks import check_arguments, check_date


class TestCheckArguments(unittest.TestCase):
    """
    Class used for testing the check_arguments() function from checks.py
    """
    # => To be filled by student
    def test_CheckArguments_sucess(self):
        expected = ['2020-09-01','USD','AUD']
        result = check_arguments(['2020-09-01','USD','AUD'])
        self.assertEqual(expected,result)

    def test_CheckArguments_fail(self):
        
       with self.assertRaises(SystemExit) as cm:
         result = check_arguments(['2020-09-01','USD'])
       self.assertEqual(cm.exception.code, 0)


class TestCheckDate(unittest.TestCase):
    """
    Class used for testing the check_date() function from checks.py
    """
    # => To be filled by student
    def test_CheckDate_invaid_DateType(self):
        
        with self.assertRaises(SystemExit) as ex:
           result = check_date('2020-09/01')
        self.assertEqual(ex.exception.code,0)


    def test_CheckDate_vaidDate(self):
        expected = True
        result = check_date('2020-09-01')
        self.assertEqual(expected,result)

    def test_CheckDate_InvaidDate(self):
        with self.assertRaises(SystemExit) as ex:
            result = check_date('2020-09-31')
        self.assertEqual(ex.exception.code,0)
if __name__ == '__main__':
    unittest.main()