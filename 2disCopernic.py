from skyfield.api import load, JulianDate
import math

# carica i dati degli orbitali dei pianeti
ts = load.timescale()
eph = load('de421.bsp')
earth = eph['earth']
mars = eph['mars']

# definisci le date di inizio e fine
start_date = JulianDate(2023, 3, 30)
end_date = JulianDate(2024, 3, 30)

# calcola la distanza media tra la Terra e Marte
mean_distance = earth.at(start_date).observe(mars).distance().km

# ciclo per calcolare la distanza tra i due pianeti in diverse date
date = start_date
while date < end_date:
    # calcola la distanza tra la Terra e Marte in questa data
    distance = earth.at(date).observe(mars).distance().km
    
    # stampa la data e la distanza tra i due pianeti
    print(date.utc_jpl(), distance)
    
    # vai avanti di un giorno
    date += ts.utc(0, 0, 1)

# confronta la distanza effettiva con la distanza media
if distance > mean_distance:
    print("La distanza tra la Terra e Marte supera la distanza media.")
else:
    print("La distanza tra la Terra e Marte è inferiore alla distanza media.")
