# 445. Add Two Numbers II
# https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        lst1 = []
        lst2 = []

        while l1:
            lst1.append(l1.val)
            l1 = l1.next

        while l2:
            lst2.append(l2.val)
            l2 = l2.next

        head = None
        c = 0
        while len(lst1) > 0 and len(lst2) > 0:
            n1 = lst1.pop()
            n2 = lst2.pop()
            n3 = n1 + n2 + c
            if n3 >= 10:
                temp = head
                head = ListNode(n3 - 10)
                head.next = temp
                c = 1
            else:
                c = 0
                temp = head
                head = ListNode(n3)
                head.next = temp

        if len(lst1) > len(lst2):
            lst3 = lst1
        elif len(lst2) > len(lst1):
            lst3 = lst2
        else:
            if c == 1:
                temp = head
                head = ListNode(1)
                head.next = temp

            return head

        while len(lst3) > 0:
            n1 = lst3.pop() + c

            if n1 >= 10:
                c = 1
                n1 = n1 - 10
            else:
                c = 0

            temp = head
            head = ListNode(n1)
            head.next = temp

        if c == 1:
            temp = head
            head = ListNode(1)
            head.next = temp

        return head
