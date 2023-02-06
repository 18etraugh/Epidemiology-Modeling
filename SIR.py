import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# gets ode's 
def ode(stateValues, t, b, y):
    S, I, R = stateValues
    dSdt = -b * S * I / N #susceptible differntial equation
    dIdt = b * S * I / N - y * I #infected differential
    dRdt = y * I #recovered diffential
    return [dSdt, dIdt, dRdt]

# Define the parameters
b = 0.1  # infection rate
y = 0.05  # recovery rate

# Define the initial conditions
N = 1  # total population
I0 = .05  # initial infected fraction
R0 = 0  # initial recovered fraction
S0 = .95  # initial susceptible fraction
inital = [S0, I0, R0]

# amount of iterations
max_time = 200
t = range (0, max_time)

# Solve the ODEs using odeint
sol = odeint(ode, inital, t, args=(b, y))
S, I, R = sol.T

# Plot the solution
plt.plot(t, S, 'b', label='Susceptible')
plt.plot(t, I, 'r', label='Infected')
plt.plot(t, R, 'g', label='Recovered')
plt.legend()
plt.xlabel('Time (days)')
plt.ylabel('Population')
plt.show()