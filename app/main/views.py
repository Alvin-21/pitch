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

@main.route('/category/<category_name>')
def category(category_name):
    """
    Function for returning the category page.
    """

    category = category_name
    title = f'{category}'
    pitches = Pitch.get_pitches(category)

    return render_template('category.html', title=title, category=category, pitches=pitches)

@main.route('/category/pitch/comments/new/<int:pitch_id>', methods=['GET', 'POST'])
@login_required
def new_comment(pitch_id):
    """
    Function that returns the comments page.
    """

    form = CommentForm()

    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(text=comment, pitch_id=pitch_id, user_id=current_user.id)
        new_comment.save_comment()
        return redirect(url_for('.view_pitch', pitch_id=pitch_id))

    title = 'New Comment'
    return render_template('comments.html', title=title, form=form)

@main.route('/pitch/view/<int:pitch_id>', methods=['GET', 'POST'])
def view_pitch(pitch_id):
    """
    Function that returns the view page for a pitch.
    """

    pitch = Pitch.query.filter_by(id=pitch_id).first()
    comments = Comment.get_comments(pitch_id)
    
    return render_template('view.html', pitch=pitch, comments=comments, id=pitch_id)

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
