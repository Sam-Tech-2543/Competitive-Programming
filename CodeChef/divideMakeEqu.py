# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    c=0
    n1=min(a)
    
    for i in a:
        if n1!=i:
            c+=1
    
    for i in a:
        if i%n1!=0:
            c+=1
            break
    
    print(c)


"""
Sub-Task	Task #	Result    (time)
    1	      0	        WA  (0.034889)
    1	      1	        AC  (0.425917)
    1	      2	        AC  (0.712994)
"""