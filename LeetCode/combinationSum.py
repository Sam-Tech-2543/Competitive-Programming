# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, lst, total):
            if total == target:
                ans.append(lst.copy())
                return
            elif total > target or i >= len(candidates):
                return

            # Duplicates on the left Decision Tree are allowed
            lst.append(candidates[i])
            dfs(i, lst, total + candidates[i])

            # The Duplicate is removed as we want to go on the right of the decision tree
            lst.pop()
            # We do now allow duplicates in the right decision tree
            dfs(i + 1, lst, total)

        dfs(0, [], 0)

        return ans


s = Solution()


# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
s.combinationSum([2, 3, 6, 7], 7)

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
s.combinationSum([2, 3, 5], 8)
