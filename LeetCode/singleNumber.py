from typing import List

# 136. Single Number
# https://leetcode.com/problems/single-number/

# 137. Single Number II
# https://leetcode.com/problems/single-number-ii/

class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        myDict=dict()
        for i in nums:
            if i in myDict:
                myDict[i]+=1
            else:
                myDict[i]=1
        vals=list(myDict.values())
        keys=list(myDict.keys())
        return keys[vals.index(1)]
    
# 260. Single Number III
# https://leetcode.com/problems/single-number-iii/

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        myDict=dict()
        for i in nums:
            if i in myDict:
                myDict[i]+=1
            else:
                myDict[i]=1
        vals=list(myDict.values())
        keys=list(myDict.keys())
        i1=vals.index(1)
        i2=vals[i1+1:].index(1)+i1+1
        return [keys[i1],keys[i2]]
    
s=Solution1()
print(s.singleNumber([4,1,2,1,2]))

s=Solution2()
print(s.singleNumber([1,2,1,3,2,5]))
print(s.singleNumber([0,1,5,5]))

