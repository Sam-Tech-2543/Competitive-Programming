<!-- https://leetcode.com/problems/check-if-array-is-good/ -->

# Intuition
- The most common approach is to sort the array, then check if array have [1,...,n-1] and last two elements (n) are same. If above conditions are satisfied then return True else return False. The sorting Algorithm takes O(nLogn) complexity. 
- Utilising a hash map is an alternative strategy, although this will increase space complexity.

# Approach
- If we look the problem carefully, all the elements from 0 to n-1 occur only once except the n has occured twice in the array. 
- So we can just iterate through 0 to length of array. Store sum of all elements of array in s1 (sum1) and store the sum of indices in s2 (sum2). 
- s2 will be exactly s1+1 as instead of having the maximum two elements in array as n and n+1, we have n twice.

# Complexity
- Time complexity: O(n)

- Space complexity: O(1)

# Code
```
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        s1,s2=0,0
        for i in range(len(nums)):
            s1+=nums[i]
            s2+=(i+1)

        return s2==s1+1
```