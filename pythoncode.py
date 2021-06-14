from matplotlib import pyplot as plt
import numpy as np
import time

def phi(x):
    if x < 0:
        return 1.0
    return 0.0

def scheme1():
    u = np.zeros(len(x))
    u_old = np.zeros(len(x))
    for i in range(len(x)):
        u_old[i] = phi(x[i])
    plt.plot(x, u_old)
    f = True
    for k in range(len(t)):
        u[0] = phi(x[0])
        for i in range(1, len(x)):
            u[i] = u_old[i] * (1 - dt/dx) + u_old[i-1] * dt/dx
        u_old = u.copy()
        if k > 400 and f:
            f = False
            plt.plot(x, u)
            
def scheme2():
    u = np.zeros(len(x))
    u_old = np.zeros(len(x))
    for i in range(len(x)):
        u_old[i] = phi(x[i])
    
    f = True
    for k in range(len(t)):
        u[0] = phi(x[0])
        u[len(x)-1] = phi(x[len(x)-1])
        for i in range(1, len(x)-1):
            u[i] = -u_old[i+1] * dt/(2*dx) + u_old[i-1] * dt/(2*dx) + u_old[i]
        u_old = u.copy()
        if k > 400 and f:
            f = False
            plt.plot(x, u)
n = 32
x = np.linspace(-1.0, 1.0, n)
dx = x[1] - x[0]
m = 1000
t = np.linspace(0, 1.0, m)
dt = t[1] - t[0]
print(dx, dt)
scheme1()
scheme2()