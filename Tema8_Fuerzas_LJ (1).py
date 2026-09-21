# -*- coding: utf-8 -*-
"""
Created on Thu May  8 12:28:01 2025

@author: physicist

Código que calcula la fuerza sobre una partícula debido a su interacción con las otras partículas
Se utiliza el potencial de Lennard-Jones y condiciones periódicas.
"""

from numpy import zeros, sqrt, sign
from pylab import quiver, scatter, xlim, ylim, title, figure, show

# Parámetros del sistema
L = 4                      # Tamaño de la caja
N = 4                      # Número de partículas
rcorte = 3.0               # Radio de corte para el potencial
pos = zeros([N, 2])        # Posiciones (x, y) de las partículas
fuerza = zeros([N, 2])     # Fuerzas netas sobre cada partícula

# Posiciones de prueba distribuidas en cuadrado
pos[0] = [1.0, 1.0]
pos[1] = [1.0, 3.0]
pos[2] = [3.0, 1.0]
pos[3] = [3.0, 3.0]

# Función que calcula distancia mínima entre partículas considerando condiciones periódicas
def distancia_periodica(r1, r2, L):
    dx = r2[0] - r1[0]
    dy = r2[1] - r1[1]
    if abs(dx) > L / 2:
        dx -= sign(dx) * L
    if abs(dy) > L / 2:
        dy -= sign(dy) * L
    r = sqrt(dx**2 + dy**2)
    return r, dx, dy

# Calcular la fuerza total sobre cada partícula
for i in range(N):
    for j in range(N):
        if i != j:
            r, dx, dy = distancia_periodica(pos[i], pos[j], L)
            if r < rcorte:
                # Fuerza derivada del potencial de Lennard-Jones
                f = 24 * (2 / r**13 - 1 / r**7)
                fx = f * dx / r
                fy = f * dy / r
                fuerza[i, 0] += fx
                fuerza[i, 1] += fy

# Visualización de las partículas y vectores de fuerza
figure()
scatter(pos[:, 0], pos[:, 1], color='blue')          # Partículas
quiver(pos[:, 0], pos[:, 1], fuerza[:, 0], fuerza[:, 1], color='red')  # Vectores de fuerza
xlim(0, L)
ylim(0, L)
title("Fuerzas sobre partículas por potencial de Lennard-Jones")
show()
