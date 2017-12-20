#Loading needed libraries
#import json
#import networkx as nx
#from itertools import combinations
#from collections import *
#import matplotlib.pyplot as plt
#import heapq
#import seaborn as sns
#import pandas as pd
from graph import *
from centrality import *
from hop_distance import *
from shortest_path import *
data = choose_data()
data = import_data(data)
G = create_graph(data)
print("The graph has been created. Here are some info:")
print(nx.info(G))

#part 2
print("\n\n\nEnter conference id: ")
conference_id = int(input())
#A list of authors of interest is obtained and hence a subgraph having them as nodes, is generated.
authors_of_interest = [aut for aut, attr in G.nodes(data = True) if conference_id in attr["conf_id"]]
subgraph_1 = G.subgraph(authors_of_interest)
print("Here is the visualization of the sub graph:") 
plot_graph(subgraph_1)
dict_dc, dict_close, dict_bet, dict_eig = compute_centrality_measures(subgraph_1)
print('Here is a plot of the number of nodes for each degree')
bar_plot_degree(subgraph_1)
centrality_measures_plot(dict_dc, dict_close, dict_bet, dict_eig)
#################################VIOLIN PLOT IF NEEDED + SCATTER PLOT
violin_plot(dict_dc, dict_close, dict_bet, dict_eig)
scatter_plot_matrix(dict_dc, dict_bet, dict_close, dict_eig)
#################################
print('Enter author_id:')
author_id = int(input())
author_id = [author_id] #converting into list to adapt it to hop_d function
print('Enter (hop distance) d :')
d = int(input())
#Giving empty set in input to start function's job normally
authors_of_interest_2 = hop_d(author_id, d, set(), G)
#Having the authors of interest, store them in a subgraph
subgraph_2 = G.subgraph(authors_of_interest_2)
#Plot the subgraph
plot_graph(subgraph_2)
#part 3
print('Enter id of target node:')
target = int(input())
aris = 256176
# The weight of the shortest path is printed (if source and target are connected).
s = shortestPath(G, aris, target)
print(s)
print("Enter the subset of nodes: (each node separated by a space from the subsequent one)")
query = list(map(int, input().split()))
results = shortestPath_all(G, query)
for result in results:
    print("Shortest path from node " + str(result) + " to one of the query elements is: " + str(results[result]))