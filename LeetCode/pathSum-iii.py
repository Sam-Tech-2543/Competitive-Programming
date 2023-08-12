# 437. Path Sum III
# https://leetcode.com/problems/path-sum-iii/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans=0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        temp=[]

        def dfs(root, temp):
            if not root:
                return

            temp.append(root.val)

            dfs(root.left,temp)
            dfs(root.right,temp)

            sVal=0
            for i in temp[::-1]:
                sVal+=i
                if sVal==targetSum:
                    self.ans+=1

            temp.pop()

        dfs(root,temp)

        return self.ans