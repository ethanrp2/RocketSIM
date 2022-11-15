## This class contains methods for adding control to SIM_main
## Examples of control include aerodynamic drag systems, roll control, etc.
import src.atmosphere as atmosphere
import src.constants as constants

#Predicted State Variables:
alt_pred = 0
vel_pred = 0
acc_pred = 0

#PID Variables:
Kp = 0.0035
Ki = 0.000001
Kd = 0.0000001

error_sum = 0
error_derivative = 0


def active_aero_drag(x_state, flap_ext):
    z = x_state[0]
    vel = x_state[1]
    A_flaps = flap_ext * constants.flap_width * constants.flap_length_max
    return 0.5*atmosphere.density(z)*(vel**2)*constants.C_d_flaps*(A_flaps)

def active_drag_PID(predicted_apogee):
    global error_sum
    error = predicted_apogee - constants.DESIRED_APOGEE
    old_error = error_sum
    error_sum += error
    error_derivative = (error_sum-old_error)/constants.dt

    control_out = (Kp * error) + (Ki * error_sum) + (Kd * error_derivative)

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