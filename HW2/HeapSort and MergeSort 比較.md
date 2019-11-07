

|      | Merge Sort  | Heap Sort |
| ------------  | ----  | ---  |
|  |   | |
|  時間複雜度 |||
|   best case | O(NlogN)   |O(NlogN)   | 
| average case    |O(NlogN)   |O(NlogN) | 
| worst case	   |O(NlogN)  |O(NlogN) |
|  |   | |
| 空間複雜度 | O(n)  |  Ο(1)   | 
|  |   | |
| 穩定度 | 比較好   |  比較不好  | 

* 不論原本的排序為何，兩個演算法都會將其跑過一遍再排序，因此在時間上都是O(NlogN)
* Merge Sort 需要額外的記憶體來儲存分割出的小list，空間複雜度為O(N)；Heap Sort無須額外記憶體空間(in-place)，因此時間複雜度是O(1)
* Heap Sort因為依賴樹的結構需要迭代較多次比較不穩定，Merage Sort則是分割至最小的元素再合併排序，幾乎不會發生位至調換的問提比較穩定。
 

# 參考資料:
* [演算法 排序演算法的穩定性](https://www.itread01.com/content/1543897622.html)
* [判斷各種排序演算法的穩定性](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/548443/#outline__1)
