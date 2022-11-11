# This class generates simulated sensor data for a barometer and accelerometer
import numpy.random as np
import matplotlib.pyplot as plt

g = 9.81
mbarToMetersMultiplier = 8.32265 # 1mbar = 8.32265 meters under 15 C (standard conditions)
z = 1.96

def getBaroData(current_alt):
    # MS5611 barometer --> datasheet: https://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Data+Sheet%7FMS5611-01BA03%7FB3%7Fpdf%7FEnglish%7FENG_DS_MS5611-01BA03_B3.pdf%7FCAT-BLPS0036
    # Accuracy: ±1.5 mbar ≈ ±12.48 m
    # Assume 95% of data falls between 2 standard deviations of mean
    # Use equation z = (x_bar - μ)/(σ - sqrt(n)) --> z is based on confidence level, x_bar is sample value, μ is mean of data, σ is standard deviation, n is number of samples
    # Based on 95% confidence level, z = 1.96
    # Solve equation for σ

    return current_alt + np.normal(scale=((mbarToMetersMultiplier*1.5)/z))

def getAccXData(current_acc_x):
    #LSM9DS1 IMU --> datasheet: https://www.st.com/resource/en/datasheet/lsm9ds1.pdf
    # Accuracy: ± 90 mg ≈ .090g ≈ 0.8829 m/s^2
    # Assume 95% of data falls between 2 standard deviations of mean
    # Use equation z = (x_bar - μ)/(σ - sqrt(n)) --> z is based on confidence level, x_bar is sample value, μ is mean of data, σ is standard deviation, n is number of samples
    # Based on 95% confidence level, z = 1.96

    return current_acc_x + np.normal(scale=((0.090*g)/z))







# # Plotting the histogram for baro distribution
# data = np.normal(0, 1.5, 250)  
# plt.hist(list, bins=30, density=True, alpha=0.6, color='b')
# plt.show()