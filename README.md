# Ideas concerning interesting use of TLE data for project
  
## Estimating low &Delta V missions for space debris recovery

### Tech Stack (So far)

1. Using MatplotLib and TLE data from Celestrack.  
2. **I did the integration in flask instead**
Order all objects by height and use distribution to find the highest concentration of bodies.  

### Outstanding Questions

- Does the closeness of two objects at their closest point in orbit determine the ease of orbital transfer?

### Potential Issues

Multiple 'bundles' will need to be evaluated. \{ They are only valuable when the bodies are at their closest possible point in their path. _explore_ this \}
  
Ensuring that no local minimums are declared as global minimum (when optimising for closeness or some other trait).

#### Asterisks

1. If not the closest point (as per open question No1, then another seperation)

### Next steps

- The most basic integration in Flask is complete
- Next steps is to complete the ajax query in celestrack.js
- Then create the javascript class in python
- Then port the transfer logic across
- Represent the data with matplotlib
