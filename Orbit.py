"""Orbit Class"""
from math import pi, sqrt
from constants import GM

class Orbit():
    """Instance of an orbit around Earth \n
    `mean_motion` -> revolutions/day (currently unused)\n
    `eccentricity` -> abs value between 0 - 1 \n
    `perigee` -> orbital altitude in `km` \n
    `apogee` -> orbital altitude in `km` \n
    `semi_major_axis` -> distance in `km` \n
    
    """
    def __init__(self, mean_motion, eccentricity, perigee, apogee, period, semi_major_axis):
        # self.mean_motion currently unused
        self.mean_motion = mean_motion
        self.eccentricity = eccentricity
        self.perigee = perigee
        self.apogee = apogee
        self.period = period * 60
        self.semi_major_axis = semi_major_axis

    def radius_at(self, position:str) -> int:
        """ Returns the orbital radius at a given position in `km`\n`

            -> `position` accepts either 'apogee' or 'perigee'
        """
        match position:
            case "apogee":
                return self.semi_major_axis*(self.eccentricity + 1)
            case "perigee":
                return self.semi_major_axis*(1 - self.eccentricity)
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
    
    @staticmethod
    def mean_motion(a):
        n = 86400 * sqrt(GM / (4*pi**2*a**3))
        return n