class Solution:
    def nearestPalindromic(self, n: str) -> str:
        l = len(n)
        if l == 1:
            return str(int(n) - 1)
        s = n[: l // 2 + l % 2]
        s1 = str(int(s) - 1)
        s2 = str(int(s) + 1)
        return min(
            '9' * (l - 1),
            '1' + '0' * (l - 1) + '1',
            s + s[-1 - l % 2::-1],
            s1 + s1[-1 - l % 2::-1],
            s2 + s2[-1 - l % 2::-1],
            key=lambda x: (abs(int(x) - int(n)) or 114514, int(x))
        )