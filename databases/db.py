import sqlite3,click, json
from flask import current_app, g, json
from static import utils
DATABASE = "./databases/orbitalBodies.db"

def get_db():
    # What is g? RESEARCH NEEDED
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE, detect_types=sqlite3.PARSE_DECLTYPES)
        # not sure what row_factory does. RESEARCH NEEDED
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('databases/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

def insert_Data(data):
    db = get_db()
    debris_dict = utils.format_data(data)
    db.execute("""DELETE FROM orbitalBodies;""")   
    count = 1
    for characteristic in debris_dict:
        utils.orbitalBodiesSQLInsert(characteristic, count, db)
        count += 1
    db.commit()
    close_db()

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
