from math import pi, sqrt
from math import floor
from fractions import Fraction as frac
import constants

class Orbit():

    def __init__(self, mean_motion, eccentricity):
        self.mean_motion = mean_motion
        self.eccentricity = eccentricity
        self.semi_major_axis = self.calculate_semi_major_axis()

    def calculate_semi_major_axis(self) -> int:
        """Calculates the semi-major axis (Km)"""

        radians_per_second = self.mean_motion * ((2*pi)/86400)
        semi_major_axis = constants.GM_EARTH**frac(1,3) / radians_per_second**frac(2,3)
        print(semi_major_axis)
        return floor(semi_major_axis)

    def radius_perigee(self) -> int:
        """Returns orbit perigee (Km)"""
        pe = self.semi_major_axis*(1 - self.eccentricity)
        return pe

    def radius_apogee(self) -> int:
        """Returns orbit apogee (Km)"""
        ap = self.semi_major_axis*(self.eccentricity + 1)
        return ap

    def velocity_at_position(self, position:int) ->int:
        """returns velocity of satellite at a given position `(Kms^-1)` \n
                args: \n
                    `position` -> The orbital radius 'height' from which instantaneous velocity will be calculated
        """
        v = sqrt(constants.GM_EARTH*(frac(2/position) - frac(1/self.semi_major_axis)))
        return v

    # to calculate the optimal transfer window
    def orbital_period(self):
        """Returns the period of an orbit (unknown units)"""
        t = 2*pi*sqrt(frac(pow(self.semi_major_axis, 3), constants.GM_EARTH))
        return t