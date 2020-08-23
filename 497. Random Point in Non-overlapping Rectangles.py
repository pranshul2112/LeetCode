#  https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.total = 0
        self.w = []
        for x1, y1, x2, y2 in self.rects:
            c = (y2 - y1 + 1) * (x2 - x1 + 1)
            self.total += c
            self.w.append(c)
        self.w = [c/self.total for c in self.w]

    def pick(self) -> List[int]:
        index = random.choices(range(len(self.rects)), self.w)[0]
        x1, y1, x2, y2 = self.rects[index]
        
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
