# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head=ListNode()
               
        while True:
            minVal=float('inf')
            minIndex=-1
            for i in range(len(lists)):
                if lists[i] and lists[i].val<minVal:
                    minVal=lists[i].val
                    minIndex=i
            if minIndex==-1:
                break

            temp1=ListNode(minVal)
            if not head.next:
                head.next=temp1
                temp=temp1
            else:
                temp.next=temp1
                temp=temp1

            lists[minIndex]=lists[minIndex].next

        return head.next