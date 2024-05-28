class Solution:
    def countAndSay(self, n: int) -> str:
        ans="1"
        for i in range(n-1):
            j=0
            temp=""
            t=1
            
            while j<len(ans):
                if j+1<len(ans):
                    if ans[j]==ans[j+1]:
                        t+=1
                    else:
                        temp+=(str(t)+str(ans[j]))
                        t=1
                else:
                    temp+=(str(t)+str(ans[j]))

                j+=1

            ans=temp
            print(ans)

        return ans
    
s=Solution()

print(s.countAndSay(4)) 