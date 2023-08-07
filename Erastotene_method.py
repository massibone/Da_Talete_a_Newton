import math
import matplotlib.pyplot as plt

def eratostene(lat1, lon1, lat2, lon2, d):
    # Convertiamo le coordinate in radianti
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Calcoliamo l'angolo tra le due città
    angle = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))
    
    # Calcoliamo la lunghezza dello stadion in metri
    stadion = 185
    
    # Calcoliamo la distanza tra le due città in stadi
    distance = (d / stadion) * angle * stadion
    
    # Calcoliamo il diametro della Terra in stadi
    diameter = distance / math.pi
    
    # Calcoliamo il raggio della Terra in stadi
    radius_earth = diameter / 2
    
    # Stampa il raggio e il diametro della Terra in stadi
    print("Il raggio della Terra è di", radius_earth, "stadi.")
    print("Il diametro della Terra è di", diameter, "stadi.")
    
    # Disegniamo una rappresentazione grafica della misura di Eratostene
    plt.figure(figsize=(8,8))
    plt.plot([0, distance], [0, 0], 'k-', lw=2) # La linea che collega le due città
    plt.plot([0, 0], [0, radius_earth], 'k-', lw=2) # Il primo meridiano
    plt.plot([distance, distance], [0, radius_earth], 'k-', lw=2) # Il secondo meridiano
    plt.plot([0, distance], [radius_earth, radius_earth], 'k-', lw=2) # L'equatore
    plt.text(distance/2, -radius_earth/10, str(round(distance, 2)) + " stadi") # Etichetta della distanza
    plt.text(-distance/20, radius_earth/2, str(round(diameter, 2)) + " stadi") # Etichetta del diametro
    plt.text(distance/2, radius_earth*1.1, str(round(radius_earth, 2)) + " stadi") # Etichetta del raggio
    plt.xlim(-distance/10, distance*1.1)
    plt.ylim(-radius_earth/10, radius_earth*1.2)
    plt.axis('off')
    plt.show()
    
# Costruiamo un esempio
lat1 = 37.7749
lon1 = -122.4194
lat2 = 51.5074
lon2 = -0.1278
d = 7870 # distanza tra le due città in chilometri

# Chiamiamo la funzione
eratostene(lat1, lon1, lat2, lon2, d)
