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

def generate_values(lenght, mean, standard_deviation, order):
    """Generates a random array of a normal distribution"""
    array = np.random.normal(loc=mean, scale=standard_deviation, size=lenght)

    if order:
        return sorted(array)
    return array

def plot_hist_by_mean(mean):
    hist_title = "Media {x}".format(x=mean)
    start_value = 10

    for i in range(1, 5): # plot 4 hist in 1 figure
        x = generate_values(start_value, mean, 1)
        plt.subplot(2, 2, i)
        plot_histogram(x, hist_title)
        start_value *= 10

    plt.show()


# Observações para 10, 100, 1000 e 10000 amostras. Com media=0 // Figure 1
# plot_hist_by_mean(0) 

# Observações para 10, 100, 1000 e 10000 amostras. Com media=1 // Figure 2
# plot_hist_by_mean(1) 


"""
    Quartis: Graficos dos quartis da normal e quartis da exponencial
    A quartiles describe how the data is distributed. It shows the lower (25%), mean and upper values (25%).
    We will use a boxplot to plot the quartiles graph.
    Reference: 
    - https://mashimo.wordpress.com/2013/07/06/quartiles-and-summary-statistics-in-python/
    - https://mashimo.wordpress.com/2013/07/21/visualize-quartiles-and-summary-statistics-in-python/
    - https://fernandafperes.com.br/blog/interpretacao-boxplot/
"""

def plot_quartiles_graph(mean):
    boxplot_title = "Media {x}".format(x=mean)
    start_value = 10

    for i in range(1, 5): # plot 4 boxplot in 1 figure
        x = generate_values(start_value, mean, 1)
        #plt.subplot(2, 2, i)
        plt.title(boxplot_title)
        plt.boxplot(x)
        start_value *= 10
        plt.show()

def quartile_summary(data):
    print("\n\n**** Resumo ****")
    print(f"Media: {np.mean(data):.2}")
    print(f"Min: {np.min(data):.2}")
    print(f"Q1 (lower): {np.quantile(data, .25):.2}")
    print(f"Mediana (Q2): {np.median(data):.2}")
    print(f"Q3 (upper): {np.quantile(data, .75):.2}")
    print(f"Max: {np.max(data):.2}")
    print(f"IRQ (Interquartile Range): {np.quantile(data, .75) - np.quantile(data, .25):.2}")

# Print resume of quantile before plot boxplot
start_value = 10
for i in range(4):
    quartile_summary(generate_values(start_value*10,0,1, True))

# Plot boxplot graph
quartiles_mean_0 = [
    generate_values(10,0,1, True), 
    generate_values(100,0,1, True), 
    generate_values(1000,0,1, True), 
    generate_values(10000,0,1, True)
    ]
plt.boxplot(quartiles_mean_0, showmeans=True, whis=99)
plt.title('Mean = 0') # chart title
plt.xticks([1,2,3,4], ['10','100','1.000', '10.000']) # x axis labels
plt.show()


# Print resume of quantile before plot boxplot
for i in range(4):
    quartile_summary(generate_values(start_value*10,0,1, True))

# Plot boxplot graph
quartiles_mean_1 = [
    generate_values(10,1,1, True),
    generate_values(100,1,1, True), 
    generate_values(1000,1,1, True), 
    generate_values(10000,1,1, True)
    ]
plt.boxplot(quartiles_mean_1, showmeans=True, whis=99, showfliers=True)
plt.title('Mean = 1') # chart title
plt.xticks([1,2,3,4], ['10','100','1.000', '10.000']) # x axis labels

plt.show()

"""
    CONCLUSAO
    - Os valores estão agrupados em torno da média, mesmo que a quantidade de dados aumente;
    - Não temos outliers;
    - Há uma distruição simétrica, pois a mediana está no meio dos retangulos.
    - A amplitude aumenta conforme o número de dados aumenta

"""