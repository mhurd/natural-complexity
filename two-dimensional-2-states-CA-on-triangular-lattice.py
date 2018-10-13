# 2D 2-STATES CELLULAR AUTOMATON ON TRIANGULAR LATTICE32

import matplotlib.pyplot as plt
import numpy as np

N = 64                  # Size of the 2D CA
n_iter = 30             # Number of iterations
n_neighbour = 6         # Number of connected neighbours per node
scatter_marker = "."    # Plot marker style
marker_style = dict(color='black', linestyle=':', marker='o',
                    markersize=3, markerfacecoloralt='gray')

dx = np.array([1, 0, 1, -1, 0, -1])     # nearest neighbour template x
dy = np.array([-1, -1, 0, 1, 1, 0])     # nearest neighbour template y
image = np.zeros((N, N), dtype=np.int)  # Initialise the lattice to white
image[N//2, N//2] = 1                   # But set the central node to black
plt.plot(N//2, N//2, **marker_style)
plt.axis([0, N, 0, N])
plt.gca().set_aspect(1)

# Iteration loop
for iterate in range(1, n_iter):
    # Set/Reset the evolution lattice
    update = np.zeros((N, N), dtype=np.int)
    # Lattice loops
    for i in range(1, N-1):
        for j in range(1, N-1):
            acc = 0
            # Loop over nearest neighbours
            for k in range(0, n_neighbour):
                # Count the active neighbours
                acc += image[i+dx[k], j+dy[k]]
            if image[i, j] == 0 and acc == 1:
                update[i, j] = 1
                # Plot the node (triangular lattice)
                plt.plot(j+(i-N//2)/2., N//2+0.866*(i-N//2), **marker_style)
    # End lattice loops
    # synchronous update of CA
    image += update
# End of iteration loop
plt.show()