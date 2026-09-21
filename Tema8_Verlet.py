# -*- coding: utf-8 -*-
"""
Created on Mon May 12 13:09:27 2025

@author: physicist

Dinámica molecular con Verlet y potencial de Lennard-Jones.
En cada paso solo se muestra la posición actual de las partículas (sin traza).

"""

from numpy import zeros
from math import sqrt
from random import random
import matplotlib.pyplot as plt

# Parámetros del sistema
L = 20             # Tamaño de la caja (no periódica)
N = 4              # Número de partículas
pasos = 1000       # Número de pasos de simulación
dt = 0.01          # Paso de integración
v0 = 2.0           # Velocidad inicial máxima

# Inicialización de arrays de posición y velocidad
x = zeros((2, N))  # x[0]: posición en t-dt, x[1]: posición en t
y = zeros((2, N))
vx = zeros(N)
vy = zeros(N)

# Colocamos 4 partículas en una red cristalina simple
x[1, 0], y[1, 0] = 5, 5
x[1, 1], y[1, 1] = 5, 7
x[1, 2], y[1, 2] = 7, 5
x[1, 3], y[1, 3] = 7, 7

# Asignamos velocidades iniciales y calculamos posición anterior (t - dt)
for i in range(N):
    vx[i] = 2 * v0 * (random() - 0.5)
    vy[i] = 2 * v0 * (random() - 0.5)
    x[0, i] = x[1, i] - vx[i] * dt
    y[0, i] = y[1, i] - vy[i] * dt

# Preparar figura
plt.ion()
fig, ax = plt.subplots()
ax.set_xlim(0, L)
ax.set_ylim(0, L)

# Bucle de integración con Verlet
for t in range(pasos):
    x_new = zeros(N)
    y_new = zeros(N)

    # Calculamos nuevas posiciones
    for i in range(N):
        fx = fy = 0.0
        for j in range(N):
            if i != j:
                dx = x[1, j] - x[1, i]
                dy = y[1, j] - y[1, i]
                r = sqrt(dx**2 + dy**2) + 1e-8  # evitar división por cero
                if r < 3.0:
                    # Fuerza de Lennard-Jones
                    f = 24 * (2 / r**13 - 1 / r**7)
                    fx += f * dx / r
                    fy += f * dy / r

        # Verlet posicional
        x_new[i] = 2 * x[1, i] - x[0, i] + fx * dt**2
        y_new[i] = 2 * y[1, i] - y[0, i] + fy * dt**2
        # Actualización de velocidad opcional
        vx[i] = (x_new[i] - x[0, i]) / (2 * dt)
        vy[i] = (y_new[i] - y[0, i]) / (2 * dt)

    # Actualizamos arrays de posición
    x[0, :] = x[1, :]
    y[0, :] = y[1, :]
    x[1, :] = x_new
    y[1, :] = y_new

    # Representación de las posiciones
    ax.cla()
    ax.scatter(x[1, :], y[1, :], color='blue')
    ax.set_xlim(0, L)
    ax.set_ylim(0, L)
    ax.set_title(f"t = {t*dt:.2f} s")
    plt.pause(0.001)

# Desactivar modo interactivo y mostrar la última figura
plt.ioff()
plt.show()
