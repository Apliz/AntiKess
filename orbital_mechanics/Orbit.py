"""Orbit Class"""
from math import pi, sqrt
from constants import GM

class Orbit():
    """Instance of an orbit around Earth \n
    `eccentricity` -> abs value between 0 - 1 \n
    `period` -> orbital period in `s`
    `semi_major_axis` -> distance in `km` \n
    
    """
    def __init__(self, eccentricity, period, semi_major_axis):
        self.eccentricity = eccentricity
        self.period = period
        self.semi_major_axis = semi_major_axis

    def radius_at(self, position:str) -> int:
        """ Returns the orbital radius at a given position in `km`\n`

            -> `position` accepts either 'apogee' or 'perigee'
        """
        match position:
            case "apogee":
                r = self.semi_major_axis*(self.eccentricity + 1)
                return r
            case "perigee":
                r = self.semi_major_axis*(1 - self.eccentricity)
                return r
        raise NotImplementedError(position)

    def epsilon(self) -> float:
        """Returns the specific orbital energy for an elliptical orbit in `MJ kg-1`"""
        e = -abs(GM) / (2 * self.semi_major_axis)
        return e

    def velocity_at_position(self, ap_or_pe:str) ->int:
        """ Returns velocity of satellite at a given position `Km s-1` \n
            `position` -> The orbital radius 'height' from which instantaneous velocity will be calculated
        """
        v = sqrt(2*((GM / self.radius_at(ap_or_pe)) + self.epsilon()))
        return v

    def orbital_period(self) -> float:
        """Returns the period of an orbit `s`"""
        t = 2*pi*sqrt(self.semi_major_axis**3 / GM)
        return t

    @staticmethod
    def period(a):
        t = 2*pi*sqrt(a**3 / GM)
        return t

    @staticmethod
    def eccentricity(radius_ap, radius_pe):
        e = 1 - (2 / ((radius_ap/radius_pe) + 1))
        return round(e,7)

    @staticmethod
    def a(radius_ap, radius_pe):
        a = (radius_ap + radius_pe) / 2
        return a
    