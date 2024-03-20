# Pathfinder

Need to find a way to create an Orbit() object for the transfer orbit. 
It would get rid of the duplicate semi-major-axis function and make the calculation pattern for the velocities more uniform.


from chatGPT

Define the problem: Clearly specify the variables associated with each node and the objective function you want to minimize.

Design a custom algorithm: Given that this problem doesn't fit directly into existing shortest path algorithms, you may need to devise your own algorithm. This could involve a combination of graph traversal techniques and optimization methods.

Consider the trade-offs: Since you're optimizing two variables simultaneously (shortest path length and the variable associated with each node), you'll likely encounter trade-offs. You may need to define a weighted objective function that balances between minimizing the two variables.

Implement and test: Once you have a clear algorithmic approach, implement it in your preferred programming language and test it with different inputs to ensure it behaves as expected.

### Things to do
4. Eventually refactor it into a client GUI
5. Write tests!

### Bugs
1. Th eccentricity currently returns a negative value if the new the tranfer apoapsis is smaller than the transfer periapsis. The value for e is correct but if It's made positive then the total deltaV is incorrect, otherwise, it's correect
  1. I think this had something to do with how I'm calculating the transfer orbit. At the moment, the trnasfer orbit labels for apogee and perigee don't matter because they are coupled to the departure and arrival orbit velocities at the same points. 
  So when I am making the eccentricity positive the orbit is transformed as the equations need a definitive reference for apogee and perigee; my variables expect apogee > perigee, but my transfer orbit does not provide that absolute reference
Potential fix:
Calculate the transfer orbit apogee and perigee independently:
```python
def apsis(r1,r2):
  ap = r1
  pe = r2
  if r2 > r1
    ap = r2
    pe = r1
  return ap,pe

ap, pe = apsis()
```
Then I think the deltaV will be incorrect, but this will be resolved in how the individual deltaV values are added and subtracted in `Transfer.hohmann_transfer()` with Transfer.py
mainly I think it will be about the section of code:
```python
# Transfer.py class Transfer()
vt1 = self.transfer_orbit.velocity_at_position("apogee")
vt2 = self.transfer_orbit.velocity_at_position("perigee")

# negative values = velocity decreasing (altitude decreasing)
# positive values = velocity increasing (altitude increasing)
delta_v1 = vt1 - v1
delta_v2 = vt2 - v2

total_delta_v = abs(delta_v1) + abs(delta_v2)
```