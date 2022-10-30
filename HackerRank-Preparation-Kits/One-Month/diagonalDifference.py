def diagonalDifference(arr):
    # Write your code here
    i,j=0,len(arr[0])-1
    lr,rl=0,0
    for k in range(len(arr)):
        lr+=arr[k][i]
        rl+=arr[k][j]

        i+=1
        j-=1
    return abs(lr-rl)

print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))

