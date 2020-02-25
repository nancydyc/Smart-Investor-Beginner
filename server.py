"""Investing Stocks."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify, url_for
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
    """Search stocks by symbol or key words."""

    # Get user input from the search form
    symbol = request.args.get('symbol')
    # print(symbol)

    # Get stock name
    payload_name = {'function': 'SYMBOL_SEARCH',  
                    'keywords': symbol,
                    'apikey': 'KSMJ9C8N2RZ92V0D'}
    # print(payload)
    req_name = requests.get("https://www.alphavantage.co/query", params=payload_name)
    # print(req_name.url)
    js_data_name = req_name.json()
    best_matches = js_data_name.get('bestMatches', 0)
    stock_names = []
    symbols = []

    for stock in best_matches:
        stock_names.append(stock['2. name'])
        symbols.append(stock['1. symbol'])
    # print(stock_names)
    # print(symbols)
    stocks =[]
    for smbl, name in zip(symbols, stock_names):
        stocks.append({'symbol': smbl, 'name': name})
    # print(stocks)
    results = {'stocks':stocks} 
    return results


@app.route('/stock/<symbol>')
def get_realtime_price(symbol):
    """Show realtime price."""

    # symbol = request.args.get("symbol")
    print("realtime", symbol)
    payload_rt = {'function': 'TIME_SERIES_INTRADAY',  
               'symbol': symbol,
               'interval': '60min',
               'outputsize': 'compact',
               'apikey': 'KSMJ9C8N2RZ92V0D'}
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


@app.route('/chart/<symbol>')
def display_daily_ema_chart(symbol):
    """Get stocks by symbol or key words and display EMA price chart."""

    # Get user input from the search form
    print("\n\n####################below is chart data########################")
    # symbol = request.args.get("symbol")
    print("chart", symbol)
    # Get daily EMA of monthly average
    payload_ema = {'function': 'EMA',  
               'symbol': symbol,
               'interval': 'weekly',
               'time_period': 30,
               'series_type': 'open',
               'apikey': 'G91S3ATZL5YIK83E'}
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
    print('before return', data)
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
    # price_left = session['left']
    # price_right = session['right']
    # print("1", price_left, price_right)
    return render_template("screen.html")

    """Stock screener."""

    # Get price range from user
    # 2.0 Get week numbers

    # If the realtime price of the stocks in database in the price range,
    # return a list of the company names

# <number intended as offset'
@app.route('/result')
def screen_result():
    """Display stock screening results, showing symbol, company names and price."""
    
    page = request.args.get('page', type=int)
    # print(page)

    price_left = request.args.get('left')
    price_right = request.args.get('right')
    print("2", price_left, price_right)

    session['leftleft'] = price_left
    session['rightright'] = price_right
    print(session['leftleft'], session['rightright'])

    # Add pagination
    # page = request.args.get('page', type=int)
    # print(page)

    # result = Stock.query.filter(Stock.weekly_ave_price > 10)\
    #                     .paginate(page=page, per_page=2)
    
    #! Need to handle exception: what if user only enter one price 
    if price_right > price_left:
        result = Stock.query.filter(Stock.weekly_ave_price > price_left, 
                                    Stock.weekly_ave_price < price_right)\
                            .paginate(page=page, per_page=5)
        print(result)
        return render_template("result.html", result=result, leftprice=price_left, rightprice=price_right)
    else:
        result = Stock.query.filter(Stock.weekly_ave_price > price_right, 
                                    Stock.weekly_ave_price < price_left)\
                            .paginate(page=page, per_page=5)
        print(result)
        return render_template("result.html", result=result, leftprice=price_left, rightprice=price_right)
    # return render_template("result.html", result=result)


@app.route('/pages')
def more_result_pages():
    """Display stock screening results, showing symbol, company names and price."""
    
    page = request.args.get('page', type=int)
    print('page', page)
    
    # print('from sessioin', session['leftleft'], session['rightright'])

    if (session.get('leftleft') is None) or (session.get('rightright') is None):
        flash('No more page.')
        return redirect('/result')

    price_left = session.get('leftleft')
    price_right = session.get('rightright')
    print("3", price_left, price_right)
    
    if price_right > price_left:
        result = Stock.query.filter(Stock.weekly_ave_price > price_left, 
                                    Stock.weekly_ave_price < price_right)\
                            .paginate(page=page, per_page=5)
        print(result)
        return render_template("result.html", result=result, leftprice=price_left, rightprice=price_right)
    else:
        result = Stock.query.filter(Stock.weekly_ave_price > price_right, 
                                    Stock.weekly_ave_price < price_left)\
                            .paginate(page=page, per_page=5)
        print(result)
        return render_template("result.html", result=result, leftprice=price_left, rightprice=price_right)


    # if price_right > price_left:
    #     result = Stock.query.filter(Stock.weekly_ave_price > price_left, 
    #                                 Stock.weekly_ave_price < price_right)\
    #                         .paginate(page=page, per_page=5)
    #     print(result)
    #     return render_template("result.html", result=result)
    # else:
    #     result = Stock.query.filter(Stock.weekly_ave_price > price_right, 
    #                                 Stock.weekly_ave_price < price_left)\
    #                         .paginate(page=page, per_page=5)
    
    

####################################2.0 feature################################

@app.route('/watchlist')
def show_watchlist():
    """Show the watchlist."""
    return render_template("watchlist.html")


@app.route('/watchlist/<symbol>')
def edit_watchlist():
    """Add stock id to the watchlist when user clicks the star icon;
       remove the stock id when user re-clicks."""

    # if stock id exists in the watchlist table in the database , remove it;
    # else add the stock id to the watchlist table.

    # commit each change
    return "200"


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