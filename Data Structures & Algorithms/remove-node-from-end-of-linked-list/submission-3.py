# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr=curr.next
            length+=1
        
        if length ==1 or length ==0:
            head=None
            return head
        
        nth = length-n
        
        if nth ==0:
            head=head.next
            return head
        curr=head
        for _ in range(nth-1):
            curr=curr.next
        temp = curr.next
        if temp:
            curr.next = curr.next.next
        else:
            curr.next=None
        
        return head
        
        

        
