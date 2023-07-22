# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/

class Solution:
    def recursion(self,x,ans,n) -> float:
        if n==0:
            return ans
        else:
            if n%2==0:
                x*=x
                n/=2
            else:
                ans=ans*x
                n=n-1

            return self.recursion(x,ans,n)
        

    def myPow(self, x: float, n: int) -> float:
        ans=self.recursion(x,1,abs(n))
        if n<0:
            ans=1/ans
        return ans
        # return x**n


s=Solution()

print(s.myPow(2.00000,10))
print(s.myPow(2.10000,3))
print(s.myPow(2.00000,-2))