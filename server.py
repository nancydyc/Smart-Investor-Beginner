"""Investing Stocks."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db

import json
import requests


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


@app.route('/')
def search_stock_form():
    """Search stocks by symbol or key words."""

    # Get user input from the search form
    # If the symbol is in the set of symbols/key words in the company names,
    # return stock realtime price from Alpha Vantage API 
    # and company name data from Edgar Online API.
    # Else,...

    pass 
    # User Ajax to work on home.html


@app.route('/stock')
def display_stock():
    """Display single stock page of key data and company fundamentals."""

    return render_template("stock.html")


@app.route('/stock/<stock_id>')
def show_price_chart():
    """Display single stock page of key data and company fundamentals."""

    # Get user input from the search form
    # If the symbol is in the set of symbols/key words in the company names,
    # return stock realtime price and company name, daily/weekly/monthly price data
    # from Alpha Vantage API to make a chart

    pass


@app.route('/screen')
def screen_stocks():
    """Stock screener, showing screening criteria."""

    return render_template("screen.html")


@app.route('/screen')
def get_price_range():
    """Stock screener."""

    # Get price range from user
    # 2.0 Get week numbers

    # If the realtime price of the stocks in database in the price range,
    # return a list of the company names
    return redirect("result.html")


@app.route('/result')
def screen_result():
    """Display stock screening results, showing symbol, company names and price."""

    return render_template("result.html")




####################################2.0 feature################################

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


###############################################################################
if __name__ == "__main__":

    app.debug = True

    connect_to_db(app)
    #? Why do you need it in all model, server and seed?

    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")