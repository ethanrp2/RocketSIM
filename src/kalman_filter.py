import numpy as np
from filterpy.common import Q_continuous_white_noise


########### INITIAL STATE ###########
# alt_init = 0
# vel_init = 0
# accel_init = 0

########### INPUT DATA ###########
# alt_input = 0
# accel_input = 0


# TIME VARIABLES
current_time = 0
dt = 0.01 #(ms)

# PRIORI VARIABLES
x_priori = np.zeros([3,1])
P_priori = np.zeros([3,3]) #start at 0s, it will tune itself

# UPDATE VARIABLES
x_k = np.zeros([3,1])
A = np.zeros([3,3])
P = np.zeros([3,3])
R = np.zeros([2,2])
Q = np.zeros([3,3])
K = np.zeros([3,2])
z = np.zeros([2,1])
H = np.zeros([2,3])
R = np.zeros([2,2])

kalman_dict = {
    "altitude":[],
    "velocity":[],
    "acceleration":[],
}

def initialize (alt_init, vel_init, accel_init, time_step=10e-3) :
    global x_k, A, Q, R, dt, H, dt

    dt = time_step

    x_k = np.array([[alt_init],
                    [vel_init],
                    [accel_init]])

    A = np.array([[1, dt, 0.5*(dt**2)],
                  [0, 1, dt],
                  [0, 0, 1]])

    H = np.array([[1.0,0.0,0.0],
                  [0.0,0.0,1.0]])     
    
    Q = Q_continuous_white_noise(dim=3, dt=dt, spectral_density=13.)

    # Q = Q_continuous_white_noise(dim=3, dt=time_step, spectral_density=0.002)

    # Original Values
    # R = np.array ([[1., 0],
    #                [0, 0.1]])

    R = np.array ([[2., 0],
                   [0, 0.1]])


def priori(time_step) :
    global x_priori, P_priori, kalman_dict, dt
    dt = time_step

    A = np.array([[1, dt, 0.5*(dt**2)],
                  [0, 1, dt],
                  [0, 0, 1]])
    Q = Q_continuous_white_noise(dim=3, dt=dt, spectral_density=13.)

    # KF Equations 1, 2
    x_priori = A @ x_k
    P_priori = (A @ P @ A.T) + Q

def update(alt_input, accel_input) :
    global z, K, x_k, P, current_time, H

    #Load Sensor Data
    z = np.array([[alt_input],
                  [accel_input]])

    # KF Equations 3, 4, 5 
    K = (P_priori @ H.T) @ np.linalg.inv(H @ P_priori @ H.T + R) 

    x_k = x_priori + K @ (z - (H @ x_priori))
    P = (np.eye(len(K)) - (K @ H)) @ P_priori
    # current_time += dt

    # kalman_dict["altitude"].append(x_k[0,0])
    # kalman_dict["velocity"].append(x_k[1,0])
    # kalman_dict["acceleration"].append(x_k[2,0])    
    
def getState():
    # print("alt: " + str(x_k[0,0]) + "vel" + str(x_k[1,0]))
    x_k_return = [x_k[0,0], x_k[1,0], x_k[2,0]]
    return x_k_return



