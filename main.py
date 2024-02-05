
import math
import matplotlib.pyplot as plt
import json
from fractions import Fraction

# acceleration of Gravity on the surface of the Earth (m/s)
g = 9.81
# Radius of the Earth (m)
R = 6378000
Gm = 3.986004418*10**14

f = open("./lib/JSON/orbital_data.json")
orbitalJSON = json.load(f)
f.close()


# Goes through all bodies and calculates the semi-major axis (Assuming perfectly round orbits.)
#This is the start of the calculation that will eventually
# 1. Align all orbits (eccentricities included) at a given point (for example the semi-major-axis)
# 2. Return a sorted list of all heights at a point of all bodies on which pyplot can check distribution.
def semi_major_axis():
  bodies = []
  for i in orbitalJSON:
    # print(i["MEAN_MOTION"])
    n = i["MEAN_MOTION"]
    #convert mean motion (n) to usable radians/second
    radians_per_second = n * ((2*math.pi)/86400)
    # calculate semi-major axis of body
    a = Gm**Fraction(1,3) / radians_per_second**Fraction(2,3)
    print(f'{math.floor(a/10**3)}Km')
    return math.floor(a)


# test transfer
def hohmann(R, g,r1,r2) :
  gR2=g*R**2
  # semi_major_axis = (r1+r2)/2
  vTransfer_perigee = math.sqrt(gR2*((2.0/r1)-(2.0/(r1+r2))))
  vTransfer_apogee = math.sqrt(gR2*((2.0/r2)-(2.0/(r1+r2))))

  vCircular_1 = math.sqrt(gR2/r1)
  vCircular_2 = math.sqrt(gR2/r2)

  perigee_burn = vTransfer_perigee-vCircular_1
  apogee_burn = vCircular_2-vTransfer_apogee

  total_deltaV = perigee_burn + apogee_burn

  return total_deltaV

# print(hohmann(R,g,6.7*10**6,42.24*10**6))


