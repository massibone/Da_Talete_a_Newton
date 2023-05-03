import math

# costanti fisiche
G = 6.6743e-11 # costante gravitazionale
M_SUN = 1.989e30 # massa del Sole in kg
AU = 1.496e11 # unità astronomica in metri

# parametri orbitali per la Terra e Marte (da https://nssdc.gsfc.nasa.gov/planetary/factsheet/)
a_EARTH = 1.00000011 * AU # semiasse maggiore dell'orbita terrestre
e_EARTH = 0.01671022 # eccentricità dell'orbita terrestre
i_EARTH = 0.00005 # inclinazione dell'orbita terrestre rispetto all'eclittica
L_EARTH = math.radians(100.46435) # longitudine del nodo ascendente dell'orbita terrestre
w_EARTH = math.radians(102.94719) # argomento del perielio dell'orbita terrestre
M_EARTH = math.radians(0.0) # anomalia media della Terra all'epoca J2000

a_MARS = 1.52366231 * AU # semiasse maggiore dell'orbita di Marte
e_MARS = 0.09341233 # eccentricità dell'orbita di Marte
i_MARS = 1.85061 # inclinazione dell'orbita di Marte rispetto all'eclittica
L_MARS = math.radians(49.57854) # longitudine del nodo ascendente dell'orbita di Marte
w_MARS = math.radians(336.04084) # argomento del perielio dell'orbita di Marte
M_MARS = math.radians(355.45332) # anomalia media di Marte all'epoca J2000

# funzione per calcolare la posizione di un pianeta in un dato istante
def position(a, e, i, L, w, M, t):
    # calcola la posizione della Terra in questo istante
    E = M
    E_next = E + (M - e * math.sin(E) - M) / (1 - e * math.cos(E))
    while abs(E_next - E) > 1e-12:
        E = E_next
        E_next = E + (M - e * math.sin(E) - M) / (1 - e * math.cos(E))
    xv = a * (math.cos(E) - e)
    yv = a * math.sqrt(1 - e*e) * math.sin(E)
    v = math.atan2(yv, xv)
    r = math.sqrt(xv*xv + yv*yv)
    xh = r * (math.cos(L) * math.cos(v+w) - math.sin(L) * math.sin(v+w) * math.cos(i))
    yh = r * (math.sin(L) * math.cos(v+w) + math.cos(L) * math.sin(v+w) * math.cos(i))
    zh = r * math.sin(v+w) * math.sin(i)
    
    # calcola la posizione del pianeta in questo istante
    x, y, z = rotate(xh, yh, zh, L_EARTH, i_E)
