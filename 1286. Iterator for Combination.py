#  https://leetcode.com/problems/iterator-for-combination/

class CombinationIterator:

    def __init__(self, s: str, k: int):
        self.arr = itertools.combinations(s, k)
        self.arr = ["".join(c) for c in self.arr]
        self.cur = -1

    def next(self) -> str:
        if self.hasNext():
            self.cur += 1
            return self.arr[self.cur]

    def hasNext(self) -> bool:
        return self.cur + 1 < len(self.arr)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
