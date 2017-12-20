import networkx as nx

def hop_d(children, dist, output_set, G):
    #using set to avoid repetitions, since the order does not matter 
    children_next = set()
    for child in children: 
        children_next.update(set(G.neighbors(child)))
    #update output_set with new children
    output_set.update(children_next)
    #decrease hop distance
    dist-=1
    #base case d = 0 
    if dist>0:
        hop_d(children_next, dist, output_set, G)
    return output_set 