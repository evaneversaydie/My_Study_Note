
* Binary Tree(二元樹)指的是每一個節點最多只有兩個小孩。
* Binary Search Tree(二元搜尋樹)是一個每個節點左小孩都<節點本身，而右小孩都比節點還大。
* BST的最小值位置:從root開始一直往左邊找找找(中間都不可以往右邊找)，找到的節點就是整個BST的最小值。
* BST的最大值位置:從root開始一直往右邊找找找(中間都不可以往左邊找)，找到的節點就是整個BST的最小值。
* 應用:因為有規則可以搜尋，所以往往應用於資料庫中。其中BST適合「越亂越好」的資料(如果是sort好的資料去建BST的話容易產生worst case=>linked_list)
* 什麼是`pre-order`?
<br> 是一種遍訪tree的方式，先印出自己(root)再印左邊、右邊。不限於BST使用。

* 什麼是`深度優先`?
<br> 先往下尋找(每一個節點召到最深的地方再去找其他分支)，而不是像廣度優先一樣。
<br> 如圖:
![image](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_1.jpg)
