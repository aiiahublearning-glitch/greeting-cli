"""Tiny CLI that greets someone by name."""
import sys


def greet(name):
    name = name.strip()
    if not name:
        return "Hello, stranger!"
    return f"Hello, {name}!"


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else ""
    print(greet(name))


if __name__ == "__main__":
    main()
