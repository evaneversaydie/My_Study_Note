# Week4-Monday
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [Week4-Monday](#week4-monday)
- [複習](#複習)
- [Merge Sort](#merge-sort)
- [Reference](#reference)
<!-- TOC END -->


# 複習
* 看看[這個動畫](https://www.toptal.com/developers/sorting-algorithms/random-initial-order)，複習之前的SORT!!
* 上次的三個排序:bubble sort, insertion sort, and selection sort是表現最差的三個！

# Merge Sort
原裡可以參考[之前上課的筆記](https://github.com/evaneversaydie/My_Study_Note/tree/master/Week6_MergeSort)
<br>簡述如下:<br>
Merage Sort是一種用分治法(大問題=>小問題=>解決小問題後就可以解決大問題)。 方法為:

* `Divide`:把大list拆成小list(拆成len=1)
* `Conquer`:把小list排序成中list，再把中list排序。
![Mergesort](https://github.com/evaneversaydie/My_Study_Note/blob/master/HW2/MergeSort.jpg?raw=true)
> Merge的大前提：若要由小數列合併出大數列，那麼各自的小數列必須「已經排好序」
## Pseudocode
```C
On input of n elements:
    If n < 2
        Return.
    Else:
        Sort left half of elements.
        Sort right half of elements.
        Merge sorted halves.
```

* 舉例
![](https://i.imgur.com/xsW888W.jpg)

* 複雜度舉例
![](https://i.imgur.com/Olg3n2z.png)

# Reference
* [Week4 Youtube](https://www.youtube.com/watch?v=8IZ9r5kmS3Y)
* [week4m.pdf](http://cdn.cs50.net/2013/fall/lectures/4/m/week4m.pdf)
* [之前上課的筆記](https://github.com/evaneversaydie/My_Study_Note/tree/master/Week6_MergeSort
