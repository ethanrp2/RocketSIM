## This class contains methods for adding control to SIM_main
## Examples of control include aerodynamic drag systems, roll control, etc.
import atmosphere as atmosphere
import constants as constants

#Predicted State Variables:
alt_pred = 0
vel_pred = 0
acc_pred = 0

#PID Variables:
Kp = 0.1
Ki = 0
Kd = 0



def active_aero_drag(z, velocity, flap_ext):
    A_flaps = flap_ext * constants.flap_width * constants.flap_length_max
    # return 0.5*atmosphere.density(z)*(velocity**2)*constants.C_d_flaps*(A_flaps), flap_ext_percentage
    return 0.5*atmosphere.density(z)*(velocity**2)*constants.C_d_flaps*(A_flaps)

def active_drag_PID(predicted_apogee):
    #returns percentage of total flap extension
    error = predicted_apogee - constants.DESIRED_APOGEE
    control_out = Kp * error
    if (control_out > 1):
        control_out = 1
    elif (control_out < 0):
        control_out = 0
    print("Flap ext: " + str(control_out))
    return control_out
    # return 0.2

# def updateStatePredicted(time_step = 10e-3):
#     global alt_pred, vel_pred, acc_pred
#     alt_pred = alt_pred + vel_pred*time_step + 0.5*acc_pred*time_step**2
#     vel_pred = vel_pred + acc_pred*time_step

# def predicted_apogee(alt_current, vel_current, flap_ext):
#     global alt_pred, vel_pred, acc_pred
    
#     alt_pred = alt_current
#     vel_pred = vel_current
#     while (vel_pred > 0):
#         net_acceleration = -(constants.g + ((atmosphere.aero_drag(alt_pred, vel_pred) + active_aero_drag(alt_pred, vel_pred, flap_ext))/(constants.rocket_mass)))
#         acc_pred = net_acceleration
#         updateStatePredicted()

#     return alt_pred