# 503. Next Greater Element III
# https://leetcode.com/problems/next-greater-element-iii/

from typing import List

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n1,n2=0,0
        sn=[int(i) for i in str(n)]
        i1,i2=0,1

        if len(sn)>2:
            n1=sn[0]
            n2=sn[1]
        elif len(sn)==2:
            sn=str(n)[::-1]
            if int(sn)>n:
                return int(sn)
            else:
                return -1
        else:
            return -1
        print("Ok")
        for i in range(1,len(sn)):
            if sn[i]==n1:
                n1=sn[i]
                i1=i
            elif sn[i]<n1:
                n2=n1
                n1=sn[i]
                i1=i
            elif sn[i]<n2 and n1!=sn[i]:
                n2=sn[i]
                i2=i

        sn[i1],sn[i2]=sn[i2],sn[i1]
        
        print(i1,n1)
        print(i2,n2)
        print(sn)

        sn=list(map(str,sn))
        sn=int("".join(sn))

        if sn.bit_length()<=32 and sn>n:
            return sn
        return -1
    

s=Solution()

# Input: n = 12
# Output: 21
# s.nextGreaterElement(648161354867)
# print(s.nextGreaterElement(12))
print(s.nextGreaterElement(101))