# Gold is Old
# https://practice.geeksforgeeks.org/contest/gfg-weekly-coding-contest-112/problems

from typing import List


class Solution:
    def MaxXP(self, n : int, k : int, initial_exp : int, exp_req : List[int], exp_gain : List[int]) -> int:
        # code here
        
        hm=dict()
        for i in range(n):
            hm[i]=1
        
        
        for j in range(k):
            mv=0
            iv=-1
            for i in range(n):
                if hm[i] and exp_req[i]<=initial_exp and mv<exp_gain[i]:
                    mv=exp_gain[i]
                    iv=i
            
            if iv==-1:
                return initial_exp
            
            initial_exp+=mv
            hm[iv]=0
            
        return initial_exp
    

s=Solution()

# Input:
# n = 5
# intial_exp = 10
# exp_req = [3,2,4,1,2]
# exp_gain = [5,3,6,2,4]
# k = 3
# Output: 
# 25
# Explanation:
# As your initial experience points are enough to begin any quest, 
# you can complete quests 1,3 and 5 gaining 5, 6 and 4 points respectively, having 25 points at the end.
print(s.MaxXP(5,3,10,[3,2,4,1,2],[5,3,6,2,4]))


# Input:
# n = 3
# initial_exp = 15
# exp_req = [20,10,30]
# exp_gain = [1,5,2]
# k = 3
# Output: 
# 21
# Explanation: 
# You can complete the 2nd quest and gain 5 points. Now having 20 points, you can now complete the first quest as well.
# As you do not have enough points to complete the last quest, 21 is the maximum number of points you can accumulate.
print(s.MaxXP(3,3,15,[20,10,30],[1,5,2]))