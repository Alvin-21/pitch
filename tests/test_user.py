import unittest
from app.models import User


class UserModelTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the User Class.
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test.
        '''

        self.new_user = User(password='banana')

    def test_password_setter(self):
        '''
        Test case to test if the password was entered.
        '''

        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        '''
        Test case to confirm that our application raises an AttributeError when we a user tries to access the password property.
        '''

        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        '''
        Test case to check whether the password is correct.
        '''

        self.assertTrue(self.new_user.verify_password('banana'))