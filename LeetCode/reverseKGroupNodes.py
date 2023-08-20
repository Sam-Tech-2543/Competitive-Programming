from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next==None:
            return head

        dummy=ListNode(0)
        dummy.next=head
        head=dummy
        
        l,r=head.next,head.next
        grpPrev=dummy
    
        start=True

        while True:
            kth = self.getKth(grpPrev,k)
            if not kth:
                break
                
            grpNext=kth.next

            prev,curr=grpNext,grpPrev.next

            while curr!=grpNext:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp

            temp=grpPrev.next
            grpPrev.next=kth
            grpPrev=temp

        return dummy.next

    def getKth(self, curr, c):
        while c>0 and curr:
            curr=curr.next
            c-=1
        return curr