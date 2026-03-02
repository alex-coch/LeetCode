class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        window = []
        cnt = result = 0

        for idx in range(len(nums)):
            window.append(nums[idx])
            if nums[idx] == 0:
                cnt += 1
                while cnt > k:
                    if window[0] == 0:
                        cnt -= 1
                    window = window[1:]
            result = max(result, len(window))
        return result
