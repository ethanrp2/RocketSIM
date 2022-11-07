# This class creates a basic simulation of a rocket through its 5 stages with a constant time step then graphs it
import matplotlib.pyplot as plt
import plotSIM as plotSIM
import constants as constants
import pandas as pandas
import atmosphere as atmosphere
import math
import controls as controls
import sys

# sys.setrecursionlimit(50000)
#CLASS VARIABLES

dt = 10e-3
current_time = 0

motor_thrust = 90 #  (N)
rocket_mass = constants.rocket_mass
rocket_weight = constants.rocket_mass * constants.g # (N)

altitude = 0
velocity = 0
acceleration = 0

apogee = 0


# LAUNCH VARIABLES
ejection_delay = 0



# State Space Matricies
# --> x = Ax + Bu


# A = [[1, dt, 0.5*(dt**2)],
#      [0, 1, dt],
#      [0, 0, 0]
# ]


# Simulation State Dictionary
sim_dict = { 
    "altitude": [],
    "velocity": [],
    "acceleration": [],
    "time": []
}

def updateState(time_step=10e-3): 
    #TODO: Use State Space Form

    global acceleration, velocity, altitude, current_time, sim_dict

    sim_dict["altitude"].append(altitude)
    sim_dict["velocity"].append(velocity)
    sim_dict["acceleration"].append(acceleration)
    sim_dict["time"].append(current_time)
    altitude = altitude + velocity*time_step + 0.5*acceleration*time_step**2
    velocity = velocity + acceleration*time_step
    current_time += time_step

def launch_SIM(ejection_delay_time):
    global ejection_delay
    ejection_delay = ejection_delay_time

    print("launch")
    boost()

def boost():
    print ("boost")
    global boost_time, acceleration

    thrust_data = pandas.read_csv("csv_data/AeroTech_M2500T_Trimmed.csv").to_dict()
    boost_time = thrust_data["Time (s)"][len(thrust_data["Time (s)"])-1]
    thrust_time_delta = thrust_data["Time (s)"][0]

    for x in thrust_data["Time (s)"]:
        acceleration = (thrust_data["Thrust (N)"][x])/(rocket_mass) - constants.g - (atmosphere.aero_drag(altitude, velocity))/(rocket_mass)

        if(x!=0):
            thrust_time_delta = thrust_data["Time (s)"][x] - thrust_data["Time (s)"][x-1]
        updateState(thrust_time_delta)

    coast()

def coast():
    print("coast")
    global acceleration, apogee
    flap_extension = 0
    while (velocity > 0):
        predicted_alt = predict_alt(altitude, velocity, flap_extension)
        flap_extension = controls.active_drag_PID(predicted_alt)
        acceleration = -(constants.g + ((atmosphere.aero_drag(altitude, velocity) + controls.active_aero_drag(altitude, velocity, flap_extension))/(rocket_mass)))
        updateState()

    apogee = altitude

    print("apogee reached (m): " + str(apogee))
    print("time to apogee (s): " + str(current_time))

def predict_alt(alt_current, vel_current, flap_ext_current=0.2, time_step=10e-3):    
    
    while (vel_current > 0):
        net_acceleration = -(constants.g + ((atmosphere.aero_drag(alt_current, vel_current) + controls.active_aero_drag(alt_current, vel_current, flap_ext_current))/(constants.rocket_mass)))
        acc_pred = net_acceleration
        alt_current = alt_current + vel_current*time_step + 0.5*acc_pred*time_step**2
        vel_current = vel_current + acc_pred*time_step

    return alt_current


############ RUN SIM ##############
launch_SIM(5)
plotSIM.plotter(sim_dict, apogee)
