

import numpy as np
import matplotlib.pyplot as plt

# Definiamo la funzione matematica per la posizione angolare della particella
def particle_position(t, A, omega):
    return A * np.sin(omega * t)

# Definiamo i parametri per la funzione di posizione angolare della particella
A = 1    # ampiezza dell'oscillazione
omega = 2 * np.pi   # frequenza angolare costante

# Calcoliamo la posizione angolare della particella in funzione del tempo per un intervallo di 2 periodi
t = np.linspace(0, 2 * np.pi / omega, 100)
theta = particle_position(t, A, omega)

# Visualizziamo la posizione angolare della particella in funzione del tempo
plt.plot(t, theta)
plt.xlabel('Tempo (s)')
plt.ylabel('Posizione angolare (rad)')
plt.title('Oscillazioni angolari di una particella')
plt.show()
