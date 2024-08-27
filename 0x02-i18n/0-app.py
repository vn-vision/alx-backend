#!/usr/bin/env python3
"""
basic flask app, single / route
"""
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def hello_world() -> str:
    """
    home/index page
    """
    return render_template('0-index.html')
