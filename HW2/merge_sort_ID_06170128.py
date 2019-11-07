
# coding: utf-8

# In[1]:


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
  

