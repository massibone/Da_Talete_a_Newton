import numpy as np
import matplotlib.pyplot as plt

# Definizione dei parametri del prisma
n1 = 1.0 # Indice di rifrazione dell'aria
n2 = 1.5 # Indice di rifrazione del prisma
A = 30.0 # Angolo del prisma (in gradi)

# Calcolo dell'angolo di deviazione
d = (n1*np.sin(np.deg2rad(A))) / n2
delta = np.rad2deg(np.arcsin(d))

# Calcolo dello spettro di dispersione
lambda0 = 589.3 # Lunghezza d'onda della luce gialla (in nm)
delta_lambda = (n2-n1)/n2 * (1/lambda0) * np.cos(np.deg2rad(delta/2))

# Plot dello spettro di dispersione
fig, ax = plt.subplots()
ax.plot([lambda0-delta_lambda, lambda0, lambda0+delta_lambda], [0, 1, 0])
ax.set_xlabel('Lunghezza d\'onda (nm)')
ax.set_ylabel('Intensità')
ax.set_title('Spettro di dispersione del tridente di Newton')
plt.show()
