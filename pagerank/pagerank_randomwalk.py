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

##the function returns the list of the nodes sorted by their points  
def get_nodes_sorted_by_Random_Walks(points):
	##sort the index for the values of the indices in the list points
	##converting the list into a numpy array
	points_array = np.array(points)
	nodes_sorted_by_RW = np.argsort(-points_array) #first sorting the points with argsort in decending order (check numpy documentation)
	return nodes_sorted_by_RW


def random_walk(G):
	nodes = G.nodes() 										##chose a node randomly
	RW_points = [0 for i in range(G.number_of_nodes())] 	#generate list of nodes
	r = random.choice(nodes) 								#randomly chosing a node to start the RW 
	RW_points[r] += 1 										#once visited the node is incremented to the next
	out = G.out_edges(r) 									##generate list of all neignbours of this nodes

	##method to select a node at random, find the neighbours by outlinks and walk to one of the neighbours at random
	##till all node are covered
	c = 0
	while (c != 100000):
		if (len(out) == 0):									##if the node does not have any outlinks
			focus = random.choice(nodes) 					##randomly select a focus node and make it the current node
		else:
			r1 = random.choice(out)
			focus = r1[1]									#if multiple edges are found, make the next node the focus
		RW_points[focus] += 1
		out = G.out_edges(focus)
		c += 1

	return RW_points
	 	

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
	###Perform Random Walk
	RW_points = random_walk(G) 

	##Sort the nodes based on RW points
	nodes_sorted_by_RW = get_nodes_sorted_by_Random_Walks(RW_points)
	print 'get_nodes_sorted_by_Random_Walks: ', nodes_sorted_by_RW

	'''
	Small test to check Random Walks method
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