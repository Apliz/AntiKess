import spacetrack.operators as op
from spacetrack import SpaceTrackClient
from dotenv import dotenv_values

envar = dotenv_values("../.env")

st = SpaceTrackClient(envar["SPACETRACK_USERNAME"], envar["SPACETRACK_PASSWORD"])
print(st.generic_request("gp",object_type="DEBRIS",format="json",limit=10))
