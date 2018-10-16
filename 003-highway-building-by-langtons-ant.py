# HIGHWAY BUILDING BY LANGTON'S ANT

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col

N = 300             # Lattice size
n_iter = 20000      # Number of iterations

x_step = np.array([0, -1, 0, 1])                # Template arrays for steps
y_step = np.array([1, 0, -1, 0])
image = np.zeros((N, N), dtype=np.int)          # Initialise the lattice to white
ix = N//4                                       # Ant's x starting position
iy = N//4                                       # Ant's y starting position
direction = 1                                   # Ant's starting direction (North)

# Temporal loop
for iterate in range(0, n_iter):

    ix += x_step[direction]                     # Ant moves
    iy += y_step[direction]
    ix = (N+ix) % N                             # Enforce periodicity (i.e. wrap the lattice)
    iy = (N+iy) % N

    if image[ix, iy] == 0:                      # On a white node
        update = 1                              # Paint it black...
        direction += 1                          # ..and turn right
        direction = direction % 4               # ... but stay within the step array
    else:                                       # On a black node
        update = -1                             # Paint it white
        direction -= 1                          # ... and turn left
        direction = (4+direction) % 4           # ... but stay within step array

    image[ix, iy] += update
# End of temporal loop

# Use a colormap to map 0 to white and 1 to black
plt.imshow(image, interpolation="nearest", cmap=col.ListedColormap([(1, 1, 1), (0, 0, 0)]))
plt.show()