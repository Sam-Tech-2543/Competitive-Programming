"""flag=0
if s[0]=="1": 
        
    for j in range(len(s)):
        if s[j]!="1" and flag==0:
            flag=1
        if s[j]!="0" and flag==1:
            ans+=1
            break
"""

def check(n,s):
    ans=0
    flag=0
    stillToFind=True
    if s[0]=="0":
        if "1"*(int(n)-1)==s[1:]:
            ans=0
            stillToFind=False
            
        for j in range(len(s)):
            if stillToFind:
                if s[j]!="0" and flag==0:
                    flag=1
                if s[j]!="1" and flag==1:
                    ans+=1
                    break
            else:
                break
    print(ans)


check(5,"00000")
check(6,"010001")
check(6,"011111")