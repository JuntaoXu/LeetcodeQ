class Solution():
    def bestRotation(self, A):
        score = [0] * len(A)
        for i in range(len(A)):
            score[(i + len(A) - A[i] + 1) % len(A)] -= 1
        for i in range(1, len(A)):
            score[i] += score[i - 1] + 1
        return score.index(max(score))