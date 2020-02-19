"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from sqlalchemy import func #? What func is doing here?

from model import User, Stock, Watchlist, connect_to_db, db
from server import app
from faker import Faker
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
    
    data_a = ['80.9032', '18.8916', '0', '15.0968', '0.0051']
    data_b = ['1.5071', '0.5300', '0.0006', '0.0002', '0.2487']
    data_c = ['0.0120', '0.0538', '28.3974', '13.4501', '2.0821']
    data_d = ['60.9237', '11.1399', '50.1589', '150.0254', '272.8828']
    data_e = ['0.0001', '0.6432', '0.4482', '46.5159', '4.7133']
    
    emas = data_a + data_b + data_c + data_d + data_e
    # print(emas)
    companies = ['AGILENT TECHNOLOGIES, INC.', 'ALCOA CORP', 'AAA CENTURY GROUP USA, INC.', 'PERTH MINT PHYSICAL GOLD ETF', 'ASIA BROADBAND INC', 'ATA CREATIVITY GLOBAL', 'AAC HOLDINGS, INC.', 'AMERICAN COMMERCE SOLUTIONS INC', 'ALL AMERICAN GOLD CORP.', 'AFTERMATH SILVER LTD.', 'AMERICA GREAT HEALTH', 'ALABAMA AIRCRAFT INDUSTRIES, INC', 'AMERICAN AIRLINES GROUP INC.', 'ALTISOURCE ASSET MANAGEMENT CORP', 'ATLANTIC AMERICAN CORP', "AARON'S INC", 'APPLIED OPTOELECTRONICS, INC.', 'AAON, INC.', 'ADVANCE AUTO PARTS INC', 'APPLE INC.', 'ALL AMERICAN PET COMPANY, INC.', "AMERICA'S SUPPLIERS, INC.", 'ALL AMERICAN SPORTPARK INC', 'AMERICAN ASSETS TRUST, INC.', 'AGAPE ATP CORP']
    symbols = ['A', 'AA', 'AAAG', 'AAAU', 'AABB', 'AACG', 'AACH', 'AACS', 'AAGC', 'AAGFF', 'AAGH', 'AAIIQ', 'AAL', 'AAMC', 'AAME', 'AAN', 'AAOI', 'AAON', 'AAP', 'AAPL', 'AAPT', 'AASL', 'AASP', 'AAT', 'AATP']

    for symbol, company, ema in zip(symbols, companies, emas):
        # print(symbol)
        stock = Stock(stock_id=symbol,
                      company_name=company,
                      weekly_ave_price=ema)

        db.session.add(stock)
    print(stock)

    db.session.commit()

    # apikey = "b7fd7ed058d07566df76db3dafc2ecb9"
    # resourcename = "companies"
    # fieldname = "primarysymbol"
    # req_symbol = requests.get(f"https://datafied.api.edgar-online.com/v2/descriptions/{resourcename}/{fieldname}?Appkey={apikey}")
    # print(req_symbol.url)
    # # print(req_symbol.json())
    # js_symbol = req_symbol.json() # A-AAPL-ACIA
    # symbols = js_symbol['descriptions']
    # # print(symbols)
    # symbolstring = ''
    # for symbol in symbols:
    #     symbolstring = symbolstring + ',' + symbol
    # symbolstring = symbolstring[1:]
    # # print(symbolstring)

    # payload = {'Appkey': apikey,
    #            'primarysymbols': symbolstring} 
    # req_company = requests.get(f"https://datafied.api.edgar-online.com/v2/companies", params=payload)
    # print(req_company.url)
    # rows = req_company.json()['result']['rows']
    # # print(rows)

    # companies = []
    # primary_symbols = []
    # for row in rows:
    #     companies.append(row['values'][1]['value'])
    #     primary_symbols.append(row['values'][6]['value'])

    # print(companies)
    # print(primary_symbols) # companies and symbols match at the same index

    # Get matched symbols and company names
    # symbols = []
    # primary = ['A', 'AA', 'AAAG', 'AAAU', 'AABB', 'AACG', 'AACH', 'AACS', 'AAGC', 'AAGFF', 'AAGH', 'AAIIQ', 'AAL', 'AAMC', 'AAME', 'AAN', 'AAOI', 'AAON', 'AAP', 'AAPL', 'AAPT', 'AASL', 'AASP', 'AAT', 'AATP', 'AATV', 'AAU', 'AAVVF', 'AAWC', 'AAWW', 'AAXN', 'AAXT', 'AB', 'ABAHF', 'ABB', 'ABBB', 'ABBV', 'ABBY', 'ABC', 'ABCB', 'ABCE', 'ABCP', 'ABDR', 'ABEC', 'ABENU', 'ABEO', 'ABEPF', 'ABEV', 'ABG', 'ABGOY', 'ABILF', 'ABIO', 'ABKB', 'ABLE', 'ABLT', 'ABM', 'ABMC', 'ABMD', 'ABML', 'ABMT', 'ABNAF', 'ABPR', 'ABQQ', 'ABR', 'ABSR', 'ABT', 'ABTI', 'ABTO', 'ABTX', 'ABUS', 'ABVC', 'ABVG', 'ABVN', 'ABWN', 'ABZUF', 'AC', 'ACA', 'ACAD', 'ACAM', 'ACAN', 'ACB', 'ACBD', 'ACBI', 'ACBM', 'ACC', 'ACCA', 'ACCO', 'ACCR', 'ACEL', 'ACER', 'ACEZ', 'ACFN', 'ACGI', 'ACGL', 'ACGX', 'ACH', 'ACHC', 'ACHFF', 'ACHV', 'ACIA']
    # primary_one = primary[:5]
    # primary_two = primary[5:10]
    # primary_three = primary[10:15]
    # primary_four = primary[15:20]
    # primary_five = primary[20:25]
    # Get the most recent month 5 days EMA 
    # emas = []

    # for symbol in primary_one:
    #     payload_ema = {'function': 'EMA',  
    #                'symbol': symbol,
    #                'interval': 'monthly',
    #                'time_period': 5,
    #                'series_type': 'open',
    #                'apikey': 'G91S3ATZL5YIK83E'}
    #     req_ema = requests.get("https://www.alphavantage.co/query", params=payload_ema)
    #     print(symbol, req_ema.url)
    #     js_date_ema = req_ema.json().get('Technical Analysis: EMA', 0)
    #     # get a list of prices of the symbol but some stock has no values of technical EMA
    #     # print(js_date_ema)
    #     if js_date_ema == 0:
    #         emas.append('0')
    #         print(emas)
    #     # return
    #     elif js_date_ema == {}:
    #         emas.append('0')
    #         print(emas)
    #     else:        
    #         print(js_date_ema)
    #         prices = list(js_date_ema.values())
    #         print(prices)
    #         price = prices[0]
    #         emas.append(price['EMA'])
    #         print(emas)
    # print(emas)



    # for symbol in primary_two:
    #     payload_ema = {'function': 'EMA',  
    #                'symbol': symbol,
    #                'interval': 'monthly',
    #                'time_period': 5,
    #                'series_type': 'open',
    #                'apikey': 'G91S3ATZL5YIK83E'}
    #     req_ema = requests.get("https://www.alphavantage.co/query", params=payload_ema)
    #     print(symbol, req_ema.url)
    #     js_date_ema = req_ema.json().get('Technical Analysis: EMA', 0)
    #     # get a list of prices of the symbol but some stock has no values of technical EMA
    #     # print(js_date_ema)
    #     if js_date_ema == 0:
    #         emas.append('0')
    #         print(emas)
    #     # return
    #     elif js_date_ema == {}:
    #         emas.append('0')
    #         print(emas)
    #     else:        
    #         print(js_date_ema)
    #         prices = list(js_date_ema.values())
    #         print(prices)
    #         price = prices[0]
    #         emas.append(price['EMA'])
    #         print(emas)
    # print(emas)

    # for symbol in primary_four:
    #     payload_ema = {'function': 'EMA',  
    #                'symbol': symbol,
    #                'interval': 'monthly',
    #                'time_period': 5,
    #                'series_type': 'open',
    #                'apikey': 'KSMJ9C8N2RZ92V0D'}
    #     req_ema = requests.get("https://www.alphavantage.co/query", params=payload_ema)
    #     print(symbol, req_ema.url)
    #     js_date_ema = req_ema.json().get('Technical Analysis: EMA', 0)
    #     # get a list of prices of the symbol but some stock has no values of technical EMA
    #     # print(js_date_ema)
    #     if js_date_ema == 0:
    #         emas.append('0')
    #         print(emas)
    #     # return
    #     elif js_date_ema == {}:
    #         emas.append('0')
    #         print(emas)
    #     else:        
    #         print(js_date_ema)
    #         prices = list(js_date_ema.values())
    #         print(prices)
    #         price = prices[0]
    #         emas.append(price['EMA'])
    #         print(emas)
    # print(emas)

    # for symbol in primary_five:
    #     payload_ema = {'function': 'EMA',  
    #                'symbol': symbol,
    #                'interval': 'monthly',
    #                'time_period': 5,
    #                'series_type': 'open',
    #                'apikey': 'PVW38W9JBAXB0XGX'}
    #     req_ema = requests.get("https://www.alphavantage.co/query", params=payload_ema)
    #     print(symbol, req_ema.url)
    #     js_date_ema = req_ema.json().get('Technical Analysis: EMA', 0)
    #     # get a list of prices of the symbol but some stock has no values of technical EMA
    #     # print(js_date_ema)
    #     if js_date_ema == 0:
    #         emas.append('0')
    #         print(emas)
    #     # return
    #     elif js_date_ema == {}:
    #         emas.append('0')
    #         print(emas)
    #     else:        
    #         print(js_date_ema)
    #         prices = list(js_date_ema.values())
    #         print(prices)
    #         price = prices[0]
    #         emas.append(price['EMA'])
    #         print(emas)
    # print(emas)



            
        



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

############################################################################
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
