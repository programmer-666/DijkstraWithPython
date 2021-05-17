import hashlib
from random import randbytes
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class CreateGraph:
    def __init__(self):
        self.__node = []
        self.__edge = []
        self.__graphId = hashlib.sha512(randbytes(32)).hexdigest()
    # init
    def getGId(self):
        return self.__graphId
    def getNodeEdge(self, arg = 0):
        # 0 node & relay
        # 1 node
        # 2 relay
        if arg == 0:
            return self.__node, self.__edge
        elif arg == 1:
            return self.__node
        elif arg == 2:
            return self.__edge
    # info functions
    def addEdge(self, sN, dN, v = 0):
        # sN    source node
        # dN    destination node
        # v     relation value
        # d     direction (? is undirected, - directed)
        self.__node.append(sN)
        self.__node.append(dN)
        self.__edge.append((sN, dN, v))
    def readCSV(self, filename):
        csvdata = pd.read_csv('libs/comnetpr/CSV/'+str(filename), skipinitialspace = True)
        self.rawcsv = csvdata
        for i in range(len(csvdata)):
            self.addEdge(csvdata['sn'][i], csvdata['dn'][i], csvdata['v'][i])
    # input functions
    def convertAdjTable(self):
        adjset = set()
        for i in self.__edge:
            adjset.add(i[0])
            adjset.add(i[1])
        # taking total vertex
        self.vertextTable = pd.DataFrame(np.zeros((len(adjset),len(adjset))), dtype=int)
        self.edgeTable = pd.DataFrame(np.zeros((len(adjset),len(adjset))))
        srcs, dsts, vals = [], [], []
        for i in range(len(self.__edge)):
            srcs.append(self.__edge[i][0]-1)
            dsts.append(self.__edge[i][1]-1)
            vals.append(self.__edge[i][2])
        # decompositing source-destination nodes
        for i in range(len(self.__edge)):
            self.vertextTable[dsts[i]][srcs[i]] = 1
        # taking vertex data
        for i in range(len(self.__edge)):
            self.edgeTable[dsts[i]][srcs[i]] = vals[i]
        # taking edge data
        return (self.vertextTable, self.edgeTable)
    # convert
    def getGraph(self, ax):
        g = nx.from_pandas_edgelist(self.rawcsv, source='sn', target='dn', edge_attr='v')
        pos=nx.spring_layout(g) 
        nx.draw_networkx(g,pos, font_color='white', cmap='inferno', node_color='#1c1c1c', ax=ax)
        labels = nx.get_edge_attributes(g,'v')
        return nx.draw_networkx_edge_labels(g,pos, edge_labels=labels, ax=ax)
    # graphic
    
class RandomizedGraphCreator:
    pass