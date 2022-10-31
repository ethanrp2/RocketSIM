# This class creates a basic simulation of a rocket through its 5 stages with a constant time step then graphs it

#Define Variables
time_step = 10e-3
current_time = 0

motor_thrust = 90 #  (N)
rocket_mass = 0.76 # (Kg)
rocket_weight = rocket_mass * 9.8 # (N)


sim_dict = { 
    "altitude": [],
    "velocity": [],
    "acceleration": [],
    "time": []
}

def updateState(): {
    
}

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

boost()






# print(time_step)
