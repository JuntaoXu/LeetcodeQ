class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num  # a ^ b ^ b = a
        return ans