#!/usr/bin/env python3
"""
basic babel setup
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel


app = Flask(__name__)


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
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        g.locale = locale
        return locale

    # otherwise, use the best match from request headers
    locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    g.locale = locale
    return locale

# setup routes
@app.route('/')
def index() -> str:
    """ home/index page """
    return render_template('4-index.html')
