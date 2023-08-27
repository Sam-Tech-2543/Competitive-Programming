# 2833. Furthest Point From Origin
# https://leetcode.com/problems/furthest-point-from-origin/

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        n1,n2=0,0

        for i in moves:
            if i=='L':
                n1-=1
                n2-=1
            elif i=='R':
                n1+=1
                n2+=1
            else:
                n1-=1
                n2+=1
            
        return max(abs(n1),abs(n2))
            
        
# Input: moves = "L_RL__R"
# Output: 3
# Explanation: The furthest point we can reach from the origin 0 is point -3 through the following sequence of moves "LLRLLLR".
s=Solution()
print(s.furthestDistanceFromOrigin("L_RL__R"))