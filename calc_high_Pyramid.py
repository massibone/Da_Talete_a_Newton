'''
programma Python per calcolare l'altezza di una piramide utilizzando l'ombra proiettata da una persona alta 170cm, e una rappresentazione grafica
la lunghezza dell'ombra (76.5 metri), l'altezza della persona (1.7 metri) e l'angolo formato dal sole e la verticale (45 gradi). Questi dati vengono poi passati alla funzione calculate_height per calcolare l'altezza della Piramide di Giza. Infine, il programma stampa il risultato arrotondato a due cifre decimali.



'''
import math
import matplotlib.pyplot as plt
import numpy as np

def calculate_height(shadow_length, person_height, angle):
    """
    Calcola l'altezza della Piramide di Giza a partire dalla lunghezza dell'ombra proiettata da una persona alta person_height
    e dall'angolo formato dalla direzione del sole e la verticale.
    """
    angle = math.radians(angle)
    height = shadow_length * 139 / (shadow_length * math.tan(angle) + person_height)
    return height

if __name__ == '__main__':
    # Dati noti
    shadow_length = 76.5 # in metri
    person_height = 1.7 # in metri
    angle = 45 # in gradi

    # Calcola l'altezza della Piramide di Giza
    height = calculate_height(shadow_length, person_height, angle)
    print(f"L'altezza della Piramide di Giza è di circa {height:.2f} metri.")

    # Rappresenta graficamente la Piramide di Giza e l'altezza della persona
    fig, ax = plt.subplots(figsize=(10, 10))

    # Disegna la piramide
    base = 230
    height = 139
    ax.plot([0, base, base/2, 0], [0, 0, height, 0], 'k-', lw=1)

    # Disegna l'ombra della persona
    ax.plot([0, shadow_length], [0, person_height], 'r--', lw=2)
    ax.plot([shadow_length], [person_height], 'ro', markersize=8)

    # Disegna il cono d'ombra
    shadow_angle = math.atan(person_height / shadow_length)
    shadow_height = height * shadow_length / (shadow_length * math.tan(angle) - height * math.tan(shadow_angle))
    shadow_width = shadow_height * shadow_length / person_height
    shadow = plt.Circle((shadow_width, 0), shadow_height, color='black', alpha=0.2)
    ax.add_artist(shadow)

    # Aggiunge etichette e titoli
    ax.text(shadow_length+2, person_height, f'{shadow_length:.1f}m', fontsize=14)
    ax.text(base/2-5, height+5, f'{height}m', fontsize=14)
    ax.text(0, -10, '0', fontsize=14)
    ax.text(base-10, -10, f'{base}m', fontsize=14)
    ax.text(base/2-10, height/2, f'{angle}°', fontsize=14)
    ax.text(shadow_length/2, -10, f'Persona alta {person_height}m', fontsize=14)
    ax.set_xlabel('Lunghezza della base')
    ax.set_ylabel('Altezza')

    # Limiti degli assi
    ax.set_xlim(-10, base+10)
    ax.set_ylim(-10, height+20)

    # Aggiunge il cono d'ombra
    x_shadow = np.linspace(shadow_width-shadow_height, shadow_width+shadow_height, 100)
    y_shadow = np.linspace(-shadow_height, shadow_height, 100)
    X_shadow, Y_shadow = np.meshgrid(x_shadow, y_shadow)
    R_shadow = (X_shadow-shadow_width)**2

    plt.title(' Piramide di Giza')
    plt.show()

