"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from sqlalchemy import func #? What func is doing here?

from model import User, Stock, Watchlist, connect_to_db, db
from server import app 
# app is from flask


def load_users(email, buying_power):
    """Load users info into database from registered and user input."""

    print("Users")




def load_watchlists():
    """Load watchlists into database from user input."""

    print("Watchlists")




def load_stocks(company_name, ave_price):
    """Load company names into database from a file downloading data from Edgar Online.
       Load weekly EMA price from a file downloading data from Alpha Vantage."""

    print("Stocks")

    # for i, row in enumerate(open(rating_filename)):
    #     row = row.rstrip()

    #     user_id, movie_id, score, timestamp = row.split("\t")

    #     user_id = int(user_id)
    #     movie_id = int(movie_id)
    #     score = int(score)

    #     # We don't care about the timestamp, so we'll ignore this

    #     rating = Rating(user_id=user_id,
    #                     movie_id=movie_id,
    #                     score=score)

    #     # We need to add to the session or it won't ever be stored
    #     db.session.add(rating)

    #     # provide some sense of progress
    #     if i % 1000 == 0:
    #         print(i)

    #         # An optimization: if we commit after every add, the database
    #         # will do a lot of work committing each record. However, if we
    #         # wait until the end, on computers with smaller amounts of
    #         # memory, it might thrash around. By committing every 1,000th
    #         # add, we'll strike a good balance.

    #         db.session.commit()

    # # Once we're done, we should commit our work
    # db.session.commit()


# def set_val_user_id():
#     """Set value for the next user_id after seeding database"""

#     # Get the Max user_id in the database
#     result = db.session.query(func.max(User.user_id)).one()
#     max_id = int(result[0])

#     # Set the value for the next user_id to be max_id + 1
#     query = "SELECT setval('users_user_id_seq', :new_id)"
#     db.session.execute(query, {'new_id': max_id + 1})
#     db.session.commit()


if __name__ == "__main__":
    
    connect_to_db(app)
    #? Why do you need it in all model, server and seed?

    db.create_all()

    # user_filename = "seed_data/u.user"
    # movie_filename = "seed_data/u.item"
    # rating_filename = "seed_data/u.data"
    # load_users(user_filename)
    # load_movies(movie_filename)
    # load_ratings(rating_filename)
    # set_val_user_id()
