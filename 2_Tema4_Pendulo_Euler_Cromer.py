# -*- coding: utf-8 -*-

"""
Created on Sat Feb 15 14:49:59 2025

@author: physicist
"""

"""
Ejemplo de código para la implementación del método de Euler-Cromer en caso del péndulo.
"""

# Llamada a las librerías y funciones necesarias
from math import radians
from numpy import zeros
from pylab import plot, show, xlabel, ylabel, title

# Inicialización de variables
g = 9.8
l = 1
theta0 = radians(5) # Permite la entrada del ángulo inicial en grados
omega0 = 0.
t0 = 0.

timeTotal = 10 

dt = 0.04           # Intervalo de tiempos
NN = timeTotal / dt # Número de elementos de las colecciones
N = int(NN)         # Transformación de NN en un entero.

theta = zeros(N, float) # Declaración de las colecciones a utilizar: ángulo
omega = zeros(N, float) # Velocidad angular
t = zeros(N,float)      # Tiempo

# Valores iniciales de las colecciones
theta[0] = theta0
omega[0] = omega0
t[0] = t0

# Bucle que calcula los valores de las coordenadas "i+1" en función de las de "i".
for i in range(N-1):
    print(i, theta[i], omega[i])
    omega[i+1] = omega[i] - (g/l)*theta[i]*dt
    theta[i+1] = theta[i] + omega[i+1]*dt           #Método de Euler-Cromer
    t[i+1] = t[i] + dt

# Instrucciones para la realización de las gráficas.
plot(t,theta)
xlabel("t (s)"), ylabel(r'$\theta$ (rad)')
title("Péndulo Ideal - Método de Euler-Cromer")

show()