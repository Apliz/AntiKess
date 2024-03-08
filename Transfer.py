import math
# import matplotlib.pyplot as plt
# import json
# import sqlite3
from math import sqrt
import constants
from Orbit import Orbit
# import databases.db as database

# This file only works in isolation. Attempts to call in as part of the flask app will fail.

class Transfer(Orbit):
    """
        Input: origin and target orbital data
        Output: most efficient transfer between them
    """

    def __init__(self, departure_orbit, arrival_orbit):
        self.departure_orbit = departure_orbit
        self.arrival_orbit = arrival_orbit

    #   This method WONT WORK until r1,r2 are able to be calculated
    #   r1r2 method needed.
    # @staticmethod
    # def calculate_radii_ratio(r1:int, r2:int) -> int:

    #     radii_ratio = r2/r1
    #     return radii_ratio
        
    def a_transfer(self):
        """return the semi-major axis of a transfer orbit"""
        r1 = self.departure_orbit.radius_at("apogee")
        r2 = self.arrival_orbit.radius_at("perigee")
        return (r1+r2) / 2

    def hohmann_transfer(self):
        # variables
        # v1 - velocity at mission orbit apogee before burn
        # vt1 - velocity at transfer orbit start (the apogee)
        # v2 - velocity at final orbit perigee before burn
        # vt2 - velocity at new orbit
        v1 = self.departure_orbit.velocity_at_position("apogee")
        v2 = self.arrival_orbit.velocity_at_position("perigee")

        vt1 = sqrt(2*((constants.GM_EARTH / self.departure_orbit.radius_at("apogee")) + (-abs(constants.GM_EARTH) / (2 * self.a_transfer()))))
        vt2 = sqrt(2*((constants.GM_EARTH / self.arrival_orbit.radius_at("perigee")) + (-abs(constants.GM_EARTH) / (2 * self.a_transfer()))))

        delta_v1 = vt1 - v1
        delta_v2 = vt2 - v2

        total_delta_v = delta_v1 + delta_v2
        print(f'velocity before departure orbit burn : {v1}')
        print(f'velocity before arrival orbit burn : {v2}')
        print(f'v1 burn : {delta_v1}')
        print(f'v2 burn : {delta_v2}')
        return total_delta_v
   