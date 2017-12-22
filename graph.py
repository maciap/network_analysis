import json
import networkx as nx
from itertools import combinations
import matplotlib.pyplot as plt


def choose_data():
    ans = input("Do you want to use the complete data set? (y/n) ")
    if ans == "y" or ans == "Y":
        full = True
    else:
        full = False
    return full

def import_data(full):
    if full:
        data = json.load(open('full_dblp.json'))
    else:
        data= json.load(open('reduced_dblp.json'))
    return data

def create_graph(data_to_load):
    G=nx.Graph()
    
    #adding nodes
    #for each note we give attributes the name of the, his publications,
    #with id's and titles, and the conferences he's been to
    
    authors_for_publ = []
    for publ in data_to_load:
        authors = []
        for aut in publ["authors"]:
            authors.append(aut["author_id"])
            try: 
                G.node[aut["author_id"]]
            except:
                G.add_node(aut["author_id"], name = aut["author"], publ_id = set(), title =  set(), conf_id = [])
            G.node[aut["author_id"]]["publ_id"].add(publ['id_publication_int'])
            G.node[aut["author_id"]]["title"].add(publ['title'])
            G.node[aut["author_id"]]["conf_id"].append(publ['id_conference_int'])
        authors_for_publ.append(authors)
                
    #adding edges
    for auth in authors_for_publ:
        Allcombinations = combinations(auth,2)
        for comb in Allcombinations:
            Jaccard = 1 - (len(G.node[comb[0]]["publ_id"].intersection(G.node[comb[1]]["publ_id"])) / len(G.node[comb[0]]["publ_id"].union(G.node[comb[1]]["publ_id"])))    
            G.add_edge(comb[0], comb[1], weight = Jaccard)
    return G


def plot_graph(G, color, author = None ):
    #Assigning random positions for the graph nodes. The size of the nodes reflect their degrees.
    pos = nx.random_layout(G)
    degrees = nx.degree(G)
    #Plotting the graph
    if author is not None:
        name = G.node[author]['name'] 
        nx.draw_networkx_labels(G, {author : pos[author]}, labels = {author: name}, font_size = 12)
        nx.draw_networkx_nodes(G, pos, node_shape = "o", node_size =[v for v in degrees.values()] , node_color = color)
        nx.draw_networkx_edges(G, pos, width = 0.2 , edge_color = "red", alpha = 0.5)
    else:
        nx.draw_networkx_nodes(G, pos, node_shape = "o", node_size =[v*20 for v in degrees.values()] , node_color = color)
        #use instead node_size =[(1 + v*20) for v in degrees.values()] to also visualize nodes having degree zero
        nx.draw_networkx_edges(G, pos, width = 0.2 , edge_color = "red", alpha = 0.5)
    plt.axis('off')
    plt.show()
