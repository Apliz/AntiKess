import sqlite3, click
from flask import current_app, g
from functools import wraps
from static import utils
from decorators import insert_into_table

DATABASE = "./databases/orbitalBodies.db"

def init_db():
    """Initialises database with script"""
    db = get_db()
    with current_app.open_resource('databases/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
       
def get_db():
    """Creates a connection to the database at path `DATABASE` within the application context `g`"""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE, detect_types=sqlite3.PARSE_DECLTYPES)
    return db

def close_db(e=None):
    """ Removes the database attribute from the application context `g`
        and closes the connetion is the attribute is not `None`
    """
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

@insert_into_table
def orbitalbodies(data,db):
    """Insert into table orbitalBodies table"""
    orbital_bodies_dict = utils.format_data(data)
    db.execute("""DELETE FROM orbitalBodies;""")
    count = 1
    for characteristic in orbital_bodies_dict:
        utils.orbitalBodiesSQLInsert(characteristic, count, db)
        count += 1
