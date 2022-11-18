"""
    2. Faça um algoritmo para multiplicar matrizes que sejam compatíveis.
"""

import numpy as np

# Create matrixes (min_value, max_value, size=(rows, columns))
matrix1 = np.random.randint(1,10, size=(4,4))
matrix2 = np.random.randint(1,10, size=(4,4))
matrix3 = np.random.randint(1,10, size=(3,4))

print("Matrix 1: \n", matrix1)
print("\nMatrix 2: \n",matrix2)
print("\nMatrix 3: \n",matrix3)

result_matrix1 = np.multiply(matrix1,matrix2) # multiply compatible matrix
#result_matrix2 = np.multiply(matrix1,matrix3) #multiply uncompatible matrix (returns error)

print("\nResultado: \n", result_matrix1)