# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digits = 0
        num1 = 0
        while l1:
            mult = 10**digits
            num1 += l1.val*mult
            l1=l1.next
            digits+=1
        digits = 0
        num2 = 0
        while l2:
            mult = 10**digits
            num2 += l2.val*mult
            l2=l2.next
            digits+=1
        
        sum = num1+num2
        prev = ListNode(sum%10)
        res_head=prev
        sum = sum//10
        while sum>0:
            val=sum%10
            sum=sum//10
            prev.next=ListNode(val)
            prev=prev.next
        return res_head
