
import math
# import matplotlib.pyplot as plt
# import json
from fractions import Fraction
import constants
import databases.db as database

class Transfer():

  # def __init__(self):


  def calculate(self):
    Transfer.semi_major_axis()
    return 0 


  # Compares the radii ratio to the constant ratios and calls the correct transfer type function
  # for the greatest efficiency
  def most_efficient(self):
    match Transfer.calculate_radii_ratio():
      case [r] if r < constants.RATIO_HOHMANN:
        # r1,r2 have no definition

        # Transfer.hohmann(constants.R_EARTH, constants.G_EARTH,r1,r2)

        # stub return
        return 0
      case [r] if r < constants.RATIO_BIELLIPTIC and r >= constants.RATIO_HOHMANN:
        # stub return
        return 0
      case [r] if r >= constants.RATIO_BIELLIPTIC:
        # stub return
        return 0
        
  @staticmethod
  def calculate_radii_ratio(r1:int, r2:int) -> int:
    # final orbit radii / initial orbit radii (r2/r1)
    # r1,r2 have no definition ye
    radii_ratio = r2/r1
    return radii_ratio

  # deltaV calculation for a Hohmann transfer between 2 perfectly circular orbits
  # Still need to add in considerations for eccentricity
  @staticmethod
  def hohmann(R, g,r1,r2) :

    # Get the semi major axis (USE FUCNTION - DEFUNCT FOR NOW)
    # semi_major_axis = (r1+r2)/2

    #Calculate transfer velocity needed at apogee and perigee (m/s)
    vTransfer_perigee = math.sqrt(constants.GR2*((2.0/r1)-(2.0/(r1+r2))))
    vTransfer_apogee = math.sqrt(constants.GR2*((2.0/r2)-(2.0/(r1+r2))))

    #Calculate velocities of circular orbits (Start, target) (m/s)
    vCircular_1 = math.sqrt(constants.GR2/r1)
    vCircular_2 = math.sqrt(constants.GR2/r2)

    # Total needed burns at perigee and apogee to complete insertion into new orbit
    perigee_burn = vTransfer_perigee-vCircular_1
    apogee_burn = vCircular_2-vTransfer_apogee

    #Total deltaV
    total_deltaV = perigee_burn + apogee_burn

    return total_deltaV
  # Goes through all bodies and calculates the semi-major axis (Assuming perfectly round orbits.)
  @staticmethod
  def semi_major_axis():
    bodies = []
    db = database.get_db()

    mean_motion_list = db.execute("""SELECT mean_motion FROM orbitalBodies""")

    #go through all orbital bodies

    # UPDATE TO USE SQLITE3 DATABASE
    for i in mean_motion_list:
      #convert mean motion (n) to usable radians/second
      radians_per_second = i * ((2*math.pi)/86400)

      # calculate semi-major axis of body
      sma = constants.GM_EARTH**Fraction(1,3) / radians_per_second**Fraction(2,3)

      #format
      print(f'{math.floor(sma/10**3)}Km')

      return math.floor(sma)


# deltaV calculation for a Hohmann transfer between 2 perfectly circular orbits
transfer = Transfer()
transfer.calculate()  