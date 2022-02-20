class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        temp = ""   # set temp
        while dominoes != temp:
            temp = dominoes # store dominos before time elapse
            dominoes = dominoes.replace("R.L", "I") # protect domino between drop from both side
            dominoes = dominoes.replace(".L", "LL") # all left falls
            dominoes = dominoes.replace("R.", "RR") # all right falls
            dominoes = dominoes.replace("I", "R.L") # unprotect
        return dominoes