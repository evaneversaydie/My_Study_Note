#Hw5
BFS DFS 實作
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [Hw5](#hw5)
- [小整理](#小整理)
    - [🔸BFS說明、DFS說明](#bfs說明dfs說明)
        - [圖的定義:](#圖的定義)
        - [為什麼要有走訪?](#為什麼要有走訪)
        - [BFS&BFS](#bfsbfs)
    - [🔸BFS、DFS流程圖、原理比較](#bfsdfs流程圖原理比較)
        - [BFS、DFS流程圖](#bfsdfs流程圖)
    - [比較](#比較)
- [🔸參考資料](#參考資料)
<!-- TOC END -->
# 小整理

## 🔸BFS說明、DFS說明
深度優先搜尋(DFS)與廣度優先搜尋(BFS)這兩種搜尋法，作用在於圖的「走訪」(traversal)。
> 走訪是從圖的某一個點開始拜訪其餘的點，且每一個點都址拜訪一次的過程。

### 圖的定義:
<br>是由`邊(edge)`和`點(vertex)`組成的，會注重點雨點之間的連接關係，像是`單向`或`雙向`。
圖的組成十分自由與多樣，樹也是一種圖，其中若兩個圖的點與其連接關係一樣，則會稱為`「同構」`。
簡單整理一下圖會怎麼表現點雨點之間的聯接關係:
* Edge List:記錄所有點與點之間的邊。
    * `adjacency matrix`:一個矩陣，用來紀錄兩個點是否有連接。
    <br>舉例:第(0,1)個內容代表編號0、1這兩個點是否聯接。紀錄的內容可能是邊的權重，也可能是邊的個數。
    ***注意:因為有有像圖，所以不一定是對稱矩陣。***
    * `adjacency lists` :可能是一個linked list 或是 dictionary 等等的資料結構。主要是紀錄(某個點A=>所有跟點A有聯接的點)。

### 為什麼要有走訪?
由於圖的結構較為多變複雜，走訪可以確保我們以有效率的方式拜訪每個節點、確認全部截點的內容且沒有遺漏。同時，也因為圖允許「loop」，走訪的演算法必須避開「訪問相同的點」、「陷入loop」的問題。

### BFS&BFS
<br>&emsp;&emsp;而BFS與DFS就是其中的演算法。其不同點在於走訪順序不同，但皆可以完成走訪。
以樹舉例，深度優先搜尋(DFS)是紅色的蠟筆的部分，而廣度優先搜尋(BFS)是綠色的蠟筆。
* DFS:走訪的順序會以起點碰到的「子節點及其小孩」一直走下去，直到沒有小孩才繼續走訪起點的其他子節點。
* BFS:走訪的順序會以起點可以碰到的「所有子節點」為優先，再找「起點的子節點會碰到的所有小孩走訪」。
樹的走訪，起點通常是root，子節點就是相鄰的點。圖則可以指定任意起點。(圖就需要注意有沒有loop，但只拜訪沒有拜訪過的點就可以解決)。
![image](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_1.jpg?raw=true)


<br>
<br>
BFS、DFS很相似，唯一比較大的差別是拜訪的順序。
***BFS、DFS實作需要的工具:***
* Adjency list
* 儲存找到但還沒拜訪的資料。
* 要記得剪枝:記下有拜訪過的點。

在找資料的時候看到一個很可愛的比喻:<font color=#9E7A7A>DFS像是走迷宮，一直搜尋直到沒有退路在回到起點。BFS像是多拉A夢的大雄眼鏡掉了在找眼鏡，會從近的地方開始找，找不到才找遠的地方。</font>
* DFS=>使用Stack=>迷宮中往往前一步，看到新的路就先拜訪，直到遇到死路=>比較後面看到的比較先拜訪
* BFS =>使用QUEUE=>四周看到先拜訪，先看到的先拿出來

BFS時，我們將起點放進去Queue，拜訪了起點(把起點刪掉放到拜訪過的紀錄中)，再把臨邊表的點放到Queue中，先拜訪先看到的點(依照林邊表順序)......直到沒有點可以拜訪。加入林邊表的數據時，要檢查有沒有拜訪過。
<br>
DFS時，我們將起點放進去Stack，拜訪了起點(把起點刪掉)，再把臨邊表的點放到Stack中，先拜訪最後看到的點(依照林邊表順序)......直到沒有點可以拜訪。加入臨邊表的數據時，要檢查有沒有拜訪過。

## 🔸BFS、DFS流程圖、原理比較

### BFS、DFS流程圖
[原圖請點這裡](https://i.imgur.com/L7SOBsx.jpg)
![](https://i.imgur.com/L7SOBsx.jpg)

## 比較
複雜度會依據有沒有適用遞迴、是使用Adjency List還是矩陣有所差異。
以下為使用Adjency list 的複雜度:


|項目|BFS|DFS|備註|
|---|---|---|---|
|走訪|以同一深度為優先()|以可以走到最深路徑為優先||
|最差時間複雜度|O(v+e)|O(v+e)|1.找完全部點與邊<br>2.使用矩陣O(V^2)) <br>3.例外:稀疏圖(點多邊少)、密集圖(邊多點少)的複雜度偏重點或編的數量|
|最佳時間複雜度	|O(1)|O(1)|一找就中|
|平均時間複雜度	|O(v+e)|O(v+e)||
|最差時間複雜度	|O(v+e)|O(v+e)||
|實作|Stack|Queue||
|應用|路徑的邊的數量(轉機問題)|走迷宮、拓樸排序、路徑的權重和|

# 🔸參考資料
* PowerPoints in class:
    * [PowerPoints in class](https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.g7aa022d8bc_2_5)

* My Code and Notes:
    * [My Queue](https://github.com/evaneversaydie/My_Study_Note/blob/master/leetcode/232%20Implement%20Queue%20using%20Stacks.md)
    * [My Stack](https://github.com/evaneversaydie/My_Study_Note/blob/master/leetcode/155.%20Min%20Stack.md)

* How to use defaultdict?
    * [collections雜談之一 ——— dict的key值存不存在乾我屁事](https://ithelp.ithome.com.tw/articles/10193094)
    * [python中defaultdict和dict的區別與使用](https://www.itread01.com/content/1544414054.html)
* BFS & DFS
    * [Graph Traversal Algorithm](https://www.javatpoint.com/breadth-first-search-algorithm)
    * [My Github:HW3](https://github.com/evaneversaydie/My_Study_Note/blob/master/HW3/My_Study.ipynb)
    * 大話資料結構
    * [Graph](http://www.csie.ntnu.edu.tw/~u91029/Graph.html)
    * [BFS和DFS算法原理（通俗易懂版](https://blog.csdn.net/u011437229/article/details/53188837)
    * [公開簡報](http://billor.chsh.chc.edu.tw/train/BFS&DFS.pptx)
    * [圖的遍歷：DFS和BFS演算法](https://www.itread01.com/content/1549388200.html)
    * [圖的廣度優先搜索遍歷的時間複雜度是多少？](https://www.quora.com/What-is-the-time-complexity-of-Breadth-First-Search-Traversal-of-a-graph)
* My picture
    * [flow chart](https://i.imgur.com/DMt7xix.jpg)
    * [bug :flow chart](https://i.imgur.com/L7SOBsx.jpg)
    * [BFS VS DFS](https://i.imgur.com/yNtOtOp.png)
