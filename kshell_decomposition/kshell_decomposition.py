import networkx as nx 
import matplotlib.pyplot as plt 


#defining stopping criteria of the k-shell iterations
def check_existence(H,d1):
	f=0		#there is no node of deg <=d after all iterations
	for each in H.nodes():
		if H.degree(each)<=d1:
				f=1
				break
	return f

#finding all nodes having degree less than or equal to it
def find(H,it):
	set1=[]
	for each in H.nodes():
		if H.degree(each)<=it:
			set1.append(each)
		
	return set1

##creating a trial directed graph 
DG = nx.DiGraph()
DG.add_weighted_edges_from([(1, 2, 1), (2, 3, 1), (3, 4, 1),
                            (1, 5, 0.5), (5, 6, 0.5), (6, 4, 1),
                            (4, 7, 1), (7, 8, 2.3), (7, 10, 1),
                            (8, 9, 1), (4, 12, 1.3), (12, 13, 1),
                            (12, 10, 0.06), (13, 14, 1), (10, 11, 0.2),
                            (11, 14, 1)
                            ])

DG.out_degree(1, weight='weight')

H=DG.copy()
it=1
tmp=[] #for the bucket being filled currently
buckets=[] #list of lists (buckets)

while (1):
	flag=check_existence(H,it)
	if flag==0:
		it=it+1
		buckets.append(tmp)	#bucket full
		tmp=[]				#start with a fresh bucket
	if flag==1:
		node_set=find(H,it) #from find()
		for each in node_set: ##pruning the nodes from the network and adding to the current bucket
			H.remove_node(each)
			tmp.append(each)
	if H.number_of_nodes()==0:		##terminating condition
				buckets.append(tmp) ##mark buckets filled
				break

print buckets		

pos=nx.spectral_layout(DG)
nx.draw(DG)
nx.draw_networkx_edge_labels(DG,pos)
plt.show()
