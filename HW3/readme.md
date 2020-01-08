# HW3
Binary Search Tree 實作
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [HW3](#hw3)
  - [繳交檔案](#繳交檔案)
<!-- TOC END -->


##繳交檔案
* `功能說明`:程式中每個def的功能
* `binary_search_tree_06170128`:完成的程式碼。
* `My_Study_Note`:程式碼撰寫歷程。

## 小整理

* Binary Tree(二元樹)指的是每一個節點最多只有兩個小孩。
* Binary Search Tree(二元搜尋樹)是一個每個節點左小孩都<節點本身，而右小孩都比節點還大。
* BST的最小值位置:從root開始一直往左邊找找找(中間都不可以往右邊找)，找到的節點就是整個BST的最小值。
* BST的最大值位置:從root開始一直往右邊找找找(中間都不可以往左邊找)，找到的節點就是整個BST的最小值。
* 應用:因為有規則可以搜尋，所以往往應用於資料庫中。其中BST適合「越亂越好」的資料(如果是sort好的資料去建BST的話容易產生worst case=>linked_list)
* 什麼是`pre-order`、`深度優先搜尋`?
<br> `pre-order`是一種遍訪tree的方式，先印出自己(root)再印左邊、右邊。不限於BST使用。
<br> 如圖:

![image](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_1.jpg?raw=true)
[圖片沒有正常顯示請點此處看原圖>~<](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_1.jpg)
<br>深度優先搜尋是先往下尋找(每一個節點找到最深的地方再去找其他分支)
<br>圖片中紅筆的方向仕紳度優先。廣度優先搜尋則是綠色的方向。使用哪一種搜尋法，則在這個方向的節點將被優先搜尋到。
# 學習總結
這次作業沒有跟之前sort一樣可以用print直接印出arrays看看程式運行狀況跟自己想的一不一樣，一開始也想找找網路上有沒有人有可以把樹圖像化的方式，後來重新用debug mode。

這次作業用了debug mode，可以更了解程式是怎麼跑的(像是再insert裡面有TreeNode(val)會跑到Class TreeNode(object)建一個物件、if child_count == 某個數字也是)這些過程有些是跟自己的時候想不一樣。無窮迴圈也因為debug mode才找出來哪裡錯了。有些錯誤更需要知道程式是怎麼跑的才可以避免(ex:'local variable XXXXXX referenced before assignment')
題目的return type，TreeNode()是一組位置(這個物件在記憶體的什麼地方......等等)!=TreeNode.val。
感覺比較能體會老師說的「資料結構與演算法更是一個概念，而作業是將這個概念實際寫出來」的感覺。


# 流程圖
delete、modify放上的是思考的一個case，以此表示並出程式會怎麼處理的流程✍
- [流程圖原圖(沒有縮小)請點這裡](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_BST_flow.jpg?raw=true)-
- [流程圖手繪部分search不清楚請點這裡](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_3.jpg?raw=true)
- [流程圖手繪部分delete不清楚請點這裡](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_5.jpg?raw=true)
- [流程圖手繪部分modify不清楚請點這裡](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_4.jpg?raw=true)
![HW3_BST_flow.jpg](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/HW3_BST_flow.jpg?raw=true)
