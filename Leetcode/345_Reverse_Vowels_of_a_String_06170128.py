#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def reverseVowels(self, s: str) -> str:
        data = []
        dataindex = []
        for i in range(len(s)):
            if s[i] in ['a','e','i','o','u',"A","E","I","O","U"]:
                data.append(s[i])
                dataindex.append(i)
        data = data[::-1]
        for i in range(len(dataindex)):

            s=s[:dataindex[i]]+data[i]+s[dataindex[i]+1:]
        return s

