from itertools import combinations, permutations


class Solution:
    def countDistinct(self, nums: list[int], k: int, p: int) -> int:
        # time O(n^2), space O(n^2)
        hset = set()
        for idx, v in enumerate(nums):
            il = (v, )
            hset.add(il)
            i = 1 if v % p == 0 else 0
            for idxi, vi in enumerate(nums[idx+1:]):
                i += 1 if vi % p == 0 else 0
                if i >k:
                    continue
                il = il + (vi, )
                hset.add(il)

        return len(hset)
