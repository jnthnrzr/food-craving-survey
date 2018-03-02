import unittest
from src import app


class TestViews(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_index(self):
        result = self.app.get('/')
        self.assertEqual(result.data, b"Hello World!")


if __name__ == '__main__':
    unittest.main()
