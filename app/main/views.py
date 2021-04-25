from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Pitch, Comment
from .forms import UpdateProfile, PitchForm, CommentForm
from .. import db

# Views
@main.route('/')
def index():
    '''
    Function that returns the index page and its data.
    '''

    title = 'Home'

    return render_template('index.html', title=title)

@main.route('/category/pitch/new/<category_name>', methods=['GET', 'POST'])
@login_required
def new_pitch(category_name):
    """
    Function that returns the pitches page.
    """
    
    form = PitchForm()
    category = category_name

    if form.validate_on_submit():
        pitch_category = form.category.data
        pitch = form.pitch.data
        new_pitch = Pitch(category=pitch_category, pitch=pitch, user=current_user)
        new_pitch.save_pitch()
        return redirect(url_for('.category', category_name=category))

    title = 'New Pitch'
    return render_template('pitches.html', title=title, form=form, category=category)

@main.route('/user/<uname>')
def profile(uname):
    """
    Function that returns the user's profile page.
    """

    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    """
    Function that updates the user's profile.
    """

    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)
