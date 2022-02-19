class Solution:
    def knightProbability(self, n: int, k: int, r: int, c: int) -> float:
        return sum(reduce(lambda p, _: {(i, j): sum(p.get((i + u, j + v), 0.0) + p.get((i + v, j + u), 0.0) for u, v in product((1, -1), (2, -2))) / 8.0 for i, j in product(range(n), range(n))}, range(k) , {(r, c): 1}).values())
