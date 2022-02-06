class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ls = [['a',a],['b', b],['c', c]]
        res = ''

        flag = True
        while flag:
            flag = False
            ls.sort(key = lambda x: x[1],reverse = True)

            for element in ls:
                if (len(res) < 2 or not res[-2] == res[-1] == element[0]):
                    if element[1] > 0:
                            flag = True
                            res += element[0]
                            element[1] -= 1
                            break

        return res