class Solution(object):
    def reverseOnlyLetters(self, S):
        letters = [c for c in S if c.isalpha()]     # create ls with only alphabets
        ans = []
        for c in S:
            if c.isalpha():     # when char is an alphabet
                ans.append(letters.pop())   # ans append letters -1
            else:
                ans.append(c)   # append the char if char not an alphabet
        return "".join(ans)