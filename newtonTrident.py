import numpy as np
import matplotlib.pyplot as plt

# Define the constants
a = 1
b = 2

# Define the hyperbola
x1 = np.linspace(-10, -0.1, 1000)
x2 = np.linspace(0.1, 10, 1000)
y1 = b*np.sqrt(1 + (x1/a)**2)
y2 = -b*np.sqrt(1 + (x2/a)**2)

# Define the parabola
x3 = np.linspace(-10, 10, 1000)
y3 = (b*x3**2 - a**2)/(2*a*x3)

# Create a plot
fig = plt.figure()
ax = fig.add_subplot(111)

# Plot the hyperbola
ax.plot(x1, y1, linestyle='--', color='gray', label='Hyperbola')
ax.plot(x2, y2, linestyle='--', color='gray')

# Plot the parabola
ax.plot(x3, y3, label='Parabola')

# Add labels and title to the plot
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Parabola and Hyperbola with Asymptotes')

# Add legend to the plot
ax.legend()

# Show the plot
plt.show()
