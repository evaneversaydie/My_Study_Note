#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        reslist=[]    
        for i in nums:
            res=0
            if i//10000>=1:
                res=5
            elif i//1000>=1:
                res=4
            elif i //100>=1:
                res=3
            elif i // 10>=1:
                res=2
            elif i//1>=1:
                res=1
            reslist.append(res)
        r=0
        for i in reslist:
            
            if i%2==0:
                r+=1
        return r

