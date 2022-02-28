class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        words = ["" for _ in range(numRows)]

        i, flag = 0, -1
        for char in s:
            words[i] += char
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag

        return "".join(words)