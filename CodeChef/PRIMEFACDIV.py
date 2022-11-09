t=int(input())
for i in range(int(t)):
    lst=list(map(int,input().split()))
    
    op="YES"
    
    n=lst[1]
    
    l=[]
    # Save Prime Factors of lst[1] in l
    while n%2==0:
        if 2 not in l:
            l.append(2)
        n=n//2
    for i in range(3,int(n**0.5)+1,2):
        while n%i==0:
            if i not in l:
                l.append(i)
            n=n//i
    if n>2:
        if n not in l:
            l.append(n)
        

    for i in l:
        if lst[0]%i!=0:
            op="NO"
            break
    
    print(op)