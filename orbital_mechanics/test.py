from Orbit import Orbit
from Transfer import Transfer

print("transfer 1")
print("############")

i1 = Orbit(0.0013117, 88.284, 6567.704)
f1 = Orbit(0.0010391, 99.597, 7117.427)
transfer1 = Transfer(i1,f1)
print(transfer1.hohmann_transfer())
print(f'eccentricity of transfer orbit : {transfer1.transfer_orbit.eccentricity}')

print("transfer 2")
print("############")

i2 = Orbit(0.0010391, 99.597, 7117.427)
f2 = Orbit(0.0013117, 88.284, 6567.704)
transfer2 = Transfer(i2,f2)
print(transfer2.hohmann_transfer())
print(f'eccentricity of transfer orbit : {transfer2.transfer_orbit.eccentricity}')
