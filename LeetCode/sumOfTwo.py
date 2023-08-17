# 371. Sum of Two Integers
# https://leetcode.com/problems/sum-of-two-integers/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # n1=0
        # n2=0
        # while a>0 and b>0:
        #     n1=n1|(a^b)
        #     n2=n2|(a&b) #Problem
        #     print(bin(a),bin(b),bin(n1),n1,bin(n2),n2,a&b)
        #     a>>=1
        #     b>>=1
        #     n1<<=1
        #     n2<<=1
    
        # Problem in Python
        # while b!=0:
        #     temp=(a&b)<<1
        #     a=a^b
        #     b=temp
        #     print(a,bin(a),b,bin(b))

        # return a
        return sum([a,b])

s=Solution()

print(s.getSum(9,11))