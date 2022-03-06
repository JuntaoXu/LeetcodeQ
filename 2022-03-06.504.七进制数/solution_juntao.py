class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = []
        if num == 0:
            return str(0)

        flag = num < 0
        num = abs(num)

        while num > 0:
            ans.append(num % 7)
            num //= 7

        if flag:
            ans.append("-")

        return ''.join([str(i) for i in reversed(ans)])
