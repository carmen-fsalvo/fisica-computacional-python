# -*- coding: utf-8 -*-
"""
Created on Mon Mar  24 10:30:33 2025

@author: physicist
"""
# LLamada de librerías
from numpy import ones, zeros
from random import random

J = 1                               # Constante de intercambio


N = 25                              # Número de espines en cada dirección. Número alto ya que no se establecen condiciones períodicas.
espin = zeros([N, N], int)          # Matriz de N x N espines inicializados a cero    

for i in range(N):                  # Bucle para establecer aleatoriamente el espín_{ij} como +1 ó -1
    for j in range(N):              # pero que es irrelevante, pues se inicializan los espines a 1.
        if random() < 0.5:
            espin[i, j] = +1
        else:
            espin[i, j] = 1

espin = ones([N, N], int)           # Inicializar a +1 los espines para comprobar que se obtiene una energía de -2 por espín.
print(espin)                        # Imprime la matriz resultante
energia = 0                         # Inicializa la energía
energia1 = 0

# Bucle sobre todos los espines para calcular la energía, según:
# E = - Sumatorio(S_{ij}*S_{kl}) donde S_{kl} son los espines contiguos al S_{ij}
for i in range(1, N-1):             
    for j in range(1, N-1):
        energia += (espin[i, j] * espin[i, j-1] + espin[i, j] * espin[i, j+1] \
                  +  espin[i, j] * espin[i-1, j] + espin[i, j] * espin[i+1, j]) # Se multiplica aquí por 1/2

energia = - J * 0.5 * energia / (N*N)       # Se multiplica al final e implica menos operaciones
            
print("Energia = ", energia)                # Imprime la energía de la configuración

# ATENCIÓN: El código sólo calcula la energía debida a los espines internos.