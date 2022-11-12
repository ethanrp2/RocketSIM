import os
import src.kalman_filter as kalman_filter
import pandas as pandas
import matplotlib.pyplot as plt

time_step = 0
df_highG_data = 0
noisy_barometer = 0


# def readData () :
#     global time_step, df_highG_data, noisy_barometer
#     # df = pandas.read_csv("flight-data/20220623/flight_computer.csv" , 
#     #     usecols= ['lowG_data.timestamp', 'highG_data.ax', 'barometer_data.altitude', 'has_lowG_data', 'has_highG_data', 'has_barometer_data'])
    
#     df = pandas.read_csv("flight-data/20220623/flight_computer_trimmed.csv" , 
#         usecols= ['timestamp_ms', 'highg_az', 'barometer_altitude', 'state_est_x'])

    
#     # Remove a bunch of data from the time the rocket was sitting on the launch pad
#     # df.drop(labels=range(160, 194), inplace=True)
    
#     # remove any data that doesn't have useful information (i.e., a row of all 0s)

#     # indices_to_drop = df[(df['has_barometer_data'] == 0) & (df['has_highG_data'] == 0) & (df['has_lowG_data'] == 0) | (df['lowG_data.timestamp'] == 0) | (df['barometer_data.altitude'] == 0)].index
#     # df.drop(indices_to_drop, inplace=True)

    
#     # Print the first 5 elements to make sure everything looks correct
#     # print(df.head())

    
#     # print("Altimeter at " + str(measurementDataDict["lowG_data.timestamp"][0]) + " is " + str(measurementDataDict["barometer_data.altitude"][0]) + "m")
#     # print("Altimeter at " + str(measurementDataDict["lowG_data.timestamp"][223583]) + " is " + str(measurementDataDict["barometer_data.altitude"][223583]) + "m")

#     return df.to_dict()


def implementKF (sim_dict_noisy):

    barometer_data = sim_dict_noisy["altitude"]
    accel = sim_dict_noisy["acceleration"]
    time = sim_dict_noisy["time"]

    kalman_filter.initialize(barometer_data[0], 0 , accel[0])
    for x in range(len(barometer_data)):
        kalman_filter.priori(time[x])
        # print("Altimeter at " + str(measuredDict["timestamp"][x]) + "ms is " + str(measuredDict["barometer_altitude"][x]) + "ft")
        kalman_filter.update(barometer_data[x], accel[x])



def plotGraph (sim_dict_noisy):
    global time_step, df_highG_data, noisy_barometer
    
    time_step = sim_dict_noisy['time']
    noisy_barometer = sim_dict_noisy['altitude']
    plt.plot(time_step, noisy_barometer, label = "noisy barometer data")
    plt.plot(time_step, kalman_filter.kalman_dict["altitude"], label = "state estimate")

    # time_step = list(sim_dict_noisy['timestamp_ms'])
    # noisy_barometer = list(sim_dict_noisy['barometer_altitude'])
    # plt.plot(time_step, noisy_barometer, label = "noisy barometer data")
    # plt.plot(time_step, kalman_filter.kalman_dict["altitude"], label = "state estimate")

    plt.title('State estimate vs Measurement')
    plt.xlabel('timestamp (ms)')
    plt.ylabel('altitude (m)')
    plt.legend()
    plt.show()




##### CALLING THE METHODS ##########

# implementKF(data)
# plotGraph(data)

