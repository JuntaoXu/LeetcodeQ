from math import gcd

class Solution:
    def maxScore(self, nums) -> int:
        n=len(nums)
        # 2^n
        dp=[0]*(1<<n)
        for i in range(1<<n):
            # checking number of 1s in the binary form of i
            cnt=bin(i).count('1')
            # if cnt is odd continue
            if cnt&1:continue

            for j in range(n):
                for k in range(j+1,n):
                    # tmp = 2^j + 2^k
                    tmp=(1<<j)|(1<<k)
                    # makes sure the 2 number chosen is at position j and position k
                    # eg: j=1,k=3,tmp=10
                    # when i==6, bin(i)=1010,tmp&i==tmp,the position(reverse order) of 1s match with j and k
                    if tmp&i==tmp:
                        print('j,k,tmp,i:',j,k,tmp,i)
                        print('dp[i],dp[i-tmp],gcd,cnt: ',
                              dp[i],dp[i-tmp],gcd(nums[j],nums[k])*cnt//2, cnt)
                        dp[i]=max(dp[i],dp[i-tmp]+gcd(nums[j],nums[k])*cnt//2)
                        print(dp)
        return dp[-1]

# sol = Solution()
# n = sol.maxScore([1,2,3,4])
# print(n)
