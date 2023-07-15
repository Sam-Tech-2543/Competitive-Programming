# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

from typing import List

class Solution:
    # Time Complexity in Worst Case = O(n^2)
    def dailyTemperatures_TLE(self, temperatures: List[int]) -> List[int]:
        ans=[0]*(len(temperatures))
        for i in range(len(temperatures)):
            temp=temperatures[i]
            for j in range(i,len(temperatures)):
                if temp<temperatures[j]:
                    ans[i]=j-i
                    break
        return ans

    # Time Complexity = O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*(len(temperatures))

        stack=[]
        stack.append(len(temperatures)-1)

        for i in range(len(temperatures)-1,-1,-1):
            while(stack!=[]):
                t=stack.pop()
                if temperatures[t]>temperatures[i]:
                    ans[i]=t-i
                    stack.append(t)
                    break
            stack.append(i)
            
        print(ans)

        return ans

s=Solution()

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
s.dailyTemperatures([73,74,75,71,69,72,76,73])

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
s.dailyTemperatures([30,40,50,60])

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
s.dailyTemperatures([30,60,90])