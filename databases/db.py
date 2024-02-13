import sqlite3, click, json
from flask import current_app, g, json
from static import utils
DATABASE = "./databases/orbitalBodies.db"

def get_db():
    # What is g? RESEARCH NEEDED
    if 'db' not in g:
        # Create/open the DATABASE
        # Not sure what PARSE_DECLTYPES does. RESEARCH NEEDED
        g.db = sqlite3.connect(DATABASE, detect_types=sqlite3.PARSE_DECLTYPES)
        # not sure what row_factory does. RESEARCH NEEDED
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():

    # connect to the database file, if created then open
    db = get_db()

    # execute the  sql code as written in schema.sql
    # Research needed into how the stream is operating here!
    with current_app.open_resource('databases/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

def insert_Data(data):
    db = get_db()
    decoded_json = utils.json_decode(data)

    count = 1
    for characteristic in decoded_json:
    # db.execute() inserts the JSON into the orbitalBodies.db
    ################################################## 
        db.execute("""
            INSERT INTO orbitalBodies(
                id,
                objectname,
                objectid,
                epoch,
                mean_motion,
                eccentricity,
                inclination,
                ra_ascending_node,
                mean_anomaly,
                ephemeris_type,
                classification_type,
                norad_cat_id,
                element_set_no,
                revolution_no,
                bstar,
                mean_motion_dot,
                mean_motion_ddot  
            ) VALUES (
                (SELECT MAX(id) + 1 FROM orbitalBodies),
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
            )""",(
                ################################################# 
                    # characteristic[n] is a stub value for the properties of a single body, accessed as the JSON is iterated through.
                #################################################         
                
                characteristic["OBJECT_NAME"],
                characteristic["OBJECT_ID"],
                characteristic["EPOCH"],
                float(characteristic["MEAN_MOTION"]),
                float(characteristic["ECCENTRICITY"]),
                float(characteristic["INCLINATION"]),
                float(characteristic["RA_OF_ASC_NODE"]),
                # float(characteristic["ARG_OF_PERICENTER"]),
                float(characteristic["MEAN_ANOMALY"]),
                int(characteristic["EPHEMERIS_TYPE"]),
                characteristic["CLASSIFICATION_TYPE"],
                int(characteristic["NORAD_CAT_ID"]),
                int(characteristic["ELEMENT_SET_NO"]),
                int(characteristic["REV_AT_EPOCH"]),
                float(characteristic["BSTAR"]),
                int(characteristic["MEAN_MOTION_DOT"]),
                int(characteristic["MEAN_MOTION_DDOT"]),
            ))
        count += 1

    # commit changes to database  
    db.commit()

    # Close the connection the database as per best practices
    close_db()
    
    # Might want to return a success/ error message here
    return None


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
