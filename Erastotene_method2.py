'''
Il programma calcola la posizione di Giove, Saturno, Urano e Nettuno rispetto all'osservatore terrestre per un intervallo di tempo di un mese (dal 1 aprile al 1 maggio 2023) e traccia un grafico della loro longitudine apparente rispetto
'''

import ephem
import numpy as np
import matplotlib.pyplot as plt

# Costruiamo un oggetto "Observer" per l'osservatore terrestre
observer = ephem.Observer()
observer.lat = '0'   # Latitudine dell'osservatore (equatoriale)
observer.lon = '0'   # Longitudine dell'osservatore (meridiano di Greenwich)
observer.elevation = 0    # Altezza dell'osservatore dal livello del mare

# Costruiamo gli oggetti per i pianeti Giove, Saturno, Urano e Nettuno
jupiter = ephem.Jupiter()
saturn = ephem.Saturn()
uranus = ephem.Uranus()
neptune = ephem.Neptune()

# Calcoliamo la posizione dei pianeti e dell'osservatore terrestre per un dato intervallo di tempo
start_date = '2023/04/01'
end_date = '2023/05/01'
dates = np.arange(ephem.Date(start_date), ephem.Date(end_date), 1)    # Array di date ogni giorno
jupiter_pos = []
saturn_pos = []
uranus_pos = []
neptune_pos = []
observer_pos = []
for date in dates:
    observer.date = date
    jupiter.compute(observer)
    saturn.compute(observer)
    uranus.compute(observer)
    neptune.compute(observer)
    jupiter_pos.append([jupiter.ra, jupiter.dec])
    saturn_pos.append([saturn.ra, saturn.dec])
    uranus_pos.append([uranus.ra, uranus.dec])
    neptune_pos.append([neptune.ra, neptune.dec])
    observer_pos.append([observer.sidereal_time(), observer.lat])

# Converitamo le posizioni in gradi e le trasformiamo in un array NumPy
jupiter_pos = np.array(jupiter_pos) * 180 / np.pi
saturn_pos = np.array(saturn_pos) * 180 / np.pi
uranus_pos = np.array(uranus_pos) * 180 / np.pi
neptune_pos = np.array(neptune_pos) * 180 / np.pi
observer_pos = np.array(observer_pos)

# Creiamo un grafico della longitudine dei pianeti rispetto all'osservatore terrestre
fig, ax = plt.subplots()
ax.plot(observer_pos[:,0], jupiter_pos[:,0], label='Giove')
ax.plot(observer_pos[:,0], saturn_pos[:,0], label='Saturno')
ax.plot(observer_pos[:,0], uranus_pos[:,0], label='Urano')
ax.plot(observer_pos[:,0], neptune_pos[:,0], label='Nettuno')
ax.set_xlabel('Tempo (ore)')
ax.set_ylabel('Longitudine (gradi)')
ax.legend()
plt.show()
