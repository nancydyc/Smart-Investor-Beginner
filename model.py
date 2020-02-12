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

        return f'<id:{self.user_id} buying power:{self.buying_power}>'


class Watchlist(db.Model):
    """Data model for a watchlist, recording the stocks which the user is watching."""

    __tablename__ = "watchlists"

    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.user_id'), 
                        primary_key=True)
    stock_id =  db.Column(db.Integer, 
                          db.ForeignKey('users.user_id'), 
                          primary_key=True) 
    ave_cost = db.Column(db.Integer, nullable=False, default=0)
    shares =  db.Column(db.Integer, nullable=False, default=0)

    # Identify relationships between the tables
    user = db.relationship('User', backref='watchlists')
    stock = db.relationship ('Stock', backref='watchlists')

    def __repr__(self):
        """Return a readable representation of a watchlist."""

        return f'<user id:{self.user_id} stock id:{self.stock_id} average cost:{self.ave_cost}>'       


class Stock(db.Model):
    """Data model for the details of the holding stock, recording price and amount."""

    __tablename__ = "stocks"

    stock_id = db.Column(db.String(10), 
                         nullable=False, 
                         primary_key=True)
    company_name = db.Column(db.String(50), nullable=False)
    weekly_ave_price = db.Column(db.Integer, nullable=False)
                
    # watchlists: one-many relationship to Stock class.

    def __repr__(self):
        """Return a readable representation of a watchlist."""

        return f'<watch-list id:{self.watch_id} stock-list:{self.stock_ids}>'

##############################################################################

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///stocks"
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
