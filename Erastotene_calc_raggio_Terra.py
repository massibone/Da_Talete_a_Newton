import math
import matplotlib.pyplot as plt

def calculate_radius(angle, distance):
    """
    Calcola il raggio della Terra a partire dall'angolo sotteso dall'arco di meridiano e dalla sua distanza.
    """
    angle = math.radians(angle)
    radius = distance / (2 * math.sin(angle / 2))
    return radius

if __name__ == '__main__':
    # Dati forniti da Eratostene
    distance = 5000 # in stadi (circa 930 km)
    angle = 7.2 # in gradi

    # Calcola il raggio della Terra
    radius = calculate_radius(angle, distance)
    print(f"Il raggio della Terra è di circa {radius:.2f} stadi.")

    # Rappresenta graficamente la situazione
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim([-radius, radius])
    ax.set_ylim([-radius, radius])
    circle = plt.Circle((0, 0), radius, fill=False)
    ax.add_artist(circle)
    ax.plot([0, 0], [-radius, radius], 'k-')
    ax.plot([-radius, radius], [0, 0], 'k--')
    ax.text(radius / 2, 0, 'D', fontsize=9)
    ax.text(0, radius / 2, 'E', fontsize=9)
    ax.text(0, -radius / 2, 'F', fontsize=14)
    ax.text(distance / 2, 0, 'G', fontsize=9)
    ax.text(distance / 2, radius / 2, 'H', fontsize=10)
    ax.text(distance / 2, -radius / 2, 'I', fontsize=10)
    ax.text(distance / 2, -10, f'    d = {distance} stadi', fontsize=10)
    ax.text(radius / 2, 10, f'   R = {radius:.2f} stadi', fontsize=12)
    plt.show()
