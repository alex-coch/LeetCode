class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # time O(n), space O(n)
        return len(nums) != len(set(nums))
