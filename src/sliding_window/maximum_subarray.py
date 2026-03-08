class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current = best = nums[0]

        for x in nums[1:]:
            current = max(x, current + x)
            best = max(best, current)

        return best
