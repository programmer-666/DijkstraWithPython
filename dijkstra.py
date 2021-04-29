from libs.comnetpr.Graph import *
from libs.comnetpr.Algorithms import *
import pandas as pd
import matplotlib.pyplot as plt
from subprocess import call
import os, threading

graph = CreateGraph()
#graph.readCSV('graph1.csv')
graph.readCSV('internal.csv')

# Show Raw Edges And Vertex
dir = r'C:\Users\suhar\OneDrive\OMU\E2M2\ProgrammingComputerNetworks\Kodlar'
rc = call("start cmd /K " + "python djkg.py", cwd=dir, shell=True)
#

dijkstra = Dijkstra()
dijkstra.giveVexTable(graph.convertAdjTable()[0].values.tolist()) # Vertex Table
dijkstra.giveEdgTable(graph.convertAdjTable()[1].values.tolist()) # Edge Table

calcWay = dijkstra.findWay()
os.system('cls')

# Shortest Ways #
#shortestWaysTable = dijkstra.showEdgesDF()
#print('# Shortest Ways (Dataframe) #')
#print(shortestWaysTable)

calcWay = pd.DataFrame(calcWay, columns=['Source', 'Cost'])
pidTimes = pd.DataFrame(dijkstra.getTimes(), columns=['Times'])
pidTimes.insert(0, 'PID', [i+1 for i in range(len(dijkstra.getTimes()))])
calcWay.insert(1, 'Destination', [i+1 for i in range(len(calcWay['Source']))], True)
#

# Matplot
fig, ax = plt.subplots(nrows=1, ncols=2)
ax[1].title.set_text('Process Times')
ax[0].title.set_text('Distances To #1 Node')
pidTimes.plot(kind='line', x = 'PID', y = 'Times', ax=ax[1],colormap='cividis')
calcWay.plot(kind='line', x='Destination', y='Cost', ax=ax[0],colormap='viridis')
plt.show()
#
