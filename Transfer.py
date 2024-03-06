
import math
# import matplotlib.pyplot as plt
# import json
import sqlite3
from fractions import Fraction
import constants
# import databases.db as database

# This file only works in isolation. Attempts to call in as part of the flask app will fail.

class Transfer():

    def __init__(self, origin,target):
        self.origin = origin
        self.target = target
    # def calculate(self):
    #     Transfer.semi_major_axis()
    #     return 0 

    #   This method WONT WORK until r1,r2 are able to be calculated
    #   r1r2 method needed.
    @staticmethod
    def calculate_radii_ratio(r1:int, r2:int) -> int:

        radii_ratio = r2/r1
        return radii_ratio

    # deltaV calculation for a Hohmann transfer between 2 perfectly circular orbits
    # Still need to add in considerations for eccentricity
    # WONT WORK UNTIL SEMI-MAJOR AXIS FUNCTION IS WORKING
    @staticmethod
    def hohmann(R, g,r1,r2) :
        
        # transfer orbit velocities at apogee and perigee (m/s)
        vTransfer_perigee = math.sqrt(constants.GR2*((2.0/r1)-(2.0/(r1+r2))))
        vTransfer_apogee = math.sqrt(constants.GR2*((2.0/r2)-(2.0/(r1+r2))))

        #Calculate velocities of circular orbits (Start, target) (m/s)
        vCircular_1 = math.sqrt(constants.GR2/r1)
        vCircular_2 = math.sqrt(constants.GR2/r2)

        # Total needed burns at perigee and apogee to complete insertion into new orbit
        perigee_burn = vTransfer_perigee-vCircular_1
        apogee_burn = vCircular_2-vTransfer_apogee

        #Total deltaV
        total_deltaV = perigee_burn + apogee_burn

        return total_deltaV


# deltaV calculation for a Hohmann transfer between 2 perfectly circular orbits
transfer = Transfer()
transfer.calculate()
