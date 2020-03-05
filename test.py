"""Demo test suite for testing Flask."""

import server
import unittest


class TestFlaskRoutes(unittest.TestCase):
    """Test Flask routes."""

    def test_home(self):
        """Make sure home page returns correct HTML."""

        # Create a test client
        client = server.app.test_client()

        # Use the test client to make requests
        result = client.get('/')

        # Compare result.data with assert method
        self.assertIn(b'<h2>Home</h2>', result.data)

    def test_search_stock_form(self):
        """Test that /stock route processes form data correctly."""

        client = server.app.test_client()
        result = client.get('/stock', query_string={'word': 'lk'})

        self.assertIn(b'Luckin Coffee Inc.', result.data)


if __name__ == '__main__':
    # If called like a script, run our tests
    unittest.main()