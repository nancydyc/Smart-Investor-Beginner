"""Investing Stocks."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify, url_for
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Watchlist, Stock

from smart import key_word_search, get_realtime_price, get_monthly_ema_data, get_user_id

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
       word: stock id or company name key word.
    """

    # Get user input from the search form
    word = request.args.get('word') 

    return key_word_search(word)


@app.route('/stock/<symbol>')
def display_realtime_price(symbol):
    """Show realtime (close) price from Alphavantage API."""

    real_time = get_realtime_price(symbol)

    return jsonify(real_time)


@app.route('/chart/<symbol>')
def display_daily_ema_chart(symbol):
    """Get stocks by symbol or key words and display EMA price chart."""

    data = {}    
        
    data['data'] = get_monthly_ema_data(symbol)

    return data


@app.route('/screen')
def screen_stocks():
    """Stock screener, showing screening criteria."""

    return render_template("screen.html")


@app.route('/result')
def screen_result():
    """Display stock screening results in a table. Showing stock symbols, 
       company names and prices.
       left: the price user types in the left input box on stock screener page.
       right: the price user types in the right input box on stock screener page.
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

    this_id = get_user_id(email)

    # Get daily EMA of monthly average
    watchlist_data = []

    data = {}

    user_watchlist = Watchlist.query.filter(Watchlist.user_id == this_id).all()
    
    for i in user_watchlist:
        symbol = i.stock_id
        watchlist_data.append({'symbol': symbol,
                               'datas': get_monthly_ema_data(symbol)})
 
    data = {'watchlist': watchlist_data}

    return data


@app.route('/watchlist', methods=["POST"])
def edit_watchlist():
    """Add stock id to the watchlist when user clicks the star icon;
       remove the stock id when user re-clicks."""
    
    stock = request.form.get('stock')
    email = request.form.get('email')
   
    user_id = get_user_id(email)

    watchlist_by_stock_ids = {}

    for watchlist in the_user.watchlists:
        print("the user's interested stock: ", watchlist)
        watchlist_by_stock_ids[watchlist.stock_id] = watchlist

    # delete the whole object if this stock exists in watchlists table
    if stock in watchlist_by_stock_ids:
        db.session.delete(watchlist_by_stock_ids[stock]) 
        db.session.commit()
        print("Deleted", stock)

    else:
        new_watchlist = Watchlist(user_id=user_id, 
                                  stock_id=stock, 
                                  ave_cost=0, 
                                  shares=0)
        print("add", new_watchlist)
        db.session.add(new_watchlist)
        db.session.commit()

    return "200"


@app.route('/login', methods=["POST"])
def add_user():
    """New member signin with Google."""

    email = request.form.get('email')
    session['email'] = email
    
    # check if this email in database: 
    emails = []
    for i in db.session.query(User.email).all():
        emails.append(i[0])

    if email in emails:
        
        return "You've logged in."

    else:
        new_user = User(email=email)
        db.session.add(new_user)
        db.session.commit()

        return "Hello, new user!" 
 


@app.route('/profile')
def show_profile():
    """New member signed in with Google, then go to profile page to register info."""

    return render_template("profile.html")


@app.route('/update', methods=["POST"])
def update_user_info():
    """Update user buying power, etc."""

    email = session.get('email')

    new_buying_power = request.form.get('buying-power')

    this_user = User.query.filter_by(email=email).first()
    # print("before update", this_user)
    this_user.buying_power = new_buying_power
    # print("After update", this_user)
    db.session.commit()
    
    return 'New information updated.'


@app.route('/saved')
def check_saved_stocks():
    """Check to see if there're saved stocks and mark them blue on the result pages."""

    # Check user id via email
    email = session.get('email')

    this_id = get_user_id(email)
     
    # Get user's watchlists
    user_watchlists = db.session.query(Watchlist.stock_id).filter(Watchlist.user_id==this_id).all()
    print(user_watchlists)

    watchlists = {'watchlist': user_watchlists}

    return jsonify(watchlists)


###############################################################################
if __name__ == "__main__":

    # from doctest import testmod

    # if testmod().failed == 0:
    connect_to_db(app)
    app.debug = True
    DebugToolbarExtension(app)
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.run(host="0.0.0.0")
    