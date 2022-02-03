class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if not k:
            return 0
        f0, f1 = 1, 1   # first two fibonacci numbers
        while f1 <= k:  # get the closest fibonacci number f0 to k
            f0 = f1     # next step
            f1 = f0 + f1    # Fn = Fn-1 + Fn-2
        return 1 + self.findMinFibonacciNumbers(k - f0)
        # return +1 fibonacci number required, residual value for k - f0