# 920. Number of Music Playlists
# https://leetcode.com/problems/number-of-music-playlists/

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9+7
        dp={}

        def count(currGoal, oldSongs):
            if currGoal==0 and oldSongs==n:
                return 1
            if currGoal==0 or oldSongs>n:
                return 0

            if (currGoal, oldSongs) in dp:
                return dp[(currGoal,oldSongs)]

            # Choose New Song
            ans = (n - oldSongs) * count(currGoal-1, oldSongs+1)

            if oldSongs>k:
                # Choose Old Song
                ans+=(oldSongs-k)*count(currGoal-1,oldSongs)

            dp[(currGoal,oldSongs)]=ans % mod
            return dp[(currGoal,oldSongs)]

        return count(goal,0)
    

s=Solution()

# Input: n = 3, goal = 3, k = 1
# Output: 6
# Explanation: There are 6 possible playlists: 
# [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].
print(s.numMusicPlaylists(3,3,1))

# Input: n = 2, goal = 3, k = 0
# Output: 6
# Explanation: There are 6 possible playlists: 
# [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].
print(s.numMusicPlaylists(2,3,0))

# Input: n = 2, goal = 3, k = 1
# Output: 2
# Explanation: There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].
print(s.numMusicPlaylists(2,3,1))