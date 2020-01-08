# Binary Search Tree
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [Binary Search Tree](#binary-search-tree)
- [關於 Binary Search Tree](#關於-binary-search-tree)
 - [尋值](#尋值)
 - [應用:](#應用)
 - [什麼是`pre-order`、`深度優先搜尋`?](#什麼是pre-order深度優先搜尋)
- [示意圖](#示意圖)
- [參考資料](#參考資料)
<!-- TOC END -->


# 關於 Binary Search Tree
* Binary Tree(二元樹)指的是每一個節點最多只有兩個小孩。
* Binary Search Tree(二元搜尋樹)是一個每個節點左小孩都<節點本身，而右小孩都比節點還大。
## 尋值
* BST的最小值位置:從root開始一直往左邊找找找(中間都不可以往右邊找)，找到的節點就是整個BST的最小值。
* BST的最大值位置:從root開始一直往右邊找找找(中間都不可以往左邊找)，找到的節點就是整個BST的最小值。
## 應用:
因為有規則可以搜尋，所以往往應用於資料庫中。其中BST適合「越亂越好」的資料(如果是sort好的資料去建BST的話容易產生worst case=>linked_list)
## 什麼是`pre-order`、`深度優先搜尋`?
<br> `pre-order`是一種遍訪tree的方式，先印出自己(root)再印左邊、右邊。不限於BST使用。
<br> 如圖:

![image](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_1.jpg?raw=true)
[圖片沒有正常顯示請點此處看原圖>~<](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_1.jpg)
<br>深度優先搜尋是先往下尋找(每一個節點找到最深的地方再去找其他分支)
<br>圖片中紅筆的方向仕紳度優先。廣度優先搜尋則是綠色的方向。使用哪一種搜尋法，則在這個方向的節點將被優先搜尋到。

# 示意圖
![HW3_BST_flow.jpg](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_BST_flow.jpg?raw=true)

# 參考資料
###### tree:

* [演算法圖鑑](https://www.books.com.tw/products/0010771263)
* [What is the worse-case time complexity for a binary search tree for searching?](https://www.quora.com/What-is-the-worse-case-time-complexity-for-a-binary-search-tree-for-searching)
* [二元搜尋樹](https://zh.wikipedia.org/zh-tw/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9)
* [Binary Tree](http://www.csie.ntnu.edu.tw/~u91029/BinaryTree.html)
* [How to Implement a Binary Search Tree in Python
](https://medium.com/@stephenagrice/how-to-implement-a-binary-search-tree-in-python-e1cdba29c533)
* [BinarySearchTree.py on github](https://github.com/joeyajames/Python/blob/master/Trees/BinarySearchTree.py)
* [Binary Search Tree library in Python](https://www.laurentluce.com/posts/binary-search-tree-library-in-python/)
###### python 物件:
* ['物件導向程式設計'](https://kaochenlong.com/2011/10/13/python-oop/)
* [positional argument vs keyword argument](https://blog.csdn.net/lanchunhui/article/details/50039769)
* [Python，你到底是在__底線__什麼啦！](https://aji.tw/python%E4%BD%A0%E5%88%B0%E5%BA%95%E6%98%AF%E5%9C%A8__%E5%BA%95%E7%B7%9A__%E4%BB%80%E9%BA%BC%E5%95%A6/)
###### 印出tree:(最後用pycharm debug)
* ['Python nltk -- Tree'](http://cpmarkchang.logdown.com/posts/184948-python-nltk-tree)
* ['python 按圖形列印二叉樹'](https://www.itread01.com/content/1547977526.html)

###### markdown:
* [如何使用 Markdown 來撰寫 Docs](https://docs.microsoft.com/zh-tw/contribute/how-to-write-use-markdown)

###### 自己的流程圖圖片
* [pre-order、深度優先搜尋](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_1.jpg)
- [流程圖原圖](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_BST_flow.jpg)-
- [流程圖手繪部分search](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_3.jpg?raw=true)
- [流程圖手繪部分delete](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_5.jpg?raw=true)
- [流程圖手繪部分modify](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_4.jpg?raw=true)
