def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    n1,n2=0,0
    
    for i in apples:
        if(i + a >= s and i + a <= t):
            n1+=1
    
    for j in oranges:
        if(j + b >= s and j + b <= t):
            n2+=1
    
    print(n1)           
    print(n2)   