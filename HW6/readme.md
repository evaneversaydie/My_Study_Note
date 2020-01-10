# HW6
Dijkstra、Kruskal 實作
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [HW6](#hw6)
- [整理](#整理)
    - [🔸Dijkstra說明與Kruskal說明](#dijkstra說明與kruskal說明)
        - [Kruskal](#kruskal)
        - [Dijkstra](#dijkstra)
    - [🔸Dijkstra與Kruskal流程圖](#dijkstra與kruskal流程圖)
- [參考資料](#參考資料)
<!-- TOC END -->

- [HW6](#hw6)
<!-- TOC END -->
# 整理


## 🔸Dijkstra說明與Kruskal說明

###  Kruskal
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

### Dijkstra
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

## 🔸Dijkstra與Kruskal流程圖
* [Dijkstra 原圖請點這裡](https://i.imgur.com/ncA3StM.jpg)
* [Kruskal 原圖請點這裡](https://i.imgur.com/Jz6FJnC.jpg)
![](https://i.imgur.com/aD09ltG.png)
![](https://i.imgur.com/Jz6FJnC.jpg)

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
