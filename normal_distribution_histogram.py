import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.stats import norm

N = 100 #vector length

"""
    Altura: Masc e Fem
"""

# Variables
central_value_fem = 1.65
scale_fem = 0.1
central_value_masc = 1.8
scale_masc = 0.1

# Generating Normal Distribution vectors
#altura_fem = np.random.normal(central_value_fem, scale_fem, N)
#Gerar numero aleatorio entre -0.2 e 0.2
#altura_fem = [random.normalvariate(1.65, 0.3) for i in range(N)]

altura_fem = np.random.normal(central_value_fem, scale_fem, N)
altura_masc = np.random.normal(central_value_masc, scale_masc, N)

print(altura_fem)
# Correction
# for i in range(N):
#     altura_fem[i] = altura_fem[i] + 1.65


## Plot the histogram
# plt.title("Altura mulheres")
# plt.plot()
# plt.hist(altura_fem)
# plt.show()

#Plot seaborn histogram overlaid with KDE
import seaborn as sns
ax = sns.histplot(data=altura_fem, kde=True, 
                  line_kws=dict(color='red', alpha=0.5, linewidth=1.5))
ax.get_lines()[0].set_color('red') # edit line color due to bug in sns v 0.11.0
ax.set_title('Altura mulheres', fontsize=14, pad=15)
plt.show()

plt.title("Altura homens")
plt.hist(altura_masc)
plt.show()



# """
#     Peso: Masc e Fem
# """
# Variables
central_value_fem = 65
scale_fem = 5
central_value_masc = 80
scale_masc = 8

# Generating Normal Distribution vectors
peso_fem = np.random.normal(central_value_fem, scale_fem, N )
peso_masc = np.random.normal(central_value_masc, scale_masc, N )

## Plot the histogram
plt.title("Peso mulheres")
plt.hist(peso_fem)
plt.show()

plt.title("Peso homens")
plt.hist(peso_masc)
plt.show()

