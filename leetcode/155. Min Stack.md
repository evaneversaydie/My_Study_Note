# 155. Min Stack
<!-- TOC START min:1 max:3 link:true asterisk:false update:true -->
- [155. Min Stack](#155-min-stack)
    - [題目](#題目)
    - [解法](#解法)
    - [結果](#結果)
<!-- TOC END -->


## [題目](https://leetcode.com/problems/min-stack/)



Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- getMin() -- Retrieve the minimum element in the stack.

## 解法
```Python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.t = []

    def push(self, x: int) -> None:
        self.t.append(x)

    def pop(self) -> None:
        self.t=self.t[:-1]

    def top(self) -> int:
        return self.t[-1]

    def getMin(self) -> int:
        return sorted(self.t)[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```
## 結果
![](https://i.imgur.com/5ELPFKR.png)
