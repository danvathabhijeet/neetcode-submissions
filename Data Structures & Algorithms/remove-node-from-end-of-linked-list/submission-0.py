# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        firstpointer = head
        secondpointer = head

        for _ in range(n):
            secondpointer = secondpointer.next

        if secondpointer is None:
            return head.next

        while secondpointer.next is not None:
            secondpointer = secondpointer.next
            firstpointer = firstpointer.next

        firstpointer.next = firstpointer.next.next

        return head
        