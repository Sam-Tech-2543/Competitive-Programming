# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        ans=0
        l,r=0,1
        while r<len(intervals):
            if intervals[l][0]==intervals[r][0] and intervals[l][1]==intervals[r][1]:
                ans+=1
                r+=1
            elif intervals[l][1]>intervals[r][0]:
                ans+=1
                if intervals[l][1]>intervals[r][1]:
                    l=r
                r+=1
            else:
                l=r
                r+=1

        return ans
    

s=Solution()

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))

print(s.eraseOverlapIntervals([[1,2],[1,3],[1,4]])) #2

print(s.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]])) #2

print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]])) #2

print(s.eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]])) #2