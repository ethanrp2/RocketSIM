## This class contains methods for adding control to SIM_main
## Examples of control include aerodynamic drag systems, roll control, etc.
import atmosphere as atmosphere
import constants as constants

#Predicted State Variables:
alt_pred = 0
vel_pred = 0
acc_pred = 0

#PID Variables:
Kp = 1
Ki = 0
Kd = 0



def active_aero_drag(z, velocity, current_flap_ext):
    
    flap_ext_percentage = active_drag_PID(z, velocity, current_flap_ext)
    A_flaps = flap_ext_percentage * constants.flap_width * constants.flap_length_max
    return 0.5*atmosphere.density(z)*(velocity**2)*constants.C_d_flaps*(A_flaps), flap_ext_percentage

def active_drag_PID(alt_current, vel_current, u):
    #returns percentage of total flap extension
    error = constants.DESIRED_APOGEE - predicted_apogee(alt_current, vel_current, u)

    return Kp*(error/constants.DESIRED_APOGEE)*100

def updateStatePredicted(time_step = 10e-3):
    global alt_pred, vel_pred, acc_pred
    alt_pred = alt_pred + vel_pred*time_step + 0.5*acc_pred*time_step**2
    vel_pred = vel_pred + acc_pred*time_step

def predicted_apogee(alt_current, vel_current, flap_ext):
    global alt_pred, vel_pred, acc_pred
    
    alt_pred = alt_current
    vel_pred = vel_current
    while (vel_pred > 0):
        net_acceleration = -(constants.g + ((atmosphere.aero_drag(alt_pred, vel_pred) + active_aero_drag(alt_pred, vel_pred, flap_ext))/(constants.rocket_mass)))
        acc_pred = net_acceleration
        updateStatePredicted()

    return alt_pred