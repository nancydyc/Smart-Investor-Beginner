from model import connect_to_db, db, User, Watchlist, Stock

import requests

def key_word_search(word):
    """Search stocks by the stock symbol or the key words of the company names.
       symbol: stock id.
    """

    # Get the company name of the stocks from Alphavantage search endpoint
    payload_name = {'function': 'SYMBOL_SEARCH',  
                    'keywords': word,
                    'apikey': 'CYUYBFS101MCWYTS'}

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


def get_realtime_price(symbol):
    """Show realtime (close) price from Alphavantage API."""

    payload_rt = {'function': 'TIME_SERIES_INTRADAY',  
               'symbol': symbol,
               'interval': '60min',
               'outputsize': 'compact',
               'apikey': 'CYUYBFS101MCWYTS'}

    req_realtime = requests.get("https://www.alphavantage.co/query", params=payload_rt)
    # print(req.url)
    js_data_rt = req_realtime.json()
    
    hourly_series_dict = js_data_rt.get('Time Series (60min)', 0)
    
    middle_key = list(hourly_series_dict.keys())[0]

    price = hourly_series_dict.get(middle_key, 0).get('4. close', 0)
    # print(price)
    realtime = {'symbol': symbol, 'realtime': price}
    print(realtime)
    return realtime


def get_weekly_ave(symbol):
    """Display weekly EMA of 10 days average price in the chart."""

    # Get weekly EMA open price data in csv from Alphavantage API
    payload_ema = {'function': 'EMA',  
               'symbol': symbol,
               'interval': 'weekly',
               'time_period': 10,
               'series_type': 'open',
               'datatype': 'csv',
               'apikey': 'CYUYBFS101MCWYTS'}
    
    data = requests.get("https://www.alphavantage.co/query", params=payload_ema)
    print(data.url)
    result = {'data': data.text, 'stock': symbol}
    # print(result)
    return result


def get_weekly_price(symbol):
    """Get weekly open price to display in the chart."""

    # Get weekly open price data in csv from Alphavantage API
    payload_ema = {'function': 'TIME_SERIES_WEEKLY',  
               'symbol': symbol,
               'interval': 'weekly',
               'datatype': 'csv',
               'apikey': 'G91S3ATZL5YIK83E'}
    
    data = requests.get("https://www.alphavantage.co/query", params=payload_ema)
    result = {'data': data.text, 'stock': symbol}
    print('/nIt is working')
    return result


def get_user(email):
    """Query database for user id.

    Examples:
        >>> get_user_id('johnsonamanda@hotmail.com')
        1
        >>> get_user_id('msdaiyichen@gmail.com')
        48
    """

    # Get user id via its email
    this_user = User.query.filter_by(email=email).first()
    
    return this_user


if __name__ == "__main__":

  from server import app
  
  connect_to_db(app)
  
  print("Connected to DB.")

  # key_word_search('luck')
  # get_realtime_price('lk')
  # get_monthly_ema_data('lk')
  # get_user_id('msdaiyichen@gmail.com')