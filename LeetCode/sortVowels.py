# 6926. Sort Vowels in a String
# https://leetcode.com/contest/biweekly-contest-109/problems/sort-vowels-in-a-string/

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A','E','I','O','U','a','e','i','o','u']
        lst1=[]
        lst2=[]
        s=list(s)
        
        for i in range(len(s)):
            if s[i] in vowels:
                lst1.append(s[i])
                lst2.append(i)

        lst1.sort()

        for i in range(len(lst2)):
            s[lst2[i]]=lst1[i]
        
        return "".join(s)
        

s=Solution()

# Input: s = "lEetcOde"
# Output: "lEOtcede"
# Explanation: 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. 
# The vowels are sorted according to their ASCII values, and the consonants remain in the same places.
print(s.sortVowels("lEetcOde"))

# Input: s = "lYmpH"
# Output: "lYmpH"
# Explanation: There are no vowels in s (all characters in s are consonants), so we return "lYmpH".
print(s.sortVowels("lYmpH"))