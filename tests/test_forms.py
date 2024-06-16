import unittest
from flask import Flask
from app.forms import Registration, LoginForm, Recycling, Scheduling_form, updateAccount

class TestForms(unittest.TestCase):

    def setUp(self):
        # Create a Flask application instance for testing
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'mysecret'
        self.app.config['WTF_I18N_ENABLED'] = False
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        # Remove the application context
        self.app_context.pop()

    def test_registration_form_valid_data(self):
        form = Registration(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'sex': 'Male',
            'address': '123 Main St',
            'house_number': '456',
            'location': 'City',
            'phone_number': '1234567890',
            'password': 'password123',
            'confirm_password': 'password123'
        })
        self.assertTrue(form.validate())

    def test_registration_form_missing_data(self):
        form = Registration(data={
            'first_name': 'John',
            'last_name': '',
            'email': 'john.doe@example.com',
            'sex': 'Male',
            'address': '123 Main St',
            'house_number': '',
            'location': 'City',
            'phone_number': '1234567890',
            'password': 'password123',
            'confirm_password': 'password123'
        })
        self.assertFalse(form.validate())

    def test_login_form_valid_data(self):
        form = LoginForm(data={
            'email': 'john.doe@example.com',
            'password': 'password123',
            'remember': True
        })
        self.assertTrue(form.validate())

    def test_login_form_invalid_email(self):
        form = LoginForm(data={
            'email': 'not-an-email',
            'password': 'password123',
            'remember': True
        })
        self.assertFalse(form.validate())

    def test_recycling_form_valid_data(self):
        form = Recycling(data={
            'date': '2023-06-15',
            'type': 'plastic',
            'amount': 5
        })
        self.assertTrue(form.validate())

    def test_recycling_form_invalid_amount(self):
        form = Recycling(data={
            'date': '2023-06-15',
            'type': 'plastic',
            'amount': -1
        })
        self.assertFalse(form.validate())

    def test_scheduling_form_valid_data(self):
        form = Scheduling_form(data={
            'date': '2023-06-15',
            'type': 'plastic'
        })
        self.assertTrue(form.validate())

    def test_update_account_form_valid_data(self):
        form = updateAccount(data={
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'jane.doe@example.com'
        })
        self.assertTrue(form.validate())

    def test_update_account_form_invalid_email(self):
        form = updateAccount(data={
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'not-an-email'
        })
        self.assertFalse(form.validate())

if __name__ == '__main__':
    unittest.main()
