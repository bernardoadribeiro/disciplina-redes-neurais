import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

matrix = np.zeros(shape=[20,4]) # Create a matrix filled with zeros

# Col 1
mean, std = 0, 1
for i in range(20):
    matrix[i, 0] = round(np.random.normal(mean, std), 2)

# Col 2
mean, std = 3, 0.5
for i in range(20):
    matrix[i, 1] = round(np.random.normal(mean, std), 2)

# Col 3
mean, std = 6, 0.3
for i in range(20):
    matrix[i, 2] = round(np.random.normal(mean, std), 2)

# Col 4
mean, std = 9, 3
for i in range(20):
    matrix[i, 3] = round(np.random.normal(mean, std), 2)

df = pd.DataFrame(matrix)
print(df)

plt.plot(df,"-o")
plt.show()

plt.figure(figsize=(8,5))
df.rename(columns={0:'Média=0 DP=1', 1:'Média=3 DP=0.5', 2:'Média=6 DP=0.3', 3:'Média=9 DP=3'}, inplace=True)
sns.scatterplot(data=df)
plt.savefig("Ex03-Figure_1")
plt.show()

"""
    É possível observar que os pontos ficam mais dispersos quando há um desvio padrão maior e tende a não ser tão constante.
    Já quando há um desvio padrão menor, os pontos tendem a ser mais próximos um dos outros meio que formando uma linha em torno da média.
    Também é observado que o desenho formado pelos pontos (ao ligar um no outro) parecem tentar seguir um padrão de desenhado. Isso foi observado ao rodar algumas vezes o código e ver que a distribuição dos pontos, apesar de serem aleatórias, tentam seguir um "padrão".
"""