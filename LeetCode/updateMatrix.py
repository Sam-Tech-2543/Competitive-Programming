# 542. 01 Matrix
# https://leetcode.com/problems/01-matrix/

from collections import deque
from typing import List

from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n,m=len(mat),len(mat[0])

        visited=[[0 for _ in range(m)] for _ in range(n)]
        dist=[[0 for _ in range(m)] for _ in range(n)]

        direction=[[1,0],[-1,0],[0,-1],[0,1]]

        q=deque()

        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    visited[i][j]=1
                    q.append((i,j,0))

        while q:
            temp=q.popleft()
            for i in direction:
                r,c=temp[0]+i[0],temp[1]+i[1]
                if r>=0 and r<n and c>=0 and c<m and visited[r][c]==0:
                    d=temp[2]+1
                    dist[r][c]=d
                    visited[r][c]=1
                    q.append((r,c,d))

        return dist
    

s=Solution()

# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
s.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])

# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
