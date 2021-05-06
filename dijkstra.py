from libs.comnetpr.Graph import *
from libs.comnetpr.Algorithms import *
import pandas as pd
import matplotlib.pyplot as plt
from subprocess import call
import os, threading
import networkx as nx

graph = CreateGraph()
graph.readCSV('graph1.csv')
#graph.readCSV('internal.csv')

# Show Raw Edges And Vertex
rc = call("start cmd /K " + "python djkg.py", shell=True)
#

dijkstra = Dijkstra()
dijkstra.giveEdgTable(graph.convertAdjTable()[1].values.tolist()) # Edge Table
dijkstra.giveVexTable(graph.convertAdjTable()[0].values.tolist()) # Vertex Table

calcWay = dijkstra.findWay()
os.system('cls')

# Shortest Ways #
shortestWaysTable = dijkstra.showEdgesDF()
print('# Shortest Ways (Dataframe) #')
print(shortestWaysTable, '\n')
for i in range(len(calcWay)):
    print(calcWay[i][0], i+1, calcWay[i][1])
djk_e = pd.DataFrame(dijkstra.getDEdges(), columns=['s', 'd', 'v'])
djk_e = pd.DataFrame({'s':djk_e['s']+1, 'd': djk_e['d']+1, 'v': djk_e['v']})
#

calcWay = pd.DataFrame(calcWay, columns=['Source', 'Cost'])
pidTimes = pd.DataFrame(dijkstra.getTimes(), columns=['Times'])
pidTimes.insert(0, 'PID', [i+1 for i in range(len(dijkstra.getTimes()))])
calcWay.insert(1, 'Destination', [i+1 for i in range(len(calcWay['Source']))], True)
#

# Networkx
def createDjkGraph(df, ax):
    g = nx.from_pandas_edgelist(df, source='s', target='d', edge_attr='v')
    pos=nx.spring_layout(g)
    nx.draw_networkx(g,pos, font_color='white', cmap='inferno', node_color='#1c1c1c')
    labels = nx.get_edge_attributes(g,'v')
    return nx.draw_networkx_edge_labels(g,pos, edge_labels=labels, ax=ax)
#

# Matplot
fig, ax = plt.subplots(nrows=1, ncols=4)
ax[3].title.set_text('Dijkstra')
ax[2].title.set_text('Graph')
ax[1].title.set_text('Process Times')
ax[0].title.set_text('Distances To #1 Node')
createDjkGraph(djk_e, ax = ax[3])
graph.getGraph(ax = ax[2])
pidTimes.plot(kind='line', x = 'PID', y = 'Times', ax=ax[1],colormap='cividis')
calcWay.plot(kind='line', x='Destination', y='Cost', ax=ax[0],colormap='viridis')
plt.show()
#