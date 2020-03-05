"""Investing Stocks."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify, url_for
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Watchlist, Stock

from smart import make_monthly_ema_line_chart

import requests


app = Flask(__name__)

app.secret_key = "ABC" #? Is it always ABC?

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """Homepage."""

    return render_template("home.html")


@app.route('/stock')
def search_stock_form():
    """Search stocks by the stock symbol or the key words of the company names.
       symbol: stock id.
    """

    # Get user input from the search form
    symbol = request.args.get('symbol')

    # Get the company name of the stocks from Alphavantage search endpoint
    payload_name = {'function': 'SYMBOL_SEARCH',  
                    'keywords': symbol,
                    'apikey': 'PVW38W9JBAXB0XGX'}

    req_name = requests.get("https://www.alphavantage.co/query", params=payload_name)
    # print(req_name.url)
    js_data_name = req_name.json()

    best_matches = js_data_name.get('bestMatches', 0)

    stock_names = []
    symbols = []
    for stock in best_matches:
        stock_names.append(stock['2. name'])
        symbols.append(stock['1. symbol'])

    stocks =[]
    for smbl, name in zip(symbols, stock_names):
        stocks.append({'symbol': smbl, 'name': name})

    results = {'stocks':stocks} 

    return results


@app.route('/stock/<symbol>')
def get_realtime_price(symbol):
    """Show realtime (close) price from Alphavantage API."""

    payload_rt = {'function': 'TIME_SERIES_INTRADAY',  
               'symbol': symbol,
               'interval': '60min',
               'outputsize': 'compact',
               'apikey': 'PVW38W9JBAXB0XGX'}

    req_realtime = requests.get("https://www.alphavantage.co/query", params=payload_rt)
    # print(req.url)
    js_data_rt = req_realtime.json()
    
    hourly_series_dict = js_data_rt.get('Time Series (60min)', 0)
    
    middle_key = list(hourly_series_dict.keys())[0]

    price = hourly_series_dict.get(middle_key, 0).get('4. close', 0)

    realtime = {'symbol': symbol, 'realtime': price}
    
    return jsonify(realtime)


@app.route('/chart/<symbol>')
def display_daily_ema_chart(symbol):
    """Get stocks by symbol or key words and display EMA price chart."""

    # Get daily EMA price using 30 days' average calculation method

    return make_monthly_ema_line_chart(symbol)


@app.route('/screen')
def screen_stocks():
    """Stock screener, showing screening criteria."""

    return render_template("screen.html")


@app.route('/result')
def screen_result():
    """Display stock screening results in a table. Showing stock symbols, 
       company names and prices.
       left: the value of the price user types on the left on stock screener page.
       right: the value of the price user types on the right on stock screener page.
    """
    
    page = request.args.get('page', type=int)

    price_left = request.args.get('left')
    price_right = request.args.get('right')

    session['left'] = price_left
    session['right'] = price_right

    # Add pagination on screen result page 
    if price_right > price_left:
        result = Stock.query.filter(Stock.weekly_ave_price > price_left, 
                                    Stock.weekly_ave_price < price_right)\
                            .paginate(page=page, per_page=5)
        
        return render_template("result.html", result=result, 
                                              leftprice=price_left, 
                                              rightprice=price_right)
    else:
        result = Stock.query.filter(Stock.weekly_ave_price > price_right, 
                                    Stock.weekly_ave_price < price_left)\
                            .paginate(page=page, per_page=5)
        
        return render_template("result.html", result=result, 
                                              leftprice=price_left, 
                                              rightprice=price_right)


@app.route('/pages')
def more_result_pages():
    """Use page links to navigate through stock screening results. Displaying 5 results per page."""
    
    page = request.args.get('page', type=int)
    
    if (session.get('left') is None) or (session.get('right') is None):
        flash('No more page.')
        return redirect('/result')

    price_left = session.get('left')
    price_right = session.get('right')
    
    if price_right > price_left:
        result = Stock.query.filter(Stock.weekly_ave_price > price_left, 
                                    Stock.weekly_ave_price < price_right)\
                            .paginate(page=page, per_page=5)
        print(result)
        return render_template("result.html", result=result, 
                                              leftprice=price_left, 
                                              rightprice=price_right)
    else:
        result = Stock.query.filter(Stock.weekly_ave_price > price_right, 
                                    Stock.weekly_ave_price < price_left)\
                            .paginate(page=page, per_page=5)
        print(result)
        return render_template("result.html", result=result, 
                                              leftprice=price_left, 
                                              rightprice=price_right)


####################################2.0 feature################################


@app.route('/watchlist')
def show_watchlist():
    """Show the watchlist."""

    # Check user id via email
    email = session.get('email')
    print(email, "in the session")
    user_id = db.session.query(User.user_id).filter_by(email=email).first()
    this_id = user_id[0]
     
    # Get user's watchlists
    user_watchlist = Watchlist.query.filter(Watchlist.user_id==this_id).all()
    print(user_watchlist)

    return render_template("watchlist.html", watchlist=user_watchlist)


@app.route('/linechart')
def show_linechart():
    """Show linechart for each stocks saved in the watchlists table."""

    # Check user id via email
    email = session.get('email')
    print(email, "in the session")
    user_id = db.session.query(User.user_id).filter_by(email=email).first()
    this_id = user_id[0]

    # Get daily EMA of monthly average
    watchlist_data = []
    data = {}
    user_watchlist = Watchlist.query.filter(Watchlist.user_id == this_id).all()
    for i in user_watchlist:
        symbol = i.stock_id
        print("chart", symbol)
        payload_ema = {'function': 'EMA',  
                   'symbol': symbol,
                   'interval': 'weekly',
                   'time_period': 30,
                   'series_type': 'open',
                   'apikey': 'G91S3ATZL5YIK83E'}
        req_ema = requests.get("https://www.alphavantage.co/query", params=payload_ema)
        print(req_ema.url)
        js_date_ema = req_ema.json().get('Technical Analysis: EMA', 0)
        
        if js_date_ema == 0:
            print('Change API key')
        
        # Grab date and ema from API dict into two lists
        emas = []
        dates = []
        for daily_date in js_date_ema:

            dates.append(daily_date)
            
        for daily_ema in js_date_ema.values():

            emas.append(daily_ema['EMA'])
        # Put data and emas in dict and add to data_list
        data_list = []
        for date, ema in zip(dates, emas):
            data_list.append({'date': date,
                         'ema': ema})
        # datalist example [{'date': '2020-02-25 15:25:03', 'ema': '11.9567'}, {'date': '2020-02-24', 'ema': '12.3'}]
        print("\n\n##################### data_list is working ##################")
        
        chart_data = {'symbol': symbol,'datas': data_list}

        watchlist_data.append(chart_data)

        # new data structure: [{'symbol': symbol,'data': data_list}, {'symbol': symbol,'data': data_list}]
        # old option: {'AAPL': [{'date': '2020-02-25 15:25:03', 'ema': '11.9567'}, {'date': '2020-02-24', 'ema': '12.3'}]}
    data = {'watchlist': watchlist_data}
    print(data['watchlist'][0]['datas'][0]['ema'])
    return data


@app.route('/watchlist', methods=["POST"])
def edit_watchlist():
    """Add stock id to the watchlist when user clicks the star icon;
       remove the stock id when user re-clicks."""
    
    stock = request.form.get('stock')
    email = request.form.get('email')
   
    print('\n\n\n\n*********', email, stock)
    the_user = User.query.filter_by(email=email).first()
    print("the user's info: ", the_user) # a user object
    user_id = the_user.user_id
    watchlist_by_stock_ids = {}
    for watchlist in the_user.watchlists:
        print("the user's interested stock: ", watchlist) # the user's watchlist object
        watchlist_by_stock_ids[watchlist.stock_id] = watchlist

    # delete the whole object if this stock exists in watchlists table
    if stock in watchlist_by_stock_ids: # key->id
        db.session.delete(watchlist_by_stock_ids[stock]) 
        db.session.commit()
        print("Deleted", stock)
    else:
        new_watchlist = Watchlist(user_id=user_id, stock_id=stock, ave_cost=0, shares=0)
        print("add", new_watchlist)
        db.session.add(new_watchlist)
        print("finish adding")
        db.session.commit()
    return "200"


@app.route('/login', methods=["POST"])
def add_user():
    """New member signin with Google."""

    email = request.form.get('email')
    session['email'] = email
    print("\nStored in session", session['email'])
    print('\n\n\n\n\n\n\n\n\n\n\n#################')
    
    # check if this email in database: 
    emails = []
    for i in db.session.query(User.email).all():
        emails.append(i[0])
    print(emails)

    if email in emails:
        print("\n**************Checked: ", email)
        return "You've logged in."
    else:
        new_user = User(email=email)
        print('About to add new user ', new_user)
        db.session.add(new_user)
        db.session.commit()
        print(User.query.filter_by(email=email).all())
        return "Hello, new user!" 
        #! cannot redirect to profile if install google on the frontend  


@app.route('/profile')
def show_profile():
    """New member signed in with Google, then go to profile page to register info."""

    return render_template("profile.html")


@app.route('/update', methods=["POST"])
def update_user_info():
    """Update user buying power, etc."""

    email = session.get('email')
    print('\n\n****', email)
    new_buying_power = request.form.get('buying-power')
    print('\n****', new_buying_power)

    this_user = User.query.filter_by(email=email).first()
    print("before update", this_user)
    this_user.buying_power = new_buying_power
    print("After update", this_user)
    db.session.commit()
    print('Updated new user information')
    
    return 'New information updated.'


@app.route('/saved')
def check_saved_stocks():
    """Check to see if there're saved stocks and mark them blue on the result pages."""

    # Check user id via email
    email = session.get('email')
    print("Logged in via:", email)
    user_id = db.session.query(User.user_id).filter_by(email=email).first()
    this_id = user_id[0]
    # user = User.query.filter_by(email=email).first()
     
    # Get user's watchlists
    user_watchlists = db.session.query(Watchlist.stock_id).filter(Watchlist.user_id==this_id).all()
    print(user_watchlists)
    # watchlist = user.watchlists
    # for i in watchlist:

    watchlists = {'watchlist': user_watchlists}
    response = jsonify(watchlists)
    return response


###############################################################################
if __name__ == "__main__":

    app.debug = True

    connect_to_db(app)
    #? Why do you need it in all model, server and seed?

    DebugToolbarExtension(app)
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.run(host="0.0.0.0")