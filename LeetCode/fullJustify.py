# 68. Text Justification
# https://leetcode.com/problems/text-justification/

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans=[]
        lst,l=[],0

        i=0
        while i<len(words):
            if l+len(lst)+len(words[i])>maxWidth: #len(lst) as we are not adding spaces earlier
                spaces=maxWidth-l # Spaces we need to have

                # Used max if we have only 1 word in Line
                sb=spaces//max(1,(len(lst)-1)) # Spaces between
                sr=spaces%(max(1,len(lst)-1)) # Extra spacing Between words

                for j in range(max(1,len(lst)-1)):
                    lst[j]+=" "*sb
                    # Greedy Approach to add extra spaces
                    if sr:
                        lst[j]+=" "
                        sr-=1
                
                ans.append("".join(lst))

                lst,l=[],0 # Resetting the Line and Length

            # Adding the Word in the line and updating the length
            lst.append(words[i])
            l+=len(words[i])

            i+=1

        # Adding the Last Line
        rem=maxWidth-(l+len(lst)-1)
        lst[-1]+=" "*rem
        ans.append(" ".join(lst))

        return ans
        