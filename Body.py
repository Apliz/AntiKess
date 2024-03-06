from math import pi
from math import floor
from fractions import Fraction as frac
import constants

class Orbit():

    def __init__(self, mean_motion, eccentricity):
        self.mean_motion = mean_motion
        self.eccentricity = eccentricity
        self.semi_major_axis = self.calculate_semi_major_axis()
    
    def calculate_semi_major_axis(self) -> int:
        """Calculates the semi-major axis"""
      
        # convert mean motion (n) to usable radians/second
        radians_per_second = self.mean_motion * ((2*pi)/86400)

        # calculate semi-major axis of body
        semi_major_axis = constants.GM_EARTH**frac(1,3) / radians_per_second**frac(2,3)
        return floor(semi_major_axis)
        #format
        # print(f'{floor(sma/10**3)}Km')

    def periapsis(self):
        pe = self.semi_major_axis*(1 - self.eccentricity)
        return pe

    def apoapsis(self):
        ap = self.semi_major_axis*(self.eccentricity + 1)
        return ap
        