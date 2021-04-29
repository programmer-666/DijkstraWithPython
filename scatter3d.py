from libs.comnetpr.Graph import *
from libs.comnetpr.Graph import *
from libs.comnetpr.Algorithms import *
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import matplotlib.pyplot as plt

graph = CreateGraph()
graph.readCSV('graph1.csv')
#graph.readCSV('internal.csv')

df = pd.DataFrame(graph.getNodeEdge()[1], columns=['Source', 'Destination', 'Cost'])

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.title.set_text('Source-Destination-Cost 3D')

x = df['Source']
y = df['Destination']
z = df['Cost']

ax.scatter(x, y, z)
ax.set_xlabel("Source")
ax.set_ylabel("Destination")
ax.set_zlabel("Cost")

plt.show()