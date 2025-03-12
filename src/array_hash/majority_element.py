from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # time O(n), space O(1) Boyer-Moore Majority Voting Algorithm
        count, candidate = 0, None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate


