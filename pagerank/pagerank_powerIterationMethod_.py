import networkx as nx 
import matplotlib.pyplot as plt

G=nx.DiGraph()
G.add_weighted_edges_from([(1, 2, 1), (2, 3, 1), (3, 4, 1),
                            (1, 5, 0.5), (5, 6, 0.5), (6, 4, 1),
                            (4, 7, 1), (7, 8, 2.3), (7, 10, 1),
                            (8, 9, 1), (4, 12, 1.3), (12, 13, 1),
                            (12, 10, 0.06), (13, 14, 1), (10, 11, 0.2),
                            (11, 14, 1)
                            ])

G.out_degree(1, weight='weight')

pr=nx.pagerank(G,0.4) 

print pr

pos=nx.spectral_layout(G)
nx.draw(G)
nx.draw_networkx_edge_labels(G,pos)
plt.show()

def pagerank(G, alpha=0.85, personalization=None, 
			max_iter=100, tol=1.0e-6, nstart=None, weight='weight', 
			dangling=None): 
	"""Return the PageRank of the nodes in the graph. 

	Parameters 
	---------- 
	G : graph 
	A NetworkX graph. Undirected graphs will be converted to a directed 
	graph with two directed edges for each undirected edge. 

	alpha : float, optional 
	Damping parameter for PageRank, default=0.85. 

	max_iter : integer, optional 
	Maximum number of iterations in power method eigenvalue solver. 

	tol : float, optional 
	Error tolerance used to check convergence in power method solver. 

	nstart : dictionary, optional 
	Starting value of PageRank iteration for each node. 

	weight : key, optional 
	Edge data key to use as weight. If None weights are set to 1. 

	Returns 
	------- 
	pagerank : dictionary 
	Dictionary of nodes with PageRank as value 
	"""
	if len(G) == 0: 
		return {} 

	if not G.is_directed(): 
		D = G.to_directed() 
	else: 
		D = G 

	# Create a copy in (right) stochastic form 
	W = nx.stochastic_graph(D, weight=weight) 
	N = W.number_of_nodes() 

	# Choose fixed starting vector if not given 
	if nstart is None: 
		x = dict.fromkeys(W, 1.0 / N) 
	else: 
		# Normalized nstart vector 
		s = float(sum(nstart.values())) 
		x = dict((k, v / s) for k, v in nstart.items()) 

	if personalization is None: 

		# Assign uniform personalization vector if not given 
		p = dict.fromkeys(W, 1.0 / N) 
	else: 
		missing = set(G) - set(personalization) 
		if missing: 
			raise NetworkXError('Personalization dictionary '
								'must have a value for every node. '
								'Missing nodes %s' % missing) 
		s = float(sum(personalization.values())) 
		p = dict((k, v / s) for k, v in personalization.items()) 

	if dangling is None: 

		# Use personalization vector if dangling vector not specified 
		dangling_weights = p 
	else: 
		missing = set(G) - set(dangling) 
		if missing: 
			raise NetworkXError('Dangling node dictionary '
								'must have a value for every node. '
								'Missing nodes %s' % missing) 
		s = float(sum(dangling.values())) 
		dangling_weights = dict((k, v/s) for k, v in dangling.items()) 
	dangling_nodes = [n for n in W if W.out_degree(n, weight=weight) == 0.0] 

	# power iteration: make up to max_iter iterations 
	for _ in range(max_iter): 
		xlast = x 
		x = dict.fromkeys(xlast.keys(), 0) 
		danglesum = alpha * sum(xlast[n] for n in dangling_nodes) 
		for n in x: 
 
			# doing a left multiply x^T=xlast^T*W 
			for nbr in W[n]: 
				x[nbr] += alpha * xlast[n] * W[n][nbr][weight] 
			x[n] += danglesum * dangling_weights[n] + (1.0 - alpha) * p[n] 

		# check convergence, l1 norm 
		err = sum([abs(x[n] - xlast[n]) for n in x]) 
		if err < N*tol: 
			return x 
	raise NetworkXError('pagerank: power iteration failed to converge '
						'in %d iterations.' % max_iter) 
