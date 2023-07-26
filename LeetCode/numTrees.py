# 96. Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def numTrees(self, n: int) -> int:
        lst=[1,1]

        for nodes in range(2,n+1):
            totalWays=0
            for root in range(1,nodes+1):
                totalWays+=(lst[root-1]*lst[nodes-root])
            lst.append(totalWays)

        return lst[n]