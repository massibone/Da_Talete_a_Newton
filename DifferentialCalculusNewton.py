import numpy as np
import matplotlib.pyplot as plt

def newton(f, df, x0, tol, max_iter):
    """
    Implementazione del metodo di Newton per il calcolo differenziale.
    
    Args:
        f (callable): La funzione da cui si vuole trovare l'intercetta.
        df (callable): La derivata della funzione f.
        x0 (float): Il valore di partenza per l'algoritmo di Newton.
        tol (float): La tolleranza per la convergenza dell'algoritmo di Newton.
        max_iter (int): Il numero massimo di iterazioni per l'algoritmo di Newton.
        
    Returns:
        float: L'intercetta della funzione f.
    """
    x = x0
    for i in range(max_iter):
        dx = -f(x) / df(x)
        x += dx
        if abs(dx) < tol:
            return x
    raise ValueError("Il metodo di Newton non ha converguto entro il numero massimo di iterazioni.")

def main():
    # Definiamo la funzione da cui vogliamo trovare l'intercetta.
    f = lambda x: x**3 - 5*x**2 + 3*x + 7
    
    # Definiamo la derivata della funzione.
    df = lambda x: 3*x**2 - 10*x + 3
    
    # Definiamo il valore di partenza per l'algoritmo di Newton.
    x0 = 2.0
    
    # Definiamo la tolleranza per la convergenza dell'algoritmo di Newton.
    tol = 1e-6
    
    # Definiamo il numero massimo di iterazioni per l'algoritmo di Newton.
    max_iter = 100
    
    # Applichiamo il metodo di Newton per trovare l'intercetta della funzione.
    x = newton(f, df, x0, tol, max_iter)
    print("L'intercetta della funzione è:", x)
    
    # Visualizziamo la funzione e l'intercetta trovata.
    x_vals = np.linspace(-2, 5, 1000)
    y_vals = f(x_vals)
    plt.plot(x_vals, y_vals, label="Funzione")
    plt.plot(x, f(x), 'ro', label="Intercetta")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
