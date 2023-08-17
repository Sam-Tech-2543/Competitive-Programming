# 1657. Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close/

from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # if len(word1)!=len(word2):
        #     return 0

        # myHash1={}
        # myHash2={}

        # for i in word1:
        #     a=myHash1.get(i,None)
        #     if a:
        #         myHash1[i]+=1
        #     else:
        #         myHash1[i]=1

        # for i in word2:
        #     a=myHash2.get(i,None)
        #     if a:
        #         myHash2[i]+=1
        #     else:
        #         myHash2[i]=1

        # if set(myHash1.keys())!=set(myHash2.keys()) or sorted(myHash1.values())!=sorted(myHash2.values()):
        #     return False

        # return True 

        myHash1=Counter(word1)
        myHash2=Counter(word2)

        if set(myHash1.keys())!=set(myHash2.keys()) or sorted(myHash1.values())!=sorted(myHash2.values()):
            return False

        return True 


s=Solution()


# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"
print(s.closeStrings("abc","bca"))

# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
print(s.closeStrings("a","aa"))

# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"
print(s.closeStrings("cabbba","abbccc"))

