class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        lst=list(number)
        for i,n in enumerate(lst):
            if i+1<len(number) and lst[i+1]==lst[i]==lst[i+1]:
                continue
            if n==digit:
                lst.pop(i)
                break
        return "".join(lst)
    
s=Solution()

print(s.removeDigit("133235","3"))