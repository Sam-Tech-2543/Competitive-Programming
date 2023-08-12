# 113. Path Sum II
# https://leetcode.com/problems/path-sum-ii/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, currSum, temp, lst):
            if not root:
                return

            currSum += root.val
            temp.append(root.val)
            if not root.left and not root.right:
                if currSum == targetSum:
                    lst.append(temp.copy())
                temp.pop()
                return

            dfs(root.left, currSum, temp, lst)
            dfs(root.right, currSum, temp, lst)
            temp.pop()

        temp, lst = [], []
        dfs(root, 0, temp, lst)

        return lst
