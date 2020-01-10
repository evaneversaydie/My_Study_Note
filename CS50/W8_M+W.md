# WEEK8 M+D
# 前言
Arrays一開始很好用，但為了動態的決定尺寸，我們介紹了linked list;因為Linked list 的特性是遍訪，我們採用了Hash Table;因為Hash Table的碰撞，我們用了Trise，而Trise又犧牲了許多空間。到底哪個最好?
> No clear winner,but just sunjective Design decisions.



![](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/1.jpg?raw=true)
> 圖片來源:https://docs.google.com/presentation/d/e/2PACX-1vQ1hb79im0vqpApCttGnXAFRT8SqH9HQP0b_oyVRCV8SVyiHLkHJjidYGAfxkvq468QMumFIDdTeiB-/pub?start=false&loop=false&delayms=3000&slide=id.g5ff860a9a8_0_5

# Stack
* 是一種`LIFO(Last in Frist out)後進先出`的資料結構。
* 可以想像像是堆盤子一般。
* 基本的動作:
 * push:把資料增加到Stack中。
  * Push it onto the top of the stack.
 * pop:把最top的資料拿出來。
  * Pop it off the top of the stack
 * size、data的參數。
 ![](https://i.imgur.com/t9R8hnP.png)
 >  圖片來源:https://www.youtube.com/watch?v=9qvt6MwBKZQ

* 實作時，使用linked List可以解決Array長度固定的問題。

* 應用:
 * 管理程式的記憶體:local var
 * 操作系統
 * 上一頁。
 * 對於驗證html的樹狀結構很有用。


# Queues
* 是一種`FIFO(First in Frist out)後進先出`的資料結構
* 想像成排隊的人潮。
* 基本的動作:
 * enqueue(尾巴進入排隊)
 * dequeue(離開隊伍)\

* size、data、font的參數
![](https://i.imgur.com/OIgM78j.png)
> 圖片來源:https://www.youtube.com/watch?v=9qvt6MwBKZQ

* 應用
 * DFS

# Trees
![](https://i.imgur.com/q8SVidq.png)
> 圖片來源:https://www.youtube.com/watch?v=9qvt6MwBKZQ

 * `Trie`這種資料結構就是一種特殊的tree。
 * 至少有一個節點。一個節點為`根(root)`。
 * 每個節點都可以有0個以上的`小孩(child)`。
  * 0個節點的是`葉子(leaf)`。

 *

# Binary Search Trees
* Tree 的一種。
* 限制每個節點最多只有2個child
* 特性:
每個left child存在(非NULL)，裡面的資料會<節點本身; 每個right child(非NULL)存在，裡面的資料會>節點本身。

* 圖片中左邊為BST，不論新增修改刪除，都需要符合BST的性質。
![](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_2.jpg?raw=true)
> 圖片來源:(HW3) https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_2.jpg?raw=true

* 應用:html提供節構。
* DOM:文件物件模型
![](https://i.imgur.com/mTb6AQy.png)
>圖片來源: https://ithelp.ithome.com.tw/articles/10202689

# Reference
* https://www.youtube.com/watch?v=9qvt6MwBKZQ
* http://cdn.cs50.net/2013/fall/lectures/8/m/week8m.pdf
* https://www.youtube.com/watch?v=ihmHDZKOkA8
* http://cdn.cs50.net/2013/fall/lectures/8/w/week8w.pdf
* [DOM](https://ithelp.ithome.com.tw/articles/10202689)
