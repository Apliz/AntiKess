from spacetrack import SpaceTrackClient
from dotenv import dotenv_values

envar = dotenv_values(".env")

def spacetrack() ->str:
    """GET and return data from `spactrack.org`"""
    st = SpaceTrackClient(envar["SPACETRACK_USERNAME"],envar["SPACETRACK_PASSWORD"])
    data = st.generic_request("gp",object_type="DEBRIS",format="json",limit=10)
    return data
