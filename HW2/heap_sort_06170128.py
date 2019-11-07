
# coding: utf-8

# In[5]:


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

