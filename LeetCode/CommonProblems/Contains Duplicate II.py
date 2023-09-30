import input


class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:

        Setnums = set(nums)

        #nums = []

        TempDict = {}

        #Setnums1 = Setnums.copy()


        for item in Setnums:

            counts = nums.count(item)

            if nums.count(item) == 1:
                pass
                # Setnums1.remove(item)
            else:
                TempDict[item] = []
                startindex = 0
                for item1 in range(counts):

                    #index = nums.index(item, startindex))
                    index = nums.index(item, startindex)
                    TempDict[item].append(index)
                    startindex = index+1

        for item in TempDict.values():

            for item1 in range(len(item)-1):

                if item[item1+1] - item[item1] <= k:
                    return True

        return False

    def containsNearbyDuplicate1(self, k: int) -> bool:
        # Create hset for storing previous of k elements...
        hset = {}
        # Traverse for all elements of the given array in a for loop...
        for idx in range(len(nums)):
            # If duplicate element is present at distance less than equal to k, return true...
            if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
                return True
            hset[nums[idx]] = idx
        # If no duplicate element is found then return false...
        return False

    def containsNearbyDuplicate3(self, nums: List[int], k: int) -> bool:

        index_dict = {}

        for i, n in enumerate(nums):
            if n in index_dict and i - index_dict[n] <= k:
                return True

            index_dict[n] = i

	return False











S1 = Solution()

print(S1.containsNearbyDuplicate(input.nums, input.k))

nums = [1,2,3,1,2,3]








