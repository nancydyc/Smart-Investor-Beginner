# Smart-Investor-Beginner
Hackbright Academy Graduation Project

Smart Investor is a web app aims at advocating financial education for new investors interested in the stock market. The main features are:

  - Searching stocks by key words
  - Visualizing stock price
  - Stock screener
  - Bookmarking favorite stocks
  - Editing holding stocks value in the watchlist
 
This project was made at Hackbright Academy in San Francisco over four weeks from Febrary to March 2020.


# Contents

 - [Technologies] (#tech)
 - [Installation] (#install)
 - [Features] (#features)
 - [Features for Version 2.0] (#futureft)
 - [About the Developer] (#aboutme)
 
 
## <a name="tech"></a>Tech

Tech Stack: Python, JavaScript, HTML, CSS, Flask, Jinja, jQuery, AJAX, PostgreSQL, SQLAlchemy, Bootstrap, chart.js, Highcharts, unittest
APIs: Alpha Vantage, Edgar Online, Google Auth 2.0


## <a name="install"></a>Installation

To run Smart Investor requires:

- PostgreSQL
- [Python 3.6] (https://www.python.org/downloads/release/python-360/)
- API key for Edgar Online, Alpha Vantage APIs and Google OAuth 2.0 Client IDs

### Run Smart Investor on your local computer

Clone or fork repository:
```
$ git clone https://github.com/nancydyc/Smart-Investor-Beginner
```
Create and activate a virtual environment inside your Smart-Investor-Beginner directory:
```
$ virtualenv env (windows user use command: virtualenv env --always-copy)
$ source env/bin/activate
```
Install dependencies:
```
$ pip install -r requirements.txt
```
Add your API key into the header scripts in static/templates/base.html, eg:
<br><br>
![api](https://raw.githubusercontent.com/teganbroderick/Travelmaps/master/static/img/YOUR_API_KEY.png)

Create database 'stocks':
```
$ createdb stocks
```
Run model.py interactively in the terminal, and create database tables:
```
$ python3 -i model.py
>>> db.create_all()
>>> quit()
```
Run the app from the command line.
```
$ python3 server.py
```

## <a name="features"></a>Features






















