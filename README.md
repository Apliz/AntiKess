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

Reference https://www.omnicalculator.com/physics/hohmann-transfer?calculatorResult=H4sIAAAAAAAAA%2B1a2W7bRhT9lYBPSeuysy8BWsCN0cIPaYOmzUsRBIw0kdlQS7kYMQJ%2FTf%2BkX9YzFClSXBSqVtQ%2BVA%2B2Zjv3zr137mZ%2FDNxqEa%2FcyzzKXfD0YzCLklmRYDB%2FFaVx9DZx2Y%2FR0mXB09%2BCTRovo%2FTueZRlwUUwd1ker6I8Xq9%2BjuZx4efiVZzHUbIbR6sFwNLn66Vb5cUSM9nGzeJ38exyf%2BV6fOkKS7cuWc%2Fi%2FO6qodmavd5SxUyeRqvsnUtfVSsvMHflkls6sHZZrbHt7zf5OvdMuGX8PPp9nV5%2BiP0Nfvnpe%2Fx0sxl4SWN%2FLnh9EcxucLMhEdVAfs96NY89p5mXa7zaFHnnS8n1ZZLHeTF3IQmeduceffvNI7Iv6t12iu0D8%2FWRWpjXy02RZC5k2N6Ze%2FRtubOi6bX683r23uUhbzhpZqvdLRsIBfa1xtWORRrdxnnJVJS8iFKIJndpKLF5eGkfeWs7oWqwtzPlrvuLYF3k4wL8CC3Hi4VL49WiVo7XTZf2M2glj1Ze4bdRUmA9Twt3PyrpB%2BMOqOPBmIOKezBqR8EPxhs3h1Ox2ljMAxHvgVnE7UfatrdyGY%2F61qUZUL5fp0u4qfJx16%2Fe%2B8%2Fdhut6C6g%2FpoSQLx6nDv7HrWbulaf65EnQBvypyNsHvvZHnnzxuH%2FovvZpZyXHzkfO%2B9xxYlwdTcwfGSPWDVEHblky7YHK39vPP7h29alxBhCGHdH5FNAP7WcjPewuPkH%2FgaoY46UTYM4nhJ5nP0D6GKqHiJ1b0Utc7kW63rgk8Z74M16wnbaOk5FWM0YGPkfeeRRnTBB7Uex88t9PdM9HdizJ%2F4%2F43dH65D%2FGX5VIfs5341OkRZTOf%2FicRPpV2dlMsV8sno30UD17duJ12XwmwqDscOjZgQbDSPC%2F%2BL%2FzsOs8uA9Au4ryqCxTssv5bQQhz4On7yK4A8ghe75%2BGyduN1FkdfpUAOfu2donMsGvL70Wi9Sr6A7jH7570Zp4ebd8u4ZhBH%2F9idnEyzJauOqoW31VngYwnBBqrSj5FWLIKopez4lPWj6l310R9tonA6siSq591VXGouGN5S3g93KP6kfLKL%2F5HQeC7%2BLFj8XybWkrVUUXqFBpwYOqpquG5FM55mR4bg2qilBwKYneUenNDkT36Tfg2jT8V4PBpHQyJLUmpEbsUFvj0YpjMrgWELJphLEb39ca7ptEE2RG9dIV4sVoMd%2BVzfClXlcc90v36conMpTQiFKGaGIVt8IKIpiRVGJolWRKWKmp9TuQEeIHpcwqw7WwtpH%2FKYBazYDpdiBFyCkjhihNjdYaiEoTaa3kRFAOIkZqzZWQPp3VRDOhJLdECLBLbGNAJwBqtReOuAANmaQgRrlkoGEhQM6VkYoRKaUWRFtq%2FDu00lgCDkHREkiYGuxqXeDhQLuGxWT2mWE05NJAQiAEvRtjtCHcCM0k48oyzgiUbssxFoShEC1jnHBNhGn8wkmQBpsgky8jGaOwASYVDQ2FNYMOsyCjQE9aWIc2ioGuoVZbzgVl3i4YxMhg1rTxGCdBGnFktUvyHuniSLdWe7GRxsh0KLC65yGb8V6gPw6VhEQQKJZqQizhUlC4DgITNspCTFQwbwGGUtg15TAD4%2BVoiYQwsVu3A9iJsP6tAN4KwtsYjHT0OG13D98Px9w6evrgeRR%2BdaYF223zNFCrIkm2t%2Fffhns108UptWqH%2FtZ4qBdzgIteQ2W6pwgRwuBrOWzJIBJwRRTRFG4IUQ5RDf5WCEGoggqs96%2BCUwnnBruDSgRzX7LmAqcC66Vou3zraOOpD90PN1im4xjpTTBswtTezOEmynRtcGYJ3pQwPISnJUILTQzHw1ZGKG%2BoiIACUhMMIlM%2BmkPEUsAjIyoiijSqOAXS4dbL9FtR0ONcWyZDY5E%2FceazKMuRkFCJLAq%2FkVBRrPtgIxgCihCwIIocRkiimludAmmwYXPgce11XUo2bEiMUvI4S6wP3Y%2F3WKZHLc5MKDRSU6RI8I%2F%2BJREkSXhaDHbJECIsAgboKS4UsYwZa5UwxMdxqJs28e4USCN9m%2BnXsdyGmllkS2AA6gJ9xjXl4ApGbIWfo8LngxTWiSAH5WukfPiFEKRb1zkF0mgv6IgERYMNjpishbHMp9i0TMgJNQjNGm8QaavVBI9PwKSZsEgXEd7ABmdIb1oV2wmQBvtL0y%2BjjQxhA54%2BFRYGATeCSKx9GQRCxNdKeHz4rsAVBE7xBIlE5k7xUay5zMOR%2FOtJ3WwdJ7t%2FkImKfJ1Ft%2Fj%2BW%2FlPHgiZm8zNr%2BfZdubGJZtf3Icyiu4FyqofM5a7VMudYFR3dboJSDXfE3U1P5gCd87s2Vu1VpWSrRFrj7aVcjUui57q%2B8CTHFm53K20HN22cVT3jQ52ijKXuFnu5mXL6WVSLLKeoHdD36yK0vwmO5wzNrvfL%2FlgQtDeMdKDGdkyjnEo2jV7sz%2FeL99sXPomc%2F7%2FiUaeVxt7kx2ogbpMDNYzEzm9msxpx7P1ue2lSl0Wdi2O%2Ftld82Bwqe7t9Bermr1ZuEmzkVL44CUHo1Gf3GAMHpBEP1toUXez0b8Ot6AWvT%2FeNIsgw4Yz%2Fn0AfP4G7arEshsoAAA%3D