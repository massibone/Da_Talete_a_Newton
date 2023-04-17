import numpy as np
import matplotlib.pyplot as plt

# Definiamo la funzione matematica per il movimento del pianeta
def planet_motion(t, A, B, omega):
    return A * np.sin(omega * t) + B * np.sin(2 * omega * t)

# Definiamo i parametri per la funzione di movimento del pianeta
A = 10   # ampiezza delle oscillazioni primarie
B = 5    # ampiezza delle oscillazioni secondarie
omega = 0.1   # frequenza costante

# Calcoliamo l'angolo del pianeta in funzione del tempo per un intervallo di 1000 giorni
t = np.linspace(0, 1000, 10000)
theta = planet_motion(t, A, B, omega)

# Visualizziamo l'angolo del pianeta in funzione del tempo
plt.plot(t, theta)
plt.xlabel('Tempo (giorni)')
plt.ylabel('Angolo del pianeta (gradi)')
plt.title('Oscillazioni angolari di un pianeta immaginario')
plt.show()
