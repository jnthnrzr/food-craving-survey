import unittest

from application import app, db
from application.config import TestingConfig
from application.forms import InputForm


class TestViews(unittest.TestCase):
    def setUp(self):
        """Set testing configuration before each test."""
        app.config.from_object(TestingConfig)
        self.app = app
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        """Clear testing configuration after each test."""
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
