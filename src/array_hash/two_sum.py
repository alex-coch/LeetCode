class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # time O(n), space O(n)
        hashmap = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hashmap:
                return [i, hashmap[comp]]
            hashmap[nums[i]] = i
        return []
