
import math
import matplotlib.pyplot as plt
import json

f = open("./lib/JSON/orbital_data.json")
orbitalJSON = json.load(f)

print(orbitalJSON[0]["OBJECT_NAME"])


 
# Closing file
f.close()
# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()

# test transfer
# acceleration of Gravity on the surface of the Earth (m/s)
g = 9.81
# Radius of the Earth (m)
R = 6378000

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

print(hohmann(R,g,6.7*10**6,42.24*10**6))

