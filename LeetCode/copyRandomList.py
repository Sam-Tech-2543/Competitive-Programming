# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/description/

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        myHash = {None: None}

        temp = head
        while temp:
            copy = Node(temp.val)
            myHash[temp] = copy

            temp = temp.next

        temp = head
        while temp:
            myNode = myHash[temp]
            myNode.next = myHash[temp.next]
            myNode.random = myHash[temp.random]

            temp = temp.next

        return myHash[head]
