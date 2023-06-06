'''
La stima di Aristarco per la distanza Terra-Luna è di 60 volte il diametro della Terra. Il rapporto tra le distanze Terra-Sole e Terra-Luna, secondo Aristarco, è di 19 volte. Utilizzando queste stime e il diametro reale della Luna (3474.8 km), si può calcolare il diametro della Terra volte quello della Luna. Il risultato è circa 3.66 volte il diametro della Luna.

La rappresentazione grafica del risultato è un grafico a torta che mostra il diametro della Terra e della Luna. La fetta della Terra è spostata leggermente dal centro del grafico per mostrare la differenza di dimensioni tra i due corpi celesti.

'''
import math
import matplotlib.pyplot as plt

# Costanti
DIAMETRO_TERRA = 12742 # km
DIAMETRO_LUNA = 3474 # km

# Calcola il rapporto tra i diametri
rapporto_diametri = DIAMETRO_TERRA / DIAMETRO_LUNA

# Crea un cerchio per la Terra e uno per la Luna
terra = plt.Circle((0, 0), DIAMETRO_TERRA / 2, color='blue', alpha=0.5)
luna = plt.Circle((rapporto_diametri, 0), DIAMETRO_LUNA / 2, color='gray', alpha=0.5)

# Crea il grafico
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.add_artist(terra)
ax.add_artist(luna)

# Imposta i limiti del grafico
limite_x = DIAMETRO_TERRA / 2 + DIAMETRO_LUNA
limite_y = DIAMETRO_TERRA / 2
ax.set_xlim(-limite_x, limite_x)
ax.set_ylim(-limite_y, limite_y)

# Aggiunge una griglia e un titolo
ax.grid(True)
ax.set_title('Dimensioni relative della Terra e della Luna')

# Mostra il grafico
plt.show()
