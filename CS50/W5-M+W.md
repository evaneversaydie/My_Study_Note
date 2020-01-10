# Week5-M+W
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [Week5-M+](#week5-m)
- [Memory](#memory)
 - [Stack](#stack)
 - [Heap](#heap)
- [compiling](#compiling)
 - [圖片的儲存:](#圖片的儲存)
- [Reference](#reference)
<!-- TOC END -->





# Memory
![](https://i.imgur.com/ZD8uHfD.png)
> 圖片來源:[Cs50 Youtube1](https://www.youtube.com/watch?v=IEuvKVjw2oM)

* Top:輸入的程式碼(是一串分割的文字、用01存起來)
* Below: initialized data、 uninitialized data 、global variables

## Stack
* 就像是自助餐裡堆疊的盤子。
* 堆疊
* 儲存:區域變數、函式的參數與函式的位址等等。
* 由系統管理，必須在
Compile時知道個數、大小。
* 應用:
 * 存var和value。
 * 電腦的RAM。
 * 讓CPU更好的管理空間。
 * 例子:
 ![](https://i.imgur.com/uxvIaXu.png)
當我們寫程式時，def就像Stack一樣。Swap()中有a,b,c三個var就會如同圖片中下方的示意圖一樣。
![](https://i.imgur.com/oGbJQ9N.png)

<br>課程中還有許多記憶體分配的例子，但強調的一點是:
***程式的撰寫，就在分配記憶體。***
#### Stack Overflow
![](https://i.imgur.com/S5reycq.png)
> 圖片來源:http://cdn.cs50.net/2013/fall/lectures/5/m/week5m.pdf

惡意攻擊:如果輸入了過多的資料，超過原本指定的記憶體空間，就會發生Overflow。因為覆蓋了原本紀錄位置的記憶體，所以只程式無法指向main。很多惡意攻擊，就是利用這一點將指向mian的位置換成不安全的、惡意程式的位置。



## Heap
* 堆積。
* 責進行回收。
* 配置:malloc或是new。
* 主要是用在
Compile時`還不知道大小或個數的變數`。

![](https://i.imgur.com/sji4wPi.png)
![](https://i.imgur.com/L47cGvG.png)




#compiling
 "Compiling" 實際包含了四的步驟:
 * pre-processing
 * compiling
 * assembling
 * linking
 ![](https://i.imgur.com/R7eNyp1.png)
> 圖片來源:http://cdn.cs50.net/2013/fall/lectures/5/m/week5m.pdf

## 圖片的儲存:
* BMP是其中一種儲存方式。可能使用0為黑色，使用1為白色的方式存黑白的圖片。
* JPEG等更複雜的格式存儲0和1。



# Reference
* [Cs50 Youtube1](https://www.youtube.com/watch?v=IEuvKVjw2oM)
* [Cs50 Youtube2](http://www.youtube.com/watch?v=atBMLJdSKBo)
* [Sildes1](http://cdn.cs50.net/2013/fall/lectures/5/m/week5m.pdf)
* [Sildes2](http://www.youtube.com/watch?v=atBMLJdSKBo)
* [三種記憶體區間: global、stack、heap](http://wp.mlab.tw/?p=312)
