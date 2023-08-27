# 2834. Find the Minimum Possible Sum of a Beautiful Array
# https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        l=0
        lst=set()
        i=1
        ans=0

        while l<n:
            if target-i in lst:
                i+=1
                continue
            lst.add(i)
            ans+=i
            l+=1
            i+=1

        return ans
    
s=Solution()

print(s.minimumPossibleSum(3, 3))