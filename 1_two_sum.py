class two_sum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

'''
has complexity of n^2
'''

class two_sum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = dict()
        for i, num in enumerate(nums):
            # for all elements in nums, append index number at start,
            # creating a tuple (index of element, nums) inside a new list
            if target - num in dictionary:
                return [dictionary[target - num], i]
            dictionary[nums[i]] = i
        return []

'''
has complexity of n
'''

