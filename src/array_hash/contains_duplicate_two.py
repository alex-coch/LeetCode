class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # time O(n), space O(n)
        hm = {}
        for idx, num in enumerate(nums):
            if num in hm and (idx - hm[num]) <= k:
                return True
            hm[num] = idx
        return False