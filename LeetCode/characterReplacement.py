# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/description/

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        ans=0

        myHash=defaultdict(int)

        maxVal=0
        while r<len(s):
            myHash[s[r]]+=1
            
            maxVal=max(maxVal, myHash[s[r]])

            while (r-l+1)-maxVal>k:
                myHash[s[l]]-=1
                l+=1

            ans=max(ans,r-l+1)

            r+=1

        return ans
                