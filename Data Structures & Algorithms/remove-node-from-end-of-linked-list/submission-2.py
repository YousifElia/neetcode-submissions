# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        fast = slow = dummy

        # move fast n steps ahead
        for i in range(n):
            fast = fast.next

        # fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # we need to find the node right before we delete it
        slow.next = slow.next.next

        return dummy.next
        # if head = None
        #   return
        #
        # current = 0
        # while current != n
        # head.next
        #
        # if current == n
        #  prev.next = cur.next
