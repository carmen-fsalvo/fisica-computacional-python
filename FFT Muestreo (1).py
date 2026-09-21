# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:58:45 2025

@author: physicist
"""

from math import pi
from pylab import plot, show, xlabel, ylabel, figure, subplot, legend, title, tight_layout, empty
from numpy import arange, sin, zeros
from numpy.fft import rfft

# Constantes

N = 128                     # 2**7 = 128
dt = 0.1                    # intervalo de muestreo
T = (N-1)*dt/3              # período (ya que se han escogido 128 puntos y queremos tres períodos)
nu = 1/T                    # frecuencia

# Tabla de puntos

t = arange(0, 3*T, dt)      # Tabla de tiempos que cubre tres periodos
y = sin(2*pi*nu*t)          
c = rfft(y)
freq = zeros(len(c), float)
z = sin(2*pi*nu*t + pi/4)
cz = rfft(z)
tt = arange(0, 3.2*T, dt)
NN = len(tt)
yy = sin(2*pi*nu*tt)
cyy = rfft(yy)
freqyy = empty(len(cyy)-1, float)   # Ya que la FFT devueve una tabla con un elemento de más: 69
new_cyy = empty(len(cyy)-1, complex)
for n in range(len(freq)):
        freq[n] = n / (N * dt)  # Ya que f_n = n / (N * dt)

for n in range(len(freqyy)):
        freqyy[n] = n / (NN * dt)  # Ya que f_n = n / (N * dt)
        new_cyy[n] = cyy[n]


figure(4)
subplot(211)
pot = plot(freq, abs(c),"ro-")
ylabel(r'P($\nu$)')
legend((pot[0], ), (r't = 3 T',), shadow = True )
title("Potencia")
subplot(212)
pott = plot(freqyy, abs(new_cyy),"go-")
xlabel("Frecuencia (Hz)")
ylabel(r'P($\nu$)')
legend((pott[0], ), (r't = 3.2 T',), shadow = True )
tight_layout()
show()

figure(3)
subplot(211)
noentero = plot(tt,yy, "go-")
legend((noentero[0], ), (r't = 3.2 T',), shadow = True )
xlabel("Tiempo (s)")
ylabel("y(t)")
title("Número de Periodos No Entero")
subplot(212)
real = plot(freqyy, new_cyy.real+10,"ro-" )
imag = plot(freqyy, new_cyy.imag,"bo-" )
xlabel("Frecuencia (Hz)")
ylabel(r'Y($\nu$)')
legend((real[0], imag[0]), ("Re", "Im"), shadow = True )
tight_layout()
show()

figure(2)
subplot(211)
phi0 = plot(t,y, "go-")
phipi4 = plot(t,z, "yo-")
xlabel("Tiempo (s)")
ylabel("y(t)")
legend((phi0[0], phipi4[0]), (r'$\phi = 0$' , r'$\phi = \pi/4$'), shadow = True )
title("Presencia de Fase")
subplot(212)
real = plot(freq, cz.real+10,"ro-" )
imag = plot(freq, cz.imag-10,"bo-" )
xlabel("Frecuencia (Hz)")
ylabel(r'Y($\nu$)')
legend((real[0], imag[0]), ("Re", "Im"), shadow = True )
tight_layout()
show()

"""
figure(2)
subplot(211)
entero = plot(y, "go-")
xlabel(r'Índice de t (i)')
ylabel("y(t)")
legend((entero[0], ), (r't = 3 T',), shadow = True )
title("Número Entero de Periodos")
subplot(212)
real = plot(c.real+10,"ro-" )
imag = plot(c.imag,"bo-" )
xlabel(r'Índice de $\nu$ (i)')
ylabel(r'Y($\nu$)')
legend((real[0], imag[0]), ("Re", "Im"), shadow = True )
tight_layout()
show()
"""

figure(1)
subplot(211)
entero = plot(t,y, "go-")
xlabel("Tiempo (s)")
ylabel("y(t)")
legend((entero[0], ), (r't = 3 T',), shadow = True )
title("Número Entero de Periodos")
subplot(212)
real = plot(freq, c.real+10,"ro-" )
imag = plot(freq, c.imag,"bo-" )
xlabel("Frecuencia (Hz)")
ylabel(r'Y($\nu$)')
legend((real[0], imag[0]), ("Re", "Im"), shadow = True )
tight_layout()
show()



# Estudio del caso en que el rango de muestreo no coincide con múltiplos del período
