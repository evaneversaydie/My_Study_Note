# HeapSort
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [HeapSort](#heapsort)
- [關於Heap Sort](#關於heap-sort)
    - [什麼是Heap?](#什麼是heap)
    - [關於Heap sort:](#關於heap-sort-1)
- [設計Heap Sort的想法:](#設計heap-sort的想法)
- [流程圖:](#流程圖)
- [heap 程式碼](#heap-程式碼)
    - [補充](#補充)
- [參考資料:](#參考資料)
<!-- TOC END -->


上課摘要
--
> 演算法注重的是average和 worst_case的情況。

除了優缺點，我們要思考與評估的是:平均而言會花多少時間?遇到最差的情況又會是多少?適不適用目前的情形?時間成本可不可以負擔?

# 關於Heap Sort


## 什麼是Heap?
![](https://i.imgur.com/iAoDsiu.jpg)
* min heap:root一定是最大的
* max heap:root一定是最小的

## 關於Heap sort:
* HeapSort是一種lineked list 變形
* 也是tree 的特例
* 是一種`Complete Tree`，除了最下面的那一層以外，一定要填滿滿的。會先填左邊的子節點再填右邊的。所以只有最下層的右邊可以有空缺。
* 可以用array來顯示tree。
* 有`Max Heap`和`Min Heap`兩種:
 * Max heap: root一定比葉子大，子樹也是一樣類推下去(父節點>小孩)。
 * Min heap: root一定比葉子小，子樹也是一樣類推下去(父節點<小孩)。
* 試法將冊資形成Max Heap 或 Min Heap。因為只要一旦形成符合Max heap 或 Min heap 的結構。我們就可以移除root，並將最下層最右邊的節點移至root，並再次排成Heap Sort並繼續取出root，如此即可完成排序。其中這種將節點移置root的並再次將結構轉為Heapsort的過程稱為`sift-down`。

# 設計Heap Sort的想法:

例子:test = [3,7,24,0,-1,99,7.1,80,30]

1. 在HeapSort 裡面，需要的步驟:
 * 排成max heap或min heap。
 * 把ROOT和heap裡最後一個元素對調。(root這個值從這棵樹裡面消失了，繼續對其他沒有刪掉的元素做Heap Sort)

2. 用list的index 來對照各元素在tree的位置。
        這邊想了比較久，用tree可以畫出來排序過程但在想怎麼用程式寫的時候卡住了。尤其是怎麼知道誰是誰誰的父節點、知道一個節點之後怎麼知道他的小孩是哪兩個人。



   * 因為python 從索引從0開始。
   * 對任一索引值i而言:
       * 找到父節點:
           * 奇數:i//2
           * 偶數:i//2-1
           ->同一個父節點的節點索引值(奇數、偶數)只差1，可以化簡為:(i-1)//2
       * 找到左邊的小孩:2*i+1
       * 找到右邊的小孩:2*i+2

       對每一個節點而言，左邊小孩是奇數，右邊小孩都是偶數。
       <br>先這樣子找找找就把胎們變成max heap。
       1. heap_sort(self, nums):作業呼叫格式。
           <br>
       2. max_heap(nums):把nums變成max heap結構。
           <br>可能需要之前打的找爸爸和找小孩的function。
       3. swap(nums):把root和沒有排好的最尾巴的元素對調。
           <br>像是這樣子(|後面是排好的root)
           <br>
           <br>[O,O,O,O,O,O,O|]
           <br>[O,O,O,O,O,O|,O]
           <br>[O,O,O,O,O|,O,O]
           <br>_ _ _ _ _ _ ^插入到這裡
           <br>
           <br>想要用之前一直想不懂的in-place版本QAQ，因為root的index是[0]所以可能需要用到1個變數(暫訂place):
               <br>用來記得現在到底要交換的元素的位置(|前面的數字)

       <br>有點像這樣子:2->3->2->3......直到place==1->排好了

 4. max heap:去參考網路的程式程式碼，整理出以下邏輯:
像是用分治法一樣，先切成最小的問題=>只有兩層且全滿的樹:

 * 紀錄father、r、l哪一個最大，將最大的和father交換。
 * 由下而上的去檢查(由list後往前)=>可以用for迴圈
　*　新增一個let_max_heap()來實現（採用倒序的方式完成）
# 流程圖:![](https://github.com/evaneversaydie/My_Study_Note/blob/master/HW2/HeapSort.jpg?raw=true)
# heap 程式碼

```Python
class Solution(object):
    def heap_sort(self, nums):
        self.nums=nums
        return Solution.swap(nums)


    def max_heap(nums):
        for i in range((len(nums)-1)//2,-1,-1):
            Solution.let_max_heap(nums,i)
        return nums
    #倒敘排成max heap


    def let_max_heap(nums,i):
        root = i
        r= 2*i+1
        l= 2*(i+1)
        #刪掉到找子節點的def改成宣告
        if r<len(nums) and nums[r] > nums[root]:  
            nums[root],nums[r]=nums[r],nums[root]
            Solution.let_max_heap(nums,r)
        if l<len(nums) and nums[l] > nums[root]:
            nums[root],nums[l]=nums[l],nums[root]
            Solution.let_max_heap(nums,l)
        #改成不用max()，葉子大於跟就交換
        return(nums)



    def swap(nums):
        place=len(nums)
        while place>0:
            if nums[0:place]==Solution.max_heap(nums[:place]):
                #符合maxheap且place>=1(不用作nums[0],nums[0]交換)
                nums[0],nums[place-1]=nums[place-1],nums[0]
                #換了就會破壞maxheap
                place-=1
            elif nums[:place] != Solution.max_heap(nums[:place]):
                #不符合的就把nums[:place+1]變成maxheap
                nums[:place],nums[place:] = Solution.max_heap(nums[:place]),nums[place:]
        return nums
# 找父節點=>用不到我隱藏了:
#    def f(i):
#        if i>0:
#            return (i-1)//2
print(Solution.max_heap([3,5,6]))
print(Solution.max_heap([3,5,6,8]))
print(Solution.max_heap([3,5,6,8,8,0,9,10,2,0,0,0,4]))
```
## 補充
* 會寫程式的鑑賞等級

# 參考資料:
#### heap sort(概念複習與學習資源):

* Youtube: [Heap Sort | GeeksforGeeks](https://www.youtube.com/watch?v=MtQL_ll5KhQ)
* Youtube: [Heaps and Heap Sort](https://www.youtube.com/watch?v=H5kAcmGOn4Q)
* [Comparison Sort: Heap Sort(堆積排序法)](http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html)
* [堆積排序 Heapsort](https://rust-algo.club/sorting/heapsort/)
* [Heap Sort 的原理及Python實現](https://www.twblogs.net/a/5c7100f9bd9eee68dc3f1be8)
* [維基百科](https://zh.wikipedia.org/wiki/%E5%A0%86%E6%8E%92%E5%BA%8F#Python)
* [GITHUB_PY程式碼](https://github.com/joeyajames/Python/blob/master/MaxHeap.py)
* [自己的github](https://github.com/evaneversaydie/My_Study_Note/blob/master/HW2)
