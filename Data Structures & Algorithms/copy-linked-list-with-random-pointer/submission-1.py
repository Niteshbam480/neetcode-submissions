"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        curr=head
        nodes = {}
        while curr:
            node = Node(curr.val)
            nodes[curr] = node
            curr=curr.next
        curr=head
        while curr:
            node=nodes[curr]
            node.next = nodes.get(curr.next)
            node.random = nodes.get(curr.random)
            curr=curr.next
        
        return nodes[head]
        