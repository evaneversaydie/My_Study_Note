#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        b=0
        ans=0
        for i in points:
            data={} #{距離:個數}
            for j in points:
                c = self.rangepoint(i,j)
                if c not in data:
                    data[c]=1
                else:
                    b += data[c]*2
                    data[c]+=1
            for k in data:    
                if data[k] > 1:
                    ans += data[k]*(data[k]-1)
        return ans
    def rangepoint(self,A,B):
        return ((A[0]-B[0])**2+(A[1]-B[1])**2)**0.5

