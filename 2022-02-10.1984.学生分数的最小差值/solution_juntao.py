class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0

        ans = 100000
        nums.sort()
        for i in range(len(nums) - k + 1):
            if (nums[i + k - 1] - nums[i] < ans):
                ans = nums[i + k - 1] - nums[i]
        return ans