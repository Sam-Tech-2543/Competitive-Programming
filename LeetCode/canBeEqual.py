# bool canBeEqual(string s1, string s2) {
     
#         if(s1 == s2)
#                 return 1;
#         swap(s1[0] , s1[2]);
#         if(s1 == s2)
#                 return 1;
#         swap(s1[1] , s1[3]);
#         if(s1 == s2)
#                 return 1;
#         swap(s1[0],s1[2]);
#         if(s1 == s2)
#                 return 1;
    
#         return 0;
#     }
# };

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        
        s1=list(s1)
        s2=list(s2)

        s1[0],s1[2]=s1[2],s1[0]
        if s1==s2:
            return True
        
        s1[1],s1[3]=s1[3],s1[1]
        if s1==s2:
            return True
        
        s1[0],s1[2]=s1[2],s1[0]
        if s1==s2:
            return True
        
        return False
        
        
        

# You can apply the following operation on any of the two strings any number of times:

# Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.
# Return true if you can make the strings s1 and s2 equal, and false otherwise.


s=Solution()

# Input: s1 = "abcd", s2 = "cdab"
# Output: true
# Explanation: We can do the following operations on s1:
# - Choose the indices i = 0, j = 2. The resulting string is s1 = "cbad".
# - Choose the indices i = 1, j = 3. The resulting string is s1 = "cdab" = s2.
print(s.canBeEqual("abcd","cdab"))\

# Input: s1 = "abcd", s2 = "dacb"
# Output: false
# Explanation: It is not possible to make the two strings equal.
print(s.canBeEqual("abcd","dacb"))