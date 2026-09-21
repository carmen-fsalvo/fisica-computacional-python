# -*- coding: utf-8 -*-
"""
Created on Mon Mar  24 10:17:11 2025

@author: physicist
"""
# LLamada de librerías
from numpy import zeros
from pylab import imshow, colorbar, gray
from random import random

N = 20                                  # Número de espines en cada dirección
espin = zeros([N, N], int)              # Matriz de N x N espines inicializados a cero 

for i in range(N):                      # Bucle para establecer aleatoriamente el espín_{ij} como +1 ó -1
    for j in range(N):
        if random() < 0.5:
            espin[i, j] = +1
        else:
            espin[i, j] = -1
        
print(espin)                            # Imprime la matriz resultante

imshow(espin), colorbar(), gray()       # Representación de los espines