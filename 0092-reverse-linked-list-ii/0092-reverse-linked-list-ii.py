# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        leftprev, curr = dummy, head
        for _ in range(left-1):
            leftprev = curr
            curr = curr.next
        #curr at left and leftprev is one before that
        prev = None
        for _ in range(right-left+1):
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        
        leftprev.next.next = curr
        leftprev.next = prev

        return dummy.next
        