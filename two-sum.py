class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]: #them or bo -> list[int] cung k sao
        # 1. base case, if len(nums) < 2, return []
        if len(nums) < 2:
            return []
        # 2. set up an empty answer array and an empty hashmap
        #answer = []
        hashmap = {}
        # 3. go thru the indices in the nums array, and put (target - nums[i]) as i in the hashmap if it isn't, but return [hashmap[nums[i]], i] if it is
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]
            else:
                hashmap[target - nums[i]] = i
                print(i)

a = Solution()
print(a.twoSum([2,7,11,15], 9))