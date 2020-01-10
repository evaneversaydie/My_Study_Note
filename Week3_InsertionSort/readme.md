# Insertion Sort
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [Insertion Sort](#insertion-sort)
- [關於Insertion Sort](#關於insertion-sort)
- [示意圖](#示意圖)
- [時間複雜度](#時間複雜度)
- [參考資料](#參考資料)
<!-- TOC END -->


# 關於Insertion Sort
* 通常不使用額外的空間存已排序的步方，都是使用In-place完成。
 * Array左邊:已排序的部分。
 * Array右邊:沒排序的部分。
* 流程：
1. 將「沒排序部分」最左邊元素儲存到變數A中。(第一個元素也可以視為已經排序)
2. `由後往前`和「已排序部分」元素B比較。
 * 若「B>自己」，則將B往右邊移。
3. 重複2，直到遇到「<=自己」的元素C，將A放在C之後的位置；若都沒有則C，則A會在最Array前面。
4. 重複直到「沒排序部分」為null。
# 示意圖
![](https://zh.wikipedia.org/wiki/File:Insertion-sort-example-300px.gif)
> 圖片來源:https://zh.wikipedia.org/wiki/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F

# 時間複雜度
* 最佳時間複雜度：O(n)
* 平均時間複雜度：O(n^2)
* 最差時間複雜度：O(n^2)
* 空間複雜度：O(1)
* Stable

# 參考資料
* https://emn178.pixnet.net/blog/post/93791164
* https://zh.wikipedia.org/wiki/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F
