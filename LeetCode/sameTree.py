# 100. Same Tree
# https://leetcode.com/problems/same-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(t1, t2):
            if (t1 and not t2) or (t2 and not t1):
                return False
            if not t1 and not t2:
                return True

            if t1.val == t2.val:
                return dfs(t1.left, t2.left) and dfs(t1.right, t2.right)

        return dfs(p, q)
