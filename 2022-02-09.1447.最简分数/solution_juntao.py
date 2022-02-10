class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans, i, j = [], 1, 2
        while i < n:
            while j <= n:
                if gcd(i, j) == 1 and i < j:
                    ans.append(str(i) + "/" + str(j))
                j += 1
            j = 2
            i += 1
        return ans
