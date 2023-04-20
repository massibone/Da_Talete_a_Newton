import matplotlib.pyplot as plt
import numpy as np

# Definiamo una funzione per il quadrato di (a+b)
def square_sum(a, b):
    return (a + b)**2

# Definiamo una funzione per il rettangolo 4ab
def rectangle_area(a, b):
    return 4*a*b

# Creiamo un array di valori per a e b
a_values = np.linspace(0, 10, 100)
b_values = np.linspace(0, 10, 100)

# Creiamo una griglia di punti (a, b)
a_grid, b_grid = np.meshgrid(a_values, b_values)

# Calcoliamo i valori del quadrato di (a+b) e del rettangolo 4ab per ogni punto della griglia
square_sum_values = square_sum(a_grid, b_grid)
rectangle_area_values = rectangle_area(a_grid, b_grid)


