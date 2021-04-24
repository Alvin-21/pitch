from . import db

class User:
    """
    This class defines new User objects.
    """

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'


class Comment:
    """
    """
