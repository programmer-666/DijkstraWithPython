from libs.comnetpr.Graph import *
from libs.comnetpr.Graph import *
from libs.comnetpr.Algorithms import *
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import matplotlib.pyplot as plt
import os, threading

# Thread
class Thread2(threading.Thread):
    def run(self):
        os.system('python scatter3d.py')
# 

graph = CreateGraph()
graph.readCSV('graph1.csv')
#graph.readCSV('internal.csv')

print('# Vertex Table #')
print(graph.convertAdjTable()[0]) # Vertex Table
print('\n\n# Edge Table #')
print(graph.convertAdjTable()[1]) # Edge Table

pdFr = pd.DataFrame(graph.getNodeEdge()[1], columns=['Source', 'Destination', 'Cost'])
edges = pd.DataFrame(graph.getNodeEdge(1)).value_counts().values.tolist()
x,y = [],[]
for i in range(len(edges)):
    x.append(i+1)
    y.append(edges[i])
edp = pd.DataFrame(x)
edp[1] = pd.DataFrame(y)

# Matplot
fig, ax = plt.subplots(nrows=1, ncols=2)
# Subplot
ax[0].title.set_text('Source-Destination-Cost')
pdFr.plot.scatter(x = 'Source', y = 'Destination', c = 'Cost', colormap='viridis', ax=ax[0]) # sources-destinations-costs
# Scatter
ax[1].title.set_text('Connection Counts Of Nodes')
edp.plot(kind = 'bar', x = 0, y = 1,ax=ax[1]) # nodes connection counts
# Line
sc3th = Thread2()
sc3th.start()
# 3D Scatter
plt.show()
#