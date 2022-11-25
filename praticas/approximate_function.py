import numpy as np
import matplotlib.pyplot as plt

N = 200 # qtt of data

x = np.arange(N)
delta = np.random.normal(x, N, size=N)
# y = .4 * x +3 + delta
y = (0.5 * (x**2) + 3*x + 10) + 10* delta

plt.plot(x,y, 'o')

# obtain m(slope) and b(intercept) of best fit line
m, b = np.polyfit(x, y, 1)

# use red as color for regression line
plt.plot(x, m*x+b, color='red')

plt.show()