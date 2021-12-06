"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return
        cur_node = head
        while cur_node:
            if cur_node.child:
                next = cur_node.next
                cur_node.next = cur_node.child
                cur_node.next.prev = cur_node
                cur = cur_node.next
                while cur.next:
                    cur = cur.next
                cur.next = next
                if next:
                    next.prev = cur
                cur_node.child = None
            cur_node = cur_node.next
        return head