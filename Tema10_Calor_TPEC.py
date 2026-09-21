# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 19:41:12 2025

@author: physicist
"""
from numpy import empty
from pylab import legend, plot,xlabel,ylabel,show

# Constants
L = 0.01                # Espesor del recipiente en metros
D = 4.25e-6             # Difusividad térmica del acero
N = 100                 # Número de divisiones en la malla del espesor
a = L/N                 # Espaciado de la malla
h = 5e-4                # paso temporal
epsilon = h/1000        # Valor para comparar dos números reales

Tlo = 0.0               # Temperatura del baño frío (Celsius)
Tmid = 20.0             # Temperatura del recipiente
Thi = 50.0              # Temperatura del contenido caliente

t1 = 0.01               # Instantes de tiempo escogidos para la representación (en segundos)
t2 = 0.1
t3 = 0.4
t4 = 1.0
t5 = 10.0
tend = t5 + epsilon     # Instante de tiempo para finalizar los cálculos

# Declaración e inicialización de colecciones
T = empty(N+1,float)    # Temperaturas
T[0] = Thi              # Temperatura caliente como primer elemento de T
T[N] = Tlo              # Temperatura fría como último elemento de T
T[1:N] = Tmid           # Temperaturas de todos los elementos del recipeinte en t = 0
Tp = empty(N+1,float)   # Colección para guardar los nuevos valores de T
Tp[0] = Thi             # Temperatura caliente como primer elemento de Tp
Tp[N] = Tlo             # Temperatura fría como último elemento de T

# Bucle principal
t = 0.0                 # Instante inicial
c = h*D/(a*a)           # Variable que contiene los pasos espaciales, temporales y D

while t<tend:
    # Calcular los nuevos valores de T
    for i in range(1,N):
        Tp[i] = T[i] + c*(T[i+1]+T[i-1]-2*T[i])
    T,Tp = Tp,T
    t += h

    # realizar las gráficas en los instantes elegidos, comparando con el instante "t"
    if abs(t-t1)<epsilon:
        g1 = plot(T)
    if abs(t-t2)<epsilon:
        g2 = plot(T)
    if abs(t-t3)<epsilon:
        g3 = plot(T)
    if abs(t-t4)<epsilon:
        g4 = plot(T)
    if abs(t-t5)<epsilon:
        g5 = plot(T)

legend((g1[0], g2[0], g3[0], g4[0], g5[0]),
(f't = {t1} s', f't = {t2} s', f't = {t3} s', f't = {t4} s', f't = {t5} s'), shadow = True)
xlabel("x")
ylabel("T")
show()