# This Function is slower because we have used lists, lists are slower while finding any item then set

def slowQueensAttack(n, k, r_q, c_q, obstacles):
    moves=0
    
    if n==0:
        return 0

    directions=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

    for i,j in directions:
        curr=[r_q+i,c_q+j]
        while 1<=curr[0]<=n and 1<=curr[1]<=n and [curr[0],curr[1]] not in obstacles:
            curr=[curr[0]+i,curr[1]+j]
            moves+=1


    return moves

def queensAttack(n, k, r_q, c_q, obstacles):
    moves=0
    
    if n==0:
        return 0

    ob=obstacles
    obstacles=set(tuple(i) for i in ob)

    directions={(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)}

    for i,j in directions:
        curr=(r_q+i,c_q+j)
        while 1<=curr[0]<=n and 1<=curr[1]<=n and (curr[0],curr[1]) not in obstacles:
            curr=(curr[0]+i,curr[1]+j)
            moves+=1


    return moves

print(queensAttack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]]))
print(queensAttack(10000,0,4187,5068,[])) 