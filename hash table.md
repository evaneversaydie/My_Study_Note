# Hash table
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [Hash table](#hash-table)
- [刷題實作](#刷題實作)
- [參考資料](#參考資料)
<!-- TOC END -->





>　Hash Table 是儲存 (key, value) 這種 mapping 關係的一種資料結構。[出處](https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/)

&emsp;&emsp;**<font color= '#CC543A'>Hash Table(雜湊表)</font>**是一種資料結構，以<font color= '#CC543A'>key</font>透過**Hash function**得到f(k)，而f(k)指的是資料存在記憶體對位置(常常有人說這是一個桶子)。
![img](https://raw.githubusercontent.com/evaneversaydie/My_Study_Note/master/_img/Hash%20explain_small.jpg)
&emsp;&emsp;相比於二元搜尋樹的搜尋方式，Hash Table的資料結構使我們可以直接透過key直接查到資料，而不用經過比大小等等的程序。

#### 神奇而關鍵的 Hash function
&emsp;&emsp;依據定義，key 和 f(key)是一種***函數關係***。每一個key都獨一無二且只能對應到一個值f(k)。Hash Function是由key得到 f(key)的函式。Hash Function把每一個原始資料的順序打亂並儲存，並且發給每一個key的身分證字號`f(key)`(雜湊值)。
<br>&emsp;&emsp;然而，依序加入k1、k2兩個key，(即使機率很低但仍有可能發生)重複發了一樣的兩個身分證字號(f(k1)=f(k2))，此時就發生了<font color= '#CC543A'>碰撞</font>。要經過特別的處理，以免要查k1，但f(k1)找到的值可能被取代為k2的資料。
方法有以下:
* 1.重複的f(k)用linked list 的方式把資料存在f(k).next。
* 2.若f(k)+1為空值，直接把重複的資料存在f(k)+1的位置若無則遞迴。
* 3.更改成更好的Hash function。

<br>&emsp;&emsp;一個良好的hash Function，可以有效率地把每一個key分到不重覆的位置，且碰撞發生的機率極小，在Hash Table中，Hash Function很常用來作為分配資料儲存的位置或適用於搜尋。除了使查詢更有效率。更可以用來做以下的應用:
<br>* 確保傳遞真實的資訊、錯誤校正 : 因為碰撞機率很小很小，所以可以在發送資料A時將f(A)一起傳送，如果收到的資料B之f(B)!!=f(A)代表資料經過修改或資料有誤。
##### Hash Table的性質
* 主要操作：新增、刪除、修改值、搜尋已知的鍵
    * 優點:容易搜尋。\n",
    * 缺點:不擅於時間序列(Stack可能更好)、排序困難
    * 應用:搜尋引擎、加密、區塊鍊。

#### 如何用Hash Table實現加密呢?
>實作的思路大概是：當要把資料放到雜湊表時，先給定一個 key 和存放的 value，並將 key 的每個字元轉換成 ASCII Code 或 Unicode Code 並相加，這個相加的值即是 hash 鍵值，在 table 陣列上對應到存放的 value
# 刷題實作
[leetcode|705. Design HashSet](https://leetcode.com/problems/design-hashset/)
```python
class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket=[None]*100

    def add(self, key: int) -> None:
        g = key%100
        if self.bucket[g]==None:
            self.bucket[g]=[]
            self.bucket[g].append(key)
            # self.bucket[g].sorted()
        elif key not in self.bucket[g]:
            self.bucket[g].append(key)

    def remove(self, key: int) -> None:
        g = key%100
        if self.bucket[g]==None:
            return
        elif key in self.bucket[g]:
            self.bucket[g].remove(key)


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        g = key%100
        if self.bucket[g]==None:
            return False
        elif key in self.bucket[g]:
            return True
        elif key not in self.bucket[g]:
            return False

        # Your MyHashSet object will be instantiated and called as such:
        # obj = MyHashSet()
        # obj.add(key)
        # obj.remove(key)
        # param_3 = obj.contains(key)
```
![](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/leetcode705res.jpg?raw=true)


# 參考資料
- [圖解資料結構:使用python 吳燦銘著9-15_]()
- [演算法圖鑑]()
- [蔡芸琤老師資料結構與演算法](https://www.youtube.com/watch?v=oqzStHk36PI&feature=youtu.be)
- [TechBridge 技術共筆部落格](https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/)
- [用 JavaScript 學習資料結構和演算法：字典（Dictionary）和雜湊表（Hash Table）篇](https://blog.kdchang.cc/2016/09/23/javascript-data-structure-algorithm-dictionary-hash-table/)
- [設計高效能的Hash Table（一）](https://medium.com/@fchern/%E8%A8%AD%E8%A8%88%E9%AB%98%E6%95%88%E8%83%BD%E7%9A%84hash-table-%E4%B8%80-303d9713abab)
-[以Python實作資料結構](https://super9.space/archives/1105)
- [資料結構雜湊(Hash)](https://ithelp.ithome.com.tw/articles/10208884)
- [維基百科](https://zh.wikipedia.org/wiki/%E5%93%88%E5%B8%8C%E8%A1%A8)
- [用 JavaScript 學習資料結構和演算法：字典（Dictionary）和雜湊表（Hash Table）篇](https://blog.kdchang.cc/2016/09/23/javascript-data-structure-algorithm-dictionary-hash-table/)
- [雜湊函式](https://zh.wikipedia.org/wiki/%E6%95%A3%E5%88%97%E5%87%BD%E6%95%B8)
