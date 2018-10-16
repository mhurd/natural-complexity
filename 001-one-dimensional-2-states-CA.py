# 1D 2-STATES CELLULAR AUTOMATON

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col

N = 513         # Size of the 1D CA
n_iter = 512    # Number of iterations

image = np.zeros((n_iter, N), dtype=np.int)       # Initialise the lattice to white
image[0, N//2] = 1                                # But set the central node to black

# Iteration loop (each line)
for iterate in range(1, n_iter):
    # Lattice loop (along the line)
    for j in range(1, N-1):
        # Third CA rule from book
        if image[iterate-1, j+1] + image[iterate-1, j-1] == 1:
            # Turn node black
            image[iterate, j] = 1
        # Enforce periodicity (but don't fall off the end of the matrix)
        if iterate < n_iter-1:
            # Move the end value to the start of the next iteration
            image[iterate+1, 0] = image[iterate, N-2]
            # Move the last value to the start of the next row
            image[iterate+1, N-1] = image[iterate, 1]

# Use a colormap to map 0 to white and 1 to black
plt.imshow(image, interpolation="nearest", cmap=col.ListedColormap([(1, 1, 1), (0, 0, 0)]))
plt.show()
