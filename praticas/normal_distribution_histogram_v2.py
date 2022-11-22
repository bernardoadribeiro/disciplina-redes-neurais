import numpy as np

VECTOR_LENGTH = 1000 # vectors length
import matplotlib.pyplot as plt
def plot_histogram(data_source, title):
    """
        Plot a histogram with curve of the the given data
        Required libs: Seaborn and matplotlib.pyplot
    """
    import seaborn as sns
    #import matplotlib.pyplot as plt

    #Plot seaborn histogram overlaid with KDE
    ax = sns.histplot(data=data_source, kde=True, edgecolor='white', linewidth=0.5, stat='density',
                      line_kws=dict(color='red'))
    
    ax.get_lines()[0].set_color('red') # edit line color due to bug in sns v 0.11.0
    ax.set_title(title, fontsize=14, pad=15)
    
    #plt.show()


"""
    Height: Mens and Womans
"""
# Variables
h_central_value_fem = 1.65 
h_scale_fem = 0.1
h_central_value_masc = 1.8
h_scale_masc = 0.1

# Generating Normal Distribution vectors
height_fem = np.random.normal(h_central_value_fem, h_scale_fem, VECTOR_LENGTH)
height_masc = np.random.normal(h_central_value_masc, h_scale_masc, VECTOR_LENGTH)

plt.subplot(2, 2, 1)
plot_histogram(height_fem, "Altura de Mulheres")
plt.subplot(2, 2, 2)
plot_histogram(height_masc, "Altura de Homens")


"""
    Weight: Mens and Womans
"""
w_central_value_fem = 65
w_scale_fem = 5
w_central_value_masc = 80
w_scale_masc = 8

# Generating Normal Distribution vectors
weight_fem = np.random.normal(w_central_value_fem, w_scale_fem, VECTOR_LENGTH)
weight_masc = np.random.normal(w_central_value_masc, w_scale_masc, VECTOR_LENGTH)

plt.subplot(2, 2, 3)
plot_histogram(weight_fem, "Peso Mulheres")
plt.subplot(2, 2, 4)
plot_histogram(weight_masc, "Peso Homens")

#plot all graphics
plt.show()