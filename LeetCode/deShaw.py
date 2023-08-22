from collections import defaultdict
def idk(arr, k):

    seen = defaultdict(list)
    pre = []
    s = 0
    for i in range(len(arr)):
        if arr[i] == k:
            s+= 1
        else:
            seen[arr[i]].append(i)
        pre.append(s)

    # print(seen)
    # print(pre)

    op_max = 0
    for i, j in seen.items():
        maxss = float('-inf')
        temp = 0
        lst = 0
        for k in range(len(j)):
            temp = pre[j[lst]] + (k - lst) - pre[j[k]] + 1
            maxss = max(temp, maxss)
            if temp < 0:
                lst = k
                temp =  0
        op_max = max(maxss, op_max)
    return op_max+s


def soln(nums, target):
    ans=0
    count=nums.count(target)
    temp=count

    for j in range(0,len(nums)):
        v=1
        lst=[nums[j]]
        diff=target-lst[0]

        for k in range(j+1,len(nums)):
            lst.append(nums[k])
            if target-nums[k]==diff:
                v+=1
            if nums[k]==target:
                temp-=1

            a1=v+temp
            ans=max(ans,a1)

        temp=count

    return ans

a = [1,2,1,3,3,2,2,2,2,3]
print("My Answer: ",soln(a, 2))
print("Avdhut's Answer: ",idk(a, 2))

arr = [1 ,2, 1, 2, 2, 1, 3, 3, 3, 2, 2 ,2 ,3, 3, 2, 4, 8, 1, 2]
k =3
print("Answer: ",soln(arr, k))
print("Avdhut's Answer: ",idk(arr, k))

a = [1,2,1,2,1,2,3,1,3,2,3,3,2]
print("Answer: ",soln(a, 2))
print("Avdhut's Answer: ",idk(a, 2))

a = [1,2,1,2,1,2,3,1,3]
print("Answer: ",soln(a, 2))
print("Avdhut's Answer: ",idk(a, 2))

 

# a = [1,2,1,2,1,2,3,1,3]
# print(idk(a, 2))
# a = [1,2,1,2,1,2,3,1,3,2,3,3,2]
# print(idk(a, 2))



# def soln(nums, target):
#     ans=0
#     count=nums.count(target)
#     temp=count

#     for j in range(0,len(nums)):
#         for k in range(j,len(nums)):
#             lst=nums[j:k+1]
#             print(lst, j ,k+1)
            
#             v=1
#             if lst:
#                 diff=target-lst[0]
#                 for m in range(1,len(lst)):
#                     if target-lst[m]==diff:
#                         v+=1
#                     if lst[m]==target:
#                         temp-=1
                
#                 print(f"{lst=}, {v=}, {temp=}, {diff=}")

#                 a1=v+temp
#                 ans=max(ans,a1)
#                 temp=count
#         print("---------------")
                   
#     return ans