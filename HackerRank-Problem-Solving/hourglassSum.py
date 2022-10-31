def hourglassSum(arr):
    lst=[]

    for r in range(4):
        s=0
        for i in range(4):
            value=0
            for j in range(3):
                value+=(arr[r][s+j]+arr[r+2][s+j])
            value+=arr[r+1][i+1]
            lst.append(value)
            
            s+=1

    return max(lst)