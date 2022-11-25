"""
    4. Faça o gráfico do exemplo anterior utilizando agora a função f(x) = x3 + x2 +x+3.
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """Returns the value of Y axis using the given X value"""
    return x*3 - x*2 + 3

# Filling the vector with random values for x
x_values = np.random.random(20)

# Plot the graph for all x_values
plt.plot(x_values, f(x_values))
plt.grid()
plt.show()
