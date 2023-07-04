class Solution:
    def isValid(self, s: str) -> bool:
        lst=[]
        myDict={')':'(','}':'{',']':'['}
        for i in s:
            if i=='{' or i=='(' or i=='[':
                lst.append(i)
            else:
                if lst==[]:
                    return False
                if lst[-1]==myDict[i]:
                    lst.pop()
                else:
                    return False
        if(lst==[]):
            return True
        else:
            return False