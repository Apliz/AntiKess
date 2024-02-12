import sqlite3, click, json
from flask import current_app, g
import json

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
    my_json = data.decode('utf8').replace('"','"')

    data = json.loads(my_json)
    print(data["OBJECT_NAME"])

    # Code to change the JSON back to str
    # s = json.dumps(data, indent=4, sort_keys=True)
    # print(type(s))   
     

     ################################################## 
    # Eventually the below db.execute() call will insert the JSON into the database using the provided SQL
    # by iterating through the bodies and adding the values in dynamically

    # This pseudocode still needs a commit to database function to be added.
    
    # The schema will also be optimised eventually. it currently contains ALL of the data included by celestrack. Once the data needed
    # for the transfer calculations are identified, the redundant properties should be removed from the schema so they are
    # not stored in the database
    ################################################## 

    # db.execute('''
    #     INSERT INTO orbitalBodies(
    #         id,
    #         objectname,
    #         objectid,
    #         epoch,
    #         mean_motion,
    #         eccentricity,
    #         inclination,
    #         ra_ascending_node,
    #         mean_anomaly,
    #         ephemeris_type,
    #         classification_type,
    #         norad_cat_id,
    #         element_set_no,
    #         revolution_no,
    #         bstar,
    #         mean_motion_dot,
    #         mean_motion_ddot,   
    #     ) VALUES (
    #         ?,
    #         ?,
    #         ?,
    #         ?,
    #         ?,
    #         ?,
    #         ?,
    #         ?,
    #         ?,
    #         ?,
    #         ?,
    #         ?,
    #         ?,
    #         ?,
    #         ?,
    #         ?,
    #         ?,
    #     )'''
    #     (
            ################################################## 
            #  characteristic[n] is a stub value for the properties of a single body, accessed as the JSON is iterated through.
            ##################################################         
    #         characteristic[0],
    #         characteristic[1],
    #         characteristic[2],
    #         characteristic[3],
    #         characteristic[4],
    #         characteristic[5],
    #         characteristic[6],
    #         characteristic[7],
    #         characteristic[8],
    #         characteristic[9],
    #         characteristic[10],
    #         characteristic[11],
    #         characteristic[12],
    #         characteristic[13],
    #         characteristic[14],
    #         characteristic[15],
    #         characteristic[16]   
    #     ))
     ################################################## 
    
    # Close the connection the database as per best practices
    close_db()
    #Not sure if it's necessary for the function to return anything. RESEARCH NEEDED
    return 0


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
