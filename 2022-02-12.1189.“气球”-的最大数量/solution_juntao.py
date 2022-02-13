class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(text.count('a'), text.count('b'), text.count('n'), int(text.count('l')/2), int(text.count('o')/2))

