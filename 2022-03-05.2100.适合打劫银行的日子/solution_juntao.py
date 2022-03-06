class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        left, right = [0] * n, [0] * n
        for i in range(1, n):
            if security[i - 1] >= security[i]:
                left[i] = left[i - 1] + 1
            if security[n - i] >= security[n - 1 - i]:
                right[n - 1 - i] = right[n - i] + 1
        return [i for i in range(n) if left[i] >= time and right[i] >= time]