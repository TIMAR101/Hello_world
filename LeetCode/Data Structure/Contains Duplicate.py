def containsDuplicate(nums) -> bool:

    nums.sort()

    if len(nums) == 2:
        return nums[0] == nums[1]

    for item in range(len(nums)-1):

        if nums[item] == nums[item+1]:

            return True

    return False



def containsDuplicateSet(nums) -> bool:

    return len(set(nums)) != len(nums)

print(containsDuplicate([0,1,2,3,4,5,6,7,8,9,10,0,1]))
print(containsDuplicateSet([0,1,2,3,4,5,6,7,8,9,10,0,1]))

l1 = [0,1,2,3,4,5,6,7,8,9,10,0,1]
l1.sort(reverse=True)
S1 = set(l1)
print(S1)









