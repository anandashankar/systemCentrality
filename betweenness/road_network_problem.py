#Modelling the roadnetwork of Indian cities

import networkx as nx
import matplotlib.pyplot as plt
import random

G=nx.Graph()    #undirected graph

city_set=['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hydrabad', 'Pune', 'Jaipur', 'Ahmedabad']

for each in city_set:
    G.add_node(each)

#nx.draw(G)
#plt.show()

costs=[]
value=100
while (value<=2000):
    costs.append(value)
    value=value+100

print (costs)

#adding 16 edges to the network
while(G.number_of_edges()<16):
    c1=random.choice(G.nodes())                 ##have to import random
    c2=random.choice(G.nodes())     
    if c1!=c2 and G.has_edge(c1,c2)==0:         #check if there exist a node between the nodes
        w=random.choice(costs)                  #the weight is cost
        G.add_edge(c1,c2,weight=w)

nx.draw(G)
plt.show()
