
import matplotlib.pyplot as plt
import json

f = open("./lib/JSON/orbital_data.json")
orbitalJSON = json.load(f)

print(orbitalJSON[0]["OBJECT_NAME"])

# for i in orbitalJSON[0]:
#     print(i)
 
# Closing file
f.close()
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()