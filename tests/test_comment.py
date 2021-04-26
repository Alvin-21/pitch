import unittest
from app.models import User, Pitch, Comment
from app import db

class CommentTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Comment Class.
    """

    def tearDown(self):
        """
        Cleans up after each test case has run.
        """

        User.query.delete()
        Pitch.query.delete()
        Comment.query.delete()
        
    def setUp(self):
        """
        Set up method that will run before every Test.
        """

        self.new_user = User(username="john", email="john@gmail.com", pass_secure="trial1")
        self.new_pitch = Pitch(category="pickup lines", description="asdfghjkl")
        self.new_comment = Comment(text="good pitch")

    def test_check_instance_variables(self):
        """
        Test case to check if the values of variables are correctly being placed.
        """

        self.assertEquals(self.new_comment.text, "good pitch")
        self.assertEquals(self.new_comment.pitch_id, self.new_pitch.id)

    def test_save_comment(self):
        """
        Test case to check if the comment is saved to the database.
        """

        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_pitch(self):
        """
        Test case to check if comments can be returned.
        """

        self.new_pitch.save_pitch()
        self.new_comment.save_comment()
        got_comment = Comment.get_comments(self.new_comment.pitch_id)
        self.assertTrue(len(got_comment) == 1)