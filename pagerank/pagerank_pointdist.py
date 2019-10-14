import networkx as nx 
import random
import numpy as np
import matplotlib.pyplot as plt 


#add all possible edges that can be added to the graph
#replace this block with imported network
def add_edges(G, p):
	for i in G.nodes():
		for j in G.nodes():
			if i != j:
				r = random.random()
				if r<=p:
					G.add_edge(i,j)
				else:
					continue
	return G


##a function where every node will be dristributing its points
def distribute_points(G, points):
	prev_points = points
	new_points = [0 for i in range(G.number_of_nodes())]

	for i in G.nodes():
		out = G.out_edges(i) #defining out edges. This function is available for DiGraphs only
		if len(out) == 0:	#if the node does not have any outlinks
			new_points[i] += prev_points[i]
		else:
			share = (float)(prev_points[i])/len(out) #previous points gets distributed in equal share
			for each in out:
				new_points[each[1]] += share
			
	return G, new_points 	

##this function is the node tax. This removes 20% of the node rank and redistributes in all the nodes
def handle_points_sink(G, points):
	for i in range(len(points)):
		points[i] = (float)(points[i])*0.8

	n = G.number_of_nodes()
	extra = ((float)(n)*100*0.2)/n
	for i in range(len(points)):
		points[i] += extra

	return points


###this function has to keep calling distribute_points func
def keep_distributing_points(G, points):
	prev_points = points
	print 'Enter # to stop'
	while(1):
		G, new_points = distribute_points(G, prev_points)
		print new_points

		new_points = handle_points_sink(G, new_points)

		char = raw_input()
		if char == '#':
			break
		prev_points = new_points

	return G, new_points


def initialize_points(G):
	points = [100 for i in range(G.number_of_nodes())]
	return points



##the function returns the list of the nodes sorted by their points  
def get_nodes_sorted_by_points(points):
	##sort the index for the values of the indices in the list points
	##converting the list into a numpy array
	points_array = np.array(points)
	nodes_sorted_by_points = np.argsort(-points_array) #first sorting the points with argsort in decending order (check numpy documentation)
	return nodes_sorted_by_points



def main():
	##Create a directed graph with n nodes
	##Import network as a collection of nodes and edges  
	G=nx.DiGraph()
	G.add_nodes_from([i for i in range(100)]) 
	G=add_edges(G, 0.3) #add_edges function assign starting probabilities
	"""
	In case of imported network assign probabilities as: 
	G=add_edges(G, 1/number_of_nodes) 
	"""

	#Assigning 100 points to each node
	points=initialize_points(G)
	print points

	###keep distributing the points until convergence
	G, points = keep_distributing_points(G, points)

	##Rank the nodes based on the point convergence 
	nodes_sorted_by_points = get_nodes_sorted_by_points(points)
	print 'nodes_sorted_by_points: ', nodes_sorted_by_points

	'''
	Small test to check point distribution method
	compare with library PageRank method of netwrokx
	-----------------------------------------------
	'''
	##Compare the ranks obtained with the ranks obtained from inbuilt PageRank method 
	##it returns a dictionary where the keys are the nodes and values are the pageranks of the nodes
	pr = nx.pagerank(G) 
	###creating a list of tuples from the dictionary 
	pr_sorted = sorted(pr.items(), key = lambda x:x[1], reverse = True)

	print 'Test result: '
	for i in pr_sorted:
	  	print i[0],   


	nx.draw(G,with_labels=1)
	#pos=nx.spectral_layout(DG)
	nx.draw(G)
	#nx.draw_networkx_edge_labels(DG,pos)
	plt.show()


main()