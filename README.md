# systemCentrality
centrality measures of graph based systems

1. Centrality of nodes in graph-based system representation
	A. Betweenness centrality implementation on a trial network. 

	B. Modified PageRank centrality measure by 2 methods:
		i. Point Distribution: This method assigns arbitrary starting points to the nodes in the network and iterates to find the node rank. In the code implementation, note the use of sinks. 
		This acts like penalties or taxes on the network. In this case, after the node rank is obtained by point distribution, a penalty is put on all nodes and the ranks are normalized. 
		Note the use of sink function. 
		ii. Random walks: 

2. Influence of nodes on other nodes in complex networks
	A. K-shell decomposition of trial network identifying buckets of nodes. This method identifies those nodes which are more core to the network defined by coreness and hence considered as influential spreaders.  


