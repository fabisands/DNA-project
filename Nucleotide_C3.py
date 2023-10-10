import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle

# Define the scaling factor for pentagon
scaling_factor = 0.25

# Define the coordinates of the vertices of the pentagon
x = [0.5 + scaling_factor * 0.4 * np.cos(2 * np.pi * i / 5) for i in range(5)]
y = [0.5 + scaling_factor * 0.4 * np.sin(2 * np.pi * i / 5) for i in range(5)]

# Create a figure and axes
fig, ax = plt.subplots()

# Mirror the pentagon on the X and Y axes
x_mirror = [1.0 - xi for xi in x]
y_mirror = [1.0 - yi for yi in y]

# Plot the mirrored pentagon with a black outline
plt.fill(x_mirror + [x_mirror[0]], y_mirror + [y_mirror[0]], color='silver', edgecolor='black', lw=2)

# Add the letter "S" to the pentagon
ax.text(0.5, 0.5, "S", color='black', fontsize=20, ha='center', va='center')

# Add a first line
line_x = [0.5800, 0.6225]
line_y = [0.4400, 0.3000]
plt.plot(line_x, line_y, color='black', lw=2)

# Add a second line
line_x2 = [0.6225, 0.7725]
line_y2 = [0.3000, 0.2600]
plt.plot(line_x2, line_y2, color='black', lw=2)

# Add a yellow circle with specified diameter
circle_inner = Circle((0.8620, 0.2600), 0.080, fill=True, color='yellow', edgecolor='black', lw=2)
ax.add_patch(circle_inner)

# Draw a black circumference
circle_outer = Circle((0.8620, 0.2600), 0.081, fill=False, color='black', lw=2)
ax.add_patch(circle_outer)

# Add the letter "P" to the circle
ax.text(0.8620, 0.2600, "P", color='black', fontsize=20, ha='center', va='center')

# Set axis limits and equal aspect ratio
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')

# Add a third line
line_x3 = [0.40, 0.20]
line_y3 = [0.50, 0.35]
plt.plot(line_x3, line_y3, color='black', lw=2)

# Add a square with equal sides starting from (0.20, 0.35)
square = Rectangle((0.04, 0.29), 0.160, 0.120, fill=True, color='cyan', edgecolor='black', lw=2)
ax.add_patch(square)

# Add the letter "A" to the square
ax.text(0.12, 0.35, "C", color='black', fontsize=20, ha='center', va='center')

# Add four black lines around the square starting from (0.200, 0.400)
line_x4 = [0.04, 0.20, 0.20, 0.04, 0.04]
line_y4 = [0.41, 0.41, 0.29, 0.29, 0.41]
plt.plot(line_x4, line_y4, color='black', lw=2)

# Remove axis labels
ax.axis('off')

# Show the plot
plt.show()

# Save the plot as an image to your PC
# plt.savefig('Nucleotide_C3.png', dpi=300, bbox_inches='tight')

# Close the plot window
plt.close()
