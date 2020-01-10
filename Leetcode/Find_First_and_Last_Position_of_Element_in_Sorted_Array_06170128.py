#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[]
        if target not in nums:
            return [-1,-1]
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        res = [res[0],res[-1]]
        return res

