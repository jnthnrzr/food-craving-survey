"""tasks.py - Some tasks to test Travis CI."""


def say_hello(name=None):
    """Say hello with or without name."""
    if name == None:
        return "Hello"
    else:
        return f"Hello, {name}"


def say_greetings():
    """Say Greetings."""
    return "Greetings!"
