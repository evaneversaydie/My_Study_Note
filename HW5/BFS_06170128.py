#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import defaultdict 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) #預設為一個空的dict
    def addEdge(self,u,v): 
        self.graph[u].append(v) #如果要新增adjacency list的話，dict會有資料
        
    
    def __travel__(self, s, store):
        if s not in self.graph:
            return []

        visited = []
        now = s
        store.push(s)
        while not store.empty():
            now = store.top()
            add = store.top()
            store.pop()
            if add not in visited: #
                visited.append(add)
            for i in self.graph[now]:
                if i not in visited and i not in store.data:
                    store.push(i)
        return visited

    def BFS(self, s): 
        return self.__travel__(s,MyQueue())
    
    def DFS(self, s):
        return self.__travel__(s,MinStack())
        
        
class MinStack:
    def __init__(self):
        self.data = []
    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> None:
        self.data=self.data[:-1]

    def top(self) -> int:
        if len(self.data)>=1:
            return self.data[-1]
        return None 
    def empty(self) -> bool:
        if len(self.data)==0:
            return True
        else:
            return False
class MyQueue:
    def __init__(self):
        self.data=[]
        self.data1=self.data[::-1]
    def push(self, x: int) -> None:
        self.data.append(x)
    def pop(self) -> int: 
        self.data = self.data[1:]
        #a =  self.data[0]
        #return a
    def top(self):
        if len(self.data)>=1:
            return self.data[0]
        return 
    def empty(self) -> bool:
        if len(self.data)==0:
            return True
        else:
            return False

