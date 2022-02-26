class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # (a + bi) * (c + di) ==> (ac - bd) + (bc+ad)i
        arr1 = num1.split('+')
        arr2 = num2.split('+')
        a,bi = int(arr1[0]),int(arr1[1][:-1])
        c,di = int(arr2[0]),int(arr2[1][:-1])
        return str(a*c-bi*di)+'+'+str(bi*c+a*di)+'i'