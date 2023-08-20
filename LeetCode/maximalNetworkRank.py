# 1615. Maximal Network Rank
# https://leetcode.com/problems/maximal-network-rank/

from typing import List
from collections import defaultdict


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        ans = 0
        myHash = defaultdict(set)

        for i in roads:
            myHash[i[0]].add(i[1])
            myHash[i[1]].add(i[0])

        for i in range(n):
            for j in range(i + 1, n):
                curr = len(myHash[i]) + len(myHash[j])
                if j in myHash[i]:
                    curr -= 1

                ans = max(ans, curr)

        return ans


s = Solution()


# Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
# Output: 4
# Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1.
# The road between 0 and 1 is only counted once.
n = 4
roads = [[0, 1], [0, 3], [1, 2], [1, 3]]
print(s.maximalNetworkRank(n, roads))


# Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
# Output: 5
# Explanation: There are 5 roads that are connected to cities 1 or 2.
n = 5
roads = [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]
print(s.maximalNetworkRank(n, roads))


# Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
# Output: 5
# Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.
n = 8
roads = [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]
print(s.maximalNetworkRank(n, roads))
