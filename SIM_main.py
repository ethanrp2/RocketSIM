# This class creates a basic simulation of a rocket through its 5 stages with a constant time step then graphs it
import matplotlib.pyplot as plt
import plotSIM as plotSIM
import constants as constants
import pandas as pandas
import atmosphere as atmosphere
import math

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
    # print(velocity)
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
    drag = 0

    print(boost_time)
    for x in thrust_data["Time (s)"]:
        drag = atmosphere.density(altitude)*constants.rocket_Cd*((velocity**2)/2)*(constants.rocket_radius**2)*math.pi
        net_acceleration = (thrust_data["Thrust (N)"][x])/(rocket_mass) - constants.g - drag
        acceleration = net_acceleration

        if(x!=0):
            thrust_time_delta = thrust_data["Time (s)"][x] - thrust_data["Time (s)"][x-1]
        updateState(thrust_time_delta)

    coast()

def coast():
    print("coast")
    global acceleration, apogee
    # acceleration = -9.8
    while (velocity > 0):
        drag = atmosphere.density(altitude)*constants.rocket_Cd*((velocity**2)/2)*(constants.rocket_radius**2)*math.pi
        net_acceleration = -(constants.g + drag)
        acceleration = net_acceleration
        updateState()
    apogee = altitude

    print("apogee reached: " + str(apogee))
    # ejection()

# def ejection():
#     print("ejection")
#     global acceleration, current_time
    
#     delay_initial_time = current_time
#     while (current_time <= delay_initial_time + ejection_delay):
#         updateState()
#     acceleration = 0
#     recovery()

# def recovery():
#     print("recovery")
#     global velocity, altitude
#     while (velocity < 0 and altitude > 0):
#         updateState()
#     ground_hit()

# def ground_hit():
#     print("ground hit")
#     print("SIM ended")

# boost()

############ RUN SIM ##############
launch_SIM(5)
plotSIM.plotter(sim_dict, apogee)
