import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d

"""
    Create matrix bi-dimensional with M-rows and N-column
"""
M = 26 #rows_qtt
N = 26 #columns_qtt

# Create a empty matrix
matrix = np.empty(shape=(M,N), dtype=int) 

x = 4 # exponential
n_start = -26 # start of range
n_end = 26 # end of range

# Filling the matrix with quadratic fuction
for i in range(n_start, n_end):
    for j in range(n_start, n_end):
        matrix[i][j] = j**x + 4*i + i*j # Quadractic function to fill the matrix with
        #matrix[i][j] = i**3 + j**3 + 6*i*j # Quadractic fuction -- Prof
print(matrix)


"""
    [Option 1] Plotting the matrix as a 3d graph
"""

# Create a dataframe from the matrix
df = pd.DataFrame(matrix)
print(df)

# Define the XYZ axis
x = df.columns
y = df.index
X,Y = np.meshgrid(x,y)
Z = df

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X,Y,Z, cmap='plasma')
plt.show()



"""
    [Option 2] Plotting the matrix as a 3d graph
"""
 
# Creating dataset
x = matrix
y = x.copy().T # transpose
z = (np.sin(x **2) + np.cos(y **2) )
 
# Creating figure
fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')
 
# Creating plot
ax.plot_surface(x, y, z, cmap='plasma')
 
# show plot
plt.show()

# def f(x, y):
#     return np.sin(np.sqrt(x ** 2 + y ** 2))

# x = np.linspace(-26, 26, 30)
# y = np.linspace(-26, 26, 30)
# X, Y = np.meshgrid(x, y)
# Z = f(X, Y)
# fig = plt.figure(figsize=(10, 10))
# ax = plt.axes(projection='3d')
# ax.contour3D(X, Y, Z, 50, cmap='coolwarm')
# ax.set_title('Gráficos de contorno no Espaço 3D', fontsize=18)
# ax.set_xlabel('Eixo X', fontsize=15)
# ax.set_ylabel('Eixo Y', fontsize=15)
# ax.set_zlabel('Eixo Z', fontsize=15)
# ax.view_init(70, 35)
# plt.show()

