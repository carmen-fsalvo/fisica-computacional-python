# -*- coding: utf-8 -*-
"""
Created on Sun Feb 09 13:01:29 2025

@author: physicist
"""
# Código que calcula la trayectoria de proyectiles con distinta 
# celeridad y ángulo inicial, teniendo en cuenta la resistencia del aire.

from math import cos, sin, sqrt
from numpy import arange, radians, degrees
from pylab import plot, xlabel, ylabel, show

# Se declaran e inicializan las variables.
t0 = 0
x0 = 0
y0 = 0
v0 = 700 
g = 9.8
B2m = 4e-5      # Cociente entre la constante de proporcionalidad de la fuerza de arrastre y la masa.

theta_degree = arange(10, 80, 5)    # Tabla con los valores de ángulos a explorar.
theta = radians(theta_degree)
deltat = 0.1
alcance = []                        # Declaración de la lista para el alcance.

for j in range(len(theta)):         # Bucle sobre todos los ángulos
    t, x, y, vx, vy, v = [], [], [], [], [], [] # Se vuelven a declarar las listas para cada ángulo
    t.append(t0)
    x.append(x0), y.append(y0)      # Se añaden los valores iniciales.
    vx.append(v0 * cos(theta[j]))
    vy.append(v0 * sin(theta[j]))
    v.append(v0)
    i = 0                           # Para cada ángulo se incializa el índice de tiempos.
    while y[i] >= 0:
        t.append(t[i]+deltat)       # Se añaden los valores a cada lista a medida que se añade deltat
        x.append(x[i] + vx[i]*deltat)
        y.append(y[i] + vy[i]*deltat)
        vx.append(vx[i] - B2m*v[i]*vx[i]*deltat)
        vy.append(vy[i] - g*deltat - B2m*v[i]*vy[i]*deltat)
        v.append(sqrt(vx[i]**2 + vy[i]**2))
        i += 1
    alcance.append(x[-2] + (x[-1] - x[-2])/2)   # Se define como alcance la media entre lso dos últimos 
    plot(x, y)                                  # Gráfica de la trayectoria para el ángulo "j"
    print(degrees(theta[j]), alcance[j])        # Imprime el ángulo y su alcance.
    j += 1

alcance_maximo = alcance[0]         # Define el alcance máximo y el índice
i_max = 0

for i in range((len(alcance))):     # Explora todos los elementos de alcance y define como máximo
    if(alcance[i] > alcance_maximo):    # al mayor, después de ir comparando.
          alcance_maximo = alcance[i]
          i_max = i
          
xlabel("Alcance (Kms)")             # Nombre a los ejes
ylabel("Altura (Kms)")
show()                              # Muestra la gráfica. Opcional.
# Imprime el alcance que ha obtenido como máximo entre todos los ángulos.
print(f"El alcance máximo es de {alcance_maximo} y se alcanza a los {theta_degree[i_max]} grados")