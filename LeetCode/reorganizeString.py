# 767. Reorganize String
# https://leetcode.com/problems/reorganize-string/

from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def reorganizeString(self, s: str) -> str:
        myHeap = [(-count, char) for char, count in Counter(s).items()]
        heapify(myHeap)

        ans=""

        while myHeap:
            i1,c1=heappop(myHeap)
            if not ans or ans[-1]!=c1:
                ans+=c1
                if i1+1!=0:
                    heappush(myHeap,(i1+1,c1))
            else:
                if not myHeap:
                    return ""
                i2,c2=heappop(myHeap)
                ans+=c2
                if i2+1!=0:
                    heappush(myHeap,(i2+1,c2))
                heappush(myHeap,(i1,c1))

        return ans
                
                            
