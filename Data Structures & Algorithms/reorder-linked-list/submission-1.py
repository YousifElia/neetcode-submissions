# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
            
        nodes = []
        current = head

        while current:
            nodes.append(current)
            current = current.next
        
        left, right = 0, len(nodes) - 1
        
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            if left == right:
                break
            nodes[right].next = nodes[left]
            right -= 1

        nodes[left].next = None        

# 0, 1, 2, 3, 4, 5, 6
# l,  ,  ,  ,  ,  , r  ; l = 0, r = len(head) - 1
# 
# 0, 1, 2, 3, 4, 5, 6
# l,  ,  ,  ,  ,  , r (.append(l))
# 
# 0, 1, 2, 3, 4, 5, 6
# l,  ,  ,  ,  ,  , r (.append(r))
# 
# 0, 1, 2, 3, 4, 5, 6
#  , l,  ,  ,  ,  r,  (l++, r--)
# 
# etc, etc ..
#
# 0, 1, 2, 3, 4, 5, 6
#  ,  , l, r,  ,  ,   (while index of l != r)