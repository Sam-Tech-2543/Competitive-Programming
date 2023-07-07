# 2024. Maximize the Confusion of an Exam
# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans=0 # The Max Count of Consecutive Answers
        t=k # Back of the K = Number of changes allowed


        # For Consecutive F's
        l,r=0,0
        k=t
        while(r<len(answerKey)):
            if (answerKey[r]=="T"):
                if k>0:
                    k-=1
                else:
                    if answerKey[l]=="T":
                        k+=1
                    ans=max(ans,r-l)
                    l+=1
                    r-=1
            r+=1

        if k>=0:
            ans=max(ans,r-l)


        # For Consecutive T's
        l,r=0,0
        k=t
        while(r<len(answerKey)):
            if (answerKey[r]=="F"):
                if k>0:
                    k-=1
                else:
                    if answerKey[l]=="F":
                        k+=1
                    ans=max(ans,r-l)
                    l+=1
                    r-=1
            r+=1

        if k>=0:
            ans=max(ans,r-l)

        return ans


s=Solution()

# Input: answerKey = "TTFF", k = 2
# Output: 4
print(s.maxConsecutiveAnswers("TTFF",2))

# Input: answerKey = "TFFT", k = 1
# Output: 3
print(s.maxConsecutiveAnswers("TFFT",1))

# Input: answerKey = "TTFTTFTT", k = 1
# Output: 5
print(s.maxConsecutiveAnswers("TTFTTFTT",1))

# Input: answerKey = "FFFTTFTTFT", k = 3
# Output: 8
print(s.maxConsecutiveAnswers("FFFTTFTTFT",3))

# Input: answerKey = "FTFFTFTTTT", k = 4
# Output: 10
print(s.maxConsecutiveAnswers("FTFFTFTTTT",4))