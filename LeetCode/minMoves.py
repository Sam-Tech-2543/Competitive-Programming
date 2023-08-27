# 2139. Minimum Moves to Reach Target Score
# https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if target%2==0:
            temp=target
        else:
            temp=target-1

        lst=[]

        i=maxDoubles
        while temp//2>0 and i>0:
            temp=temp//2
            lst.append(temp)
            i-=1

        lst=lst[::-1]

        n=1
        ans=0
        while n!=target:
            if lst==[]:
                ans+=(target-n)
                n+=(target-n)
                break
        
            if n==lst[0]:
                n=2*n
                lst.pop(0)
                ans+=1
            else:
                t=lst[0]
                ans+=(t-n)
                n+=(t-n)

            if n==target:
                break

        return ans
    
s=Solution()

# target = 656101987
# maxDoubles = 1
print(s.minMoves(656101987,1))

# Input: target = 19, maxDoubles = 2
# Output: 7
print(s.minMoves(19,2))

# Input: target = 10, maxDoubles = 4
# Output: 4
print(s.minMoves(10,4))
