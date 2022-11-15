# This class creates a basic simulation of a rocket through its 5 stages with a constant time step then graphs it
import plotSIM as plotSIM
import src.constants as constants
import pandas as pandas
import src.atmosphere as atmosphere
import src.controls as controls
import time
import src.sensors as sensors
import src.kalman_filter as kalman

#CLASS VARIABLES
current_time = 0
kalman_apogee = 0
predicted_alt = constants.DESIRED_APOGEE
coast_start_time = 0
sim_runtime = 0
#State Array: altitude [0], velocity [1], acceleration [2]
x_state = [0, 0, 0]
x_state_kalman = [0, 0, 0]

# Noisy sensor readings: barometer [0], accelerometer [1]
sensors_noisy = [0, 0]

# Simulation State Dictionary
sim_dict = { 
    "altitude": [],
    "velocity": [],
    "acceleration": [],
    "time": []
}

sim_dict_kalman = { 
    "altitude": [],
    "velocity": [],
    "acceleration": [],
    "time": []
}

sim_dict_noisy = { 
    "altitude": [],
    "acceleration": [],
    "time": []
}

sim_error = {
    "error": [],
    "time": []
}

def updateState(time_step=10e-3): 
    global x_state, current_time, sim_dict, x_state_kalman, sim_dict_noisy, sim_error

    sim_error["error"].append(predicted_alt-constants.DESIRED_APOGEE)
    sim_error["time"].append(current_time)

    sim_dict["altitude"].append(x_state[0])
    sim_dict["velocity"].append(x_state[1])
    sim_dict["acceleration"].append(x_state[2])
    sim_dict["time"].append(current_time)

    kalman.priori(time_step)

    # Get noisy sensor values
    sensors_noisy = [sensors.getBaroData(x_state[0]), sensors.getAccXData(x_state[2])]
    sim_dict_noisy["altitude"].append(sensors_noisy[0])
    sim_dict_noisy["acceleration"].append(sensors_noisy[1])
    sim_dict_noisy["time"].append(current_time)

    kalman.update(sensors_noisy[0], sensors_noisy[1])
    x_state_kalman = kalman.getState()
    
    sim_dict_kalman["altitude"].append(x_state_kalman[0])
    sim_dict_kalman["velocity"].append(x_state_kalman[1])
    sim_dict_kalman["acceleration"].append(x_state_kalman[2])
    sim_dict_kalman["time"].append(current_time)


    x_state[0] = x_state[0] + x_state[1]*time_step + 0.5*x_state[2]*time_step**2
    x_state[1] = x_state[1] + x_state[2]*time_step
    current_time += time_step

def launch_SIM():
    print("launch")
    wait()

def wait():
    kalman.initialize(sensors.getBaroData(x_state[0]), 0, sensors.getAccXData(x_state[2]))
    for x in range(int(constants.sim_start_delay/constants.dt)):
        updateState()
    
    boost()

def boost():
    print ("boost")
    global boost_time, x_state, x_state_kalman, coast_start_time

    thrust_data = pandas.read_csv("csv_data/AeroTech_M2500T_Trimmed.csv").to_dict()
    
    boost_time = thrust_data["Time (s)"][len(thrust_data["Time (s)"])-1]
    thrust_time_delta = thrust_data["Time (s)"][0]

    for x in thrust_data["Time (s)"]:
        
        x_state[2] = (thrust_data["Thrust (N)"][x])/(constants.rocket_mass) - constants.g - (atmosphere.aero_drag(x_state_kalman))/(constants.rocket_mass)
        if(x!=0):
            thrust_time_delta = thrust_data["Time (s)"][x] - thrust_data["Time (s)"][x-1]
        updateState(thrust_time_delta)
    
    coast_start_time = current_time
    coast()

def coast():
    print("coast")
    global x_state, kalman_apogee, x_state_kalman, predicted_alt, coast_start_time, sim_runtime

    flap_extension = 0
    while (x_state_kalman[1] > 0):

        predicted_alt = controls.predict_alt(x_state_kalman, flap_extension)

        flap_extension = controls.active_drag_PID(predicted_alt)

        x_state[2] = -(constants.g + ((atmosphere.aero_drag(x_state_kalman) + controls.active_aero_drag(x_state_kalman, flap_extension))/(constants.rocket_mass)))
        updateState()
    kalman_apogee = x_state_kalman[0]
    sim_runtime = time.time() - start_time



def printSIMStatus():
    print("kalman apogee reached (m): " + str(kalman_apogee))
    print("time to apogee (s): " + str(current_time))
    print("sim runtime (s): " + str(sim_runtime))


############ RUN SIM ##############
start_time = time.time()
launch_SIM()
printSIMStatus()
plotSIM.plotter(sim_dict, sim_dict_noisy, sim_dict_kalman, sim_error, kalman_apogee, coast_start_time, sim_runtime)