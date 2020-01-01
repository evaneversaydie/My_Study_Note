#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import defaultdict 

#Class to represent a graph 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices  #節點個數
#         self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.graph = [[0 for column in range(vertices)]
            for row in range(vertices)]
        self.edges = [] #邊的資訊儲存
        self.INFINITY = 65536 # Dijkstra:設定無限大的值
    def addEdge(self,u,v,w): 
        self.graph[u][v] = self.graph[v][u] = w
        #建立資料，因為是無像圖對稱矩陣

    def Dijkstra(self, s):
        cost = [self.INFINITY if i is not s else 0 for i in range(self.V)]
        #如果i不是起點，先記為無限大。i-i==0
        labelled = [False for i in range(self.V)]
        for i in range(self.V):
            next = self.__getMinCost(cost, labelled)
            if next >= 0:
#                 print(next)
                self.__update(next, cost, labelled)
        return {str(v): cost[v] for v in range(self.V)}

    def __getMinCost(self, cost, labelled):
        minCost = self.INFINITY
        minCostNode = -1
        for v in range(self.V):
            if not labelled[v]:
                if cost[v] < minCost:
                    minCost = cost[v]
                    minCostNode = v
        return minCostNode

    def __update(self, next, cost, labelled):
        labelled[next] = True
        for v in range(self.V):
            if not labelled[v] and self.graph[next][v] > 0:
                newCost = cost[next] + self.graph[next][v]
                if cost[v] > newCost:
                    cost[v] = newCost

                    
#     -----------------------------------------------------------------------------------------------------------------                

    def Kruskal(self):
        """
        :rtype: dict
        """
        edges = []
        for i in range(self.V):
            for j in range(i+1, self.V):
                if self.graph[i][j] != 0:
                    edges.append([i, j, self.graph[i][j]])
        edges.sort(key=lambda x: x[2]) #依照權重排序

        result = []
        rootArray = [-1 for x in range(self.V)]
        for i in range(len(edges)):
            fromNode, toNode, cost = edges[i]
            fromRoot = self.__findRoot(fromNode, rootArray) #起點來子哪個爸爸
            toRoot = self.__findRoot(toNode, rootArray) #終點來自哪個爸爸
            if fromRoot != toRoot: 
                result.append(edges[i])
                if rootArray[fromRoot] <= rootArray[toRoot]:
                    rootArray[toRoot] = fromRoot  #更改父節點為 邊的起點
#                     print('v;',rootArray)
                else:
                    print('e;',rootArray)
#                     print(toRoot)
#                     print(rootArray[toRoot])
                    rootArray[fromRoot] = toRoot #更改父節點為 邊的起點
                if len(result) >= self.V - 1:
                    break
#         print(rootArray)
        return {'{0}-{1}'.format(r[0], r[1]): r[2] for r in result}

    def __findRoot(self, node, rootArray):
        while rootArray[node] >= 0:
            node = rootArray[node]
        return node

