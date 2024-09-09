print("Simple ODE: free-fall motion with air resistance")

import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, y0, t0, tf, h):
    t = np.arange(t0, tf, h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i-1] + h * f(t[i-1], y[i-1])
    return t, y

# Define the ODE: Free-fall with air resistance
def free_fall(t, v):
    g = 9.81
    k = 0.1
    m = 70
    return g - (k/m) * v

# Initial conditions
v0 = 0
t0, tf, h = 0, 10, 0.01

# Solve using Euler's method
t_vals, v_vals = euler_method(free_fall, v0, t0, tf, h)

# Plot results
plt.plot(t_vals, v_vals, label="Euler's Method")
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.legend()
plt.show()
