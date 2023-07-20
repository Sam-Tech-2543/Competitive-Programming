# 2126. Destroying Asteroids
# https://leetcode.com/problems/destroying-asteroids/description/

from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for i in range(len(asteroids)):
            if mass < asteroids[i]:
                return False
            mass += asteroids[i]

        return True
    
s=Solution()

# Input: mass = 10, asteroids = [3,9,19,5,21]
# Output: true
print(s.asteroidsDestroyed(10, [3,9,19,5,21]))

# Input: mass = 5, asteroids = [4,9,23,4]
# Output: false
print(s.asteroidsDestroyed(5, [4,9,23,4]))