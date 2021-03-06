from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    """
    This class defines new User objects.
    """

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, index=True)
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    likes = db.relationship('Like',backref = 'user',lazy = "dynamic")
    dislikes = db.relationship('Dislike',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):
    """
    Class for defining pitches.
    """

    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitch_username = db.Column(db.String(255), db.ForeignKey("users.username"))
    category = db.Column(db.String(255))
    description = db.Column(db.Text, index = True)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship('Comment',backref='pitch',lazy='dynamic')
    likes = db.relationship('Like',backref = 'pitch',lazy = "dynamic")
    dislikes = db.relationship('Dislike',backref = 'pitch',lazy = "dynamic")

    def save_pitch(self):
        """
        Method for saving the pitch to the database.
        """

        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, category):
        """
        Method to get the pitches.
        """

        pitch = Pitch.query.filter_by(category=category).order_by(Pitch.time.desc()).all()
        return pitch

class Comment(db.Model):
    """
    Class for defining comments for the pitches.
    """

    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment_username = db.Column(db.String(255), db.ForeignKey("users.username"))
    text = db.Column(db.Text)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save_comment(self):
        """
        Method for saving the comments to the database.
        """

        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        """
        Method for getting the comments.
        """
        
        comments = Comment.query.filter_by(pitch_id=id).all()
        return  comments


class Like(db.Model):
    """
    Class for liking pitches.
    """

    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True)
    like = db.Column(db.Integer, default=1)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_like(self):
        """
        Function for saving like to database.
        """

        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_likes(cls, pitch_id):
        """
        Function for getting pitch likes.
        """

        likes = Like.query.order_by('id').all()
        return likes


class Dislike(db.Model):
    """
    Class for disliking pitches.
    """

    __tablename__ = 'dislikes'
    id = db.Column(db.Integer, primary_key=True)
    dislike = db.Column(db.Integer, default=1)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_dislike(self):
        """
        Function for saving dislikes to database.
        """

        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_dislikes(cls, pitch_id):
        """
        Function for getting pitch dislikes.
        """

        dislike = Dislike.query.order_by('id').all()
        return dislike
