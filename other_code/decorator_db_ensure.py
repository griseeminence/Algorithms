import sqlite3


def ensure_connection(func):
    """
    The decorator allows not to explicitly open a connection in each function.
    The decorator opens a connection (using with...), passes it to the function to which it is applied.
    And after exiting the with block, the decorator closes the connection.
    This makes database connections more secure.
    """

    def inner(*args, **kwargs):
        with sqlite3.connect('something.db') as conn:
            res = func(*args, conn=conn, **kwargs)
        return res
    return inner
