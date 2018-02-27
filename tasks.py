"""tasks.py - Some tasks to test Travis CI."""


def say_hello(name=None):
    """Say hello with or without name."""
    return "Hello" if name is None else "Hello, {}".format(name)


def say_greetings():
    """Say Greetings."""
    return "Greetings!"
