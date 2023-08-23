# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/

from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counting=Counter(tasks)
        myHeap=[-i for i in counting.values()]
        heapq.heapify(myHeap)
        q=deque()
        ans=0

        while myHeap or q:
            ans+=1
            
            if myHeap:
                t=heappop(myHeap)+1
                if t:
                    # Count of the task, Time when it will be availabe
                    q.append([t,ans+n]) 
            
            if q and q[0][1]<=ans:
                heappush(myHeap,q.popleft()[0])
                

        return ans