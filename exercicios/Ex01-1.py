"""
    1. Dada uma lista com a nota de cinco alunos, encontre a média, o desvio padrão e ordene as notas.
"""

import pandas as pd
import numpy as np

n_alunos = 5 #quantidade de alunos

notas_alunos = np.random.uniform(0, 10, n_alunos) # create the vector  from  0 to 10
for i in range(n_alunos):
    notas_alunos[i] = round(notas_alunos[i], 2) # round notes

mean = np.mean(notas_alunos) #Calculate the mean of notes
standard_deviation = np.std(notas_alunos) #Calculate the standard deviation of notes
ordered_notes = sorted(notas_alunos)

print("Notas dos alunos:", notas_alunos,
      "\nMedia: ", mean,
      "\nDesvio padrao: ", standard_deviation,
      "\nNotas ordenadas", ordered_notes)
