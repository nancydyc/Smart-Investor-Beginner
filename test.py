"""Demo test suite for testing Flask."""

from server import app
from unittest import TestCase
from model import example_data, connect_to_db, db
from flask import session

class TestFlaskRoutes(TestCase):
    """Test Flask routes."""

    def setUp(self):
        """Create a test client. """

        self.client = app.test_client()
        app.config['TESTING'] = True


    def test_home(self):
        """Make sure home page returns correct HTML."""

        # Use the test client to make requests
        result = self.client.get('/')
        # Compare result.data with assert method
        self.assertIn(b'<h2>Home</h2>', result.data)


    def test_search_stock_form(self):
        """Test that /stock route processes form data correctly."""

        result = self.client.get('/stock', query_string={'word': 'lk'})

        self.assertIn(b'Luckin Coffee Inc.', result.data)


class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")
        # Create tables and add sample data
        db.create_all()
        example_data()


    def test_screen_result(self):
        """Test screen result pages."""

        result = self.client.get("/result", query_string={'left': 1, 'right': 20})
        self.assertIn(b"HMI", result.data)


    def test_show_watchlist(self):
        """Test watchlist page."""

        result = self.client.get("/watchlist", query_string={'email': 'ydai7@mail.ccsf.edu'})
        self.assertIn(b"HMI", result.data)


    def tearDown(self):
        """Do at end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()


if __name__ == '__main__':

    import unittest
    unittest.main()