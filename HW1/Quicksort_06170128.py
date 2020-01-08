#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Quicksort(inputlist):


    if len(inputlist)<=1:
        return inputlist


    pivot=inputlist[0] #pivot為第一個值
    right = len(inputlist)-1
    small=[]
    big=[]
    pivots=[]
    
    while right>=0:
        #print(right)
        
        if inputlist[right] > pivot:
            big.append(inputlist[right])
            right-=1
        elif inputlist[right] == pivot:
            pivots.append(inputlist[right])
            right-=1
        elif inputlist[right]<pivot:
            small.append(inputlist[right])
            right-=1

        #print('s:',small,'p',pivots,'b',big)
    
    small=Quicksort(small)
    big = Quicksort(big)
    listresult=small+ pivots+big
    #print('res:',listresult)
    return listresult
    
    

    

