import networkx as nx

import numpy as np
import pandas as pd

def nx_connected_components(nodelist):
    """
    """
    G = nx.Graph()
    G.add_nodes_from(sum(nodelist, []))
    e = [[(s[i],s[i+1]) for i in range(len(s)-1)] for s in nodelist]
    
    for i in e:
        G.add_edges_from(i)
    
    return [list(i) for i in nx.connected_components(G)]

