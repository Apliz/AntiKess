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
        self.transfer_orbit = None
    
    def hohmann_transfer(self):
        """Returns total deltaV for a hohmann transfer manoeuvre in `km s-1`"""

        v1 = self.departure_orbit.velocity_at_position("apogee")
        v2 = self.arrival_orbit.velocity_at_position("perigee")

        if v1 > v2:
            self.transfer_orbit = Transfer.orbit(
                self.arrival_orbit.radius_at("perigee"),
                self.departure_orbit.radius_at("apogee")
            )
            vt1 = self.transfer_orbit.velocity_at_position("perigee")
            vt2 = self.transfer_orbit.velocity_at_position("apogee")
        elif v1 < v2:
            self.transfer_orbit = Transfer.orbit(
                self.departure_orbit.radius_at("apogee"),
                self.arrival_orbit.radius_at("perigee")
            )
            vt1 = self.transfer_orbit.velocity_at_position("apogee")
            vt2 = self.transfer_orbit.velocity_at_position("perigee")

        delta_v1 = vt1 - v1
        delta_v2 = vt2 - v2

        total_delta_v = abs(delta_v1) + abs(delta_v2)
        return f'total delta v for transfer is: {total_delta_v} km s-1'

    @staticmethod
    def switch_apsis(ap_in,pe_in):
        ap = pe_in
        pe = ap_in
        return ap, pe
    
    @staticmethod
    def orbit(ap,pe):
        e = Orbit.eccentricity(ap, pe)
        a = Orbit.a(ap, pe)
        P = Orbit.period(a)
        return Orbit(e,P,a)
