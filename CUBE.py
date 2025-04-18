# CUBE.PY

import matplotlib.pyplot as plt
import numpy as np

# First 5 cubes
x_small = np.arange(1, 6)
y_small = x_small ** 3

plt.figure(figsize=(8, 5))
plt.scatter(x_small, y_small, c=y_small, cmap='viridis', s=100, edgecolors='black')
plt.title('First 5 Cubic Numbers')
plt.xlabel('Number')
plt.ylabel('Cube')
plt.colorbar(label='Cube Value')
plt.grid(True)
plt.tight_layout()
plt.savefig('first_5_cubes.png')  # Save the plot
plt.show()

# First 5000 cubes
x_large = np.arange(1, 5001)
y_large = x_large ** 3

plt.figure(figsize=(10, 6))
plt.scatter(x_large, y_large, c=y_large, cmap='plasma', s=2)
plt.title('First 5000 Cubic Numbers')
plt.xlabel('Number')
plt.ylabel('Cube')
plt.colorbar(label='Cube Value')
plt.grid(True)
plt.tight_layout()
plt.savefig('first_5000_cubes.png')  # Save the plot
plt.show()
