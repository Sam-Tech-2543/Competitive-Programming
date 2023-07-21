# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            n=numbers[l]+numbers[r]
            if n>target:
                r-=1
            elif n<target:
                l+=1
            else:
                return [l+1,r+1]

s=Solution()

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
print(s.twoSum([2,7,11,15],9))

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
print(s.twoSum([2,3,4],6))

print(s.twoSum([0,0,3,4],0))