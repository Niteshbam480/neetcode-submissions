# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        if length <= 1:
            return
        curr = head
        mid_length = (length + 1) // 2
        for _ in range(mid_length - 1):
            curr = curr.next
        second = curr.next
        curr.next = None
        rev = self.reverseList(second)
        first = head
        while rev:
            tmp1, tmp2 = first.next, rev.next
            first.next = rev
            rev.next = tmp1
            first, rev = tmp1, tmp2
    
    def reverseList(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev