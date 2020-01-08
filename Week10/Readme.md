# 紅黑樹
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [紅黑樹](#紅黑樹)
- [為什麼要有紅黑樹?](#為什麼要有紅黑樹)
- [紅黑樹規則](#紅黑樹規則)
- [影片](#影片)
- [紅黑樹如何平衡?](#紅黑樹如何平衡)
 - [用旋轉平衡:](#用旋轉平衡)
- [helper:網頁](#helper網頁)
- [參考資料:](#參考資料)
<!-- TOC END -->


# 為什麼要有紅黑樹?
* Binary Search Tree在新增、修改、刪除後，容易退化成不利搜尋的 linked list。
* 紅黑樹的優點在於每次新增後，都會平衡樹的結構，維持最短的樹高。
# 紅黑樹規則
* 是BST
* 每個節點是紅或黑
* 根必為色
* 節點為紅色，子節點必為黑色
* 節點是黑色，子節點可紅可黑
* 每個null的節點都是黑色
* 根到葉子的每條路徑，黑色的節點必為相同數目




# 影片
[參考影片](https://www.youtube.com/watch?v=4WjwmHeKa1Q)
![](https://i.imgur.com/jNSM2Or.png)
# 紅黑樹如何平衡?
* 最低限度的修改:改變顏色。
## 用旋轉平衡:
旋轉節點時，必須維持BST的性質。
  #### RR:新增的點在出問題的節點的右邊的右邊▶左旋
![](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/RR.gif?raw=true)
 #### LL:新增的點在出問題的節點的左邊的左邊▶右旋
![](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/LL.gif?raw=true)
 #### RL:新增的點在出問題的節點的右邊的左邊▶右旋再左旋
![](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/RL.gif?raw=true)
 #### LR:新增的點在出問題的節點的左邊的右邊▶左旋再右旋
![](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/LR.gif?raw=true)
# helper:網頁
[Red/Black Tree](https://www.cs.usfca.edu/~galles/visualization/RedBlack.html)
# 參考資料:
* [課堂簡報](https://docs.google.com/presentation/d/e/2PACX-1vRxyJRARq0BNuGJq_o2cUHIXBWrRSZrAOyXOSt9qCTSjQtyp8XqFq3VuNn3gCt3sXenOZmWLqIjcyFs/pub?start=false&loop=false&delayms=3000&slide=id.p)
* [參考影片](https://www.youtube.com/watch?v=4WjwmHeKa1Q)
