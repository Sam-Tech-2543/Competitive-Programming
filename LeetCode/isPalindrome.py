# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=""
        for i in s:
            if i.isalpha():
                l+=i.lower()

        return l==l[::-1]
    

s=Solution()

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
print(s.isPalindrome("A man, a plan, a canal: Panama"))