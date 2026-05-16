# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        listset = set()
        current = head
        while current is not None:
            listset.add(current)
            current = current.next
            if current in listset:
                return True
        return False
        