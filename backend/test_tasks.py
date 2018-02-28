import unittest
from tasks import say_hello, say_greetings


class TestTasks(unittest.TestCase):
    def test_say_hello_jonathan(self):
        hello_jonathan = say_hello("Jonathan")
        self.assertEqual(hello_jonathan, "Hello, Jonathan")

    def test_say_hello(self):
        hello = say_hello(None)
        self.assertEqual(hello, "Hello")

    def test_say_greetings(self):
        greetings = say_greetings()
        self.assertEqual(greetings, "Greetings!")


if __name__ == '__main__':
    unittest.main()
