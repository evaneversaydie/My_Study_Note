# Binary Tree
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [Binary Tree](#binary-tree)
- [什麼是Tree?](#什麼是tree)
  - [樹的組成:](#樹的組成)
  - [注意:](#注意)
    - [森林](#森林)
- [二元樹的條件:](#二元樹的條件)
  - [應用](#應用)
- [參考資料](#參考資料)
<!-- TOC END -->


# 什麼是Tree?
> 若熟悉Linked List(連結串列)將會更容易理解樹：Linked list是一維的線性結構(不是往前、就是往後)，樹(與Graph)則推廣成多維的結構。
![](https://i.imgur.com/IrbmH9g.png)
連結各個node之間的連結(link)稱為edge，可能是單方向，或者雙向。

[Linked list筆記](https://github.com/evaneversaydie/My_Study_Note/blob/master/Week1_Linked%20list/Week1_Linked%20list.md)

> Tree(樹)是用以描述具有階層結構(hierarchical structure)的問題的首選，階層結構意味著明確的先後次序。

例如:檔案的目錄、大綱的重點。
## 樹的組成:
![](https://i.imgur.com/fch4LU6.png)
* 註:
  * siblings：擁有相同父節點的nodes。(藍色長方形處)
  * leaf:沒有子節點的節點。
  * root:最一開始的節點，只會有一個

## 注意:
*  不可以迴圈，否則樹不成立
*  樹沒有規定要有幾個小孩，弱化成linked list，也是一種樹。

### 森林
兩顆以上的樹
![](https://i.imgur.com/NzXGfE3.png)


#二元樹的條件:

* Binary Tree(二元樹)指的是每一個節點最多只有兩個小孩的樹。
* 每個節點只有left child和right child。

##應用
* BST
* Binary Space Partition
* Binary Tries
* Heaps
* Huffman Coding Tree
* DOM

# 參考資料
* [課堂簡報](https://docs.google.com/presentation/d/e/2PACX-1vSC3P8sGElP48mJTjqT309470SmTFBwJXWsU9hTX2hg5tVpiG4yC703qA7ibPep-Qakmm2Mw_F-ScZh/pub?start=false&loop=false&delayms=3000&slide=id.p)
* [Tree(樹): Intro(簡介)](http://alrightchiu.github.io/SecondRound/treeshu-introjian-jie.html)
* [Binary Tree: Intro(簡介)](http://alrightchiu.github.io/SecondRound/binary-tree-introjian-jie.html)
