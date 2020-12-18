"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>> with supressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager


class Suppressor:
    def __init__(self, *exception):
        self.errors_to_skip = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return issubclass(exc_type, self.errors_to_skip)


@contextmanager
def suppressor(*exception):
    try:
        yield
    except exception:
        pass
