"""Investing Stocks."""

from jinja2 import StrictUndefined

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC" #? Is it always ABC?

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return "<html><body>Placeholder for the homepage.</body></html>"


@app.route('/stock')
def display_stock():
    """Display single stock page of key data and company fundamentals."""
    pass


@app.route('/compare')
def compare_stocks():
    """Compare two-three companies at a time on key data and company fundamentals."""
    pass


@app.route('/login')
def log_in():
    """User login."""
    pass


@app.route('/register')
def register():
    """New member register."""
    pass


@app.route('/screen')
def screen_stocks():
    """Stock screener."""
    pass


@app.route('/result')
def screen_result():
    """Display the results of stocks screening."""
    pass


###############################################################################
if __name__ == "__main__":

    app.debug = True

    connect_to_db(app)
    #? Why do you need it in all model, server and seed?

    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")