import matplotlib.pyplot as plt
import numpy as np

# Define the scaling factor (50% smaller)
scaling_factor = 0.50

# Define the coordinates of the vertices of the smaller pentagon
x = [0.5 + scaling_factor * 0.4 * np.cos(2 * np.pi * i / 5) for i in range(5)]
y = [0.5 + scaling_factor * 0.4 * np.sin(2 * np.pi * i / 5) for i in range(5)]

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the smaller pentagon with a black outline
plt.fill(x + [x[0]], y + [y[0]], color='blue', edgecolor='black', lw=2)

# Add a line from (0.330, 0.620) to (0.330, 0.920)
line_x = [0.3375, 0.3375]
line_y = [0.6200, 0.8200]
plt.plot(line_x, line_y, color='black', lw=2)

# Add a black line from (0.3375, 0.8200) to (0.1300, 0.8200)
line_x2 = [0.3375, 0.1300]
line_y2 = [0.8200, 0.8200]
plt.plot(line_x2, line_y2, color='black', lw=2)

# Set axis limits and equal aspect ratio
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')

# Remove axis labels
ax.axis('off')

# Show the plot
plt.show()

# Save the plot as an image to your PC
# plt.savefig('Pentagon_With_Lines_And_Outline.png', dpi=300, bbox_inches='tight')

# Close the plot window
plt.close()
