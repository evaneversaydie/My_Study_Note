
參考資料
==
#### Merge Sort
* https://emn178.pixnet.net/blog/post/87965707
* http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html
* [合併排序法 - 使用Python(Merge sort)](https://newaurora.pixnet.net/blog/post/224658923-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95---%E4%BD%BF%E7%94%A8python)
* [Merge Sort - 合併排序](https://algorithm.yuanbin.me/zh-tw/basics_sorting/merge_sort.html)

#### 隨機生成list
* https://stackoverflow.com/questions/39379515/how-do-i-generate-a-random-list-in-python-with-duplicates-numbers
* https://stackoverflow.com/questions/3559337/how-to-generate-a-random-list-of-fixed-length-of-values-from-given-range


#### 檢查隨意的結果是否已經sort
*  https://www.itread01.com/content/1550354967.html

# MerageSort
* 最佳時間複雜度：O(nlog n)
* 平均時間複雜度：O(nlog n)
* 最差時間複雜度：O(nlog n)

Merage Sort是一種用分治法(大問題=>小問題=>解決小問題後就可以解決大問題)。
方法為:
1. `Divide`:把大list拆成小list(拆成len=1)
2. `Conquer`:把小list排序成中list，再把中list排序。
> Merge的大前提：若要由小數列合併出大數列，那麼各自的小數列必須「已經排好序」。



# 學習歷程



```python
import random
a = random.sample(range(30), 20)
a
```




    [28, 8, 21, 9, 18, 0, 10, 11, 15, 29, 25, 20, 22, 7, 14, 12, 1, 26, 23, 24]




```python
###### merge_sort_ID.py
class Solution(object):    
    def merge_sort(nums):
        return 
    
    def Divide(nums):
        if len(nums)<=1:
            return nums
     ####### maximum recursion depth exceeded ##########
     #沒有設置遞迴的限制=>容易一直遞迴而沒有結果(無窮迴圈)
     ###################################################
        a = len(nums)//2
        b = len(nums)-a
        left=nums[:a]
        right=nums[b:]       
        c = list(Solution.Divide(left))
        d = list(Solution.Divide(right))
        
        return c,d
    #######################################################

        

        
    def Conquer(r,l):
        return
```


```python
Solution.Divide(a)
#確認Divide可以切切切成小list
```




    ([[[[28], [8]], [[9], [18]]], [[[0], [10]], [[15], [29]]]],
     [[[[25], [20]], [[7], [14]]], [[[12], [1]], [[23], [24]]]])




```python
class Solution(object):    
    
    def Conquer(r,l):
        res =[] 
        if len(r)==0:
            return r
        
        elif len(l)==0:
            return l
        
        elif len(r)==1 and len(l) ==1 and r[0] > l[0]:
            res.append(l[0])
            res.append(r[0])
            return res

        elif l[0] < r[0]:
            res=[l[0]] + Conquer(l[1:], r)
            return res
        
        elif l[0] >= r[0]:
            res = [l[0]] + Conquer(l, r[1:])

            return res



    def Divide(nums):
        if len(nums)<=1:
            return nums
     ####### maximum recursion depth exceeded ##########
     #沒有設置遞迴的限制=>容易一直遞迴而沒有結果(無窮迴圈)
     ###################################################
        a = len(nums)//2
        b = len(nums)-a
        left=nums[:a]
        right=nums[b:]       
        r = list(Solution.Divide(left))
        l = list(Solution.Divide(right))
        
        returnData =Conquer(r,l)
        ### 加一個:小問題都切好了開始排排站並合成大問題
        return returnData
    #######################################################


    def merge_sort(self,nums):
        self.nums=nums
       # Conquer
        if len(nums)<=1:
            return nums
        else:
            return Solution.Divide(nums)
  
```


```python

Solution().merge_sort(a)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-218-a60663063c70> in <module>()
          1 
    ----> 2 Solution().merge_sort(a)
    

    <ipython-input-217-caf60a81dc0c> in merge_sort(self, nums)
         50             return nums
         51         else:
    ---> 52             return Solution.Divide(nums)
         53 
    

    <ipython-input-217-caf60a81dc0c> in Divide(nums)
         35         left=nums[:a]
         36         right=nums[b:]
    ---> 37         r = list(Solution.Divide(left))
         38         l = list(Solution.Divide(right))
         39 
    

    <ipython-input-217-caf60a81dc0c> in Divide(nums)
         35         left=nums[:a]
         36         right=nums[b:]
    ---> 37         r = list(Solution.Divide(left))
         38         l = list(Solution.Divide(right))
         39 
    

    <ipython-input-217-caf60a81dc0c> in Divide(nums)
         35         left=nums[:a]
         36         right=nums[b:]
    ---> 37         r = list(Solution.Divide(left))
         38         l = list(Solution.Divide(right))
         39 
    

    <ipython-input-217-caf60a81dc0c> in Divide(nums)
         38         l = list(Solution.Divide(right))
         39 
    ---> 40         returnData =Conquer(r,l)
         41         ### 加一個:小問題都切好了開始排排站並合成大問題
         42         return returnData
    

    NameError: name 'Conquer' is not defined


網路上說會出現這個erro是因為變數名稱寫錯，但是這邊沒有，所以有其他的錯誤。<br>所以加上`Solution.`在Conquer前面。<br>可能是對Class要更多的了解QAQ


```python
class Solution(object):    
    
    def Conquer(r,l):
        res =[] 
        if len(r)==0:
            return r
        
        elif len(l)==0:
            return l
        
        elif len(r)==1 and len(l) ==1 and r[0] > l[0]:
            res.append(l[0])
            res.append(r[0])
            return res

        elif l[0] < r[0]:
            res=[l[0]] + Solution.Conquer(l[1:], r)
            return res
        
        elif l[0] >= r[0]:
            res = [l[0]] + Solution.Conquer(l, r[1:])

            return res



    def Divide(nums):
        if len(nums)<=1:
            return nums
     ####### maximum recursion depth exceeded ##########
     #沒有設置遞迴的限制=>容易一直遞迴而沒有結果(無窮迴圈)
     ###################################################
        a = len(nums)//2
        b = len(nums)-a
        left=nums[:a]
        right=nums[b:]       
        r = list(Solution.Divide(left))
        l = list(Solution.Divide(right))
        
        returnData =Solution.Conquer(r,l)
        ### 加一個:小問題都切好了開始排排站並合成大問題
        return returnData
    #######################################################


    def merge_sort(self,nums):
        self.nums=nums
       # Conquer
        if len(nums)<=1:
            return nums
        else:
            return Solution.Divide(nums)
  
```


```python
import random
a = random.sample(range(30), 20)
print(a)
print(Solution().merge_sort(a))
```

    [23, 3, 20, 0, 6, 12, 10, 8, 4, 19, 11, 27, 25, 5, 7, 21, 16, 15, 28, 26]
    [26, 23, 26, 23]
    


```python
import random
a = random.sample(range(30), 5)
print(a)
print(Solution.Divide(a))

```

    [10, 13, 4, 28, 11]
    [11, 13, 28]
    


```python
print(Solution.Conquer([[10], [13]], [[28], [11]]))
```

    [[28], [13]]
    

怎麼這樣子我懷疑人生了。
再從Divid開始看好了


```python
class Solution(object):    
    def Divide(nums):
        if len(nums)<=1:
            return nums
     ####### maximum recursion depth exceeded ##########
     #沒有設置遞迴的限制=>容易一直遞迴而沒有結果(無窮迴圈)
     ###################################################
        a = len(nums)//2
        b = len(nums)-a
        left=nums[:a]
        right=nums[b:]       
        r = list(Solution.Divide(left))
        l = list(Solution.Divide(right))
        
        return left,right   #改成left right看看
    #######################################################
```


```python
import random
a = random.sample(range(30), 5)
b = random.sample(range(30), 6)
print(a)
print(b)
print(Solution.Divide(a))
print(Solution.Divide(b))
```

    [3, 10, 11, 29, 0]
    [20, 0, 6, 24, 16, 10]
    ([3, 10], [29, 0])
    ([20, 0, 6], [24, 16, 10])
    

所以切的時候切錯了QAQ。
遇到奇數長度的list就會因為只取商數的關係而有錯。
<br>像是上面r=[:2]，l=[3:]，兩邊切片的起始點不同，再加上切片尾巴的index不包含在切的list裡面
把right=nums[a:] 
不要b=len(nums)-a了。
這樣子切片才可以一個不含第a個，一個含第a個。


```python
class Solution(object):    
    def Divide(nums):
        if len(nums)<=1:
            return nums
     ####### maximum recursion depth exceeded ##########
     #沒有設置遞迴的限制=>容易一直遞迴而沒有結果(無窮迴圈)
     ###################################################
        a = len(nums)//2
        left=nums[0:a]
        right=nums[a:]        
        r = list(Solution.Divide(left))
        l = list(Solution.Divide(right))
        return left,right
    #######################################################
```


```python
import random
a = random.sample(range(30), 5)
b = random.sample(range(30), 6)
print(a)
print(b)
print(Solution.Divide(a))
print(Solution.Divide(b))
```

    [0, 15, 18, 29, 10]
    [24, 8, 3, 9, 14, 6]
    ([0, 15], [18, 29, 10])
    ([24, 8, 3], [9, 14, 6])
    


```python
class Solution(object):    
    
    def Conquer(r,l):
        res =[] 
        if len(r)==0:
            return r
        
        elif len(l)==0:
            return l
        
        elif len(r)==1 and len(l) ==1 and r[0] > l[0]:
            res.append(l[0])
            res.append(r[0])
            return res

        elif l[0] < r[0]:
            res=[l[0]] + Solution.Conquer(l[1:], r)
            return res
        
        elif l[0] >= r[0]:
            res = [l[0]] + Solution.Conquer(l, r[1:])

            return res


    def Divide(nums):
        if len(nums)<=1:
            return nums
     ####### maximum recursion depth exceeded ##########
     #沒有設置遞迴的限制=>容易一直遞迴而沒有結果(無窮迴圈)
     ###################################################
        a = len(nums)//2
        left=nums[0:a]
        right=nums[a:]    
        r = list(Solution.Divide(left))
        l = list(Solution.Divide(right))
        
        returnData =Solution.Conquer(r,l)
        ### 加一個:小問題都切好了開始排排站並合成大問題
        return returnData
    #######################################################\
    
    def merge_sort(self,nums):
        self.nums=nums
       # Conquer
        if len(nums)<=1:
            return nums
        else:
            return Solution.Divide(nums)
  
```


```python
import random
a = random.sample(range(30), 5)
b = random.sample(range(30), 6)
print(a)
print(b)
print(Solution.Divide(a))
print(Solution.Divide(b))
```

    [16, 19, 21, 9, 6]
    [16, 5, 4, 23, 10, 3]
    [6, 19, 21]
    [3, 4, 23]
    

Conquer寫錯了(因為把divide 的retrn改成要用到 Conquer)


```python
class Solution(object):    
    
    def Conquer(r,l):
        res =[] 
        if len(r)==0:
            return r
        
        elif len(l)==0:
            return l
        
        elif len(r)==1 and len(l) ==1 and r[0] > l[0]:
            res.append(l[0])
            res.append(r[0])
            return res

        elif l[0] < r[0]:
            res=[l[0]] + Solution.Conquer(l[1:], r)
            return res
        
        elif l[0] >= r[0]:
            res = [l[0]] + Solution.Conquer(l, r[1:])

            return res

```


```python
print(Solution.Conquer([],[2]))
print(Solution.Conquer([1,4],[2,3]))
print(Solution.Conquer([2,4],[1,3,5]))
print(Solution.Conquer([2],[0]))
```

    []
    [2, 4, 3, 4]
    [1, 2, 3, 4, 5]
    [0, 2]
    


```python
class Solution(object):    
    
    def Conquer(r,l):
        res =[] 
#====================================================
#這邊這樣不合理，改成return要return另一個不是自己
        if len(r)==0:
            return l
        
        elif len(l)==0:
            return r
#====================================================   
#OK
        elif len(r)==1 and len(l) ==1 and r[0] > l[0]:
            res.append(l[0])
            res.append(r[0])
            return res
#=======================================================
#改這邊:
        elif l[0] < r[0]:
            res=[l[0]] + Solution.Conquer(l[1:], r)
            return res
        
        elif l[0] >= r[0]:
            res = [r[0]] + Solution.Conquer(l, r[1:])
                #本來打錯了!!是R比較小要取出來呀
            return res

```


```python
print(Solution.Conquer([],[2]))
print(Solution.Conquer([1,4],[2,3]))
print(Solution.Conquer([2,4],[1,3,5]))
print(Solution.Conquer([2],[0]))
```

    [2]
    [1, 2, 3, 4]
    [1, 2, 3, 4, 5]
    [0, 2]
    


```python
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


```python
import random
a = random.sample(range(30), 5)
b = random.sample(range(30), 6)
print(a)
print(Solution().merge_sort(a))
print(b)
print(Solution().merge_sort(b))

```

    [28, 18, 25, 2, 3]
    [2, 3, 18, 25, 28]
    [20, 15, 28, 18, 3, 16]
    [3, 15, 16, 18, 20, 28]
    

開心!!!!!!!!!!!!!!!
引用檢查的程式碼再跑一次!!



```python
a = [random.randint(0,1000) for _ in range(100)] # 生成長度為100的整型陣列,元素大小為(0,1000]
print(bool(Solution().merge_sort(a) == sorted(a)))
```

    True
    

試試看助教說的如果有負數和小數點行不行。


```python
a = [9,4.3,-1,-4.3,1,4.2,0,-4.2]
print(Solution().merge_sort(a))
```

    [-4.3, -4.2, -1, 0, 1, 4.2, 4.3, 9]
    

終於!!!!!!!!!!!!!!!!!!!!!!!!!!!
<br>希望下次可以裝spider或pychram練習debugmode  QAQ
<br>再heap sort 先複習了class後卡卡的就先過來寫MergeSort。但過程中發現自己對物件還是不熟啊!
<br>如果def中間有self，那呼叫的時候要有`class名稱`+ `().`+`def(看裡面有幾個變數)`才可以用，不然就不可以運行了。

<br>可能是py比較自由的關係，不一定要有self，等等有寫完Heap Sort有時間的話要趕快來研究。
