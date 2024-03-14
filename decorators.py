"""Contains all custom decorators"""
from functools import wraps
from databases import db

def insert_into_table(func):
    """ Inserts decorated function data within table within db.   
    """
    @wraps(func)
    def decorator_wrap(*args):
        conn = db.get_db()
        func(*args, conn)
        conn.commit()
        db.close_db()
    return decorator_wrap
