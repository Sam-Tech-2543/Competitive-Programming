class Solution:
    def twoSumCloset(self, nums, target):
        pair= None
        minVal= float('inf')

        nums.sort()

        left, right = 0, len(nums)-1
        while left<right:
            diff=abs(nums[left]+nums[right]-target)
            if diff<minVal:
                minVal=diff
                pair=(nums[left], nums[right])
            if nums[left]+nums[right]>target:
                right-=1
            else:
                left+=1

        return pair
    

s=Solution()
print(s.twoSumCloset([10,20,30,40,50], 100))
print(s.twoSumCloset([-1, 2, 1, -4], 4))
