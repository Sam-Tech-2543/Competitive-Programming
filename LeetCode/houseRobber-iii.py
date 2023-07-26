# 337. House Robber III
# https://leetcode.com/problems/house-robber-iii/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root: Optional[TreeNode]):
        if root is None:
            return [0, 0]

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        withRoot = root.val + left[1] + right[1]
        withoutRoot = max(left) + max(right)

        return [withRoot, withoutRoot]

    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root))
