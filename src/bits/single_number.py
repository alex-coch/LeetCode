class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # time O(n), space O(1)
        xor = 0
        for num in nums:
            xor ^= num
        return xor
