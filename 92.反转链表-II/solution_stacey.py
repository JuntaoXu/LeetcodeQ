# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        cnt = 1
        start = head
        cur = head
        while cnt < left:
            cnt +=1
            start = cur
            cur = cur.next
        prev = None
        tail = cur
        while cnt <= right:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            cnt += 1
        start.next = prev
        tail.next = cur
        # if reversing the list from the start, head is actually point to the end of the reversed
        # list, and the actual start is the prev which is also the start of the reversed list
        if left > 1:
            return head
        else:
            return prev


