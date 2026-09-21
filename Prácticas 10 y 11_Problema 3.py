# Prácticas 10 y 11. Problema 3.

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dst
from matplotlib.animation import FuncAnimation

# --- Constantes físicas ---
hbar = 1.055e-34      # Constante de Planck reducida (J·s)
M = 9.109e-31         # Masa del electrón (kg)

# --- Parámetros del sistema ---
L = 1.0e-8            # Longitud de la caja 1D (m)

# --- Discretización espacial y temporal ---
N = 1002                    # Número de puntos en la malla
x = np.linspace(0, L, N)    # Posiciones de los puntos en la malla (m)
dx = x[1] - x[0]            # Distancia entre los puntos de la malla. Paso espacial (m)
dt = 1e-18                  # Paso temporal (s)
steps = 10000               # Número de pasos de tiempo

x_internal = x[1:-1]  # Excluimos extremos de la caja donde la función de onda es 0 (condiciones de contorno)

# --- Parámetros del paquete de ondas (gaussiano) ---
x0 = L / 2            # Centro (m)
sigma = 1e-10         # Ancho (desviación típica) (m)
kappa = 5e10          # Número de onda (1/m)

# --- Estado inicial ψ(x, 0) ---
gaussian = np.exp(-((x_internal - x0)**2) / (2 * sigma**2))
oscillation = np.exp(1j * kappa * x_internal)
psi0_internal = gaussian * oscillation

# Normalización
norm = np.sqrt(np.sum(np.abs(psi0_internal)**2) * dx)
psi0_internal /= norm

# Verificar la norma de la función de onda
norm_check = np.sum(np.abs(psi0_internal)**2) * dx
print(f"Norma de la función de onda en t=0: {norm_check}")

# --- DST tipo I ortonormal (coeficientes espectrales) ---
# DST-I (Transformada Discreta del Seno) impone condiciones de frontera tipo seno (ψ=0 en los bordes)
alpha_k = dst(np.real(psi0_internal), type=1)/(N-1)
eta_k   = dst(np.imag(psi0_internal), type=1)/(N-1)

# --- Energía espectral ---
k_vals = np.arange(1, N-1)  # modos desde 1 hasta N-2
omega_k = (np.pi**2 * hbar * k_vals**2) / (2 * M * L**2)
E_k = hbar * omega_k

# --- Energía total ---
E_total = np.sum(E_k * (alpha_k**2 + eta_k**2))

# ----- Función para ψ(x, t) -----
def psi_xt(t):
    cos_part = np.cos(omega_k * t)
    sin_part = np.sin(omega_k * t)

    re_coeff = alpha_k * cos_part - eta_k * sin_part
    im_coeff = alpha_k * sin_part + eta_k * cos_part

    basis = np.sin(np.pi * k_vals[:, None] * np.arange(1, N-1) / (N-1))
    psi_real = np.sum(re_coeff[:, None] * basis, axis=0)
    psi_imag = np.sum(im_coeff[:, None] * basis, axis=0)

    return psi_real + 1j * psi_imag

# Verificar la norma de la función de onda
norm_check = np.sum(np.abs(psi_xt(0))**2) * dx # Evaluar en t = 0
print(f"Norma de la función de onda en t=0: {norm_check}")

# --- Visualización en un instante fijo ---
t_fixed = 1e-16
psi_real_t = np.zeros(N)
psi_real_t[1:-1]=np.real(psi_xt(t_fixed))

plt.figure(figsize=(8, 4))
plt.plot(x, psi_real_t)
plt.title(f"Re[ψ(x, t)] en t = {t_fixed:.2e} s", fontsize=14, fontweight='bold')
plt.xlabel("x (m)", fontsize=12, fontweight='bold')
plt.ylabel("Re[ψ(x, t)]", fontsize=12, fontweight='bold')
plt.xlim(0, L)
plt.tight_layout()
plt.show()

# --- Animación de la evolución temporal ---
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 8))

# Primer gráfico: Re[ψ(x, t)] vs x
line_re, = ax1.plot(x_internal, np.real(psi_xt(0)), label='Re[ψ(x, t)]')
ax1.set_ylabel('Re[ψ(x, t)]', fontsize=12, fontweight='bold')
ax1.set_xlim(0, L)
ax1.legend()

# Segundo gráfico: |ψ(x, t)|² vs x
line_prob, = ax2.plot(x_internal, np.abs(psi_xt(0))**2, label='|ψ(x, t)|²', color='red')
ax2.set_ylabel('|ψ(x, t)|²', fontsize=12, fontweight='bold')
ax2.set_xlabel('Posición x (m)', fontsize=12, fontweight='bold')
ax2.set_xlim(0, L)
ax2.legend()

# Tercer gráfico: Energía vs t
tiempo = np.linspace(0, steps*dt, N)
energía = E_total*np.ones(N)
line_energy, = ax3.plot(tiempo, energía, label='Energía total', color='green')
ax3.set_ylabel('Energía (J)', fontsize=12, fontweight='bold')
ax3.set_xlabel('t (s)', fontsize=12, fontweight='bold')
ax3.set_ylim(0.99*E_total, 1.01*E_total)
ax3.set_xlim(tiempo[0], tiempo[-1])
ax3.legend()

title = ax1.set_title('t = 0 s')

# --- Parámetros de animación ---

frame_counter = [0]
def update(_):
    t = frame_counter[0] * dt
    psi = psi_xt(t)

    # Actualizar datos de la onda
    line_re.set_ydata(np.real(psi))
    line_prob.set_ydata(np.abs(psi)**2)

    title.set_text(f't = {t:.2e} s')
    frame_counter[0] += 1
    return line_re, line_prob, line_energy, title

ani = FuncAnimation(fig, update, frames=steps, interval=1, blit=True)

# Guardar como Gif
guardar_gif = False
if guardar_gif:
    print("Guardando animación como 'onda_cuantica.gif'...")
    ani.save("onda_cuantica.gif", writer='pillow', fps=30)
    print("Gif guardado.")

# Guardar como MP4
guardar = False
if guardar:
    print("Guardando animación como 'onda_cuantica.mp4'...")
    ani.save("onda_cuantica.mp4", fps=30, writer='ffmpeg')
    print("Video guardado.")

plt.tight_layout()
plt.show()
