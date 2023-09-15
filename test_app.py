import unittest
from app import app

class FlaskAppTest(unittest.TestCase):

    # Set up the test environment before each test method is executed
    def setUp(self):
        self.app = app.test_client()  # Create a test client for the Flask app
        self.app.testing = True  # Enable testing mode for the app

    def test_homepage_access(self):
        response = self.app.get('/')  # Send a GET request to the root URL
        self.assertEqual(response.status_code, 200)  # Check if the response status code is 200 (OK)

    # Test case to check form submission with valid data
    def test_form_submission_valid(self):
        data = {
            'amount': '100',
            'from_currency': 'USD',
            'to_currency': 'EUR'
        }
        response = self.app.post('/', data=data, follow_redirects=True)  # Send a POST request with form data
        self.assertIn(b'is equal to', response.data)  # Check if the response contains 'is equal to'

    # Test case to check form submission with invalid data
    def test_form_submission_invalid(self):
        data = {
            'amount': '100',
            'from_currency': 'INVALID',
            'to_currency': 'EUR'
        }
        response = self.app.post('/', data=data, follow_redirects=True)  # Send a POST request with form data
        self.assertIn(b'Invalid currency codes', response.data)  # Check if the response contains 'Invalid currency codes'

    # Test case to check form submission with invalid amount (not a number)
    def test_form_submission_invalid_amount(self):
        data = {
            'amount': 'invalid_amount',
            'from_currency': 'USD',
            'to_currency': 'EUR'
        }
        response = self.app.post('/', data=data, follow_redirects=True)  # Send a POST request with form data
        self.assertIn(b'Invalid amount. Please enter a valid number.', response.data)  # Check if the response contains the error message

    # Test case to check form submission with valid data and correct conversion message
    def test_form_submission_valid_conversion(self):
        data = {
            'amount': '100',
            'from_currency': 'USD',
            'to_currency': 'EUR'
        }
        response = self.app.post('/', data=data, follow_redirects=True)  # Send a POST request with form data
        self.assertIn(b'100.00 $ is equal to', response.data)  # Check if the response contains the correct conversion message

if __name__ == '__main__':
    unittest.main()
