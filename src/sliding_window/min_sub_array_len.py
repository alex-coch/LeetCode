class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        if nums[left] >= target:
            return 1
        window_sum = nums[left]
        result = 1000000
        for right in range(1, len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                result = min(result, right-left+1)
                window_sum -= nums[left]
                left += 1
        return result if result < 1000000 else 0
