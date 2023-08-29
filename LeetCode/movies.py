class Solution:
    def minRooms(self, movies):
        lst=sorted(movies, key= lambda x: x[0])

        ans=[[lst[0][0],lst[0][1]-lst[0][0]]]
        res=1

        for i in range(1,len(lst)):
            for j in range(len(ans)):
                if lst[i][0]-ans[j][0]>ans[j][1]:
                    ans[j][0]=lst[i][0]
                    ans[j][1]=0
                else:
                    ans[j][0]=lst[i][0]
                    ans[j][1]=lst[i][1]-ans[j][1]

            got=False
            n=None
            for j in range(len(ans)):
                if ans[j][1]==0:
                    got=True
                    n=j
                    break
            if got:
                ans[n][0]=lst[i][0]
                ans[n][1]=lst[i][1]-lst[i][0]
            else:
                ans.append([lst[i][0],lst[i][1]-lst[i][0]])
                res+=1

        return res
    

s=Solution()
print(s.minRooms([[30,75],[0,50],[60,150]]))
print(s.minRooms([[0,50],[30,70],[40,90],[300,400]]))
print(s.minRooms([[20,60],[30,90],[50,90],[110,150]]))
print(s.minRooms([[0,50],[30,55],[25,56],[67,68]]))