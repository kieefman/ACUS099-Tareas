import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definimos dos señales
def signal1(x):
    return 0.8**x * np.where((x >= 0) & (x <= 8), 1, 0)

def signal2(x):
    return np.where((x >= 0) & (x <= 5), 1, 0)

# Parámetros de la animación
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
x = np.linspace(-5, 10, 400)
y1 = signal1(x)
y2 = signal2(x)

# Gráfico de las señales
line1, = ax1.plot(x, y1, label='x[n]')
line2, = ax1.plot(x, y2, label='h[n]')
ax1.legend()
ax1.set_xlim(-5, 10)
ax1.set_ylim(0, 2)

# Gráfico de la convolución
line3, = ax2.plot([], [], label='Convolución', color='r')
ax2.legend()
ax2.set_xlim(-5, 10)
ax2.set_ylim(0, 2)

# Arreglos para almacenar los resultados de la convolución acumulada
conv = np.zeros_like(x)
#conv = (len(y1) + len(y2) - 1) * [0] #Pre-Alocamos ceros

# Función de actualización para la animación
def update(frame):
    t = frame - 10
    y2_shifted = signal2(x - t)

    #Set data señal 2
    line2.set_ydata(y2_shifted)
    
    #for k in range(len(y1)):
    #    conv[t+k] += (y1[t]*y2[k]) / len(y1)
    conv = np.convolve(y1, y2_shifted, mode='same') / len(x)
    #print(len(conv))

    line3.set_data(x,conv)
    return line1, line2, line3

# Crear la animación
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 25), blit=True)

# Mostrar la animación
plt.show()