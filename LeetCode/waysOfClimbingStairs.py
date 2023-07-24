# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:

        # lst=[i for i in range(n-1)]
        # lst.append(1)
        # lst.append(1)

        # for i in range(len(lst)-3,-1,-1):
        #     lst[i]=lst[i+1]+lst[i+2]

        # return lst[0]

        secondLast,last=1,1

        for i in range(0,n-1):
            temp=secondLast
            secondLast=last+temp
            last=temp

        return secondLast

s=Solution()

# Input: n = 3
# Output: 3
print(s.climbStairs(3))

print(s.climbStairs(7))
