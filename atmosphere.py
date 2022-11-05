
## Atmospheric Constants
Temp_standard_conditions = 15
T_varying_factor = 6.5/1000 # degrees C/meter
R = 287.053

def density (current_altitude):

    Temp_altitude = Temp_standard_conditions - (T_varying_factor*current_altitude)

    return pressure(current_altitude)/(Temp_altitude*R)

def pressure(altitude):
    '''
    Determine site pressure from altitude.

    Parameters
    ----------
    altitude : numeric
        Altitude above sea level. [m]

    Returns
    -------
    pressure : numeric
        Atmospheric pressure. [Pa]

    Notes
    ------
    The following assumptions are made

    ============================   ================
    Parameter                      Value
    ============================   ================
    Base pressure                  101325 Pa
    Temperature at zero altitude   288.15 K
    Gravitational acceleration     9.80665 m/s^2
    Lapse rate                     -6.5E-3 K/m
    Gas constant for air           287.053 J/(kg K)
    Relative Humidity              0%
    ============================   ================
    '''

    press = 100 * ((44331.514 - altitude) / 11880.516) ** (1 / 0.1902632)

    return press