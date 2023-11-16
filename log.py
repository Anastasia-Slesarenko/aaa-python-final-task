from functools import wraps
from random import randint


def log(text):
    """Decorator for text template"""

    def timer(func):
        """Print random int from 1 to 60"""

        @wraps(func)
        def wrapper_timer(*args):
            message = text.format(randint(1, 60))
            print(message)
            return func(*args)

        return wrapper_timer

    return timer


if __name__ == "__main__":
    pass
