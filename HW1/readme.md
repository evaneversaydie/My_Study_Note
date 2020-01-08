# 簡介:
本次作業為QuickSort 實作。
<br>`Quick_Sort - 學習歷程助教請看`:主要程式碼的書寫歷程與心得。
<br>`Quicksort_06170128`:與助教討論後的程式碼檔案。
<br>其他為留圖原始製作檔與流程圖片

# 小整理:
##流程圖
![QuickSort](QuickSort.jpg)
![QuickSort2](QickSort2.jpg)
![QuickSort](Quicksort_d.jpg)
## 關於Quick_Sort的時間複雜度:Time Complexities
* 最好的情形:O(Nlog(N))
    * 即使全部都由小到大，最少仍會需要全部跑一次才可以確定
* 平均起來: O(Nlog(N))
* 最壞的情形: O(N^2)
    * 指定到的pivot都為該次排序的最大或最小值。
    * 若都是已經排序好的資料(像是一元樹)。
