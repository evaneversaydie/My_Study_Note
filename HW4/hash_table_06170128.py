#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        self.group = []

    def crydata(self,key):
        k = MD5.new()
        k.update(key.encode('utf-8'))
        kDex = int(k.hexdigest(), 16)  # 十進位
        return str(kDex)
    def groupindex(self,key):
        k = MD5.new()
        k.update(key.encode('utf-8'))
        kDex = int(k.hexdigest(), 16)  # 十進位
        kgroup = kDex % self.capacity
        return kgroup

    def add(self, key):
        add = ListNode(self.crydata(key))  # 這是需要添加的資料要先放在if loop之前!!!!!
        kgroup = self.groupindex(key)
        if kgroup not in self.group:  # 沒有在之前的bucket中
            self.group.append(kgroup)
            self.data[kgroup] = add
            # self.capacity+=1
        elif kgroup in self.group:
            self.help_addinlist(self.data[kgroup],add,key)

    def help_addinlist(self, node, addinto,key):
        if node.next != None:
            self.help_addinlist(node.next, addinto,key)
        elif node.next == None:
            if self.contains(key):
                return
            else:
                node.next = addinto

    def remove(self, key):
        dkgroup = self.groupindex(key)
        if self.contains(key):  # 有找到所以要找到他在哪裡並刪掉=>可以設計一個方法回傳值在哪個bucket也可以直接刪掉
            self.removehelp(dkgroup, key, self.data[dkgroup])

    def removehelp(self, keygroup, key, node, prenode=None):
        if node:
            if prenode:
                if node.val == self.crydata(key):
                    prenode.next = node.next
                    del node
                else:
                    self.removehelp(keygroup, key, node.next, node)
            else:  # 是head，要刪掉capacity中的值
                if node.val == self.crydata(key):
                    if node.next:
                        self.data[keygroup] = node.next
                        del node
                    else:
                        self.data[keygroup] = None
                else:
                    self.removehelp(keygroup, key, node.next, node)

    def contains(self, key):
        ckgroup = self.groupindex(key)
        if ckgroup not in self.group:  # bucket不存在=>Key不存在不用查
            return False
        elif ckgroup in self.group:  # bucket存在=>遍訪linked list
            return self.containsinshelp(key, self.data[ckgroup])

    def containsinshelp(self, key, node):
        if node:
            if node.val == self.crydata(key):
                return True
            else:
                if node.next == None:
                    return False
                elif node.next:
                    return self.containsinshelp(key, node.next)
        else:
            return False

