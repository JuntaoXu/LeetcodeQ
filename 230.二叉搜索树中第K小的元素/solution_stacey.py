# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curNode = root
        stack=[]
        while curNode is not None or stack:
            while curNode:
                stack.append(curNode)
                curNode = curNode.left
            curNode = stack.pop()
            k-=1
            if k == 0:
                return curNode.val
            curNode = curNode.right