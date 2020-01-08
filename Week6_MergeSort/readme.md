# MergeSort
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [MergeSort](#mergesort)
- [MerageSort是什麼?](#meragesort是什麼)
    - [流程圖:](#流程圖)
    - [HeapSort and MergeSort 比較](#heapsort-and-mergesort-比較)
    - [程式碼](#程式碼)
- [參考資料](#參考資料)
        - [Merge Sort](#merge-sort)
        - [隨機生成list](#隨機生成list)
        - [檢查隨意的結果是否已經sort](#檢查隨意的結果是否已經sort)
<!-- TOC END -->


# MerageSort是什麼?
Merage Sort是一種用分治法(大問題=>小問題=>解決小問題後就可以解決大問題)。
方法為:
1. `Divide`:把大list拆成小list(拆成len=1)
2. `Conquer`:把小list排序成中list，再把中list排序。
> Merge的大前提：若要由小數列合併出大數列，那麼各自的小數列必須「已經排好序」。
## 複雜度
* 最佳時間複雜度：O(nlog n)
* 平均時間複雜度：O(nlog n)
* 最差時間複雜度：O(nlog n)



## 流程圖:
![Mergesort](MergeSort.jpg)

## HeapSort and MergeSort 比較

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


## 程式碼
```Python
class Solution(object):    

    def Conquer(r,l):
        res =[]
#====================================================
        if len(r)==0:
            return l

        elif len(l)==0:
            return r
#====================================================        
        elif len(r)==1 and len(l) ==1 and r[0] > l[0]:
            res.append(l[0])
            res.append(r[0])
            return res
#====================================================
#排序:把r[0]、l[0]比較小的抓出來，剩下的再繼續排序

        elif l[0] < r[0]:
            res=[l[0]] + Solution.Conquer(l[1:], r)
            return res

        elif l[0] >= r[0]:
            res = [r[0]] + Solution.Conquer(l, r[1:])
            return res
#====================================================

    def Divide(nums):
        if len(nums)<=1:
            return nums
     ####### maximum recursion depth exceeded ##########
     #沒有設置遞迴的限制=>容易一直遞迴而沒有結果(無窮迴圈)
     ###################################################
        a = len(nums)//2
        left=nums[0:a]
        right=nums[a:]    
        r = Solution.Divide(left)
        l = Solution.Divide(right)
        ### 加一個:小問題都切好了開始排排站並合成大問題
        return Solution.Conquer(r,l)
    #######################################################\



    #把這兩個def併在作業規範中
    def merge_sort(self,nums):
        self.nums=nums #這樣才可以用Solution().merge_sort()呼叫!!!!
        if len(nums)<=1:
            return nums
        else:
            return Solution.Divide(nums)

```
亂數測試
```
a = [random.randint(0,1000) for _ in range(100)] # 生成長度為100的整型陣列,元素大小為(0,1000]
print(bool(Solution().merge_sort(a) == sorted(a)))
```


# 參考資料
* https://emn178.pixnet.net/blog/post/87965707
* [上課簡報](https://docs.google.com/presentation/d/e/2PACX-1vRAGwnUvg6BcXoML5u9f4gO6YKcz0vXf7bDnPho_S7mG5D0SBR78djt91RKUPMxqNfkVIcu3l5WCXPh/pub?start=false&loop=false&delayms=3000&slide=id.g478da15c12_0_0)
* [Github](https://github.com/evaneversaydie/My_Study_Note/tree/master/HW2)
### Merge Sort
* http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html
* [合併排序法 - 使用Python(Merge sort)](https://newaurora.pixnet.net/blog/post/224658923-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95---%E4%BD%BF%E7%94%A8python)
* [Merge Sort - 合併排序](https://algorithm.yuanbin.me/zh-tw/basics_sorting/merge_sort.html)
* [初學者學演算法｜排序法進階：合併排序法](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E9%80%B2%E9%9A%8E-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95-6252651c6f7e)
### 隨機生成list
* https://stackoverflow.com/questions/39379515/how-do-i-generate-a-random-list-in-python-with-duplicates-numbers
* https://stackoverflow.com/questions/3559337/how-to-generate-a-random-list-of-fixed-length-of-values-from-given-range

### 檢查隨意的結果是否已經sort
*  https://www.itread01.com/content/1550354967.html
