#https://leetcode.com/contest/biweekly-contest-90/problems/destroy-sequential-targets/

"""
You have a machine which can destroy targets. Seeding the machine with some nums[i] allows it to destroy all targets with values that can be 
represented as nums[i] + c * space, where c is any non-negative integer.
You want to destroy the maximum number of targets in nums.
"""

def destroyTargets(nums, space):
    if max(nums)>space:
        limit=max(nums)
    else:
        limit=space

    c=0
    m=0

    for i in range(limit):
        ans=0
        for j in range(len(nums)):
            if nums[j]+i*space in nums:
                ans+=1
        if ans>c:
            c=ans
            m=i

    print(m)


#nums = [3,7,8,1,1,5], space = 2
print(destroyTargets([3,7,8,1,1,5], 2))#1

#nums = [1,3,5,2,4,6], space = 2
print(destroyTargets([1,3,5,2,4,6], 2))#1