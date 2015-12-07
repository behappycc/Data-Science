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
    nx.draw(G)

def ErdosRenyi():
    G = nx.erdos_renyi_graph(5000, 0.01)
    print 'random_graph value: ' + str(nx.average_clustering(G))
    nx.draw(G)

def main():
    plt.figure('random_graph')
    ErdosRenyi()
    plt.figure('CA-GrQc')
    readFile('CA-GrQc.txt')
    plt.figure('p2p-Gnutella04')
    readFile('p2p-Gnutella04.txt')
    plt.figure('Wiki-Vote')
    readFile('Wiki-Vote.txt')
    #plt.figure('p2p-Gnutella08')
    #readFile('p2p-Gnutella08.txt')
    plt.show()

if __name__ == '__main__':
    main()
   
    