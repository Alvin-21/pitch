from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    """
    Class for updating profile bio.
    """
    
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')
