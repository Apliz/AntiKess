from flask import Flask, current_app as app, json
from databases import db

def format_data(data) :
  data = json.loads(data)
  return data

def orbitalBodiesSQLInsert(characteristic, count, database):
  database.execute("""
            INSERT OR IGNORE INTO orbitalBodies(
                id,
                objectname,
                objectid,
                epoch,
                mean_motion,
                eccentricity,
                periodT,
                apoapsis,
                periapsis,
                inclination,
                mean_anomaly,
                arg_of_pericenter,
                ra_of_asc_node,
                semi_major_axis
            ) VALUES (
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
                count,
                characteristic["OBJECT_NAME"],
                characteristic["OBJECT_ID"],
                characteristic["EPOCH"],
                float(characteristic["MEAN_MOTION"]),
                float(characteristic["ECCENTRICITY"]),
                float(characteristic["PERIOD"]),
                float(characteristic["APOAPSIS"]),
                float(characteristic["PERIAPSIS"]),
                float(characteristic["INCLINATION"]),
                float(characteristic["MEAN_ANOMALY"]),
                float(characteristic["ARG_OF_PERICENTER"]),
                float(characteristic["RA_OF_ASC_NODE"]),
                float(characteristic["SEMIMAJOR_AXIS"])
            ))