#https://leetcode.com/contest/biweekly-contest-90/problems/odd-string-difference/

"""
Each string words[i] can be converted into 
a difference integer array difference[i] of length n - 1 where difference[i][j] = words[i][j+1] - words[i][j] where 0 <= j <= n - 2
"""

def oddString(words):
    """
    :type words: List[str]
    :rtype: str
    """
    alphas="abcdefghijklmnopqrstuvwxyz"
    lst=[]
    for i in words:
        ans=0
        lst1=[]
        for j in range(len(i)-1):
            #print(i[j+1],alphas.index(i[j+1]),i[j],alphas.index(i[j]))
            lst1.append(alphas.index(i[j+1])-alphas.index(i[j]))

        lst.append(lst1)


    for i in range(len(lst)):
        if lst.count(lst[i])==1:
            return words[i]
        
    #print(lst)
        
    
print(oddString(["adc","wzy","abc"]))
print(oddString(["aaa","bob","ccc","ddd"]))
print(oddString(["ddd","poo","baa","onn"]))#ddd
oddString(["ddd","poo","baa","onn"])