# 63. Unique Paths II
# https://leetcode.com/problems/unique-paths-ii/

from typing import List


class Solution:
    def uniquePathsWithObstaclesErrorWhenADiagonalRestrictsTheTarget(
        self, obstacleGrid: List[List[int]]
    ) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0

        r = len(obstacleGrid) - 1
        c = len(obstacleGrid[0]) - 1

        row = [0] * (c + 1)
        flag = 1
        for i in range(c, -1, -1):
            if obstacleGrid[-1][i] == 1:
                flag = 0
                continue
            row[i] = flag
            if not flag:
                flag = 1

        if row == [0] * (c + 1):
            return 0

        for i in range(r - 1, -1, -1):
            nRow = [0] * (c + 1)
            if obstacleGrid[i][-1] == 0:
                nRow[-1] = 1

            for j in range(c - 1, -1, -1):
                if obstacleGrid[i][j] == 0:
                    nRow[j] = nRow[j + 1] + row[j]
            row = nRow
            if row == [0] * (c + 1):
                return 0

        return row[0]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0

        r = len(obstacleGrid)
        c = len(obstacleGrid[0])

        row = [0] * (c)
        row[-1] = 1

        for i in range(r - 1, -1, -1):
            for j in range(c - 1, -1, -1):
                if obstacleGrid[i][j]:
                    row[j] = 0
                elif j + 1 < c:
                    row[j] += row[j + 1]

        return row[0]


s = Solution()

print(s.uniquePathsWithObstacles([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]]))

# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))

# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
print(s.uniquePathsWithObstacles([[0, 1], [0, 0]]))

# obstacleGrid = [[0,0],[0,1]]      0
print(s.uniquePathsWithObstacles([[0, 0], [0, 1]]))

print(s.uniquePathsWithObstacles([[0, 0], [1, 1], [0, 0]]))
