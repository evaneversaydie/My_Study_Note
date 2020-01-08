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