# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # The heap will store tuples (node value, unique id, node)
        # The unique id breaks ties when two nodes have the same value
        # (heapq requires the elements to be comparable).
        min_heap = []
        for idx, node in enumerate(lists):
            if node:                         # ignore empty lists
                heapq.heappush(min_heap, (node.val, idx, node))

        # Dummy head makes list construction easier
        dummy = ListNode(0)
        cur = dummy

        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            cur.next = ListNode(val)        # attach the smallest node
            cur = cur.next

            # Advance in the list that this node came from
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))

        return dummy.next
# List1[], List2[], ListN[]
# 
# [[1,2,4],[1,3,5],[3,6]]
#   i              
# 
# iterate through all the lists and put them in a heap
# put them in an array then .sort time compl O(nlogn)
# dont know how to code this tho