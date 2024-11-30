# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #remove all values that repeast includingoriginga
        dummy = ListNode(0,head)
        prev = dummy
        while head:
            if head.next and head.next.val == head.val:
                while head.next and head.val == head.next.val :
                    head = head.next
                #purge
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next