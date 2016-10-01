import time
start_time=time.time()
import networkx as nx
#from networkx import Graph
import random
import sys
#orig_stdout=sys.stdout
f= open('out6.txt','w')
sys.stdout=f
G=nx.gnm_random_graph(1000,1000000)
for (u,v,w) in G.edges(data=True):
    w['weight'] = random.randint(0,10)
length=nx.all_pairs_shortest_path_length(G)
print("no of nodes=")
print(nx.number_of_nodes(G))
print("\n")
print("no of edges=")
print(nx.number_of_edges(G))
print("\n")
print("dense graph")
print("\n")
print("nodes created are")
print(G.nodes(data=True))
print("\n")
print("edges created are")
print(G.edges(data=True))
print("\n")
print("Betweenness centrality values=")
print (nx.betweenness_centrality(G))
print("\n")
print("Time of execution=")
print ("---%s seconds ---\n" %(time.time()-start_time))
#sys.stdout=orig.stdout
f.close()
