# This class creates a basic simulation of a rocket through its 5 stages with a constant time step then graphs it
import matplotlib.pyplot as plt
import plotSIM as plotSIM
import constants as constants
import pandas as pandas
import atmosphere as atmosphere
import math
import controls as controls
import time

#CLASS VARIABLES
current_time = 0
apogee = 0

#State Matricies: altitude [0], velocity [1], acceleration [2]
x_state = [0, 0, 0]

# Simulation State Dictionary
sim_dict = { 
    "altitude": [],
    "velocity": [],
    "acceleration": [],
    "time": []
}

def updateState(time_step=10e-3): 
    global x_state, current_time, sim_dict

    sim_dict["altitude"].append(x_state[0])
    sim_dict["velocity"].append(x_state[1])
    sim_dict["acceleration"].append(x_state[2])
    sim_dict["time"].append(current_time)

    x_state[0] = x_state[0] + x_state[1]*time_step + 0.5*x_state[2]*time_step**2
    x_state[1] = x_state[1] + x_state[2]*time_step
    current_time += time_step

def launch_SIM():
    print("launch")
    boost()

def boost():
    print ("boost")
    global boost_time, x_state

    thrust_data = pandas.read_csv("csv_data/AeroTech_M2500T_Trimmed.csv").to_dict()
    boost_time = thrust_data["Time (s)"][len(thrust_data["Time (s)"])-1]
    thrust_time_delta = thrust_data["Time (s)"][0]

    for x in thrust_data["Time (s)"]:
        
        x_state[2] = (thrust_data["Thrust (N)"][x])/(constants.rocket_mass) - constants.g - (atmosphere.aero_drag(x_state))/(constants.rocket_mass)
        if(x!=0):
            thrust_time_delta = thrust_data["Time (s)"][x] - thrust_data["Time (s)"][x-1]
        updateState(thrust_time_delta)
    coast()

def coast():
    print("coast")
    global x_state, apogee

    flap_extension = 0
    while (x_state[1] > 0):

        predicted_alt = controls.predict_alt(x_state, flap_extension)
        flap_extension = controls.active_drag_PID(predicted_alt)
        x_state[2] = -(constants.g + ((atmosphere.aero_drag(x_state) + controls.active_aero_drag(x_state, flap_extension))/(constants.rocket_mass)))
        updateState()

    apogee = x_state[0]


def printSIMStatus():
    print("apogee reached (m): " + str(apogee))
    print("time to apogee (s): " + str(current_time))
    print("sim runtime (s): " + str(time.time() - start_time))


############ RUN SIM ##############
start_time = time.time()
launch_SIM()
printSIMStatus()
plotSIM.plotter(sim_dict, apogee)