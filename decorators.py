"""Contains all custom decorators"""
from functools import wraps
from databases import db

# Refactor database naming here. sloppy
def insert_into_table(func):
    """ Inserts decorated function data within table within db.   
    """
    @wraps(func)
    def decorator_wrap(*args):
        database = db.get_db()
        func(*args, database)
        database.commit()
        db.close_db()
    return decorator_wrap
