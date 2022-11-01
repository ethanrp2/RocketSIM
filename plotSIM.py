from turtle import color
import numpy as np
import matplotlib.pyplot as plt


def plotter(sim_dict, apogee):

    plt.style.use('Solarize_Light2')



    fig,(alt_nc,vel_nc,accel_nc) = plt.subplots(3,1,figsize=(15,10), sharex=True)
    plt.title("SIM PLOT", color='#F5B14C', fontsize = 35, pad=400)

    # Altitude Measurements vs Real Altitude vs Kalman Filter Graph (No Control)
    alt_nc.plot(sim_dict["time"], sim_dict["altitude"], label="Altitude", color="tab:red", linewidth = 3)
    alt_nc.axhline(y = apogee, color = "tab:brown", linestyle = "dotted", linewidth = 2.5, label="Apogee")
    plt.legend(fontsize = 14) 
    plt.xlabel("Time (s)", fontsize = 14)
    # alt_nc.plot(sim_dict_nc["time_sim"], sim_dict_nc["x_noise"],label="Noisy Altitude Reading",color="lightsteelblue", linewidth = 3, linestyle=":")
    # alt_nc.plot(sim_dict_nc["time_sim"], sim_dict_nc["x"],label="Real Altitude",color="royalblue", linewidth = 3);  
    # alt_nc.plot(sim_dict_nc["time_sim"], sim_dict_nc["kalman_alt"],label="Altitude Estimation",linestyle="--",color="tab:red")
    alt_nc.set(ylabel = "Altitude (m)")
   # alt_nc.axvline(x = delay, color = "tab:green", linestyle = "dotted", linewidth = 2.5, label="Launch");plt.legend(fontsize = 14); plt.xlabel("Time (s)", fontsize = 14)
    alt_nc.legend()

    # Real Velocity vs Kalman Filter Graph (No Control)
    vel_nc.plot(sim_dict["time"], sim_dict["velocity"],label="Velocity",color="royalblue", linewidth = 3);  
    # vel_nc.plot(sim_dict_nc["time_sim"], sim_dict_nc["kalman_vel"],label="Velocity Estimation",linestyle="--",color="tab:red")
    vel_nc.set(ylabel = "Velocity (m/s)")
    #vel_nc.axvline(x = delay, color = "tab:green", linestyle = "dotted", linewidth = 2.5, label="Launch");plt.legend(fontsize = 14); plt.xlabel("Time (s)", fontsize = 14)
    vel_nc.legend()

    # Acceleration Measurements vs Real Acceleration vs Kalman Filter Graph (No Control)
    # accel_nc.plot(sim_dict_nc["time_sim"], sim_dict_nc["accel_noise"],label="Noisy Accelerometer Reading",color="lightsteelblue", linewidth = 3, linestyle=":");
    accel_nc.plot(sim_dict["time"], sim_dict["acceleration"],label="Acceleration",color="tab:green", linewidth = 3);  
    # accel_nc.plot(sim_dict_nc["time_sim"], sim_dict_nc["kalman_accel"],label="Acceleration Estimation",linestyle="--",color="tab:red")
    accel_nc.set(ylabel = "Acceleration (m/s^2)")
    #accel_nc.axvline(x = delay, color = "tab:green", linestyle = "dotted", linewidth = 2.5, label="Launch");plt.legend(fontsize = 14); plt.xlabel("Time (s)", fontsize = 14)
    accel_nc.legend()

    # flap_nc.plot(sim_dict_nc["time_sim"], sim_dict_nc["flap_extension"],label="Flap Extension (Control)",color="royalblue", linewidth = 3); 
    # flap_nc.set(ylabel = "Flap Extension Length (m)")
    # #flap_nc.axvline(x = delay, color = "tab:green", linestyle = "dotted", linewidth = 2.5, label="Launch");plt.legend(fontsize = 14); plt.xlabel("Time (s)", fontsize = 14)
    # flap_nc.legend()

    plt.show()
