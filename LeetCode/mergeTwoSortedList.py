# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        current = temp

        while current.next and current.next.next:
            n1 = current.next
            n2 = current.next.next
            n1.next = n2.next
            current.next = n2
            current.next.next = n1
            current = current.next.next
            
        return temp.next