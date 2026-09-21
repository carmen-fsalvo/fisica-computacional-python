#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: carmen
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del problema
g = 9.8  # aceleración gravitacional
l = 9.8  # longitud del péndulo
q = 0.5  # coeficiente de amortiguamiento
Omega_D = 2/3  # frecuencia de la fuerza externa
dt = 0.01  # paso de tiempo
T_drive = 2 * np.pi / Omega_D  # período de la fuerza externa
t_max = 500 * T_drive  # tiempo de simulación

# Condiciones iniciales
theta0 = 0.20
omega0 = 0.0

# Valores de F_D a evaluar
F_D_values = [1.4, 1.44, 1.465]

# Método de Euler mejorado
def euler_pendulo(F_D):
    t_values = np.arange(0, t_max, dt)
    theta = np.zeros(len(t_values))
    omega = np.zeros(len(t_values))
    
    theta[0] = theta0
    omega[0] = omega0
    
    for i in range(1, len(t_values)):
        domega_dt = - (g / l) * np.sin(theta[i-1]) - q * omega[i-1] + F_D * np.sin(Omega_D * t_values[i-1])
        omega[i] = omega[i-1] + domega_dt * dt
        theta[i] = theta[i-1] + omega[i] * dt
        
        # Mantener theta en el rango [-pi, pi]
        if theta[i] > np.pi:
            theta[i] -= 2 * np.pi
        elif theta[i] < -np.pi:
            theta[i] += 2 * np.pi
    
    return t_values, theta, omega

# Gráficos de la sección de Poincaré
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharex=True, sharey=True)

for i, F_D in enumerate(F_D_values):
    t, theta, omega = euler_pendulo(F_D)
    
    # Sección de Poincaré: tomamos los valores en cada ciclo de impulsión
    indices = np.where(np.abs((t % T_drive) - 0) < dt)[0]
    theta_poincare = theta[indices]
    omega_poincare = omega[indices]
    
    # Eliminamos el transitorio
    transitorio = int(len(indices) * 0.1)  # Eliminamos el 10% inicial
    theta_poincare = theta_poincare[transitorio:]
    omega_poincare = omega_poincare[transitorio:]
    
    # Graficamos
    axes[i].scatter(theta_poincare, omega_poincare, s=5, color='black')
    axes[i].set_title(f'F_D = {F_D}')
    axes[i].set_xlabel(r'$\theta$')
    axes[i].set_ylabel(r'$\omega$')
    axes[i].grid(True)

plt.tight_layout()
plt.show()
