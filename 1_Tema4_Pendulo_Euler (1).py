# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:29:47 2025

@author: physicist
"""

from numpy import zeros
from pylab import figure, legend, plot, title, xlabel, ylabel


g = 9.8
l = 1
m = 1
theta0 = 0.2
omega0 = 0.
t0 = 0.
phi = 0.2
timeTotal = 10

dt = 0.1
NN = timeTotal / dt
N = int(NN)

theta = zeros(N, float)
omega = zeros(N, float)
t = zeros(N, float)
theta[0] = theta0
omega[0] = omega0
t[0] = t0

for i in range(N-1):
    omega[i+1] = omega[i] - (g/l)*theta[i]*dt
    theta[i+1] = theta[i] + omega[i]*dt # Reemplazar por omega[i+1] para Euler-Cromer
    t[i+1] = t[i] + dt

figure(1)
l0 = plot(t, theta)
xlabel("t (s)"), ylabel(r'$\theta$ (rad)')
title("Péndulo Ideal - Método de Euler")


#%%
K = zeros(N, float)
U = zeros(N, float)
E = zeros(N, float)

K[0] = 0.5*m*l*omega[0]
U[0] = 0.5*m*g*l*theta[0]**2
E[0] = K[0] + U[0]

for i in range(N-1):
    omega[i+1] = omega[i] - (g/l)*theta[i]*dt
    theta[i+1] = theta[i] + omega[i]*dt
    K[i+1] = K[i] + 0.5*m*l**2 *omega[i]**2*dt**2
    U[i+1] = U[i] + 0.5*m*g*l*theta[i]**2*dt**2
    E[i+1] = K[i+1] + U[i+1]
    t[i+1] = t[i] + dt
    
figure(2)
k1 = plot(t, K)
u1 = plot(t, U)
e1 = plot(t, E)
xlabel("t (s)"), ylabel("Energía (J)")
legend((k1[0], u1[0], e1[0]), ("Energía Cinética", "Energía Potencial", "Energía Total"))
title("Evolución de las energías con t")