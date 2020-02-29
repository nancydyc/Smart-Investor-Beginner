"""
Skills: Use SQLAlchemy to create database schema.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


##############################################################################

class User(db.Model):
    """Data model for a user, recording email and available money."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, 
                        nullable=False, 
                        primary_key=True, 
                        autoincrement=True)
    buying_power = db.Column(db.Integer, nullable=True)
    email =  db.Column(db.String(100), nullable=False)
   
    # watchlists: one-one relationship to User class.

    def __repr__(self):
        """Return a readable representation of a user's information."""

        return f'<id:{self.user_id} email: {self.email} buying power:{self.buying_power}>'


class Watchlist(db.Model):
    """Data model for a watchlist, recording the stocks which the user is watching."""

    __tablename__ = "watchlists"

    watch_id = db.Column(db.Integer, 
                        nullable=False, 
                        primary_key=True, 
                        autoincrement=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'), 
                        nullable=False)
                        # primary_key=True)
    stock_id =  db.Column(db.String(10),
                          db.ForeignKey('stocks.stock_id'), 
                          nullable=True) 
                          # primary_key=True) 
    ave_cost = db.Column(db.Numeric, nullable=False, default=0)
    shares =  db.Column(db.Integer, nullable=False, default=0)

    # Identify relationships between the tables
    user = db.relationship('User', backref='watchlists')
    stock = db.relationship ('Stock', backref='watchlists')

    def __repr__(self):
        """Return a readable representation of a watchlist."""

        return f'<user id:{self.user_id} stock id:{self.stock_id} average cost:{self.ave_cost} shares:{self.shares}>'       


class Stock(db.Model):
    """Data model for the details of the holding stock, recording price (latest 5-day's EMA) and amount."""

    __tablename__ = "stocks"

    stock_id = db.Column(db.String(10), 
                         nullable=False, 
                         primary_key=True)
    company_name = db.Column(db.String(50), nullable=False)
    weekly_ave_price = db.Column(db.Float(10,2), nullable=False)
                
    # watchlists: one-many relationship to Stock class.

    def __repr__(self):
        """Return a readable representation of a watchlist."""

        return f'<stock id:{self.stock_id}>'

##############################################################################

def connect_to_db(app, uri="postgres:///stocks"):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config["SQLALCHEMY_DATABASE_URI"] = uri
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    # app is from flask
    
    connect_to_db(app)
    
    print("Connected to DB.")
