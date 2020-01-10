
# Week3-Wednesday
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [Week3-Wednesday](#week3-wednesday)
 - [Searching](#searching)
- [排序](#排序)
  - [Bubble Sort](#bubble-sort)
  - [Selection Sort](#selection-sort)
  - [Insertion Sort](#insertion-sort)
- [複雜度符號:](#複雜度符號)
- [Reference](#reference)
<!-- TOC END -->


## Searching

* case:有7個有數字的門，想找到50這個數字，一個一個找，`在找到目標前，需要找了n步`的模式是 **linear algorithm**。
> ![](https://i.imgur.com/Yi9wQZC.png)
圖片來源:http://cdn.cs50.net/2013/fall/lectures/3/w/week3w.pdf

* 若已經知道`數字已經排序`:使用二元搜尋法找，複雜度為nlogn。
![](https://i.imgur.com/hPRgn0n.png)

> 圖片來源:[Youtube](https://www.youtube.com/watch?v=YxgI7ll4Xtg)

* 還有很多不同的複雜度:有些比現性的糟糕多了!!

![](https://i.imgur.com/CqteEE1.png)
> 圖片來源:[Youtube](https://www.youtube.com/watch?v=YxgI7ll4Xtg)https://www.youtube.com/watch?v=YxgI7ll4Xtg)


* 表面而言n^3很糟高，但靠靠近一點看，2^n增長速度更快，越短越少的資料反而花的時間比n^3久
![](https://i.imgur.com/urCnkwa.png)
> 圖片來源:[Youtube](https://www.youtube.com/watch?v=YxgI7ll4Xtg)

註:X軸(資料量)；Y軸(時間)。
# 排序
所以我們知道了排序有快慢之分，排序好的資料也可以讓我更快找到想要的資料，接下來是一些排序的方式。

### Bubble Sort
![](https://pic.pimg.tw/emn178/1352552991-3385741824.png)
> 圖片來源:https://emn178.pixnet.net/blog/post/93779892

氣泡排序法(Bubble Sort)是最容易理解和實作的一種排序演算法，也翻譯作冒泡排序法。
#### 運作流程如下：

1.比較相鄰的兩個元素，若前面的元素較大就進行交換。
2.重複進行1的動作直到最後面，最後一個元素將會是最大值。
3.重複進行1,2的動作，每次比較到上一輪的最後一個元素。
4.重複進行以上動作直到沒有元素需要比較。
#### 時間複雜度（Worst case）：O(n^2)
每次比較和n個需要n步，因此時間複雜度為n^2。

### Selection Sort
![](https://miro.medium.com/max/1536/1*MUEvL8qTjbRtz22PlTSXPA.jpeg)
>　圖片來源：https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E5%85%A5%E9%96%80-%E9%81%B8%E6%93%87%E6%8E%92%E5%BA%8F%E8%88%87%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F%E6%B3%95-23d4bc7085ff

#### 流程:
1. 找最小值:
從「未排序好的數字」中找到最小值
丟到左邊。
2. 把最小值丟到「未排序好的數字」的最左邊，把它標示成已排序好
3. 重複1、2，直到排好序

#### 時間複雜度（Worst case）：O(n^2)

1.找到最小值:（n+(n-1)+(n-2)+…+1)，我們可以得知總共的步驟數等於 n * (n+1) / 2 個步驟。
2.丟到最左邊:
每次找到最小數字時，每一個回合都只需要1步，總共n回，所以需n步。
3.綜合: n * (n+3) / 2，其時間複雜度我們還是會記為 O(n²)。

### Insertion Sort
![](https://pic4.zhimg.com/v2-73a86cc2703fab6745e3156d95d9ce03_b.gif)
> 圖片來源:https://zhuanlan.zhihu.com/p/36938540

####　課堂舉例：數列4261375
在檢查每個元素時，我們將其放置在左側較小列表中的正確位置。觀察：
```
 4 2 6 1 3 7 5
4  2 6 1 3 7 5
2 4  6 1 3 7 5
2 4 6  1 3 7 5
1 2 4 6  3 7 5
1 2 3 4 6  7 5
1 2 3 4 5 6  7
1 2 3 4 5 6 7
```
#### 流程(根據維基百科):
* 一般來說，都用in-place在陣列上實現。
1. 從[0]開始(可以認為已經被排序)
2. 取出下一個，在已排序的元素中`從後向前`檢查
3. 如果該元素（已排序）大於新元素，則把該元素移到下一位置
4. 重複步驟3，直到找到已排序的元素小於或者等於新元素的位置
5. 將新元素插入到該位置之後
6. 重複步驟2~5

#### 時間複雜度（Worst case）：O(n^2)
當資料的順序恰好為由大到小時，每次比較n個需要n步。

# 複雜度符號:
O:Worst Case下的時間複雜度
Ω :Best CAse下的空間複雜度
![](https://i.imgur.com/dTAk8zV.png)
> 圖片來源:[Youtube](https://www.youtube.com/watch?v=YxgI7ll4Xtg)

# Reference
* [Youtube](https://www.youtube.com/watch?v=YxgI7ll4Xtg)
* [Sildes](http://cdn.cs50.net/2013/fall/lectures/3/w/week3w.pdf)
* [Bubble Sort](https://emn178.pixnet.net/blog/post/93779892)
* [初學者學演算法｜排序法入門：選擇排序與插入排序法](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E5%85%A5%E9%96%80-%E9%81%B8%E6%93%87%E6%8E%92%E5%BA%8F%E8%88%87%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F%E6%B3%95-23d4bc7085ff)
* https://zh.wikipedia.org/zh-tw/%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F
* https://zh.wikipedia.org/wiki/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F
* https://zhuanlan.zhihu.com/p/36938540
