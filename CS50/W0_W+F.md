
# Week 0-W+F
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [Week 0-Wesday](#week-0-wesday)
 - [Binary](#binary)
 - [ASCII](#ascii)
 - [演算法](#演算法)
 - [Pseudocode](#pseudocode)
  - [Reference](#reference)
<!-- TOC END -->


<iframe width="560" height="315" src="https://www.youtube.com/embed/79gAss0K1TI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

* About Cs50:73% of CS50 students have no prior computer science experience! You’re not alone!

## Binary
*　電腦上是二進位制的方式儲存。0代表未通電、1代表通電。
*　使用多個組合擴大可能性-進位。
 *  一個數字:只有01兩種可能，兩個數字有4種可能。
 電腦計算時間是二近位，不是一般日常的10進位
 ![](https://i.imgur.com/PzqboIM.png)

## ASCII
有二進位，就可以用這些組合表示文字，可以表示文字，我們就可以利用電腦寄送email等等。
![](https://i.imgur.com/CePk538.png)

## 演算法

* 用電話簿查名字舉例:
 * 從第一頁開始找:n紅色
 * 從撕一半在找中間的一半。(二元搜尋的概念):log n綠色
![](https://i.imgur.com/NRw8Sa5.png)
當事情變的複雜，效率就十分重要，這就是`為什麼要有演算法的原因`。

## Pseudocode
<iframe width="560" height="315" src="https://www.youtube.com/embed/6hfOvs8pY1k" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
這個影片用 Pseudocode介紹演算法。

✍Pseudocode:偽代碼，常拿來說明程式碼、描述演算法。但不是真的存在的程式語言，甚至會用到自然語言。可以幫助人更好的敘述演算法，不用拘泥於具體的實作。
* [自己補充:如何寫Pseudocode](https://www.google.com/search?q=Pseudocode&rlz=1C1JZAP_zh-TWTW751TW751&oq=Pseudocode&aqs=chrome..69i57j0l7.699j0j4&sourceid=chrome&ie=UTF-8)

# 進入C的世界:
* code需要遵守語法
* hello word
```C
#include <stdio.h>
int  main （void ）
{
    printf （“ hello，world！\ n ” ）;
}
```
## [Scratch](https://scratch.mit.edu/)
![](https://i.imgur.com/ZmjgefF.png)
* Boolean expressions:True /False
* 滿足`Conditions`，使用if-eles。
*  `infinite loops`:無限迴圈
*  注意`threads program`的觀念。

### Reference
* https://www.youtube.com/watch?v=79gAss0K1TIhttp://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php
* http://cdn.cs50.net/2013/fall/lectures/0/w/week0w.pdf
* https://www.youtube.com/watch?&v=6hfOvs8pY1k
* https://www.youtube.com/watch?v=3ErTSVmQ9qo
* http://cdn.cs50.net/2013/fall/lectures/0/f/week0f.pdf
