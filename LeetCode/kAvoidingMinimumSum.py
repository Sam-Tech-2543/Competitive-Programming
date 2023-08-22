class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        if n==1:
            return 1

        ans=0
        c=0
        i=1
        while c<n:
            ans+=i
            c+=1

            if i+1==k:
                i+=2
            else:
                i+=1
            print(i,ans)

        return ans

s=Solution()
# print(s.minimumSum(5,4))
print(s.minimumSum(2,2))