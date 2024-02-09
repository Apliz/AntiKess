DROP TABLE IF EXISTS bodies;

CREATE TABLE bodies (
  id INTEGER PRIMARY KEY,
  objectname TEXT UNIQUE NOT NULL,
  objectid TEXT UNIQUE NOT NULL,
  epoch TEXT NOT NULL,
  mean_motion REAL NOT NULL,
  eccentricity REAL NOT NULL,
  inclination REAL NOT NULL,
  ra_ascending_node REAL NOT NULL,
  mean_anomaly REAL NOT NULL,
  ephemeris_type INTEGER NOT NULL,
  classification_type TEXT NOT NULL,
  norad_cat_id INTEGER NOT NULL,
  element_set_no INTEGER NOT NULL,
  revolution_no INTEGER NOT NULL,
  bstar REAL NOT NULL,
  mean_motion_dot INTEGER NOT NULL,
  mean_motion_ddot INTEGER NOT NULL
);