# Prácticas 10 y 11. Problema 2.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.sparse import diags
from scipy.sparse.linalg import splu

# --- Constantes físicas ---
hbar = 1.055e-34      # Constante de Planck reducida (J·s)
M = 9.109e-31         # Masa del electrón (kg)

# --- Parámetros del sistema ---
L = 1.0e-8            # Longitud de la caja 1D (m)

# --- Discretización espacial y temporal ---
N = 1000                     # Número de puntos en la malla (sin contar los bordes)
dx = L / (N + 1)             # Distancia entre los puntos de la malla. Paso espacial (m)
x = np.linspace(0, L, N + 2) # Posición de los puntos de la malla (N + bordes) (m)
dt = 1e-18                   # Paso temporal (s)
steps = 10000                # Número de pasos de tiempo

# --- Parámetros del paquete de ondas (gaussiano) ---
x0 = L / 2            # Centro (m)
sigma = 1e-10         # Ancho (desviación típica) (m)
kappa = 5e10          # Número de onda (1/m)

# --- Estado inicial ---
psi0 = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.exp(1j * kappa * x)
psi0[0] = psi0[-1] = 0       # Condiciones de frontera
psi = psi0[1:-1].copy()      # Eliminamos bordes para cálculo

# --- Matriz laplaciana ---
alpha = hbar**2 / (2 * M * dx**2)
main_diag = -2 * np.ones(N)
off_diag = np.ones(N - 1)
laplacian = diags([off_diag, main_diag, off_diag], [-1, 0, 1], format='csc')

# --- Matrices de Crank-Nicolson ---
I = diags([1.0] * N, 0, format='csc')
A = I + 1j * dt * alpha / hbar * laplacian / 2
B = I - 1j * dt * alpha / hbar * laplacian / 2

# --- Pre-factorización LU ---
A_lu = splu(A)

# --- Visualización (3 componentes) ---
fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
line_real, = axs[0].plot(x, np.real(psi0), 'b', label='Parte real')
line_imag, = axs[1].plot(x, np.imag(psi0), 'r', label='Parte imaginaria')
line_prob, = axs[2].plot(x, np.abs(psi0)**2, 'g', label='Densidad de probabilidad')

axs[0].set_ylabel("Re[ψ(x,t)]", fontsize=12, fontweight='bold')
axs[1].set_ylabel("Im[ψ(x,t)]", fontsize=12, fontweight='bold')
axs[2].set_ylabel("|ψ(x,t)|²", fontsize=12, fontweight='bold')
axs[2].set_xlabel("x (m)", fontsize=12, fontweight='bold')

for ax in axs:
    ax.set_ylim(-1, 1)
    # ax.grid(True)
    ax.legend()
axs[2].set_ylim(0, 1)

plt.suptitle("Evolución temporal de la función de onda en una caja cuántica", fontsize=14, fontweight='bold')

line_real.set_xdata(x[1:-1])
line_imag.set_xdata(x[1:-1])
line_prob.set_xdata(x[1:-1])

# --- Función de actualización para animación ---
def update(frame):
    global psi
    rhs = B @ psi
    psi = A_lu.solve(rhs)
    line_real.set_ydata(np.real(psi))
    line_imag.set_ydata(np.imag(psi))
    line_prob.set_ydata(np.abs(psi)**2)
    return line_real, line_imag, line_prob

ani = animation.FuncAnimation(fig, update, frames=steps, interval=1, blit=True)

# Guardar como Gif
guardar_gif = False
if guardar_gif:
    print("Guardando animación como 'schrodinger_anim.gif'...")
    ani.save("schrodinger_anim.gif", writer='pillow', fps=30)
    print("Gif guardado.")

# Guardar como MP4
guardar = True
if guardar:
    print("Guardando animación como 'schrodinger_anim.mp4'...")
    ani.save("schrodinger_anim.mp4", fps=30, writer='ffmpeg')
    print("Video guardado.")

# Mostrar animación en pantalla
plt.tight_layout()
plt.show()
