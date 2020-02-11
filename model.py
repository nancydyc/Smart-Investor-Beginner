"""Skills 5: SQLAlchemy & AJAX

This file is used in Part 1 of Skills 5: SQLAlchemy & AJAX.
"""

from flask_sqlalchemy import SQLAlchemy


# Instantiate a SQLAlchemy object. We need this to create our db.Model classes.
db = SQLAlchemy()


##############################################################################
# PART 1: COMPOSE ORM


class Human(db.Model):
    """Data model for a human."""

    __tablename__ = "humans"

    # Define your columns and/or relationships here
    human_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname =  db.Column(db.String(25), nullable=False)
    lname =  db.Column(db.String(25), nullable=False)
    email =  db.Column(db.String(100), nullable=False)
   
    animal = db.relationship('Animal', backref='humans')

    def __repr__(self):
        """Return a human-readable representation of a Human."""

        # Finish this __repr__ method
        return f'ID:{self.human_id} name:{self.fname} {self.lname} email:{self.email}'


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///animals"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
