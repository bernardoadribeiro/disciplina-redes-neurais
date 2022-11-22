"""
    Dado um vetor com 10 valores, escreva as funções que calculam a média e o desvio padrão desse vetor.
    Compare os resultados de suas funções com os resultados obtidos pelas funções mean e sd.
"""

import numpy as np
import matplotlib.pyplot as plt

# Calc manually
def mean_value(array):
    return sum(array)/len(array)

def sd_value(array):
    aritmetic_mean = mean_value(array)
    n = len(array)
    summatory = 0
    
    # Calculate the summatory
    for i in range(n):
        summatory += (array[i] - aritmetic_mean)**2

    sigma = np.sqrt(summatory/n) 

    return sigma

vector = np.random.randint(1, 30, size=10)
print("Vetor: ", vector, "\ntam.: ", len(vector))

# Calc using my functions

print("Media: ", mean_value(vector))
print("Desvio Padrao: ", sd_value(vector))

# Calc using libs
print("Media: ", vector.mean())
print("Desvio Padrao: ", vector.std())