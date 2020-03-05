import requests

def make_monthly_ema_line_chart(symbol):
    """Get stocks by symbol or key words and display EMA price chart."""

    # Get daily EMA price using 30 days' average calculation method
    payload_ema = {'function': 'EMA',  
               'symbol': symbol,
               'interval': 'weekly',
               'time_period': 30,
               'series_type': 'open',
               'apikey': 'PVW38W9JBAXB0XGX'}
    req_ema = requests.get("https://www.alphavantage.co/query", params=payload_ema)
    print(req_ema.url)

    js_date_ema = req_ema.json().get('Technical Analysis: EMA', 0)
    
    emas = []
    dates = []
    for daily_date in js_date_ema:
        dates.append(daily_date)   

    for daily_ema in js_date_ema.values():
        emas.append(daily_ema['EMA'])

    data_list = []
    for date, ema in zip(dates, emas):
        data_list.append({'date': date,
                     'ema': ema})
    data = {}
    data['data'] = data_list
    
    return data


if __name__ == "__main__":

  display_daily_ema_chart('hmi')