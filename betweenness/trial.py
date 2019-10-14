import networkx as nx
import matplotlib.pyplot as plt

'''
#H=nx.Graph()
G=nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)

G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(2,4)
G.add_edge(3,4)
G.add_edge(4,5)
G.add_edge(5,6)
'''
#Z=nx.complete_graph(10)
Z=nx.gnp_random_graph(1000,0.5)
'''
#DG = nx.DiGraph()
#DG.add_weighted_edges_from([(1, 2, 1), (2, 3, 1), (3, 4, 1),
                            (1, 5, 0.5), (5, 6, 0.5), (6, 4, 1),
                            (4, 7, 1), (7, 8, 2.3), (7, 10, 1),
                            (8, 9, 1), (4, 12, 1.3), (12, 13, 1),
                            (12, 10, 0.06), (13, 14, 1), (10, 11, 0.2),
                            (11, 14, 1)
                            ])
DG.out_degree(1, weight='weight')
'''
n=Z.nodes()
e=Z.edges()

print(n)
print('/n')
print(e)

nx.draw(Z,with_labels=1)
plt.show()

