import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates and radius of the larger circle
x1 = 0
y1 = 0
r1 = 3

# Define the coordinates and radius of the smaller circle
x2 = 2
y2 = 0
r2 = 1

# Define the epicenter, deficenter, and equant of the smaller circle
a = (r1 + r2)/2
b = np.sqrt((r1*r2)/(r1+r2))
c = np.sqrt(r1*r2)

# Create a plot
fig, ax = plt.subplots()

# Plot the larger circle
circle1 = plt.Circle((x1, y1), r1, fill=False)
ax.add_artist(circle1)

# Plot the smaller circle
circle2 = plt.Circle((x2, y2), r2, fill=False)
ax.add_artist(circle2)

# Plot the epicenter, deficenter, and equant of the smaller circle
ax.scatter(x2+a, y2, color='red', label='Epicenter')
ax.scatter(x2-a, y2, color='green', label='Deficenter')
ax.scatter(x2, y2+b, color='blue', label='Equant')

# Set the axis limits and aspect ratio
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')

# Add labels and title to the plot
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Two Circles with Epicenter, Deficenter, and Equant')

# Add legend to the plot
ax.legend()

# Show the plot
plt.show()
