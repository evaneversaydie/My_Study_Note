# 🔸Dijkstra說明與Kruskal說明
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [🔸Dijkstra說明與Kruskal說明](#dijkstra說明與kruskal說明)
    - [Kruskal](#kruskal)
    - [Dijkstra](#dijkstra)
- [🔸Dijkstra與Kruskal流程圖](#dijkstra與kruskal流程圖)
- [程式碼](#程式碼)
- [參考資料](#參考資料)
<!-- TOC END -->


##  Kruskal
* 以邊為紀錄主體的演算法。
* Greedy。
* 圖需要符合:
    * 「連通圖」:圖上任一點一定有路可以到其他點。
* 原理:
    * 圖裡有n個點，依序紀錄邊(起終點與權重)。
    * 起初每個點都視為獨立的tree。
    * 依照權重由小至大依序加入邊，連接起各個節點，並使其中之一的點為parent。
    * 加入邊的條件是tree一定要成立，不能有loop。
    * 會一直到加入的邊數為(節點數-1)為止。
    * PS:如果有兩個不相連的樹，則成為森林。最後演算法完成後就止會有一棵孤獨的樹。
* 需要紀錄:
    * 邊、起始點、終點、權重。
    * 所有點的父節點是誰:可以止極的自己的父節點，但會在搜尋上影響效能與記憶體，將所有父節點直接記為root，就是「壓縮」。
    <br>(如圖:這張圖計算完的路徑如下，左邊的樹是止記錄自己的爸爸是誰，右邊為壓縮的)
        * ![](https://i.imgur.com/EYIu6F2.png)
## Dijkstra
> 「最短路徑」不見得是邊最少、點最少的路徑。
* 尋找最短路徑的演算法之一。
* lebal setting(一定要全部算完才能有答案)
* 圖需要符合:
    * 「權重(不能為負)」。
* 原理:
    * 只紀錄目前沒有走訪過、且離根最近的點其「起點到該點的最短路徑」。
    * 為已經判定的點貼上「路徑長度」標籤。
    * 每一個階段都會產生一個標記已經被setting的點，setting的點是該次為被seting的節點中，與根最短的距離(即流程圖被藍筆圈出來的部分，有數!=有labelled)。
    * 未開始之前，所有點與起點的最短路徑為「無限大」。
    * 若沒有labelled點會走訪到重覆的節點，則會計算目前路徑的距離，如果這次計算的路徑L<先前的路徑l則會把l取代為L，確保最短路徑。
    * 會計算很多很多次路徑，但最後只會紀錄跟節點樹一樣的資訊。
    * PS:Dijkstra是一種窮舉的方式，如果說一張圖裡面B非起點，A-B有兩種走法:A-B、A-C-B兩種，假設A-B已經是最短路徑， Dijkstra仍會跑過A-C-B，比較兩種路徑的質材可以確定最短路徑。

* 需要紀錄:
     * 路徑資訊。
     * 起點A到任一點的最短路徑。(迭代更新)
     * 已經labelled的點。

# 🔸Dijkstra與Kruskal流程圖
* [Dijkstra 原圖請點這裡](https://i.imgur.com/ncA3StM.jpg)
* [Kruskal 原圖請點這裡](https://i.imgur.com/Jz6FJnC.jpg)
![](https://i.imgur.com/aD09ltG.png)
![](https://i.imgur.com/Jz6FJnC.jpg)

# 程式碼
```Python
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
```

# 參考資料
* Homewrok
    * [Homework example](https://colab.research.google.com/notebooks/welcome.ipynb#recent=true)
    * [PPT in Class](https://docs.google.com/presentation/d/e/2PACX-1vTgHO5AkHJS6iN6bnnBMMdHv6E4rabnrC0KwyTRfjad8Ab3IQjbnGvZuQOjDC9t7nKqeroiwcuasJrI/pub?start=false&loop=false&delayms=3000&slide=id.g7b9afdb0e7_0_9)
* Minimum Spanning Tree:
    * [Minimum Spanning Tree：Intro(簡介)
](http://alrightchiu.github.io/SecondRound/minimum-spanning-treeintrojian-jie.html)
    * [Minimum Spanning Tree：Kruskal's Algorithm](http://alrightchiu.github.io/SecondRound/minimum-spanning-treekruskals-algorithm.html)
* Dijkstra
* [演算法筆記](http://www.csie.ntnu.edu.tw/~u91029/Path.html)


* [Dijkstra 原圖請點這裡](https://i.imgur.com/ncA3StM.jpg)
* [Kruskal 原圖請點這裡](https://i.imgur.com/Jz6FJnC.jpg)
* [壓縮](https://i.imgur.com/EYIu6F2.png)

* [如何使用 Python 進行字串格式化](https://blog.techbridge.cc/2019/05/03/how-to-use-python-string-format-method/)
