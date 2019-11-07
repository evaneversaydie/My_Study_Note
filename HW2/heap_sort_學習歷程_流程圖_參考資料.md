
# 參考資料:

* [關於Python的類別(Class)...基本篇](https://medium.com/@weilihmen/%E9%97%9C%E6%96%BCpython%E7%9A%84%E9%A1%9E%E5%88%A5-class-%E5%9F%BA%E6%9C%AC%E7%AF%87-5468812c58f2)



##### heap sort(概念複習與學習資源):

* Youtube: [Heap Sort | GeeksforGeeks](https://www.youtube.com/watch?v=MtQL_ll5KhQ)
* Youtube: [Heaps and Heap Sort](https://www.youtube.com/watch?v=H5kAcmGOn4Q)
* [Comparison Sort: Heap Sort(堆積排序法)](http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html)
* [堆積排序 Heapsort](https://rust-algo.club/sorting/heapsort/)
* [Heap Sort 的原理及Python實現](https://www.twblogs.net/a/5c7100f9bd9eee68dc3f1be8)
* [維基百科](https://zh.wikipedia.org/wiki/%E5%A0%86%E6%8E%92%E5%BA%8F#Python)
* [GITHUB_PY程式碼](https://github.com/joeyajames/Python/blob/master/MaxHeap.py)

參考資料一:複習class與def的概念
-----

和class比較不熟，先查了參考資料1，複習class、def。
class可以想像成物種，def是可以用來行、定義每個物種的屬性。像是貓咪或是狗狗。而def一定要放入參數，這樣我們可以使用這個屬性。反過來來說，class只是這些我們寫下來的屬性的集合。

而python的自由度很高，我們不一定要在class把所有屬性打出來，可以在之後的主程式再加上去。

#### 小結論
因此我們也可以替換一下，比如說class是貓咪，然後我們可以說一隻貓咪有顏色、尾巴形狀長短、名字、性別、外號的屬性。
現在來建立一個可以來貓咪的class，並創建youtube黃阿瑪的後宮生活裡其中幾隻貓咪。


```python
class Cat(object):
    def __init__(self, color,tail,name,gender,nickname):   #self是指class不用改
        self.color = color
        self.tail = tail
        self.name = name
        self.gender = gender
        self.nickname = nickname

#來看貓咪  
黃阿瑪 = Cat('橘白色','長尾巴','黃阿瑪','雄','皇上')
招弟 = Cat('灰棕色','長尾巴','招弟','雌','皇后')
三腳 = Cat('橘白色','長尾巴','三腳','雌','腳妹')
嚕嚕 = Cat('橘色','麒麟尾','嚕嚕','雄','王爺')
袖子 = Cat('黑白','長尾巴','柚子','雄','')
#接下來就可以看看這些貓咪的屬性了，像是看嚕嚕的尾巴是什麼
print(嚕嚕.tail)

#來新增三角的健康狀況:
三腳.health="口炎"
print(三腳.health)
#但這個方式其他沒有新增health屬性的貓咪就印不出來了
```

    麒麟尾
    口炎
    

# 關於Heap sort:
整理上課與參考資料如下:

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
           *奇數:i//2
           *偶數:i//2-1
           ->同一個父節點的節點索引值(奇數、偶數)只差1，可以化簡為:(i-1)//2
       * 找到左邊的小孩:2*i+1
       * 找到右邊的小孩:2*i+2 
       
       對每一個節點而言，左邊小孩是奇數，右邊小孩都是偶數。
       <br>先這樣子找找找就把胎們變成max heap。



```python
##### heap_sort_ID.py
class Solution(object):
    def heap_sort(self, nums):
        #alreadysort=[]
        #nums1 = Solution.maxheap(nums)
        #alreadysort.append(nums1[0])
        #nums1.pop
        return
    
      
        
    def swap( nums):
        a = len(nums)-1
        b = Solution.father(len(nums))    
        
        while nums[a]>nums[b]:
            print(nums[a],nums[b])
        
            nums[a],nums[b]=nums[b],nums[a]
            
            a = Solution.father(a)
            b = Solution.father(b)
            
            print('step',nums) 
        
        return 'end',nums
        #小孩比爸爸大就交換
     
            
  
 #   def swiftdown(self,muns):
 #       return


# 找父節點與小孩:
    def father(i):
        if i==0:
            return 0
        elif i<0:
            return None
        else:
            return (i-1)//2
    
    def r(i):
        if 2*i+1>len(nums):
            return None
        else:
            return 2*i+1
    
    def l(i):
         if 2*i+2>len(nums):
            return None
         else:
            return 2*(i+1)

```


```python
b=[4,5,6,7,8]
Solution.swap(b)

#step:[4,8,6,7,5]
#答案:[8,4,6,7,5]
```

    8 6
    step [4, 5, 8, 7, 6]
    5 4
    step [5, 4, 8, 7, 6]
    




    ('end', [5, 4, 8, 7, 6])



想先試試先把最尾巴的數字放到對位置。但是結果和在紙上畫出來不同。發現打作業下來常常設錯參數，b應該要len(nums)-1，不然的話就找錯爸爸了。


```python
##### heap_sort_ID.py
class Solution(object):

    def swap( nums):
        a = len(nums)-1
        b = Solution.father(len(nums)-1)    
        
        while nums[a]>nums[b]:
            print(nums[a],nums[b])
        
            nums[a],nums[b]=nums[b],nums[a]
            
            a = Solution.father(a)
            b = Solution.father(b)
            
            print('step',nums) 
        
        return 'end',nums
        #小孩比爸爸大就交換
     
            

# 找父節點與小孩:
    def father(i):
        if i==0:
            return 0
        elif i<0:
            return None
        else:
            return (i-1)//2
    
    def r(i):
        if 2*i+1>len(nums):
            return None
        else:
            return 2*i+1
    
    def l(i):
         if 2*i+2>len(nums):
            return None
         else:
            return 2*(i+1)

```


```python
b=[4,5,6,7,8]
Solution.swap(b)
#step:[4,8,6,7,5]
#答案:[8,4,6,7,5]
```

    8 5
    step [4, 8, 6, 7, 5]
    8 4
    step [8, 4, 6, 7, 5]
    




    ('end', [8, 4, 6, 7, 5])



完成第一個檢查。可是卡住了，要怎麼地回還有說要怎麼確定整個array是maxheapQAQ。
先去寫Merge Sort好了QAQ

把之前寫得先丟掉，先來確定一下這次要用幾個function好了。
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
    <br>_ _ _ _ _ _ _^插入到這裡
    <br>
    <br>想要用之前一直想不懂的in-place版本QAQ，因為root的index是[0]所以可能需要用到1個變數(暫訂place):
        <br>用來記得現在到底要交換的元素的位置(|前面的數字)

<br>有點像這樣子:2->3->2->3......直到place==1->排好了
<br>但是要怎麼變成max heap \QAQ/


```python
#不管了先放入一個max heap然後來排序的吧!
testdata = [19,15,7,10,9,4,3]
```


```python
class Solution(object):
    def heap_sort(self, nums):
        return
    def max_heap(nums):
        return nums

    
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
```


```python
testdata = [19,15,7,10,9,4,3]
Solution.swap(testdata)
```




    [15, 7, 10, 9, 4, 3, 19]



檢查一下過程和想要的對不對(因為現在沒寫Solution.max_heap())


```python
nums=[19,15,7,10,9,4,3]
place=len(nums)
while place>0:
    if nums[0:place]==Solution.max_heap(nums[:place]):
        print('sli:',nums[0:place])
        nums[0],nums[place-1]=nums[place-1],nums[0]
        place-=1
        print('res:',nums)
```

    sli: [19, 15, 7, 10, 9, 4, 3]
    res: [3, 15, 7, 10, 9, 4, 19]
    sli: [3, 15, 7, 10, 9, 4]
    res: [4, 15, 7, 10, 9, 3, 19]
    sli: [4, 15, 7, 10, 9]
    res: [9, 15, 7, 10, 4, 3, 19]
    sli: [9, 15, 7, 10]
    res: [10, 15, 7, 9, 4, 3, 19]
    sli: [10, 15, 7]
    res: [7, 15, 10, 9, 4, 3, 19]
    sli: [7, 15]
    res: [15, 7, 10, 9, 4, 3, 19]
    sli: [15]
    res: [15, 7, 10, 9, 4, 3, 19]
    

去參考網路的程式程式碼，整理出以下邏輯:
<br>像是用分治法一樣，先切成最小的問題=>只有兩層且全滿的樹:
    1. 紀錄father、r、l哪一個最大，將最大的和father交換。
    2. 由下而上的去檢查(由list後往前)=>可以用for迴圈
 <br> 新增一個let_max_heap()來實現1

#### 先試試看for loop:


```python
for i in range(5,0,-2):
    print(i)
print()
for i in range(5,0,-1):
    print(i)
#renge(5-0)，不含0，最後一個數字=>間隔

```

    5
    3
    1
    
    5
    4
    3
    2
    1
    


```python
for i in reversed(range(5)):
    print(i)
print()
for i in range(5):
    print(i)
#range(n)皆不包含n
```

    4
    3
    2
    1
    0
    
    0
    1
    2
    3
    4
    


```python
class Solution(object):
    def heap_sort(self, nums):
        self.nums=nums
        return Solution.swap(nums)
    
    
    
    
    def max_heap(nums):
        for i in reversed(range((len(nums)-1)//2+1)):
            Solution.let_max_heap(nums,i)
        return nums
    
    def let_max_heap(nums,i):
        max0=i
        r=Solution.r(i)
        l=Solution.l(i)
        max1 = max(nums[i],nums[r],nums[l])
        if max1 == nums[r]:
            nums[r],nums[i]=nums[i],nums[r]
            max0=r
            Solution.let_max_heap(nums,max0)
        elif max1 == nums[l]:
            nums[l],nums[i]=nums[i],nums[l]
            max0=l
            Solution.let_max_heap(nums,max0)
        
        
            
    
    
    
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
    
    
    
    
    
# 找父節點與小孩:
    def f(i):
        if i>0:
            return (i-1)//2
    
    def r(i):
        if 2*i+1<=len(nums):
            return 2*i+1
    
    def l(i):
        if 2*i+2<len(nums):
            return 2*(i+1)
```


```python
Solution().heap_sort(nums)
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-274-59f28e316579> in <module>()
    ----> 1 Solution().heap_sort(nums)
    

    <ipython-input-273-1acdc5dd9dc3> in heap_sort(self, nums)
          2     def heap_sort(self, nums):
          3         self.nums=nums
    ----> 4         return Solution.swap(nums)
          5 
          6 
    

    <ipython-input-273-1acdc5dd9dc3> in swap(nums)
         34         place=len(nums)
         35         while place>0:
    ---> 36             if nums[0:place]==Solution.max_heap(nums[:place]):
         37                 #符合maxheap且place>=1(不用作nums[0],nums[0]交換)
         38                 nums[0],nums[place-1]=nums[place-1],nums[0]
    

    <ipython-input-273-1acdc5dd9dc3> in max_heap(nums)
          9     def max_heap(nums):
         10         for i in reversed(range((len(nums)-1)//2+1)):
    ---> 11             Solution.let_max_heap(nums,i)
         12         return nums
         13 
    

    <ipython-input-273-1acdc5dd9dc3> in let_max_heap(nums, i)
         16         r=Solution.r(i)
         17         l=Solution.l(i)
    ---> 18         max1 = max(nums[i],nums[r],nums[l])
         19         if max1 == nums[r]:
         20             nums[r],nums[i]=nums[i],nums[r]
    

    IndexError: list index out of range



```python
    def let_max_heap(nums,i):
        max0=i
        r=Solution.r(i)
        l=Solution.l(i)
        if r<len(nums) and l<len(nums):
            max1 = max(nums[i],nums[r],nums[l])

        if max1 == nums[r]:
            nums[r],nums[i]=nums[i],nums[r]
            max0=r
            Solution.let_max_heap(nums,max0)
        elif max1 == nums[l]:
            nums[l],nums[i]=nums[i],nums[l]
            max0=l
            Solution.let_max_heap(nums,max0)
```

嘗試限制計算出的子節點沒有超出len(nums)。【上面的方框框只列出更動let_max_heap()的部分】
<br>出現錯誤`local variable 'max1' referenced before assignment`
<br>max1還沒有被定義就被使用了(可能是因為我把max1放在if裡面的關係)
<br>想變成巢狀的if迴圈試試看。


```python
class Solution(object):
    def heap_sort(self, nums):
        self.nums=nums
        return Solution.swap(nums)
    
    
    
    
    def max_heap(nums):
        for i in reversed(range((len(nums)-1)//2+1)):
            Solution.let_max_heap(nums,i)
        return nums
    
    def let_max_heap(nums,i):
        max0=i
        r=Solution.r(i)
        l=Solution.l(i)
        
        if r<len(nums) and l<len(nums):
            max1 = max(nums[i],nums[r],nums[l])

            if max1 == nums[r]:
                nums[r],nums[i]=nums[i],nums[r]
                max0=r
                Solution.let_max_heap(nums,max0)
            elif max1 == nums[l]:
                nums[l],nums[i]=nums[i],nums[l]
                max0=l
                Solution.let_max_heap(nums,max0)
        
        
            
    
    
    
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
    
    
    
    
    
# 找父節點與小孩:
    def f(i):
        if i>0:
            return (i-1)//2
    
    def r(i):
        if 2*i+1<=len(nums):
            return 2*i+1
    
    def l(i):
        if 2*i+2<len(nums):
            return 2*(i+1)
```


```python
Solution().heap_sort(nums)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-281-59f28e316579> in <module>()
    ----> 1 Solution().heap_sort(nums)
    

    <ipython-input-280-513348d907ce> in heap_sort(self, nums)
          2     def heap_sort(self, nums):
          3         self.nums=nums
    ----> 4         return Solution.swap(nums)
          5 
          6 
    

    <ipython-input-280-513348d907ce> in swap(nums)
         37         place=len(nums)
         38         while place>0:
    ---> 39             if nums[0:place]==Solution.max_heap(nums[:place]):
         40                 #符合maxheap且place>=1(不用作nums[0],nums[0]交換)
         41                 nums[0],nums[place-1]=nums[place-1],nums[0]
    

    <ipython-input-280-513348d907ce> in max_heap(nums)
          9     def max_heap(nums):
         10         for i in reversed(range((len(nums)-1)//2+1)):
    ---> 11             Solution.let_max_heap(nums,i)
         12         return nums
         13 
    

    <ipython-input-280-513348d907ce> in let_max_heap(nums, i)
         27                 nums[l],nums[i]=nums[i],nums[l]
         28                 max0=l
    ---> 29                 Solution.let_max_heap(nums,max0)
         30 
         31 
    

    <ipython-input-280-513348d907ce> in let_max_heap(nums, i)
         17         l=Solution.l(i)
         18 
    ---> 19         if r<len(nums) and l<len(nums):
         20             max1 = max(nums[i],nums[r],nums[l])
         21 
    

    TypeError: '<' not supported between instances of 'NoneType' and 'int'



# 測試max函數可否接受None
在最下層的樹裡面l、r不一定同時存在。


```python
max(None,0,-1)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-287-38a8c408ffc0> in <module>()
    ----> 1 max(None,0,-1)
    

    TypeError: '>' not supported between instances of 'int' and 'NoneType'


max():不能用於右邊節點不存在的情形。


```python
class Solution(object):
    def heap_sort(self, nums):
        self.nums=nums
        return Solution.swap(nums)

    
    def max_heap(nums):
        return nums
        
    def let_max_heap(nums,i):
        root = i
        r=Solution.r(i)
        l=Solution.l(i)
        #改成不用max()，葉子大於跟就交換
        if r<len(nums) and nums[r] > nums[root]:  
            nums[root],nums[r]=nums[r],nums[root]
            Solution.let_max_heap(nums,r)
        if l<len(nums) and nums[l] > nums[root]:
            nums[root],nums[l]=nums[l],nums[root]
            Solution.let_max_heap(nums,l)

        return nums
        
            

    
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
    
    
    
    
    
# 找父節點與小孩:
    def f(i):
        if i>0:
            return (i-1)//2
    
    def r(i):
        if 2*i+1<=len(nums):
            return 2*i+1
    
    def l(i):
        if 2*i+2<len(nums):
            return 2*(i+1)
        
Solution.let_max_heap([3,5,6],0)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-2-69bcb5c70175> in <module>()
         60             return 2*(i+1)
         61 
    ---> 62 Solution.let_max_heap([3,5,6],0)
    

    <ipython-input-2-69bcb5c70175> in let_max_heap(nums, i)
         12     def let_max_heap(nums,i):
         13         root = i
    ---> 14         r=Solution.r(i)
         15         l=Solution.l(i)
         16         if r<len(nums) and nums[r] > nums[root]:
    

    <ipython-input-2-69bcb5c70175> in r(i)
         53 
         54     def r(i):
    ---> 55         if 2*i+1<=len(nums):
         56             return 2*i+1
         57 
    

    NameError: name 'nums' is not defined



#### Error:電腦當掉重新啟動後，發現f(i)、r(i)、l(i)的函數錯誤(nums未出現)


```python
class Solution(object):
    def heap_sort(self, nums):
        self.nums=nums
        return Solution.swap(nums)

    
    def max_heap(nums):
        return nums
        
    def let_max_heap(nums,i):
        root = i
        #刪掉到找子節點的def改成宣告
        r= 2*i+1
        l= 2*(i+1)
        #改成不用max()，葉子大於跟就交換
        if r<len(nums) and nums[r] > nums[root]:  
            nums[root],nums[r]=nums[r],nums[root]
            Solution.let_max_heap(nums,r)
        if l<len(nums) and nums[l] > nums[root]:
            nums[root],nums[l]=nums[l],nums[root]
            Solution.let_max_heap(nums,l)
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
    
    
    
    
    
# 找父節點:
    def f(i):
        if i>0:
            return (i-1)//2
print(Solution.let_max_heap([3,5,6],0))
print(Solution.let_max_heap([3,5,6,8],0))

```

    [6, 3, 5]
    [6, 8, 5, 3]
    

現在可以讓一個最小的單位呈現max heap
因為從上而下找所以8浮不上來。要用倒敘的方式。

>  算倒數第一層的節點:nums[(len(nums)-1)//2+1:len(nums)-1]
<br> 只要對nums[:(len(nums)-1)//2]做 let_max_heap()


```python
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

    [6, 3, 5]
    [8, 5, 6, 3]
    [10, 8, 9, 5, 8, 4, 6, 3, 2, 0, 0, 0, 0]
    

#### max_heapOK，測試swap()


```python
print(Solution.swap([3,5,6]))
print(Solution.swap([3,5,6,8]))
print(Solution.swap([3,5,6,8,8,0,9,10,2,0,0,0,4]))
```

    [3, 5, 6]
    [3, 5, 6, 8]
    [0, 0, 0, 0, 2, 3, 4, 5, 6, 8, 8, 9, 10]
    


```python
print(Solution().heap_sort([3,5,6]))
print(Solution().heap_sort([3,5,6,8]))
print(Solution().heap_sort([3,5,6,8,8,0,9,10,2,0,0,0,4]))
```

    [3, 5, 6]
    [3, 5, 6, 8]
    [0, 0, 0, 0, 2, 3, 4, 5, 6, 8, 8, 9, 10]
    

### 亂數list測試:


```python
import random
for i in range(5):
    a = [random.randint(0,1000) for _ in range(100)] 
    print(bool(Solution().heap_sort(a) == sorted(a)))
for i in range(5):
    a = [random.randint(0,1000) for _ in range(99)] 
    print(bool(Solution().heap_sort(a) == sorted(a)))
```

    True
    True
    True
    True
    True
    True
    True
    True
    True
    True
    


```python
a=[-2,3**3,0,-0.1,1/2]
print(Solution().heap_sort(a))
print(bool(Solution().heap_sort(a) == sorted(a)))
```

    [-2, -0.1, 0, 0.5, 27]
    True
    

天啊太開心了!!!!!!!!!!!!

# 最終流程圖
![heapsort](HeapSort.jpg)
