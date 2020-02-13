"""Investing Stocks."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC" #? Is it always ABC?

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """Homepage."""

    return render_template("home.html")


@app.route('/stock')
def display_stock():
    """Display single stock page of key data and company fundamentals."""
    return render_template("stock.html")


@app.route('/compare')
def compare_stocks():
    """Compare two-three companies at a time on key data and company fundamentals."""
    return render_template("compare.html")


@app.route('/login')
def log_in():
    """User login."""
    return render_template("login.html")


@app.route('/register')
def register():
    """New member register."""
    return render_template("register.html")


@app.route('/screen')
def screen_stocks():
    """Stock screener."""
    return render_template("screen.html")


@app.route('/result')
def screen_result():
    """Display the results of stocks screening."""
    return render_template("result.html")

###############################################################################
if __name__ == "__main__":

    app.debug = True

    connect_to_db(app)
    #? Why do you need it in all model, server and seed?

    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")