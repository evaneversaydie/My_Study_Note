class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list3 = self.alllistval(l1)+self.alllistval(l2)
        list3.sort()
        if list3==[]:
            return None
        node=ListNode(list3[0])
        head = node
        for i in range(0,len(list3)-1):
            node.next = ListNode(list3[i+1])
            node= node.next
        return head
    def alllistval(self,l):
        a=[]
        while l:
            a.append(l.val)
            l=l.next
        return a