from flask import render_template, request, redirect, url_for
from . import main

# Views
@main.route('/')
def index():
    '''
    Function that returns the index page and its data.
    '''

    title = 'Home'

    return render_template('index.html', title=title)
