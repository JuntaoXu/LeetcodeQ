class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min = [min(i) for i in matrix]
        col_max = [max(j) for j in zip(* matrix)]
        return [k for k in row_min if k in col_max]