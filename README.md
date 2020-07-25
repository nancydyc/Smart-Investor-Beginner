# Smart-Investor-Beginner
Hackbright Academy Graduation Project

Smart Investor is a web app aims at advocating financial education for new investors interested in the stock market. The main features are:

  - Searching stocks by key words
  - Visualizing stock price
  - Stock screener
  - Bookmarking favorite stocks
  - Editing holding stocks value in the watchlist
 
This project was made at Hackbright Academy in San Francisco over four weeks from Febrary to March 2020.

Deployed to AWS LightSail at [www.yichendai.com](http://www.yichendai.com/)


# Contents

 * [Technologies](#tech)
 * [Installation](#install)
 * [Features](#features)
 * [Features for Version 2.0](#futureft)
 * [About the Developer](#aboutme)
 
 
## <a name="tech"></a>Tech

Tech Stack: Python, JavaScript, HTML, CSS, Flask, Jinja, jQuery, AJAX, PostgreSQL, SQLAlchemy, Bootstrap, chart.js, Highcharts, unittest

APIs: Alpha Vantage, Edgar Online, Google Auth 2.0


## <a name="install"></a>Installation

To run Smart Investor requires:

- [PostgreSQL](https://www.postgresqltutorial.com/)
- [Python 3.6](https://www.python.org/downloads/release/python-360/)
- API key for Edgar Online, Alpha Vantage APIs and [Google OAuth 2.0 Client IDs](https://console.developers.google.com/)

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
Add your API key into the header scripts in static/templates/base.html

Create database:
```
$ createdb stocks
```
Run model.py interactively in the terminal, and create database tables of users, stocks, watchlists:
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

#### Login/Profile <br>

The user's profile picture of their Google account is shown on the left hand side of the page. Several questions of user's financial growth goal is listed on the right hand side of the page. <br><br>
![LoginSignup](https://media.giphy.com/media/Uqw7dksoH56H2nzirV/giphy.gif)
<br>

#### Search Stocks <br>

Users type key words of the company name or stock symbol to search a stock. <br><br>
![makemap](https://media.giphy.com/media/m9k3yceW91vTGeWH8x/giphy.gif)
<br>

#### Visualize Data in Charts <br>

Users click on show chart button and get a chart with two line graphs of stock weekly history price and Exponential Moving Average. Users can view the chart in full screen, zoom, download or print out a csv file of the stock price data. <br><br>
![viewcharts](https://media.giphy.com/media/MZcg09vK7ddU7NDdwD/giphy.gif)
![zoom](https://media.giphy.com/media/fWwmpUZI56jII72xkf/giphy.gif)
<br>

#### Stock Screener <br>

Users can do stock screening, filtering by price range. <br><br>
![filter](https://media.giphy.com/media/MAuUCnPmRjqLzYiBnO/giphy.gif)
<br>

#### Pagination <br>

The screening results is a long table divided by multiple pages through SQLAlchemy paginate method. <br><br>
![pagination](https://media.giphy.com/media/UW8iYgB8zMJif8krNa/giphy.gif)
<br>

#### Bookmark Stocks <br>

Users will be able to bookmark a stock by clicking the star icon in front of it once they log in via Google. <br><br>

![bookmark](https://media.giphy.com/media/lqpulwxEcOFU9OKqQo/giphy.gif)

#### Limited Access <br>

Users need to sign in to get access to the bookmarking feature and editing their watchlists. <br><br>
![LimitedAccess](https://media.giphy.com/media/L40SJYXU2wwbv75XTx/giphy.gif)
<br>

## <a name="futureft"></a>Features for Version 2.0

* Allow users to sort screening results by price
* Add chat feature to communicate with users
* Add price alert feature
* Allow users to take notes in their watchlist 

## <a name="aboutme"></a>About the Developer

Smart Investor creator Yichen Dai is a former world language teacher turned software engineer. This is her first fullstack project. She can be found on [LinkedIn](https://www.linkedin.com/in/yichen-dai-20557a195/) and on [Github](https://github.com/nancydyc).




















