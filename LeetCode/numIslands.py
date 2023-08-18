# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/description/

from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        n, m = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))

            while q:
                temp = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for i in directions:
                    nr = temp[0] + i[0]
                    nc = temp[1] + i[1]
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = -1

        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    bfs(i, j)
                    grid[i][j] = -1
                    ans += 1

        return ans
