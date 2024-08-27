#!/usr/bin/env python3
"""
basic babel setup
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel
from typing import Dict

app = Flask(__name__)

# simulate database using the mock table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Configure available languages in the app
        en, fr
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'  # babel config values for default settings
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# apply configuration to the app
app.config.from_object(Config)

# instantiate the babel object
babel = Babel(app)

# add a locale selector
@babel.localeselector
def get_locale() -> str:
    """check url parameters, user settings or browser settings"""
    # get user's profile
    user = get_user()
    # locale from url parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        g.locale = locale
        return locale
    elif user and user['locale']:
        # locale from user settings
        if user['locale'] in app.config['LANGUAGES']:
            locale = user['locale']
        return locale
    else:
        # otherwise, use the best match from request headers
        locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    
    g.locale = locale or app.config['BABEL_DEFAULT_LOCALE']
    return g.locale

# get user
def get_user() -> Dict[int, Dict[str, str]] | None:
    """
    get a user by id
    """
    user_id = request.args.get('login_as', type=int)
    if user_id and user_id in users:
        return users[user_id]
    return None

# executed before all the other functions
@app.before_request
def before_request():
    """
    set global user to the get_user return type
    """
    user = get_user()
    if user:
        g.user = user  # get single user dictionary
    else:
        g.user = None

# setup routes
@app.route('/')
def index() -> str:
    """ home/index page """
    return render_template('5-index.html')
