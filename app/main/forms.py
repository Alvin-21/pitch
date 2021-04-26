from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    """
    Class for updating profile bio.
    """

    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    """
    Class for providing the pitch.
    """

    category = RadioField('Label', choices=[('business pitch', 'business pitch'), ('interview pitch','interview pitch'), ('product pitch', 'product pitch'), ('promotion pitch', 'promotion pitch')])
    pitch = TextAreaField("Please provide your pitch.", validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    """
    Class for providing the comment for a pitch.
    """

    comment = TextAreaField('Type your comment',validators=[Required()])
    submit = SubmitField('Submit')