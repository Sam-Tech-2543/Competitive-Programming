class Solution:
    def myAtoi(self, s: str) -> int:         
        n=0
        s=s.strip()

        if s=='':
            return 0

        INT_MAX = 2147483647
        INT_MIN = -2147483648

        if(s[0]=='-'):
            flag=1
            start=1
        elif(s[0]=='+'):
            flag=0
            start=1
        else:
            flag=0
            start=0

        for i in range(start,len(s)):
            if '0' <= s[i] <= '9':
                n=n * 10 + (ord(s[i]) - ord('0'))
            else:
                break

        if flag==1:
            n=n*-1

        if(n<INT_MIN):
            return INT_MIN
        elif(n>INT_MAX):
            return INT_MAX

        return n
                