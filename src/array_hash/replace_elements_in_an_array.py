class Solution:
    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        # time O(n+m), space O(n)
        res = nums[:]
        hm = {num: idx for idx, num in enumerate(nums)}

        for x, r in operations:
            tmp = hm[x]
            res[tmp] = r
            del hm[x]
            hm[r] = tmp

        return res
        
