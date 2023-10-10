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

# Plot the pentagon with a black outline
plt.fill(x + [x[0]], y + [y[0]], color='silver', edgecolor='black', lw=2)

# Add the letter "S" to the pentagon
ax.text(0.5, 0.5, "S", color='black', fontsize=20, ha='center', va='center')

# Add a first line
line_x = [0.4200, 0.3775]
line_y = [0.5600, 0.7000]
plt.plot(line_x, line_y, color='black', lw=2)

# Add a second line
line_x2 = [0.3775, 0.2275]
line_y2 = [0.7000, 0.7400]
plt.plot(line_x2, line_y2, color='black', lw=2)

# Add a yellow circle with specified diameter
circle_inner = Circle((0.1380, 0.7400), 0.080, fill=True, color='yellow', edgecolor='black', lw=2)
ax.add_patch(circle_inner)

# Draw a black circumference
circle_outer = Circle((0.1380, 0.7400), 0.081, fill=False, color='black', lw=2)
ax.add_patch(circle_outer)

# Add the letter "P" to the circle
ax.text(0.1380, 0.7400, "P", color='black', fontsize=20, ha='center', va='center')

# Set axis limits and equal aspect ratio
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')

# Add a third line
line_x3 = [0.60, 0.80]
line_y3 = [0.50, 0.65]
plt.plot(line_x3, line_y3, color='black', lw=2)

# Add a square with equal sides starting from (0.80, 0.65)
square = Rectangle((0.80, 0.65 - 0.060), 0.160, 0.120, fill=True, color='salmon', edgecolor='black', lw=2)
ax.add_patch(square)

# Add the letter "A" to the square
ax.text(0.88, 0.80 - 0.150, "T", color='black', fontsize=20, ha='center', va='center')

# Add four black lines around the square
line_x4 = [0.80, 0.96, 0.96, 0.80, 0.80]
line_y4 = [0.59, 0.59, 0.71, 0.71, 0.59]
plt.plot(line_x4, line_y4, color='black', lw=2)

# Remove axis labels
ax.axis('off')

# Show the plot
plt.show()

# Save the plot as an image to your PC
# plt.savefig('Nucleotide_T5.png', dpi=300, bbox_inches='tight')

# Close the plot window
plt.close()
