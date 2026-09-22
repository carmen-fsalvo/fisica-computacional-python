# Prácticas 10 y 11. Problema 1.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parámetros físicos
L = 1.0     # Longitud de la cuerda (m)
v = 100.0   # Velocidad de propagación de la onda (m/s)
C = 1.0     # Constante del perfil de velocidad inicial de la onda (m/s)
sigma = 0.3 # Desviación estándar del perfil de velocidad inicial de la onda (gaussiano) (m)
d = 0.1     # Distancia desde uno de los extremos a la que se encuentra el punto de impacto (m)

# Parámetros numéricos
dx = 0.01   # Discretización del espacio (m). Paso espacial
dt = 1e-6   # Discretización del tiempo (s). Paso temporal
r = (v * dt / dx)**2 # Criterio de estabilidad de Von Neuman / Courant
assert r <= 1, "Violación de la condición de estabilidad de TPEC"

# Vector con la posición de los puntos en la malla que representa la cuerda (discretización espacial)
x = np.arange(0, L + dx, dx)
N = len(x)                   # Número de puntos en la malla

# Condiciones iniciales
u0 = np.zeros(N)             # Posición inicial de la cuerda horizontal (todos los puntos están en y=0)
psi = C * x * (L - x) / L**2 * np.exp(-((x - d)**2) / (2 * sigma**2))  # Perfil de velocidad inicial
u1 = np.zeros(N)                      # Primer paso temporal en la ecuación de onda: u(x, dt)
u1[1:-1] = u0[1:-1] + dt * psi[1:-1] + 0.5 * r * (u0[2:] - 2 * u0[1:-1] + u0[:-2])

# Número de cuadros para la animación
steps = 30000
reduction = 3 # Reducimos la cantidad de frames para optimizar

# Guardamos los estados en el tiempo
u_prev = u0.copy()
u_curr = u1.copy()
frames = [u_prev, u_curr]

# Precalcular las soluciones para la animación (Método TPEC: Tiempo Progresivo Espacio Centrado)
for j in range(steps):
    u_next = np.zeros(N)
    # Calculamos los siguientes valores de u usando la fórmula de diferencias finitas
    u_next[1:-1] = 2 * u_curr[1:-1] - u_prev[1:-1] + r * (u_curr[2:] - 2*u_curr[1:-1] + u_curr[0:-2])
    
    if j%reduction==0: 
        frames.append(u_next)  # Agregamos el siguiente estado a los frames
    
    u_prev, u_curr = u_curr, u_next  # Actualizamos los estados anteriores y actuales

# -- Visualización con matplotlib --

# Gráfico estático de la altura de la onda en distintos tiempos

# Tiempos seleccionados
selected_times = [0, (steps+1)//4, (steps+1)//2, 3*(steps+1)//4, steps]
num_plots = len(selected_times)

# Creamos los subplots con eje x compartido
fig, axes = plt.subplots(num_plots, 1, figsize=(8, 2.5*num_plots), sharex=True)

# Dibujamos cada línea
for ax, t in zip(axes, selected_times):
    ax.plot(x, frames[t//reduction])
    ax.set_ylim(-0.0005, 0.0005)
    ax.set_title(f"t = {t * dt:.2e} s", fontsize=11)
    ax.grid(True)
    ax.axhline(0, color='k', linestyle='--', linewidth=1)  # Línea de referencia en y=0

# Etiquetas comunes
axes[-1].set_xlim(0, 1)
axes[-1].set_xlabel("Posición x (m)", fontsize=12, fontweight='bold')
fig.supylabel("Desplazamiento u(x, t) (m)", fontsize=12, fontweight='bold')

# Título general
fig.suptitle("Altura de la onda a diferentes tiempos", fontsize=14, fontweight='bold')
fig.tight_layout(rect=[0, 0, 1, 0.95])  # Ajuste para espacio del título

plt.show()


# -- Gráfico del perfil inicial de la onda --

fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.plot(x, psi, label="Perfil de velocidad inicial (m/s)", color='purple')
ax2.plot(x, u0, label="Perfil de posición inicial (m)", color='green')
ax2.set_xlabel("Posición x (m)", fontsize=12, fontweight='bold')
ax2.set_ylabel("Valor", fontsize=12, fontweight='bold')
ax2.set_title("Perfil de velocidad inicial de la onda", fontsize=14, fontweight='bold')
ax2.legend(loc='best')
plt.show()

# -- Animación con Matplotlib --

# Configurar gráfico para la animación
fig, ax = plt.subplots(figsize=(8, 5))
line, = ax.plot(x, frames[0])  # Inicializamos el gráfico con el primer frame
ax.set_ylim(-0.0005, 0.0005)
ax.set_xlim(0, L)
ax.set_xlabel("Posición x (m)", fontsize=12, fontweight='bold')
ax.set_ylabel("Desplazamiento u(x, t) (m)", fontsize=12, fontweight='bold')
ax.set_title("Animación de la vibración de la cuerda tras el impacto", fontsize=14, fontweight='bold')

# Función de actualización para la animación de matplotlib
def update(frame):
    line.set_ydata(frames[frame])
    return line,

# Crear la animación con matplotlib
ani = animation.FuncAnimation(fig, update, frames=len(frames), interval= 1, blit=True)

# Guardar como Gif
guardar_gif = False
if guardar_gif:
    print("Guardando animación como 'vibracion_cuerda.gif'...")
    ani.save("vibracion_cuerda.gif", writer='pillow', fps=30)
    print("Gif guardado.")

# Guardar como MP4
guardar_video = False
if guardar_video:
    print("Guardando animación como 'vibracion_cuerda.mp4'...")
    ani.save("vibracion_cuerda.mp4", writer="ffmpeg", fps=30)
    print("Video guardado.")

# Mostrar la animación y hacer que se detenga cuando se cierra la ventana
plt.show(block=True)
