# Quick Sort
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [Quick Sort](#quick-sort)
- [流程](#流程)
- [關於Quick_Sort的時間複雜度:Time Complexities](#關於quick_sort的時間複雜度time-complexities)
- [實作:對QuickSort的想法:](#實作對quicksort的想法)
    - [第一版](#第一版)
    - [第二個:初步的想法](#第二個初步的想法)
- [參考資料:](#參考資料)
<!-- TOC END -->
![QuickSort](https://github.com/evaneversaydie/My_Study_Note/blob/master/HW1/QuickSort.jpg)

# 流程
1. 在數列中任選一個元素(通常為最左邊或最右邊的元素)作為pivot。
2. 然後調整數列，使「所有<pivot之元素」在pivot 左邊，而「>pivot，在pivot右邊」。
3. 將所有在pivot左邊、右邊的數看成「兩個獨立新的數列」，重複上述1、2(選pivot、調整數列)，直到分不出「新的數列最多只有一個元素」。
4. 回傳所有數裂

# 關於Quick_Sort的時間複雜度:Time Complexities
* 最好的情形:O(Nlog(N))
    * 即使全部都由小到大，最少仍會需要全部跑一次才可以確定
* 平均起來: O(Nlog(N))
* 最壞的情形: O(N^2)
    * 指定到的pivot都為該次排序的最大或最小值。
    * 若都是已經排序好的資料(像是一元樹)
* 是穩定的。

# 實作:對QuickSort的想法:
## 第一版
> 在輸入的list中隨機指定一個pivot(本次作業pivot為[::-1])，並依據pivot之值，將list分為:
 * 所有元素之值都大於pivot的list_r或皆小於pivot的list_l。list_r、list_l裡面元素暫未排序。
 * 回傳的值:list_r+pivot+list_l
     * 可以試著額外宣告一個list來回傳。
     * 或直接用tuple將元素換位置。
 * 將1ist_l、list_r視為list，重複指定pivot來排序大小，直到分出來的list為null停止。

#### 上課後和助教討論:
不要看網路上的參考資料，用自己的想法與理解直接打成程式碼。
* 可以將quicksort步驟拆解，如:`PARTITION`獨立成一個function


## 第二個:初步的想法
所以先把小於指定值的pivot存在一個list，反之亦然。用while包起來，最後把所有list加起來。
* 不能只用samll或big。
* 想成遞迴就是對small 和big 再做一次，如果len()值=1才停止，每個框框都是一次的Quciksort。

*  示意圖:
![QuickSort](https://github.com/evaneversaydie/My_Study_Note/blob/master/HW1/QuickSort.jpg)
![QuickSort2](https://github.com/evaneversaydie/My_Study_Note/blob/master/HW1/QickSort2.jpg尸)

# 參考資料:
* http://alrightchiu.github.io/SecondRound/comparison-sort-quick-sortkuai-su-pai-xu-fa.html
* http://notepad.yehyeh.net/Content/Algorithm/Sort/Quick/Quick.php
* https://emn178.pixnet.net/blog/post/88613503-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95(quick-sort)
* https://github.com/evaneversaydie/My_Study_Note/tree/master/HW1
