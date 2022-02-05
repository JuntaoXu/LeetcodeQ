class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = 0
        unique = list(dict.fromkeys(nums))
        count = dict(Counter(nums))
        for element in unique:
            if count[element] == 1:
                ans += element
        return ans