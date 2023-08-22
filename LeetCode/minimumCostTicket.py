# 983. Minimum Cost For Tickets
# https://leetcode.com/problems/minimum-cost-for-tickets/

from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp={}

        def dfs(i):
            if i==len(days):
                return 0

            if i in dp:
                return dp[i]

            dp[i]=float('inf')
            for d,c in zip([1,7,30], costs):
                j=1
                while j<len(days) and days[j]<days[i]+d:
                    j+=1

                dp[i]=min(dp[i],c+dfs(j))

            return dfs(i)

        return dfs(0)


s=Solution()
print(s.mincostTickets([1,4,6,7,8,20],[2,7,15]))

print(s.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31],[2,7,15]))
