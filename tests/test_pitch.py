import unittest
from app.models import User, Pitch, Comment
from app import db

class PitchTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Pitch Class.
    """

    def tearDown(self):
        """
        Cleans up after each test case has run.
        """

        User.query.delete()
        Pitch.query.delete()
        
    def setUp(self):
        """
        Set up method that will run before every Test.
        """

        self.new_user = User(username="john", email="john@gmail.com", pass_secure="trial1")

        self.new_pitch = Pitch(category="pickup lines", description="asdfghjkl")

    def test_check_instance_variables(self):
        """
        Test case to check if the values of variables are correctly being placed.
        """

        self.assertEquals(self.new_pitch.category, "pickup lines")
        self.assertEquals(self.new_pitch.description, "asdfghjkl")
        self.assertEquals(self.new_pitch.user_id, self.new_user.id)

    def test_save_review(self):
        """
        Test case to check if the pitch is saved to the database.
        """

        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch(self):
        """
        Test case to check if pitches can be returned.
        """

        self.new_pitch.save_pitch()
        got_pitch = Pitch.get_pitches("pickup lines")
        self.assertTrue(len(got_pitch) == 1)

    