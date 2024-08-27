#!/usr/bin/env python3
"""
basic babel setup
"""
from flask import Flask
from flask_babel import Babel
from flask import render_template


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

# setup routes
@app.route('/')
def index() -> str:
    """
    home/index page
    """
    return render_template('1-index.html')
