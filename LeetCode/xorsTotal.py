# 1863. Sum of All Subset XOR Totals
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class SolutionOld(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mainAns=0
        for i in range(2**len(nums)):
            tempAns=0
            for j in range(len(nums)):
                if(i&(1<<j)):
                    tempAns^=nums[j]
            mainAns+=tempAns

        return mainAns
    
class Solution(object):
    def backtracking(self, index, ans):
        if(index==len(nums)):
            return ans
        
        

    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums=nums
        

s=Solution()

# Input: nums = [1,3]
# Output: 6
nums = [1,3]
print(s.subsetXORSum(nums))

# Input: nums = [5,1,6]
# Output: 28
nums = [5,1,6]
print(s.subsetXORSum(nums))

# Input: nums = [3,4,5,6,7,8]
# Output: 480
nums = [3,4,5,6,7,8]
print(s.subsetXORSum(nums))


            
