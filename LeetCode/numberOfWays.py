# 2787. Ways to Express an Integer as Sum of Powers
# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp={}

        def recursion(i,curr):
            if curr==0:
                return 1
            elif curr<0 or i>n or i**x>curr:
                return 0
            elif (i,curr) in dp:
                return dp[(i,curr)]
            else:
                dp[(i,curr)]=recursion(i+1,curr-(i**x))+recursion(i+1,curr)
                return dp[(i,curr)]

        return recursion(1,n) % (10**9+7)
    

s=Solution()

# Input: n = 10, x = 2
# Output: 1
print(s.numberOfWays(10,2))

# Input: n = 4, x = 1
# Output: 2
print(s.numberOfWays(4,1))

# n = 213 x = 1
# 55852583
print(s.numberOfWays(213,1))


# class Solution:
#     def numberOfWays(self, n: int, x: int) -> int:
#         dp={}

#         def recursion(i,curr):
#             if curr==n:
#                 return 1
#             elif curr>n or i>n or i**x>n:
#                 return 0
#             elif (i,curr) in dp:
#                 return dp[(i,curr)]
#             else:
#                 dp[(i,curr)]=recursion(i+1,curr+i**x)+recursion(i+1,curr)
#                 return dp[(i,curr)]

#         return recursion(1,0) % (10**9+7)


