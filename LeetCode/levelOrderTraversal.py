# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        nodes=[root]

        ans=[]
        values=[root.val]

        while nodes:
            ans.append(values)

            temp=[]
            values=[]

            for j in nodes:
                if j.left:
                    temp.append(j.left)
                    values.append(j.left.val)
                if j.right:
                    temp.append(j.right)
                    values.append(j.right.val)
            nodes=temp

        return ans