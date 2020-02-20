"""Investing Stocks."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Watchlist, Stock

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


@app.route('/stock')
def search_stock_form():
    """Search stocks by symbol or key words and show realtime price."""

    # Get user input from the search form
    symbol = request.args.get('symbol')
    # print(symbol)

    # If the symbol is in the set of symbols/key words in the company names,
    # return stock realtime price from Alpha Vantage API
    payload_rt = {'function': 'TIME_SERIES_INTRADAY',  
               'symbol': symbol,
               'interval': '60min',
               'outputsize': 'compact',
               'apikey': 'PVW38W9JBAXB0XGX'}
    # print(payload)
    req_realtime = requests.get("https://www.alphavantage.co/query", params=payload_rt)
    # print(req.url)
    js_data_rt = req_realtime.json()
    # print(js_data)
    
    hourly_series_dict = js_data_rt.get('Time Series (60min)', 0)
    # print(hourly_series_dict)

    # print("#################################################")
    
    middle_key = list(hourly_series_dict.keys())[0]
    # print(middle_key)

    price = hourly_series_dict.get(middle_key, 0).get('4. close', 0)
    # print(price)
    # and company name data from Edgar Online API.
    # Else,...
    print("\n\n####################symbol,price working#######################")
    # ema = display_daily_ema_chart(symbol)
    # print(ema)
    realtime = {'symbol': symbol, 'realtime': price}
    
    return jsonify(realtime)
    # return render_template("stock.html", symbol=symbol, realtime=price,
    #                         date=date, ema=ema) 
    # User Ajax to work on home.html

# url for chart: 
# https://www.alphavantage.co/query?function=EMA&symbol=LK&interval=daily&time_period=30&series_type=open&apikey=PVW38W9JBAXB0XGX


@app.route('/chart')
def display_daily_ema_chart():
    """Get stocks by symbol or key words and display EMA price chart."""

    # Get user input from the search form
    print("\n\n####################below is chart data########################")
    symbol = request.args.get("symbol")
    print(symbol)
    # Get daily EMA of monthly average
    payload_ema = {'function': 'EMA',  
               'symbol': symbol,
               'interval': 'daily',
               'time_period': 30,
               'series_type': 'open',
               'apikey': 'PVW38W9JBAXB0XGX'}
    req_ema = requests.get("https://www.alphavantage.co/query", params=payload_ema)
    print(req_ema.url)
    js_date_ema = req_ema.json().get('Technical Analysis: EMA', 0)
    # print(type(js_date_ema))
    # print(js_date_ema)
    
    emas = []
    dates = []
    for daily_date in js_date_ema:
        # print(daily_date)
        dates.append(daily_date)
    # print(dates)    

    for daily_ema in js_date_ema.values():
        # print(daily_ema)
        emas.append(daily_ema['EMA'])
    # print(emas)
    print("\n\n##################### lists are working ##################\n\n")
    
    data_list = []
    # data_dict = {}
    data = {}
    for date, ema in zip(dates, emas):
        # data_dict['date'] = date
        # data_dict['ema'] = ema
        data_list.append({'date': date,
                     'ema': ema})
    # print("\n\n##################### data_list is working ##################")
    data['data'] = data_list
    print(data)
    return data

    # return render_template("stock.html", symbol=symbol,
                            # )

# @app.route('/stock')
# def display_stock():
#     """Display single stock page of key data and company fundamentals."""

#     return render_template("stock.html")


# @app.route('/stock/<stock_id>')
# def show_price_chart():
#     """Display single stock page of key data and company fundamentals."""

#     # Get user input from the search form
#     # If the symbol is in the set of symbols/key words in the company names,
#     # return stock realtime price and company name, daily/weekly/monthly price data
#     # from Alpha Vantage API to make a chart

#     pass


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