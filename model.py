"""
Skills: Use SQLAlchemy to create database schema.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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

def example_data():
    """Create some sample data for testing."""

    # Empty out existing data
    Watchlist.query.delete()
    User.query.delete()
    Stock.query.delete()

    # Add example stocks and watchlists
    user = User(user_id=1, email='ydai7@mail.ccsf.edu', buying_power=8888)

    stock = Stock(stock_id='HMI',
                  company_name='Huami Corp',
                  weekly_ave_price=13.8)

    db.session.add_all([user, stock])
    db.session.commit()

    # You may also use user_id=user.user_id if you don't specify user_id above
    new_watchlist = Watchlist(user_id=1, 
                              stock_id='HMI', 
                              ave_cost=13.5, 
                              shares=100)

    db.session.add(new_watchlist)
    db.session.commit()


def connect_to_db(app, uri="postgres:///stocks"):
    """Connect the database to our Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = uri
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    
    connect_to_db(app)
    
    print("Connected to DB.")
