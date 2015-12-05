import networkx as nx
import matplotlib.pyplot as plt
from networkx import *
import sys
import math

def readFile(filename):
    listData = []
    G=nx.Graph()
    with open(filename, 'r') as datafile:
        for i, line in enumerate(datafile):
            if i > 3:
                listData.append(line)
    for data in listData:
        temp = data.split('\t')
        fromNodeId = int(temp[0])
        toNodeId = int(temp[1])
        G.add_edge(fromNodeId, toNodeId)
    print filename +' value: ' + str(nx.average_clustering(G))

def ErdosRenyi():
    n=5000
    #G(n, m), G(n,p) m = c(n, 2) * p, c(5000, 2) * 0.01 = 124975
    m = int(Cnr(5000, 2) * 0.01)
    G=gnm_random_graph(n,m)
    print 'random_graph value: ' + str(nx.average_clustering(G))
    #nx.draw(G)

def Cnr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)
    
def main():
    ErdosRenyi()
    readFile('CA-GrQc.txt')
    readFile('p2p-Gnutella04.txt')
    readFile('Wiki-Vote.txt')
    readFile('WikiTalk.txt')
    #plt.show()

if __name__ == '__main__':
    main()
   
    