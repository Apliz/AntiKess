# Ideas concerning interesting use of TLE data for project
  
## Estimating low &Delta V missions for space debris recovery

### Tech Stack (So far)

1. Using MatplotLib and TLE data from Celestrack.  
2. **I'm going to use the Django Python framework for the this project. By updating this I am commiting to the pain of MVC and integration hell. It's gonna be one hell of a ride through the souk.**
Order all objects by height and use distribution to find the highest concentration of bodies.  

### Outstanding Questions

- Does the closeness of two objects at their closest point in orbit determine the ease of orbital transfer?

### Potential Issues

Multiple 'bundles' will need to be evaluated. \{ They are only valuable when the bodies are at their closest possible point in their path. _explore_ this \}
  
Ensuring that no local minimums are declared as global minimum (when optimising for closeness or some other trait).

#### Asterisks

1. If not the closest point (as per open question No1, then another seperation)
