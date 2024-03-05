
import math
# import matplotlib.pyplot as plt
# import json
import sqlite3
from fractions import Fraction
import constants
# import databases.db as database

# This file only works in isolation. Attempts to call in as part of the flask app will fail.

class Transfer():

  # def __init__(self):


    def calculate(self):
        Transfer.semi_major_axis()
        return 0 


    # Compares the radii ratio to the constant ratios and calls the correct transfer type function
    # for the greatest efficiency

    # WONT WORK - it needs calculate_radii_ratio to be complete first.
    def most_efficient(self):
        match Transfer.calculate_radii_ratio():
            case [r] if r < constants.RATIO_HOHMANN:
                # r1,r2 have no definition

                # Transfer.hohmann(constants.R_EARTH, constants.G_EARTH,r1,r2)

                # stub return
                return 0
            case [r] if r < constants.RATIO_BIELLIPTIC and r >= constants.RATIO_HOHMANN:
                # stub return
                return 0
            case [r] if r >= constants.RATIO_BIELLIPTIC:
                # stub return
                return 0

    #   This method WONT WORK until r1,r2 are able to be calculated
    #   r1r2 method needed.
    @staticmethod
    def calculate_radii_ratio(r1:int, r2:int) -> int:
        # final orbit radii / initial orbit radii (r2/r1)
        # r1,r2 have no definition ye
        radii_ratio = r2/r1
        return radii_ratio

    # deltaV calculation for a Hohmann transfer between 2 perfectly circular orbits
    # Still need to add in considerations for eccentricity
    # WONT WORK UNTIL SEMI-MAJOR AXIS FUNCTION IS WORKING
    @staticmethod
    def hohmann(R, g,r1,r2) :

        # Get the semi major axis (USE FUCNTION - DEFUNCT FOR NOW)
        # semi_major_axis = (r1+r2)/2

        #Calculate transfer velocity needed at apogee and perigee (m/s)
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

    # Currently the method calculates the semi-major axes of all database entries and returns a string
    # It should eventually take parameters of the bodies between which the transfer is being calculated.
    @staticmethod
    def semi_major_axis() -> int:
        """Calculates the semi-major axis"""
        # hardcoded database connection. Refactor into something different in future.
        conn = sqlite3.connect('./databases/orbitalBodies.db',detect_types=sqlite3.PARSE_DECLTYPES)
        rows = conn.execute("""SELECT mean_motion FROM orbitalBodies;""").fetchall()
        
        for row in rows:
            # convert mean motion (n) to usable radians/second
            radians_per_second = row[0] * ((2*math.pi)/86400)

            # calculate semi-major axis of body
            sma = constants.GM_EARTH**Fraction(1,3) / radians_per_second**Fraction(2,3)

            #format
            print(f'{math.floor(sma/10**3)}Km')

            # return math.floor(sma)


# deltaV calculation for a Hohmann transfer between 2 perfectly circular orbits
transfer = Transfer()
transfer.calculate()  
