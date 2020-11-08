"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


{
    3: 0
    1: [1, 3]
    5: 2
}



loop  through the input array
target - 1 in the dict???
answer is [0, 3]


target is 2
{ 3: 0, 1: 1, 5: 2}

[currentInd, dict[1]]

CODE
----
create dict
loop through the input 
    check if target - currelement in dict,
        then return
    keep adding stuff in dict
    if already exists, then overwrite

"""

def twoSum(nums, target):
    indices = {}
    for i in range(len(nums)):
        findInDict = target - nums[i]
        if findInDict in indices:
            return [i, indices[findInDict]]
        indices[nums[i]] = i
    return [-1, -1]

print(twoSum([1], 4))