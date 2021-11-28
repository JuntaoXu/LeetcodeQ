class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast and slow:
            if slow.next and fast.next:
                slow = slow.next
                fast = fast.next.next
            else:
                break
            if fast == slow:
                return True
        return False
