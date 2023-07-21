# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x)=="".join([i for i in str(x)[::-1]])
    
        if x<0:
            return False
        
        backUp=x

        rev=0
        while x!=0:
            n1=x%10
            x-=n1
            x/=10

            rev=(rev*10)+n1

        if rev==backUp:
            return True
        return False
    

s=Solution()


# Input: x = 121
# Output: true
print(s.isPalindrome(121))