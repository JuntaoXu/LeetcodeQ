class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        ret = []

        def f(r):
            ret.append(r.val)
            for child in r.children:
                f(child)

        f(root)
        return ret