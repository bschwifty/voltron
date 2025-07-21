import unittest
from unittest.mock import patch, mock_open
import string
from voltron import analysis_len, analysis_charset, analysis_breach

class TestVoltron(unittest.TestCase):

    def setUp(self):
        self.passwords = {
            "short": "short1",
            "medium": "---exactly----16",
            "long": "supercalifragilisticexpialadocious",
            "xkcd": "correcthorsebatterystaple",
            "breached": "123456",
            "not_breached": "Sample_Password_Is_Great_332"
        }

    def test_analysis_len_short(self):
        with patch('builtins.print') as mocked_print:
            password = self.passwords["short"]
            analysis_len(password)
            mocked_print.assert_called_with("Your password is shorter than 16 characters long, consider making it longer.")

    def test_analysis_len_medium(self):
        with patch('builtins.print') as mocked_print:
            password = self.passwords["medium"]
            analysis_len(password)
            mocked_print.assert_any_call("Your password is between 16 and 25 characters long.  Nice work!  However,")
            mocked_print.assert_any_call("you may be able to make it longer by using a passphrase.\n")

    def test_analysis_len_long(self):
        with patch('builtins.print') as mocked_print:
            password = self.passwords["long"]
            analysis_len(password)
            mocked_print.assert_called_with("Your password is more than 25 characters long.  Good to go!")

    def test_analysis_len_xkcd(self):
        with patch('builtins.print') as mocked_print:
            password = self.passwords["xkcd"]
            with self.assertRaises(SystemExit):  # Expecting exit on this password
                analysis_len(password)

    def test_analysis_charset(self):
        with patch('builtins.print') as mocked_print:
            password = self.passwords["medium"]
            analysis_charset(password)
            mocked_print.assert_called_with("Your password uses 4 character types.")
            mocked_print.assert_any_call("Nice job!\n")

    def test_analysis_charset_missing_types(self):
        with patch('builtins.print') as mocked_print:
            password = "abc"  # Only lowercase letters
            analysis_charset(password)
            mocked_print.assert_called_with("Your password uses 1 character types.")
            mocked_print.assert_any_call("Consider adding more character types to your password.\n")

    def test_analysis_breach_breached(self):
        with patch('builtins.open', mock_open(read_data='123456\npassword\n12345678\n')) as mocked_file:
            password = self.passwords["breached"]
            result = analysis_breach(password)
            self.assertTrue(result)

    def test_analysis_breach_not_breached(self):
        with patch('builtins.open', mock_open(read_data='123456\npassword\n12345678\n')) as mocked_file:
            password = self.passwords["not_breached"]
            result = analysis_breach(password)
            self.assertFalse(result)

    def test_analysis_breach_file_not_found(self):
        with patch('builtins.open', side_effect=FileNotFoundError):
            password = self.passwords["not_breached"]
            result = analysis_breach(password)
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
