import matplotlib.pyplot as plt
import numpy as np

deltaT = 0.5  #change this value to adjust the smoothness
m = 68.1
c = 12.5
g = 9.81
v0 = 0
v_0 = 0

numerical_velocity = []
analytical_velocity = []
error_list = []

x = np.arange(0 ,100 , deltaT)

#numerical equation calculation
for i in range(len(x)):

    v = (g - (c/m)*v0)*(deltaT)+v0  
    numerical_velocity.append(v)

    v0 = v

#analytical equation calculation
for i in range(len(x)):

    v = ((m*g)/c) - (m/c)*(g - ((c*v_0)/m))*np.exp(-c*deltaT/m)  
    analytical_velocity.append(v)

    v_0 = v

#error calculation
for i in range(len(numerical_velocity)):

    error = analytical_velocity[i] - numerical_velocity[i]

    error_list.append(error)

#graph plotting
plt.plot(x, numerical_velocity)
plt.plot(x, analytical_velocity)
plt.plot(x, error_list)

#plt.legend("Numerical","Analytical")
plt.xlabel("Time")
plt.ylabel("Velocity")
plt.show()
