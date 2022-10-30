def flatlandSpaceStations(n, c):
    maxLst=[0]

    if n==len(c):
        return 0

    c.sort()

    for i in range(n):
        if i not in c:
            l1=-1 #Before
            l2=-1 #After
            for j in c:
                if j>i and l2==-1:
                    l2=j
                    break

            for j in c[::-1]:
                if j<i and l1==-1:
                    l1=j
                    break

            if l2==-1:
                maxLst.append(i-l1)
            elif l1==-1:
                maxLst.append(l2-i)
            else:
                if i-l1<l2-i:
                    maxLst.append(i-l1)
                else:
                    maxLst.append(l2-i)

    return max(maxLst)

#print(flatlandSpaceStations(5,[0,4]))
#print(flatlandSpaceStations(6,[0,1,2,3,4,5]))
print("Answer=",flatlandSpaceStations(20,[13,1,11,10,6]))
#flatlandSpaceStations(20,[13,1,11,10,6])