"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from sqlalchemy import func #? What func is doing here?

from model import User, Stock, Watchlist, connect_to_db, db
from server import app
import requests 
# app is from flask


def load_users(email, buying_power):
    """Load users info into database from registered and user input."""

    print("Users")




def load_watchlists():
    """Load watchlists into database from user input."""

    print("Watchlists")




def load_stocks():
    """Load company names into database from Edgar Online.
       Load weekly EMA price from Alpha Vantage."""
    print("Stocks")
    apikey = "1dfacbf9c7a25bb0e1c626ddcfcfb5b9"
    resourcename = "companies"
    fieldname = "primarysymbol"
    req_symbol = requests.get(f"https://datafied.api.edgar-online.com/v2/descriptions/{resourcename}/{fieldname}?Appkey={apikey}")
    # print(req_symbol.url)
    # print(req_symbol.json())
    js_symbol = req_symbol.json() # A-AAPL-ACIA
    symbols = js_symbol['descriptions']
    print(symbols)
    # for symbol in symbols:
        # print(symbol)
        # stock = Stock(stock_id=symbol)

        # db.session.add(stock)
    # print(stock)

    # db.session.commit()

    # Get matched symbols and company names
    symbolstring = ''
    for symbol in symbols:
        symbolstring = symbolstring + ',' + symbol
    symbolstring = symbolstring[1:]
    # print(symbolstring)

    payload = {'Appkey': apikey,
               'primarysymbols': symbolstring} 
    req_company = requests.get(f"https://datafied.api.edgar-online.com/v2/companies", params=payload)
    # print(req_company.url)
    rows = req_company.json()['result']['rows']
    # print(rows)

    companies = []
    primary_symbols = []
    for row in rows:
        companies.append(row['values'][1]['value'])
        primary_symbols.append(row['values'][6]['value'])
    print(companies)
    print(primary_symbols)

    # Get the most recent month 10 days EMA 
    for symbol in primary_symbols:
        payload_ema = {'function': 'EMA',  
                   'symbol': symbol,
                   'interval': 'monthly',
                   'time_period': 10,
                   'series_type': 'open',
                   'apikey': 'PVW38W9JBAXB0XGX'}
        req_ema = requests.get("https://www.alphavantage.co/query", params=payload_ema)
        # print(req_ema.url)
        js_date_ema = req_ema.json().get('Technical Analysis: EMA', 0)
        # get a list of prices but some stock has no values of technical EMA
        emas = []
        for ema in js_date_ema.values():
        
            emas.append(ema['EMA'])
        print(emas) 
        




            
        



    # for i, row in enumerate(open(rating_filename)):
    #     row = row.rstrip()

    #     user_id, movie_id, score, timestamp = row.split("\t")

    #     user_id = int(user_id)
    #     movie_id = int(movie_id)
    #     score = int(score)

    #     # We don't care about the timestamp, so we'll ignore this

    #     rating = Rating(user_id=user_id,
    #                     movie_id=movie_id,
    #                     score=score)

    #     # We need to add to the session or it won't ever be stored
    #     db.session.add(rating)

    #     # provide some sense of progress
    #     if i % 1000 == 0:
    #         print(i)

    #         # An optimization: if we commit after every add, the database
    #         # will do a lot of work committing each record. However, if we
    #         # wait until the end, on computers with smaller amounts of
    #         # memory, it might thrash around. By committing every 1,000th
    #         # add, we'll strike a good balance.

    #         db.session.commit()

    # # Once we're done, we should commit our work
    # db.session.commit()


# def set_val_user_id():
#     """Set value for the next user_id after seeding database"""

#     # Get the Max user_id in the database
#     result = db.session.query(func.max(User.user_id)).one()
#     max_id = int(result[0])

#     # Set the value for the next user_id to be max_id + 1
#     query = "SELECT setval('users_user_id_seq', :new_id)"
#     db.session.execute(query, {'new_id': max_id + 1})
#     db.session.commit()


if __name__ == "__main__":
    
    connect_to_db(app)
    # #? Why do you need it in all model, server and seed?
    db.create_all()
    load_stocks()

    # user_filename = "seed_data/u.user"
    # movie_filename = "seed_data/u.item"
    # rating_filename = "seed_data/u.data"
    # load_users(user_filename)
    # load_movies(movie_filename)
    # load_ratings(rating_filename)
    # set_val_user_id()
