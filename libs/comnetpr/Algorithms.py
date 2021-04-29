import pandas as pd
import timeit
class Dijkstra:
    def __init__(self):
        self.vad = [[0 for i in range(2)]] # visited, distance
        # 1.value -> indicates if the node has been visited
        # 2.value -> distance/cost from source
    def next(self):
        # finds nodes not visited
        self.m = -32 # min
        for i in range(self.vexlen):
            # choosing node with shortest way
            if (self.vad[i][0] == 0) and (self.m < 0 or self.vad[i][1] <= self.vad[self.m][1]):
                self.m = i
        return self.m
    def giveVexTable(self, vext):
        self.vextable = vext;self.vexlen = len(self.vextable[0])
    def giveEdgTable(self, edg):
        self.edgtable = edg;self.edglen = len(self.edgtable[0])
    def findWay(self):
        self.times = []
        vexs, nxtt, ng, nds, self.dEdges = [], [], [], [], []
        i = 0
        while i < self.vexlen-1:
            self.vad.append([0, 10**10])
            i = i + 1
        f = 0
        for vertex in range(self.vexlen):
            self.times.append([timeit.default_timer()]) # timer start
            nxt = self.next() # finding the next node
            nxtt.append(nxt)
            vexs.append(vertex)
            for nghi in range(self.vexlen):
                # calculation of distance for unvisited nodes
                if (self.vad[nghi][0] == 0) and (self.vextable[nxt][nghi] == 1):
                    ng.append(nghi)
                    # update neighbor's distance if distance is available
                    nt = self.vad[nxt][1] + self.edgtable[nxt][nghi]
                    nds.append(nt)
                    #print(nxt,ndist)
                    # if the newly calculated value is greater
                    if self.vad[nghi][1] > nt:
                        self.vad[nghi][1] = nt
                        self.dEdges.append([nxt,nghi,nt]) # dijkstra edges
            self.vad[nxt][0] = 1 # visit the previously located node
            self.times[f].append(timeit.default_timer()) # timer stop
            f = f+1
        self.nxtt = nxtt
        self.ng = ng
        self.nds = nds
        self.vexs = vexs
        return self.vad
        self.clearData()
    def getDEdges(self):
        return self.dEdges
    def getTimes(self):
        tms = []
        for i in self.times:
            tms.append(i[1]-i[0])
        return tms
    def clearData(self):
        self.vad = [[0 for i in range(2)]]
        self.m = -32
        self.nxtt = []
        self.ng = []
        self.nds = []
    # Special Show Stage Functions
    def findSubListLen(self, dedges):
        r = []
        for i in dedges:
            r.append(i[0]+1)
            slstl = max(r) # sub list len
        return slstl  
    def createMainlist(self, dedges):
        mlst = [[] for i in range(self.findSubListLen(self.getDEdges()))]
        for i in self.getDEdges():
            mlst[i[0]].append(i)
        return mlst
    def sortEdges(self):
        ml = self.createMainlist(self.getDEdges())
        l = []
        x = []
        for i in ml:
            for j in i:
                l.append(j)
            x.append(pd.DataFrame(l))
            l = []
        return x
    def getSubRowCount(self):
        p = []
        x = self.sortEdges()
        for i in x: # get sub pandas row count
            lst = i.values.tolist()
            for j in lst:
                p.append(pd.DataFrame([j]))
        return p
    def findCopyCount(self):
        r = 0
        rl = []
        p = self.getSubRowCount()
        for i in p: # find copy count
            for j in p:
                if i[1][0] == j[0][0]:
                    r+=1
            rl.append(r)
            r = 0    
        return rl
    def copyData(self):
        p = self.getSubRowCount()
        rl = self.findCopyCount()
        for i in range(len(rl)): # copying data
            for j in range(rl[i]):
                    p[i] = p[i].append([p[i]], ignore_index=True)
        return p
    def combineSimilars(self):
        s = []
        ss = []
        a = None
        p = self.copyData() 
        for i in range(len(p)):
            if i == 0:
                a = p[i][0][0]
                s.append(p[i])
                continue
            if a == p[i][0][0]:
                s.append(p[i])
            else:
                if len(s) > 0:
                    ss.append(pd.concat(s, ignore_index=True))
                    a = p[i][0][0]
                    s = []
                    s.append(p[i])
                    continue
        ss.append(p[len(p)-1])
        return ss
    def showEdgesDF(self):
        # this function is static, configure before using
        newp = self.combineSimilars()
        for i in newp:
            i.rename(columns={0:'s', 1:'d', 2:'c'}, inplace=True)
        newp[1].index = [2,3]
        newp[2].index = [5]
        newp[3].index = [7]
        edgedf = pd.concat([newp[0],pd.concat([newp[1], newp[2], newp[3]], axis=0)], axis=1 )
        return edgedf
    #
