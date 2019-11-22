
# coding: utf-8

# In[ ]:


#Definition for a binary tree node.
#       :type val: int
#        :type left: TreeNode or None
#        :type right: TreeNode or None
       
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
    def child_count(self):
        count = 0
        if self.right:
            count+=1
        if self.left:
            count+=1
        return count
    #count有0、1、2三種值。
        
#Node分為:不存在、樹根、節點


class Solution(object):

    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root.val != None: #改成not root.val
            if val<=root.val :
                if root.left==None: 
                    root.left=TreeNode(val)
                    return root.left
                else:
                    # root = root.left
                    return self.insert(root.left, val) #2\3\4
            elif val>root.val:
                if root.right==None:
                    root.right =TreeNode(val)
                    return root.right
                else:
                    #root = root.right
                    return self.insert(root.right,val) #2\3\4
        else:
            root.val = val #非TreeNode
            return root #4
 ####################################################################################
        
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if not root:
            return None
        if root.val == None: #if not root.val
            return None
        if root.val == target:
            return root ####################非return target
        if target > root.val: #要找的值比root大
            return self.search(root.right,target) #往右邊找
        if target <= root.val:
            return self.search(root.left,target) #往左邊找
 ####################################################################################

    def searchwithparent(self,root,target,parent=None):
        
        if not root:
            return None,None
        if root.val == None: #if not root.val
            return None,None
        if root.val == target:
            return root,parent #############非return target
        if target > root.val: #要找的值比root大
            return self.searchwithparent(root.right,target,root) #往右邊找，parent變成root
        if target <= root.val:
            return self.searchwithparent(root.left,target,root) #往左邊找，parent變成root

#==================================================================================
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        node,p =self.searchwithparent(root,target)
        
        if node == None:
            return root
        
        while node:  
            #node,p =self.searchwithparent(root,target)
            #刪掉根
            if p == None:
                if node.child_count() ==0:
                    node.val = None
                    
                elif node.child_count() ==1:
                    if node.right:
                        new_root = node.right
                    else:
                        new_root = node.left
                    del node
                    root = new_root
                    
                elif node.child_count() ==2:
                    predecessor = node.left
                    predecessor_p = node 
                    #這行要先有，否則沒有先宣告不符合進入while loop 條件
                    #會出現'local variable 'predecessor_p' referenced before assignment'
                    while predecessor.right:
                        predecessor_p = predecessor
                        predecessor = predecessor.right
                    
                    if predecessor_p.left == predecessor:
                        node.val = predecessor.val
                        node.left = predecessor.left
                        del predecessor
                    elif predecessor_p.right == predecessor:
                        node.val = predecessor.val
                        #predecessor_p.left = predecessor.right  #left打成lfet
                        predecessor_p.right = predecessor.left
                        del predecessor
                    root = node

                
           #不是root     
            if p:    
                if node.child_count() == 0: ##不是node.child_count
                    if p.left == node:
                        p.left = None
                        del node
                        #return root
                    elif p.right == node:
                        p.right = None
                        del node 
                        #return root

                elif node.child_count() == 1: ##不是node.child_count
                    #找小孩在左邊還是右邊
                    if node.left: #打錯字有改
                        child = node.left
                    else:
                        child = node.right

                    if p.left == node:
                        p.left = child
                        #return root
                    elif p.right ==node:
                        p.right = child
                        #return root
                    del node         
    
                elif node.child_count() == 2: ##不是node.child_count
                    predecessor = node.left
                    predecessor_p = node
                    while predecessor.right:
                        predecessor_p = predecessor #這一橫要比較早，否則predecssor就不是原本的值了
                        predecessor = predecessor.right
                    #node.val = predecessor.val
                    if predecessor_p.left == predecessor:
                        node.val = predecessor.val
                        predecessor_p.left = predecessor.left
                        del predecessor
                    else:
                        node.val = predecessor.val
                        predecessor_p.right=predecessor.left
                        del predecessor     
            node,p =self.searchwithparent(root,target)
        return root  
    
  ####################################################################################
    
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        '''if target == new_val:
            return root
        '''
        node = self.search(root,target)
        if node == None:
            return root
        while node:
            node.val = new_val
            node = self.search(node.left,target)#直接荀子樹以免erro，不是:node = self.search(root.left,target)
            #一值修改直到沒有值== target
        unsort = self.pre_order(root,[])
        sort = sorted(unsort)
        root = TreeNode(self.letbst1(root,sort,[])[0])
        for i in self.letbst1(root,sort,[])[1:]:
            self.insert(root,i)
        return root

    def pre_order(self,root,array):
        array.append(root.val)
        if root.left:
            #self.pre_order(root,array)
            self.pre_order(root.left,array)
        if root.right:
            #self.pre_order(root,array)
            self.pre_order(root.right,array)
        return array

    def letbst1(self,root,array,resl):   
        if len(array)>=1:
            a = len(array)//2
            res = array[a]
            resl.append(res)
            #resl.append(res)
            self.letbst1(root,array[a+1:],resl)
            self.letbst1(root,array[:a],resl) 
        return resl



