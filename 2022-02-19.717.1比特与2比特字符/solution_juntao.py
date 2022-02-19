class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = n - 2
        while bits[i] and bits[i] == 1:
            i -= 1
        return (n - i) % 2 == 0