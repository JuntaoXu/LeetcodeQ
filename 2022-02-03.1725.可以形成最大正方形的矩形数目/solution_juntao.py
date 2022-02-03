class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxlen, count = 0, 0
        for rectangle in rectangles:
            len = min(rectangle[0], rectangle[1])
            if len > maxlen:
                count = 1
                maxlen = len
            elif len == maxlen:
                count += 1
        return count