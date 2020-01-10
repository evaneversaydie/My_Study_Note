class MyQueue:

    def __init__(self):
        self.data=[]
        self.data1=self.data[::-1]

    def push(self, x: int) -> None:
        self.data.append(x)


    def pop(self) -> int:
        a =  self.data[0]
        self.data = self.data[1:]
        return a

    def peek(self) -> int:
        return self.data[0]

    def empty(self) -> bool:
        if len(self.data)==0:
            return True
        else:
            return False

