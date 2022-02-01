class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) <2:
            return ""
        i = 0
        while i < len(s):
            if s[i].upper() not in s or s[i].lower() not in s:
                return max(self.longestNiceSubstring(s[:i]), self.longestNiceSubstring(s[i+1:]), key = len)
            i += 1
        return s
