"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        st, res = [root], []
        while st and st[0]:
            x = st.pop()
            res.append(x.val)
            st.extend(x.children)
        return res[::-1]
