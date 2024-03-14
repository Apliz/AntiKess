DROP TABLE IF EXISTS orbitalBodies;

CREATE TABLE orbitalBodies (
  id INTEGER PRIMARY KEY NOT NULL,
  objectname TEXT NOT NULL,
  objectid TEXT UNIQUE NOT NULL,
  epoch TEXT NOT NULL,
  mean_motion REAL NOT NULL,
  eccentricity REAL NOT NULL,
  periodT REAL NOT NULL,
  apoapsis REAL NOT NULL,
  periapsis REAL NOT NULL,
  semi_major_axis REAL NOT NULL
  -- inclination REAL NOT NULL,
  -- ra_ascending_node REAL NOT NULL,
  -- arg_pericenter REAL NOT NULL,
  -- mean_anomaly REAL NOT NULL,
  -- ephemeris_type INTEGER NOT NULL,
  -- classification_type TEXT NOT NULL,
  -- norad_cat_id INTEGER NOT NULL,
  -- element_set_no INTEGER NOT NULL,
  -- rev_at_epoch INTEGER NOT NULL,
  -- bstar REAL NOT NULL,
  -- mean_motion_dot INTEGER NOT NULL,
  -- mean_motion_ddot INTEGER NOT NULL
);