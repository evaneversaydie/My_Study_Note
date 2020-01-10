# 232. Implement Queue using Stacks
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [232. Implement Queue using Stacks](#232-implement-queue-using-stacks)
- [解法](#解法)
- [結果](#結果)
<!-- TOC END -->


# [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

Implement the following operations of a queue using stacks.

- push(x) -- Push element x to the back of queue.
- pop() -- Removes the element from in front of queue.
- peek() -- Get the front element.
- empty() -- Return whether the queue is empty.

# 解法

```Python
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data=[]
        self.data1=self.data[::-1]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.data.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        a =  self.data[0]
        self.data = self.data[1:]
        return a

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.data[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.data)==0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

# 結果
![圖片](https://i.imgur.com/BjLibYW.png)
