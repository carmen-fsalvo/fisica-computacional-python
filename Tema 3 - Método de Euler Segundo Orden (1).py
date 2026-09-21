# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 18:09:12 2025

@author: physicist
"""
# Codigo que ilustra el Metodo de Euler utilizando la caida
# libre de un cuerpo. Primero calcula el tiempo que se tarda en
# caer al suelo, para conocer el "tiempo caracteristico" del 
# problema. A partir de aqui, utiliza un intervalo temporal de
# aproximadamnete el 1% del tiempo caracteristico para implementar
# el Metodo de Euler. Al ser la aceleracion constante, el metodo
# de Euler proporciona un resultado exacto. 
# Se asume una masa de m = 1Kg

from math import sqrt
from numpy import empty
from pylab import plot, show, ylim, figure, xlabel, ylabel, legend, title


aceleracion_gravedad = 9.81
g = aceleracion_gravedad

h = float(input("Por favor, introduce la altura de la torre: "))

tf = sqrt(2*h/g)

print("El tiempo que se tarda en caer desde una altura de", h, \
      " metros, es ", tf, " segundos")
      
Delta_t = tf*(1/100) # 1% del tiempo caracteristico obtenido
dt = Delta_t 

# Ecuacion Diferencial del problema: d2y/dt2 = -g, la cual se 
# convierte en dos ecuaciones de primer orden: 
# dy/dt = v y dv/dt = -g. 
# O al integrar: yi+1 = yi + vi*dt y vi+1 = vi - g*dt

N = 100
t = empty(2*N) #Creamos las tablas para "t", "y" y "v"
y = empty(2*N)
v = empty(2*N)
Ep = empty(2*N) #Creamos las tablas para las energias
Ec = empty(2*N)
ETotal = empty(2*N)
t[0] = 0 # Asignamos los valores iniciales de cada variable
y[0] = h
v[0] = 0

print(t[0], y[0], v[0])

#Implementacion del Metodo de Euler
for i in range(N+1):
    t[i+1] = t[i] + dt 
    y[i+1] = y[i] + v[i]*dt # Evolucion de la posicion "y"
    v[i+1] = v[i] - g*dt    # Evolucion de la velocidad "v"
    Ep[i] = g*y[i]          # Evolucion de la E. Potencial
    Ec[i] = 0.5*v[i]*v[i]   # Evolucion de la E. Cinetica
    ETotal[i] = Ep[i] + Ec[i]
    print(t[i+1], y[i+1], v[i+1])

# Se extraen subtablas de las tablas para realizar las 
# gráficas sin aparente inconsistencias
figure(3)
l4, = plot(t[:101],ETotal[:101], label = "Energía Total")
legend(handles = [l4])
figure(2)
l2 = plot(t[:101],Ep[:101])
l3 = plot(t[:101],Ec[:101])
l4 = plot(t[:101],ETotal[:101])
legend((l2[0], l3[0], l4[0]), ("Energía Potencial", "Energía Cinética", "Energía Total"))
figure(1)
l1 = plot(t[:102],y[:102])
xlabel("Tiempo (s)"), ylabel("Altura (m)")
ylim(0)