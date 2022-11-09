# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    n1=int(n/2)
    n2=int((n/2))
    if s[:n1]==s[n2:]:
        print("YES")
    else:
        print("NO")