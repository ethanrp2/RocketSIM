## This class contains methods for adding control to SIM_main
## Examples of control include aerodynamic drag systems, roll control, etc.
import atmosphere as atmosphere
import constants as constants

#Predicted State Variables:
alt_pred = 0
vel_pred = 0
acc_pred = 0

def active_aero_drag(z, velocity, flap_extention_percentage):
    A_flaps = flap_extention_percentage * constants.flap_width * constants.flap_length_max
    return 0.5*atmosphere.density(z)*(velocity**2)*constants.C_d_flaps*(A_flaps)

##### WORK ON THIS ########
#TODO: Fix PID Method

def active_drag_PID(alt_current, vel_current):
    error = constants.DESIRED_APOGEE - predicted_apogee(alt_current, vel_current)
    kp = 0
    ki = 0
    kd = 0

    return 1

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

# print(predicted_apogee(3000, 250, 15))