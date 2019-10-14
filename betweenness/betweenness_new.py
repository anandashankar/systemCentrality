import networkx as nx
import matplotlib.pyplot as plt

'''
        Incase of a directed graph, use the DiGraph class of networkx
        import your network here
        ------------------------
        Trial network 
'''
DG = nx.DiGraph()
DG.add_weighted_edges_from([(1, 2, 1), (2, 3, 1), (3, 4, 1),
                            (1, 5, 0.5), (5, 6, 0.5), (6, 4, 1),
                            (4, 7, 1), (7, 8, 2.3), (7, 10, 1),
                            (8, 9, 1), (4, 12, 1.3), (12, 13, 1),
                            (12, 10, 0.06), (13, 14, 1), (10, 11, 0.2),
                            (11, 14, 1)
                            ])

DG.out_degree(1, weight='weight')

'''
incase of undirected graph, use H=nx.Graph(G) to convert to undirected
G=nx.erdos_renyi_graph(50,0.5) #using random graph with 50 nodes. Import your weighted network 
'''
b=nx.betweenness_centrality(DG)

print(b)

#nx.draw(DG,with_labels=1)
pos=nx.spectral_layout(DG)
nx.draw(DG)
nx.draw_networkx_edge_labels(DG,pos)
plt.show()


def betweenness_centrality(G, k=None, normalized=True, weight=None, 
						endpoints=False, seed=None): 
	"""
        Compute the shortest-path betweenness centrality for nodes.

	Parameters 
	---------- 
	G : graph 
	A NetworkX graph. 

	k : int, optional (default=None) 
	If k is not None use k node samples to estimate betweenness. 
	The value of k <= n where n is the number of nodes in the graph. 
	Higher values give better approximation. 

	normalized : bool, optional 
	If True the betweenness values are normalized by `2/((n-1)(n-2))` 
	for graphs, and `1/((n-1)(n-2))` for directed graphs where `n` 
	is the number of nodes in G. 

	weight : None or string, optional (default=None) 
	If None, all edge weights are considered equal. 
	Otherwise holds the name of the edge attribute used as weight. 

	endpoints : bool, optional 
	If True include the endpoints in the shortest path counts.

	Refere to networkx documentation at https://networkx.github.io/documentation/stable/reference/algorithms/centrality.html#shortest-path-betweenness 
	"""
	betweenness = dict.fromkeys(G, 0.0) # b[v]=0 for v in G 
	if k is None: 
		nodes = G 
	else: 
		random.seed(seed) 
		nodes = random.sample(G.nodes(), k) 
	for s in nodes: 

		# single source shortest paths 
		if weight is None: # use BFS 
			S, P, sigma = _single_source_shortest_path_basic(G, s) 
		else: # use Dijkstra's algorithm 
			S, P, sigma = _single_source_dijkstra_path_basic(G, s, weight) 

		# accumulation 
		if endpoints: 
			betweenness = _accumulate_endpoints(betweenness, S, P, sigma, s) 
		else: 
			betweenness = _accumulate_basic(betweenness, S, P, sigma, s) 

	# rescaling 
	betweenness = _rescale(betweenness, len(G), normalized=normalized, 
						directed=G.is_directed(), k=k) 
	return betweenness 

