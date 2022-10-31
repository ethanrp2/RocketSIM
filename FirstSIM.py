# This class creates a basic simulation of a rocket through its 5 stages with a constant time step then graphs it

#Define Variables
from time import time


dt = 10e-3
current_time = 0

motor_thrust = 90 #  (N)
rocket_mass = 0.76 # (Kg)
rocket_weight = rocket_mass * 9.8 # (N)

altitude = 0
velocity = 0
acceleration = 0

dict_counter = 0

# State Space Matricies
# --> x = Ax + Bu
x = [[altitude],
     [velocity],
     [acceleration]]

A = [[1, dt, 0.5*(dt**2)],
     [0, 1, dt],
     [0, 0, 0]
]



# Simulation State Dictionary
sim_dict = { 
    "altitude": [],
    "velocity": [],
    "acceleration": [],
    "time": []
}


def updateState(): 
    
    altitude = sim_dict["altitude"][dict_counter] + sim_dict["velocity"][dict_counter]*dt + 0.5*sim_dict["acceleration"][dict_counter]*dt**2

    
def launch():
    return 1

def boost():
    net_acceleration = motor_thrust - rocket_weight
    print(rocket_weight)
    #Rocket Burn lasts 10 seconds
    return 1

def coast():
    return 1

def ejection():
    return 1

def recovery():
    # parachute deployed with set delay ejection charge after apogee
    return 1

def ground_hit():
    return 1

# boost()





# print(time_step)
