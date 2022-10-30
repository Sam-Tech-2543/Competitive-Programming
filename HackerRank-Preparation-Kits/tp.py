def queensAttack(n, k, r_q, c_q, obstacles):
    #moves=[]
    ans=0

    if n==0:
        return 0

    #Up
    i=r_q+1
    while(i<=n):
        t=[i,c_q]
        if t not in obstacles:
            ans+=1
            #moves.append(t)
        else:
            break
        i+=1

    #Up-Right
    i=r_q+1
    j=c_q+1
    while(i<=n and j<=n):
        t=[i,j]
        if t not in obstacles:
            ans+=1
            #moves.append(t)
        else:
            break
        i+=1
        j+=1   

    #Right
    i=c_q+1
    while(i<=n):
        t=[r_q,i]
        if t not in obstacles:
            ans+=1
            #moves.append(t)
        else:
            break
        i+=1

    #Down-Right
    i=r_q-1
    j=c_q+1
    while(i<=n and j<=n):
        t=[i,j]
        if t not in obstacles:
            ans+=1
            #moves.append(t)
        else:
            break
        i-=1
        j+=1

    #Down
    i=r_q-1
    while(i>=1):
        t=[i,c_q]
        if t not in obstacles:
            ans+=1
            #moves.append(t)
        else:
            break
        i-=1

    #Down-Left
    i=r_q-1
    j=c_q-1
    while(i>=1 and j>=1):
        t=[i,j]
        if t not in obstacles:
            ans+=1
            #moves.append(t)
        else:
            break
        i-=1
        j-=1

    #Left
    i=c_q-1
    while(i>=1):
        t=[r_q,i]
        if t not in obstacles:
            ans+=1
            #moves.append(t)
        else:
            break
        i-=1

    #Left-Up
    i=r_q+1
    j=c_q-1
    while(i<=n and j>=1):
        t=[i,j]
        if t not in obstacles:
            ans+=1
            #moves.append(t)
        else:
            break
        i+=1
        j-=1

    
    #print(moves)
    return ans


print(queensAttack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]]))
print(queensAttack(10000,0,4187,5068,[])) #308369

"""100000 0
4187 5068"""
#queensAttack(4, 0, 4, 4, [])
#queensAttack(1, 0, 1, 1, [])