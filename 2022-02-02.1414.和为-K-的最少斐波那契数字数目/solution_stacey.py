class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        cur = 1
        nums = [1]
        while cur<=k:
            nums.append(cur)
            cur = cur+nums[-2]
        count=0
        i=len(nums)-1
        while i>=0 and k>0:
            if nums[i]==k:
                return count+1
            elif nums[i]>k:
                i-=1
                continue
            else:
                k=k-nums[i]
                i-=1
                count+=1