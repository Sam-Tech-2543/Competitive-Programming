class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans=set()
        lst=[]

        nums.sort()

        def backTracking(i):
            if i==len(nums):
                if len(lst)!=0:
                    ans.add(tuple(lst))
                return
            
            flag=1
            l, r=0, len(lst)-1
            find=nums[i]-k
            
            while l<=r:
                m=(l+r)//2
                if lst[m]>find:
                    r=m-1
                elif lst[m]<find:
                    l=m+1
                else:
                    flag=0
                    break

            if flag:
                lst.append(nums[i])
                backTracking(i+1)
                lst.pop()
                backTracking(i+1)
            else:
                backTracking(i+1)

        backTracking(0)

        print(ans)

        return len(list(ans))

        