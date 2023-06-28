import matplotlib.pyplot as plt
import numpy as np

deltaT = 0.1  #change this value to adjust the smoothness
m = 68.1
c = 12.5
g = 9.81
tx = 10
vx = 44.87
v0 = 0
v2=vx

numerical_velocity = [v2]
analytical_velocity = []
error_list = []

x = np.arange(0, 10+deltaT, deltaT)
y = np.arange(10, 0-deltaT, -deltaT)

#numerical equation calculation
for i in range(len(x)-1):

    v1 = (v2 - g*deltaT)/(1-c*deltaT/m)
    numerical_velocity.append(v1)
    v2 = v1

#analytical equation calculation
for i in range(len(x)):

    v = ((m*g)/c) - (m/c)*(g - ((c*vx)/m))*np.exp(-c*(x[i]-tx)/m)  
    analytical_velocity.append(v)

#graph plotting
plt.plot(y, numerical_velocity,"o-r",markersize=2)
plt.plot(x, analytical_velocity,"#000000")

plt.legend(["Numerical Solution","Analytical Solution"])
plt.title("Mathematical Model Representation of a free falling body")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)
plt.show()