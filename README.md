# RocketSIM
- Simulation of rocket from launch to apogee
- Plots Altitude, Velocity, Acceleration
- Accounts for Aerodynamic Drag
- Constantly calculates and predicts apogee based on current flap configuration
- Active Drag Control System with P controller for rocket to reach desired apogee (5200 m)
 
## Future Additions to SIM
 - Simulated Sensor Data from accelerometer/barometer
 - Kalman Filter for simulated noisy sensor data
 - State Space matricies format


 ### Credits
 - AeroTech Thrust Data Table csv for M2500T
 - ISSUIUC/TARS-CONTROLS --> code framework for 1dof_sim_RK4.py and related classes (https://github.com/ISSUIUC/TARS-Controls)
