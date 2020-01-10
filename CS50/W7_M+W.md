# Wee7_M+W
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [Wee7_M+W](#wee7_mw)
- [儲存的裝置](#儲存的裝置)
- [前提:Arrays](#前提arrays)
- [解決方式:Linked List](#解決方式linked-list)
- [解決方式:Hash Table](#解決方式hash-table)
 - [Linear Probing](#linear-probing)
 - [Separate Chaining](#separate-chaining)
- [解決方式:Tries](#解決方式tries)
- [第八堂的補充](#第八堂的補充)
- [Reference](#reference)
<!-- TOC END -->


# 儲存的裝置
* Hard Drives:金屬的圓盤和金屬接頭(magnetic head)組成。HD硬碟不是SSD。HD的圓型盤子是會轉動的。
![](https://images-na.ssl-images-amazon.com/images/I/81NMDyQw-0L._AC_SX466_.jpg)
>來源:https://www.amazon.com/Seagate-Barracuda-ST5000DM000-3-5-Inch-Internal/dp/B00KIVMRWU

* Floppy Disks(磁片):功能上而言和HD硬碟很相似，現在已經被淘汰(能存的枯間太小了)。
<br>時代的眼淚
![](https://images-na.ssl-images-amazon.com/images/I/41P0JwP7c5L._AC_.jpg)
>  來源:https://www.amazon.com/Double-Density-MF2-DD-Diskettes-Formatted/dp/B006NNGZ9S


# 前提:Arrays
* 把資料存儲在連續記憶體空間中。
* 缺點:
 * 大小固定。
 * 不容以在中間插入資料。
  * 必須複製Array，分配記憶體，將所有元素向右移動。


解決Array`固定大小`這個性質所產生的問題，可以用的資料結構:

# 解決方式:Linked List


![](https://i.imgur.com/HcjLwft.png)
> 圖片來源:http://cdn.cs50.net/2013/fall/lectures/7/w/week7w.pdf

* 方式:
 * **不使用連續記憶體哭間** :只要可以將資料連在一起就好。
 * **因此可以很自由的使用記憶體空間，把散落的記憶體物盡其用XD**
* 結構:
 * `data`:想存的資料。
 * `pointer`:指向下一個資料。最後一個資料pionter是空的。
* 常見的操作:
 * insert(插入)
 * delete(刪除)
 * search(搜索)
 * traverse(遍訪)

 <br>更多的可以看之前的[github筆記](https://github.com/evaneversaydie/My_Study_Note/blob/master/Week1_Linked%20list/Week1_Linked%20list.md)。

# 解決方式:Hash Table
之前hash table的筆記哩，has table的定義與注意事項:
> **Hash Table(雜湊表)** 是一種資料結構，以key透過**Hash function**得到f(k)，而f(k)指的是資料存在記憶體對位置(常常有人說這是一個桶子)。

> ![img](https://raw.githubusercontent.com/evaneversaydie/My_Study_Note/master/_img/Hash%20explain_small.jpg)同樣的，Hash Table的資料結構使我們可以直接透過key直接查到資料，而不用經過比大小等等的程序。在Hash Table中，Hash Function很常用來作為分配資料儲存的位置或適用於搜尋。
    ##### Hash Table的性質
    * 主要操作：新增、刪除、修改值、搜尋已知的鍵
    * 優點:容易搜尋。\n",
    * 缺點:不擅於時間序列(Stack可能更好)、排序困難
    * 應用:搜尋引擎、加密、區塊鍊。

* 中文是雜湊表、哈希表。
* 透過像是電話簿目錄的方式，查詢資料，解決array要一個一個找的問題，時間複雜度是O(1)。
* 而如果hash Function將資料分配到已經有值的位置，就是`衝突`。
以下是ＣＳ５０介紹的處理碰撞的方式：

## Linear Probing
想放的位置有資料了，就放在裡想放的位置最近的一個ＮＵＬＬ的位置。但這個方式最壞可能必是須拜訪Array裡面所有元素才能找到想找的資料。因此運行的時間很有可能orst Case變成線性的。
![](https://tutorialspoint.dev/image/Linear-Probing-1-1.jpg)
> 圖片來源:https://tutorialspoint.dev/data-structure/hashing-data-structure/implementing-hash-table-open-addressing-linear-probing-cpp

## Separate Chaining
![img](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/Hash%20explain_flow.jpg?raw=true)

類似功課中的Hash TAble 處理碰撞的方法，使用linked list 翻散碰撞。
*　Worat Case:遍歷HASH table的整個Linked list。如果我們認為有m個bucket時間複雜度是O（n ⁄ m）。右因為m是常數，因此是O（n）。
<br> ** 為什麼要擔心碰撞?
因為太常發生了!! **





# 解決方式:Tries
解決了Hash Table的碰撞問題。
![](https://i.imgur.com/9DVsgSK.png)
> https://www.youtube.com/watch?v=QWnZpgZKOoc

圖片中每個長方形都是A-z，從ROOT的M往A找，可以讀到MALxwell，三角形代表結束或是字串間的空白。

* 也稱為:特里樹、數字樹或、前綴樹
* 是Search Tree，一種有序的樹
* 每個節點是一個Array
* 時間複雜度：O（k）=>O(1)
 * 新增搜索都不受到已經存儲的元素影響。
  * 如:在trie中存儲了n個元素，想加入值Alex，還是一樣只需要4個步驟(每個字母一個)。
* 優點:
 * 沒有衝突。
 * 不需要HASH FUCTION
 * 便於查詢。
* 缺點:
 * 有時候比HASH TABLE需要更多的儲存空間。

# 第八堂的補充
 Arrays一開始很好用，但為了動態的決定尺寸，我們介紹了linked list;因為Linked list 的特性是遍訪，我們採用了Hash Table;因為Hash Table的碰撞，我們用了Trise，而Trise又犧牲了許多空間。到底哪個最好?
 > No clear winner,but just sunjective Design decisions.

# Reference
* http://cdn.cs50.net/2013/fall/lectures/7/m/week7m.pdf
* http://cdn.cs50.net/2013/fall/lectures/7/w/week7w.pdf
* https://www.youtube.com/watch?v=RUAsmwYC2mc
* https://www.youtube.com/watch?v=QWnZpgZKOoc
* https://tutorialspoint.dev/data-structure/hashing-data-structure/implementing-hash-table-open-addressing-linear-probing-cpp
* https://en.wikipedia.org/wiki/Trie
* http://www.csie.ntnu.edu.tw/~u91029/String.html
