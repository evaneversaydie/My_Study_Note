class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket=[None]*100

    def add(self, key: int) -> None:
        g = key%100
        if self.bucket[g]==None:
            self.bucket[g]=[]
            self.bucket[g].append(key)
            # self.bucket[g].sorted()
        elif key not in self.bucket[g]:
            self.bucket[g].append(key)

    def remove(self, key: int) -> None:
        g = key%100
        if self.bucket[g]==None:
            return
        elif key in self.bucket[g]:
            self.bucket[g].remove(key)


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        g = key%100
        if self.bucket[g]==None:
            return False
        elif key in self.bucket[g]:
            return True
        elif key not in self.bucket[g]:
            return False
