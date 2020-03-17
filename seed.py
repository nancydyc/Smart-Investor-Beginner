"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from sqlalchemy import func

from model import User, Stock, Watchlist, connect_to_db, db
from server import app
from faker import Faker
import requests
import random 

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
    # print(stock)

    db.session.commit()
    print('loaded stocks')


def load_users():
    """Load users info into database from registered and user input."""

    print("Users")

    fake = Faker()
    emails = []
    # Get email list
    for i in range(10):
        emails.append(fake.email())
    # Get buying_power list
    # buying_powers = []
    buying_powers = random.sample(range(50000), 10)
    print(emails, buying_powers)
    
    for email, power in zip(emails, buying_powers):
        user = User(email=email, buying_power=power)
        # print(user)
        db.session.add(user)
    db.session.commit()
    print('loaded users')


def load_watchlists():
    """Load watchlists into database from user input."""

    print("Watchlists")

    shares = random.sample(range(500), 10)
    # Get random floats
    costs = []
    for i in range(10):
        costs.append(round(random.uniform(1, 99.9), 2))
    
    users = list(range(1, 11))

    stocks = ['AAN', 'AAPL', 'AAON', 'AAP', 'AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAT', 'AAPL']
    for share, cost, user, stock in zip(shares, costs, users, stocks):
        watchlist = Watchlist(shares=share, ave_cost=cost, user_id=user, stock_id=stock)
        print(watchlist)
        db.session.add(watchlist)
    db.session.commit()
    print('loaded watchlists')

############################################################################
if __name__ == "__main__":
    
    connect_to_db(app)

    db.create_all()
    # load_stocks()
    # load_users()
    # load_watchlists()
    
