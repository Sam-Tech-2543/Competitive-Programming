# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans=[]

        def backTracking(start,lst,curr):
            if curr==0:
                self.ans.append(lst.copy())
            if curr<=0:
                return

            prev=-1
            for i in range(start, len(candidates)):
                if candidates[i]==prev:
                    continue
                lst.append(candidates[i])
                backTracking(i+1,lst,curr-candidates[i])

                lst.pop()
                prev=candidates[i]

        backTracking(0,[],target)

        return self.ans