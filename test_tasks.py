from unittest import TestCase
from tasks import say_hello, say_greetings


class TestTasks(TestCase):
    def test_say_hello_jonathan(self):
        self.assertEqual(say_hello("Jonathan"), "Hello, Jonathan")

    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello")

    def test_say_greetings(self):
        self.assertEqual(say_greetings(), "Greetings!")
