import src.constants as constants
import math as math
## Atmospheric Constants
T_0 = 288.15 # (Kelvin) --> equivalent of 15 degrees C; temp at standard level at sea
B = 0.0098 # (degrees Kelvin/meter) --> Temoperature Lapse Rate
R = 287.053 # (K*(J/Kg))
rho_0 = 1.225 # (kg/m^3) --> Pressure under standard conditions (Pa)
C_d = 0.35

A = math.pi * constants.rocket_radius**2

def density (z):
    # https://www.homerenergy.com/products/pro/docs/latest/altitude.html

    rho_f = rho_0 * ((1-((B*z)/(T_0)))**(constants.g/(R*B)))*(T_0/(T_0-(B*z)))
    return rho_f

def aero_drag (x_state):
    z = x_state[0]
    vel = x_state[1]
    return 0.5*density(z)*(vel**2)*C_d*(A)
