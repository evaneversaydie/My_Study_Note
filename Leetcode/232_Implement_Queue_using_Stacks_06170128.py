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

