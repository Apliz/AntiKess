import math
# import matplotlib.pyplot as plt
# import json
# import sqlite3
from math import sqrt
from fractions import Fraction as frac
import constants
from Orbit import Orbit
# import databases.db as database

# This file only works in isolation. Attempts to call in as part of the flask app will fail.

class Transfer(Orbit):
    """
        Input: origin and target orbital data
        Output: most efficient transfer between them
    """

    def __init__(self, origin, target):
        self.origin = Orbit(origin.mean_motion, origin.eccentricity)
        self.target = Orbit(target.mean_motion, target.eccentricity)

    #   This method WONT WORK until r1,r2 are able to be calculated
    #   r1r2 method needed.
    # @staticmethod
    # def calculate_radii_ratio(r1:int, r2:int) -> int:

    #     radii_ratio = r2/r1
    #     return radii_ratio

    def hohmann_transfer(self) :
        """calculates a hohmann transfer delta v requirement"""
        initial, final = self.determine_initial_and_final()

        initial_perigee = initial.radius_perigee()
        final_apogee = final.radius_apogee()

        velocity_at_initial_perigee = initial.velocity_at_position(initial_perigee)
        velocity_at_final_apogee = final.velocity_at_position(final_apogee)
        
        semi_major_axis_initial = initial.semi_major_axis
        semi_major_axis_final = final.semi_major_axis

        velocity_at_transfer_perigee = sqrt(constants.GR2*(frac(2, semi_major_axis_initial) - frac(2, semi_major_axis_initial + semi_major_axis_final)))
        velocity_at_transfer_apogee = sqrt(constants.GR2*(frac(2, semi_major_axis_final) - frac(2, semi_major_axis_initial + semi_major_axis_final)))

        delta_v_transfer_perigee = velocity_at_transfer_perigee - velocity_at_initial_perigee
        delta_v_transfer_apogee = velocity_at_final_apogee - velocity_at_transfer_apogee

        total_delta_v = delta_v_transfer_perigee + delta_v_transfer_apogee

        if self.target.radius_apogee() < self.origin.radius_perigee():
            return -abs(total_delta_v)
        else:
            return total_delta_v

    def determine_initial_and_final(self):
        if self.origin.radius_perigee() < self.target.radius_apogee():
            initial = self.origin
            final = self.target
        else:
            initial = self.target
            final = self.origin       
        return initial,final
    