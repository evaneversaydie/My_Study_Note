class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        #用遍訪的方式計算長度a(a=len(list))
        a = 0
        if head.val==None:
            a=0
            return None
        node=head
        while node:
            a+=1
            node=node.next

        #辨別是屬於奇數或單數的case
        if a%2 ==1: #[1,2,3,4,5]
            res=a//2
            index=0
            nod=head
            while nod: #從零開始遍訪(index指的是元素)list[res=2]=3
                if index !=res:
                    index+=1
                    nod=nod.next
                else:
                    return nod

        if a%2 ==0:
            res=a//2
            index=0
            nod=head
            while nod:
                if index !=res:
                    index+=1
                    nod=nod.next
                else:
                    return nod
