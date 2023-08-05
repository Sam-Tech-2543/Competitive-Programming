# 95. Unique Binary Search Trees II
# https://leetcode.com/problems/unique-binary-search-trees-ii/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(left, right):
            if left == right:
                return [TreeNode(left)]
            if left > right:
                return [None]

            ans = []

            for i in range(left, right + 1):
                for l in generate(left, i - 1):
                    for r in generate(i + 1, right):
                        root = TreeNode(i, l, r)
                        ans.append(root)
            return ans

        return generate(1, n)


s = Solution()


# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
print(s.generateTrees(3))

# Input: n = 1
# Output: [[1]]
print(s.generateTrees(1))
