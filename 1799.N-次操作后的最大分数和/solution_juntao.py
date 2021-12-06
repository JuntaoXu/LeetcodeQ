class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (1 << n)
        for i in range(1 << n):
            cnt = bin(i).count('1')
            if cnt & 1: continue
            for j in range(n):
                for k in range(j + 1, n):
                    tmp = (1 << j) | (1 << k)
                    if tmp & i == tmp:
                        dp[i] = max(dp[i], dp[i - tmp] + gcd(nums[j], nums[k]) * cnt // 2)
        return dp[-1]


