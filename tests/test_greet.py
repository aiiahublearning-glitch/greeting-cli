from greet import greet


def test_greet_with_name():
    assert greet("Ana") == "Hello, Ana!"


def test_greet_strips_whitespace():
    assert greet("  Bob  ") == "Hello, Bob!"
