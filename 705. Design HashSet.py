#  https://leetcode.com/problems/design-hashset/

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.matrix = [[] for i in range(1000)]
        self.hashMax = False
    def row(self, item):
        return item // self.size

    def col(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        if key < 1000000:
            r = self.row(key)
            c = self.col(key)
            if not self.matrix[r]:
                self.matrix[r] = [False] * self.size
            self.matrix[r][c] = True
        else:
            self.hashMax = True
    def remove(self, key: int) -> None:
        if key < 1000000:
            r = self.row(key)
            c = self.col(key)
            if self.matrix[r] and self.matrix[r][c]:
                self.matrix[r][c] = False
        if key == 1000000:
            self.hashMax = True

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key == 1000000:
            if self.hashMax:
                return False
        r = self.row(key)
        c = self.col(key)
        if self.matrix[r] and self.matrix[r][c]:
            return True
        return False
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
