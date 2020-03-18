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

- PostgreSQL
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
Add your API key into the header scripts in static/templates/base.html, eg:
<br><br>
![api](https://raw.githubusercontent.com/teganbroderick/Travelmaps/master/static/img/YOUR_API_KEY.png)

Create database 'stocks':
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

![Homepage]()
<br>

#### Login/Sign Up <br>

![LoginSignup](https://media.giphy.com/media/Uqw7dksoH56H2nzirV/giphy.gif)
<br><br>


#### User Profile <br>

The user's profile picture of their Google account is shown on the left hand side of the page. Several questions of user's financial growth goal is listed on the right hand side of the page. 
<br><br>


#### Search Stocks <br>

Users type key words of the company name or stock symbol to search a stock.
![makemap](https://media.giphy.com/media/m9k3yceW91vTGeWH8x/giphy.gif)

#### Search and Save Places to Map

Users search for places using the Google Maps Places api. A custom marker info-window allows users to view place information, add place-specific notes, and save the place to the map.
![searchadd](https://raw.githubusercontent.com/teganbroderick/Travelmaps/master/static/img/search_add_marker.gif)
<br>

#### Navigate between list of places and map

As markers are saved, a list of saved places is displayed on the left hand side of the page. Clicking on a place header in the list centers the map on that place marker, and opens another custom info-window displaying place information and a button that deletes the place from the map. Users can also click directly on a marker to view its info-window. Clicking on a website link in the list opens the website in a new browser tab.
![Navigate](https://raw.githubusercontent.com/teganbroderick/Travelmaps/master/static/img/navigate_map.gif)
<br>

#### Delete marker

Places can be deleted from a map by clicking on the "Delete location from map" button in a saved place info-window.
![delete](https://raw.githubusercontent.com/teganbroderick/Travelmaps/master/static/img/delete_marker.gif)
<br>

#### Share map

A dynamic, read-only version of each map can be shared across the web using a shareable link.
![Sharemap](https://raw.githubusercontent.com/teganbroderick/Travelmaps/master/static/img/share_map.gif)
<br>

#### Internal dashboard

An internal dashboard is visible only to 'staff users' of the site, as defined in my data model. The dashboard shows aggregated data about trends across all users, visualized in a table, two chart.js charts, and a google maps heat map. <br>

* The bar chart shows the top 10 places saved across all maps <br>
* The donut chart shows the top five types of places (as defined by Google Maps) saved across all maps
* The heat map shows the concentration of places saved across all Maps <br>
* The table shows user statistics

![dashboard](https://raw.githubusercontent.com/teganbroderick/Travelmaps/master/static/img/internal_dashboard.gif)

#### Limited Access
![LimitedAccess](https://media.giphy.com/media/L40SJYXU2wwbv75XTx/giphy.gif)
<br>

## <a name="futureft"></a>Features for Version 2.0

* Modify data model and map permissions to allow multiple users to contribute to a single map
* Export dashboard data to an excel, csv, or jpg file
* Add dashboard page with aggregated data for each individual user

## <a name="aboutme"></a>About the Developer

Smart Investor creator Yichen Dai is a former world language teacher turned software engineer. This is her first fullstack project. She can be found on [LinkedIn](https://www.linkedin.com/in/yichen-dai-20557a195/) and on [Github](https://github.com/nancydyc).




















