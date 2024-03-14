"""Transfer Class"""
from math import sqrt
from constants import GM
from Orbit import Orbit

# Not yet integrated into Flask.
# Not yet hooked up to the database
class Transfer(Orbit):
    """Instance of an orbital transfer within Earth's orbit"""

    def __init__(self, departure_orbit, arrival_orbit):
        self.departure_orbit = departure_orbit
        self.arrival_orbit = arrival_orbit
    
    def hohmann_transfer(self):
        """Returns total deltaV for a hohmann transfer manoeuvre in `km s-1`"""
        v1 = self.departure_orbit.velocity_at_position("apogee")
        v2 = self.arrival_orbit.velocity_at_position("perigee")

        transfer_orbit = Transfer.orbit(
            self.arrival_orbit.radius_at("perigee"),
            self.departure_orbit.radius_at("apogee")
        )

        vt1 = transfer_orbit.velocity_at_position("apogee")
        vt2 = transfer_orbit.velocity_at_position("perigee")
    
        delta_v1 = vt1 - v1
        delta_v2 = vt2 - v2

        total_delta_v = delta_v1 + delta_v2
        return total_delta_v
    
    @staticmethod
    def orbit(perigee,apogee):
        eccentricity = Orbit.eccentricity(apogee, perigee)
        semi_major_axis = Orbit.a(apogee, perigee)
        period = Orbit.period(semi_major_axis)
        return Orbit(0,eccentricity,perigee,apogee,period,semi_major_axis)
