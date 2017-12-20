import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from collections import *

def compute_centrality_measures(subgr):
    #Degree centrality
    dict_dc = nx.degree_centrality(subgr)
    #Closeness centrality
    dict_close = nx.closeness_centrality(subgr)
    #Betweeness centrality
    dict_bet = nx.betweenness_centrality(subgr)
    #Eigenvector centrality
    dict_eig = nx.eigenvector_centrality(subgr, max_iter = 1000)

    return [dict_dc, dict_close, dict_bet, dict_eig]

def bar_plot(d):    
    counts = Counter(d.values())
    categories = ["%.4f" % elem for elem in counts.keys()]
    ax = sns.barplot(x = categories, y = list(counts.values()),  palette = 'Blues_d')
    ax.set_xticklabels(ax.get_xticklabels(), rotation = 40, ha = 'right')
    plt.tight_layout()
    plt.ylabel('Frequency', fontsize = 25)
    plt.xlabel('Centrality Score', fontsize = 25)
    
def strip_plot(d):
    categories =  ["%.4f" % elem for elem in d.values()]
    ax = sns.stripplot(x = categories, y = list(d.keys()), palette = "Blues_d", jitter = True)
    ax.set_xticklabels(ax.get_xticklabels(), rotation = 40, ha = 'right')
    plt.tight_layout()
    plt.xlabel('Centrality score', fontsize = 25)
    plt.ylabel('Node', fontsize = 25)

def bar_plot_degree(G):
    counts = Counter(nx.degree(G).values())
    sns.barplot(x = list(counts.keys()), y = list(counts.values()),  palette = 'Blues_d')
    plt.title('Bar chart')
    plt.ylabel('Frequency')
    plt.xlabel('Degree')
    plt.show()


def centrality_measures_plot(dict_dc, dict_close, dict_bet, dict_eig):
    plt.figure(figsize = (25,45))

    #strip-plot
    plt.subplot(421)
    plt.title("Strip-Plot : Degree Centrality", fontsize = 40)
    strip_plot(dict_dc)
    #bar chart
    plt.subplot(422)
    plt.title("Bar chart : Degree Centrality", fontsize = 40)
    bar_plot(dict_dc)
    
    #Betweeness centrality
    
    #strip-plot
    plt.subplot(423)
    plt.title("Strip-Plot : Betweenness Centrality", fontsize = 40)
    strip_plot(dict_bet)
    
    #bar chart
    plt.subplot(424)
    plt.title("Bar chart : Betweenness Centrality", fontsize = 40)
    bar_plot(dict_bet)
    
    #Closeness centrality
    
    #strip-plot
    plt.subplot(425)
    plt.title("Strip-Plot : Closeness Centrality", fontsize = 40)
    strip_plot(dict_close)
    
    #bar chart
    plt.subplot(426)
    plt.title("Bar chart : Closeness Centrality", fontsize = 40)
    bar_plot(dict_close)
    
    #Eigenvector centrality
    
    #strip-plot
    plt.subplot(427)
    plt.title("Strip-Plot : Eigenvector Centrality", fontsize = 40)
    strip_plot(dict_eig)
    
    #bar chart
    plt.subplot(428)
    plt.title("Bar chart : Eigenvector Centrality", fontsize = 40)
    bar_plot(dict_eig)
    
    plt.show()
    
def scatter_plot_matrix(dict_dc, dict_bet, dict_close, dict_eig):
    df = pd.DataFrame.from_dict([dict_dc, dict_bet, dict_close, dict_eig]).transpose()
    sns.pairplot(df, kind = 'reg', palette = 'Blues_d')
    plt.show()
    
def violin_plot(dict_dc, dict_bet, dict_close, dict_eig):   
    #Degree centrality
    plt.figure(figsize = (20,30))
    plt.subplot(221)
    plt.title("Degree centrality")
    plt.ylabel("Distribution")
    sns.violinplot(y = list(dict_dc.values()))
    
    
    #Betwness centrality
    plt.subplot(222)
    plt.title("Betweenness centrality")
    plt.ylabel("Distribution")
    sns.violinplot(y = list(dict_bet.values()))
    
    #Closeness centrality
    plt.subplot(223)
    plt.title("Closeness centrality")
    plt.ylabel("Distribution")
    sns.violinplot(y = list(dict_close.values()))
    
    #Eigenvector centrality
    plt.subplot(224)
    plt.title("Eigenvector centrality")
    plt.ylabel("Distribution")
    sns.violinplot(y = list(dict_eig.values()))
    
    plt.show()