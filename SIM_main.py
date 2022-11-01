# This class creates a basic simulation of a rocket through its 5 stages with a constant time step then graphs it

#Define Variables
import matplotlib.pyplot as plt
import plotSIM as plotSIM
dt = 10e-3
current_time = 0

motor_thrust = 90 #  (N)
rocket_mass = 0.76 # (Kg)
rocket_weight = rocket_mass * 9.8 # (N)

altitude = 0
velocity = 0
acceleration = 0

apogee = 0

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

    
def launch_SIM():
    print("launch")
    boost(2)

def boost(boost_time):
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

    ejection(5)

def ejection(delay_time):
    print("ejection")
    global acceleration, current_time
    
    delay_initial_time = current_time
    while (current_time <= delay_initial_time + delay_time):
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

def plot_SIM (measuredDict):
    
    # convert the dict to a list of the values in each column so the data can be plotted
    # timestamp = measuredDict['time'].values()
    # altitude = measuredDict['altitude'].values()
    # df_flight_state_est = measuredDict['state_est_x'].values()
    plt.plot(measuredDict['time'], measuredDict['altitude'], label = "altitude plot")
    # plt.plot(timestamp, kalman_filter.kalman_dict["altitude"], label = "state estimate")
    # plt.plot(df_lowG_timestamp, df_flight_state_est, label = "flight state estimate")


    plt.title('SIM Plot')
    plt.xlabel('timestamp (s)')
    plt.ylabel('altitude (m)')
    plt.legend()
    plt.show()

# print("hello")
launch_SIM()
# print(sim_dict["velocity"])
plotSIM.plotter(sim_dict, apogee)
# plot_SIM(sim_dict)