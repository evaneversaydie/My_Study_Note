

# Definition for a binary tree node.
#       :type val: int
#        :type left: TreeNode or None
#        :type right: TreeNode or None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root.val != None:
            if val <= root.val:
                if root.left == None:  # 左邊空的，值<=跟
                    root.left = TreeNode(val)
                    return root.left
                else:
                    self = root.left
                    insert(root, val)
            elif val > root.val:
                if root.right == None:
                    root.right = TreeNode(val)
                    return root.right
                else:
                    self = root.right
                    ##self
                    insert(root, val)
        else:
            root.val = TreeNode(val)

    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """

    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """

    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype: None Do not return anything, modify nodes(maybe more than more) in-place instead.(cannot search())
        """


# %%

a = Solution()
a.insert(TreeNode(7), 3)
a.insert(TreeNode(7), 10)
a.insert(TreeNode(7), 2)
a.insert(TreeNode(7), 15)
a.insert(TreeNode(7), 13)

