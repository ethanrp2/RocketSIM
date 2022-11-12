## This class contains methods for adding control to SIM_main
## Examples of control include aerodynamic drag systems, roll control, etc.
import src.atmosphere as atmosphere
import src.constants as constants

#Predicted State Variables:
alt_pred = 0
vel_pred = 0
acc_pred = 0

#PID Variables:
Kp = 0.1
Ki = 0
Kd = 0



def active_aero_drag(x_state, flap_ext):
    z = x_state[0]
    vel = x_state[1]
    A_flaps = flap_ext * constants.flap_width * constants.flap_length_max
    return 0.5*atmosphere.density(z)*(vel**2)*constants.C_d_flaps*(A_flaps)

def active_drag_PID(predicted_apogee):
    #returns ratio (0<=x<=1) of total flap extension
    error = predicted_apogee - constants.DESIRED_APOGEE
    control_out = Kp * error
    if (control_out > 1):
        control_out = 1
    elif (control_out < 0):
        control_out = 0

    return control_out

def predict_alt(x_current, flap_ext_current, time_step=10e-3):    
    x_current = [x_current[0], x_current[1], 0]

    while (x_current[1] > 0):
        x_current[2] = -(constants.g + ((atmosphere.aero_drag(x_current) + active_aero_drag(x_current, flap_ext_current))/(constants.rocket_mass)))
        x_current[0] = x_current[0] + x_current[1]*time_step + 0.5*x_current[2]*time_step**2
        x_current[1] = x_current[1] + x_current[2]*time_step
    
    return x_current[0]