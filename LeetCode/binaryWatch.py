# 401. Binary Watch
# https://leetcode.com/problems/binary-watch/

class Solution(object):
    def getNumberOfBitsSet(self,num: int):
        n=str(bin(num).replace("0b", "")).count('1')
        return n

    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        lst=[]
        for i in range(0,12):
            for j in range(0,60):
                if self.getNumberOfBitsSet(i)+self.getNumberOfBitsSet(j)==turnedOn:
                    lst.append(f"{i}:{j:02d}")
        print(lst)
        


s=Solution()
s.readBinaryWatch(1)