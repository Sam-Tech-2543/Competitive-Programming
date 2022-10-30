def icecreamParlor(m, arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==m:
                return [i+1,j+1]


print(icecreamParlor(4,[1,4,5,3,2]))
print(icecreamParlor(4,[2,2,4,3]))