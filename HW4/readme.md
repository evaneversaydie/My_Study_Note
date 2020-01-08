# Hw4
Hash Table實作
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [Hw4](#hw4)
- [小整理](#小整理)
- [🔸HashTable說明](#hashtable說明)
                - [這次Hash Table+MD5作業我們要怎麼做?](#這次hash-tablemd5作業我們要怎麼做)
- [🔸流程圖](#流程圖)
- [🔸參考資料](#參考資料)
<!-- TOC END -->

# 小整理
#  🔸HashTable說明

>　Hash Table 是儲存 (key, value) 這種 mapping 關係的一種資料結構。[出處](https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/)


**<font color= '#CC543A'>Hash Table(雜湊表)</font>**是一種資料結構，以<font color= '#CC543A'>key</font>透過**Hash function**得到f(k)，而f(k)指的是資料存在記憶體對位置(常常有人說這是一個桶子)。相比於二元搜尋樹的搜尋方式，Hash Table的資料結構使我們可以直接透過key直接查到資料，而不用經過比大小等等的程序。
![img](https://raw.githubusercontent.com/evaneversaydie/My_Study_Note/master/_img/Hash%20explain_small.jpg)
#### 神奇而關鍵的 Hash function
依據定義，key 和 f(key)是一種***函數關係***，每一個key都獨一無二且只能對應到一個值f(k)。而Hash Function是處理由key 得到 f(key)的函式。Hash Function把每一個原始資料的順序打亂並儲存，並且發給每一個key的身分證字號`f(key)`(雜湊值)。
然而，依序加入k1、k2兩個key，即使機率很低但仍有可能發生重複發了一樣的兩個身分證字號(發生f(k1)=f(k2))，此時就發生了<font color= '#CC543A'>碰撞</font>。要經過特別的處理，以免要查k1，但f(k1)找到的值可能被取代為k2的資料。
方法有以下:
* 1.重複的f(k)用linked list 的方式把資料存在f(k).next。
* 2.若f(k)+1為空值，直接把重複的資料存在f(k)+1的位置若無則遞迴。
* 3.更改成更好的Hash function。
一個良好的hash Function，可以有效率地把每一個key分到不重覆的位置，且碰撞發生的機率極小，在Hash Table中，Hash Function很常用來作為分配資料儲存的位置或適用於搜尋。除了使查詢更有效率。更可以用來做以下的應用:
* 確保傳遞真實的資訊、錯誤校正 : 因為碰撞機率很小很小，所以可以在發送資料A時將f(A)一起傳送，如果收到的資料B之f(B)!!=f(A)代表資料經過修改或資料有誤。
##### Hash Table的性質
* 主要操作：新增、刪除、修改值、搜尋已知的鍵
    * 優點:容易搜尋。
    * 缺點:不擅於時間序列(Stack可能更好)、排序困難
    * 應用:搜尋引擎、加密、區塊鍊。



#### 如何用Hash Table實現加密呢?

>實作的思路大概是：當要把資料放到雜湊表時，先給定一個 key 和存放的 value，並將 key 的每個字元轉換成 ASCII Code 或 Unicode Code 並相加，這個相加的值即是 hash 鍵值，在 table 陣列上對應到存放的 value。

結合數學與密碼學->每個經過更改的資料都會變成唯一且差異很大的值

### 這次Hash Table+MD5作業我們要怎麼做?
<br>「給予一個字串，將他們用下列的形式『分班』。」
<br>    製造n個桶子=>建Array、用Hash function以utf-8編碼轉成數字並用f(k)/n的餘數來放到bucket裡面。
* 採用助教的測資
* 使用規定的utf-8編碼，轉成10進位。【md5套件】
* 利用linked list 處理衝突。
<br>「新增後可以找到這修字串在哪裡、也可以刪除他們。」
<br>功能:新增修改與查詢
#  🔸流程圖
[原圖請點這邊](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/Hash%20explain_flow.jpg?raw=true)
![img](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/Hash%20explain_flow.jpg?raw=true)

#  🔸參考資料
- [上課簡報與作業規範](https://docs.google.com/presentation/d/e/2PACX-1vT1HO9Nl475k2bR0l1x8_Tr4V5Wzx0BEqp9bpmHckvj8kTeJehhYVlOJUDVPhLQm6kjGCJ_sLMSBUw5/pub?start=false&loop=false&delayms=3000&slide=id.g7565e27c53_0_38)
- [蔡芸琤老師資料結構與演算法](https://www.youtube.com/watch?v=oqzStHk36PI&feature=youtu.be)
- Hash Table
    - [TechBridge 技術共筆部落格](https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/)
    - [用 JavaScript 學習資料結構和演算法：字典（Dictionary）和雜湊表（Hash Table）篇](https://blog.kdchang.cc/2016/09/23/javascript-data-structure-algorithm-dictionary-hash-table/)
    - [設計高效能的Hash Table（一）](https://medium.com/@fchern/%E8%A8%AD%E8%A8%88%E9%AB%98%E6%95%88%E8%83%BD%E7%9A%84hash-table-%E4%B8%80-303d9713abab)
    -[以Python實作資料結構](https://super9.space/archives/1105)
    - [資料結構雜湊(Hash)](https://ithelp.ithome.com.tw/articles/10208884)
    - [維基百科](https://zh.wikipedia.org/wiki/%E5%93%88%E5%B8%8C%E8%A1%A8)
    - [用 JavaScript 學習資料結構和演算法：字典（Dictionary）和雜湊表（Hash Table）篇](https://blog.kdchang.cc/2016/09/23/javascript-data-structure-algorithm-dictionary-hash-table/)
    - [雜湊函式](https://zh.wikipedia.org/wiki/%E6%95%A3%E5%88%97%E5%87%BD%E6%95%B8)

- [流程圖圖片](https://github.com/evaneversaydie/My_Study_Note/blob/master/_img/Hash%20explain_flow.jpg?raw=true)
- [圖片](https://raw.githubusercontent.com/evaneversaydie/My_Study_Note/master/_img/Hash%20explain_small.jpg)
