t = int(input())
for i in range(t):
    s=input()
    n1,n2=int(s.split()[0]),int(s.split()[1])
    o1,o2=n1,n2

    ans=True

    if o2%o1==0:
        print("YES")
        ans=False
    else:
        f=True
        while(f):
            o1+=1
            o2+=1
            if o1%n1==0 or o2%n2==0:
                f=False
                #print(o1,o2)
            if o2%o1==0:
                f=False
                print("YES")
                ans=False
        
    if ans:
        print("NO")