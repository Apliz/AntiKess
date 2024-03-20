from Orbit import Orbit
from Transfer import Transfer

i = Orbit(16.31106792, 0.0013117, 180.954, 198.184, 88.284, 6567.704)
f = Orbit(14.45833459, 0.0010391, 731.896, 746.687, 99.597, 7117.427)
transfer = Transfer(i,f)
print(transfer.hohmann_transfer())