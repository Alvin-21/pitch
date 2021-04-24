from . import db

class User(db.Model):
    """
    This class defines new User objects.
    """

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'


class Comment:
    """
    """
