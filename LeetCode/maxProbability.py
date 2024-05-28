from collections import defaultdict
import heapq
from typing import List
from pprint import pprint

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj=defaultdict(list)
        for i in range(len(edges)):
            adj[edges[i][0]].append([edges[i][1],succProb[i]])
            adj[edges[i][1]].append([edges[i][0],succProb[i]])

        mySet=[[start_node,-1]]
        ans={}
        while mySet:
            i1,i2 = heapq.heappop(mySet)
            if i1 in ans:
                continue
            ans[i1]=i2

            for j1,j2 in adj[i1]:
                heapq.heappush(mySet, [j1, i2*j2])

        return ans.get(end_node,0)*-1

        

s=Solution()

edges = [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]]
succProb = [0.37,0.17,0.93,0.23,0.39,0.04]
start_node = 3
end_node = 4

print(s.maxProbability(5,edges,succProb,start_node,end_node))