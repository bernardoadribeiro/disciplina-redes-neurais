import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot_histogram(data_source, *title):
    """
        Plot a histogram with curve of the the given data
        Required libs: Seaborn and matplotlib.pyplot
    """

    #Plot seaborn histogram overlaid with KDE
    ax = sns.histplot(data=data_source, kde=True, edgecolor='white', linewidth=0.5, #stat='density',
                      line_kws=dict(color='red'))
    
    ax.get_lines()[0].set_color('red') # edit line color due to bug in sns v 0.11.0
    ax.set_title(title, fontsize=14, pad=15)
    
    #plt.show()

def generate_values(lenght, mean, standard_deviation):
    """Generates a random array of a normal distribution"""

    array = np.random.normal(loc=mean, scale=standard_deviation, size=lenght)
    return array

def plot_hist_by_mean(mean):
    hist_title = "Media {x}".format(x=mean)
    value = 10

    for i in range(1, 5): # plot 4 hist in 1 figure
        x = generate_values(value, mean, 1)
        plt.subplot(2, 2, i)
        plot_histogram(x, hist_title)
        value *= 10

    plt.show()


# Observações para 10, 100, 1000 e 10000 amostras. Com media=0 // Figure 1
plot_hist_by_mean(0) 

# Observações para 10, 100, 1000 e 10000 amostras. Com media=1 // Figure 2
plot_hist_by_mean(1) 


"""
    Quartis: Graficos dos quartis da normal e quartis da exponencial
"""


