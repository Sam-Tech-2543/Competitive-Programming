# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = 0, 0
        rn, cn = len(matrix), len(matrix[0])

        if rn == 1 and cn == 1:
            return target == matrix[0][0]

        while r < rn and c < cn:
            if target > matrix[r][-1]:
                r += 1
            elif target < matrix[r][-1]:
                for i in range(0, cn):
                    if matrix[r][i] == target:
                        return True
                return False
            else:
                return True

        return False


s = Solution()

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
