# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
        
        mid = length // 2
        curr = head

        for i in range(mid):
            curr = curr.next
        return curr