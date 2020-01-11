#Analyzing.py
import pandas as pd
import numpy as np
import matplotlib as mpl 
import matplotlib.pyplot as plt

def analyze(df_complete):
    y = df_complete['% of World Population']
    x = df_complete['number of billionaires']
    n = df_complete['country']
    fig, ax = plt.subplots()
    plt.xlabel('Number of billionaires')
    plt.ylabel('% from world population')
    plt.figure(figsize=(890,200))
    ax.scatter(x, y)
    for i, txt in enumerate(n):
        ax.annotate(txt, (x[i], y[i]))
    return fig.savefig('/Users/Julia/labs/Ironhack-Module-1-Project---Pipelines-Julia-Roch-/data/results/scatter-plot-result.png')  
