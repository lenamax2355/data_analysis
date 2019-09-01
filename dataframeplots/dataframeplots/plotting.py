import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd 

def numeric_Hist(df, plotCols = 4, figsize = (18,18), kde = False, bins = None, color = None):

    '''Plot histograms of the numerical columns of a pandas.Dataframe
    
     Parameters:
    -----------
    - df {pandas.Dataframe}: the dataframe to be plotted

    Optional arugments:
    - plotCols {int}: number of columns the histogram will have. [Default value: 4]
    - figsize {tuple}: argument of matplotlib.pyplot.suplobts. [Default value: (18,18)]
    - kde {bool}: argument of seaborn.distplot. Whether to plot a gaussian kernel density estimate. [Default value: False] 
    - bins {int}: Specification of hist bins. [Default value: None - uses Freedman-Diaconis rule]
    - color {matplotlib color}: color to plot everything [Default value: None - output is blue]
    
    '''

    # which columns are numerical and will be plotted
    nameCols = [el for el in df if df[el].dtypes != 'object']

    # how many rows should be present
    if len(nameCols) <= plotCols:
        plotRows = 1
        plotCols = len(nameCols)
    else: 
        plotRows = -(-len(nameCols)//plotCols)

    # plotting
    fig, axes = plt.subplots(plotRows, plotCols, figsize=figsize)
    fig.suptitle('Distributions of columns with numeric values')
    fig.subplots_adjust(hspace=0.5, wspace=0.3)
    for el, ax in zip(nameCols, axes.flatten()):
        sns.distplot(df[el].dropna(), hist_kws = {'edgecolor':'grey', 'linewidth':1}, ax= ax, kde = kde, bins = bins, color = color)
        #ax.set(title=el)
    plt.show()

    return

''' to do: 

# 3D plotting - for KMeans 

def colors(x):
    if x == 0: out = 'r'
    elif x == 1: out = 'c'
    elif x == 2: out = 'g'
    else: out = 'm'
    return out

color = patients['Cluster'].apply(colors)



from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

n = 100
for c, z in zip(['r', 'g', 'b', 'p'], patients['Cluster']):
    cs = [c] * len(patients['patient_weight_kg'])
    ax.scatter(patients['patient_weight_kg'], patients['Cluster'], patients['patient_height_sm'], depthshade=True, c = color, alpha = 0.1)

ax.set_xlabel('Patient weight')
ax.set_zlabel('Patient height')
ax.set_ylabel('Cluster')

plt.show()

'''