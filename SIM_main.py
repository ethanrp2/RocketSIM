# This class creates a basic simulation of a rocket through its 5 stages with a constant time step then graphs it
import matplotlib.pyplot as plt
import plotSIM as plotSIM
import constants as constants


#CLASS VARIABLES

dt = 10e-3
current_time = 0

motor_thrust = 90 #  (N)
rocket_weight = constants.rocket_mass * constants.g # (N)

altitude = 0
velocity = 0
acceleration = 0

apogee = 0

# LAUNCH VARIABLES
boost_time = 0
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

def thrust():
    #TODO: upload thrust csv file
    return 1

def updateState(): 
    #TODO: Use State Space Form

    global acceleration, velocity, altitude, current_time, sim_dict

    sim_dict["altitude"].append(altitude)
    sim_dict["velocity"].append(velocity)
    sim_dict["acceleration"].append(acceleration)
    sim_dict["time"].append(current_time)
    # print(velocity)
    altitude = altitude + velocity*dt + 0.5*acceleration*dt**2
    velocity = velocity + acceleration*dt
    current_time += dt

def launch_SIM(boost_phase_time, ejection_delay_time):
    global boost_time, ejection_delay
    boost_time = boost_phase_time
    ejection_delay = ejection_delay_time

    print("launch")
    boost()

def boost():
    print ("boost")
    global acceleration
    net_acceleration = motor_thrust - rocket_weight
    acceleration = net_acceleration
    while (current_time < boost_time):
        updateState()
    coast()
    
def coast():
    print("coast")
    global acceleration, apogee
    acceleration = -9.8
    while (velocity > 0):
        updateState()
    apogee = altitude

    ejection()

def ejection():
    print("ejection")
    global acceleration, current_time
    
    delay_initial_time = current_time
    while (current_time <= delay_initial_time + ejection_delay):
        updateState()
    acceleration = 0
    recovery()

def recovery():
    print("recovery")
    global velocity, altitude
    while (velocity < 0 and altitude > 0):
        updateState()
    ground_hit()

def ground_hit():
    print("ground hit")
    print("SIM ended")

launch_SIM(3, 5)
plotSIM.plotter(sim_dict, apogee)
