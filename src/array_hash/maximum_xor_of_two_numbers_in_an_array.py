class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        # time O(n), space O(n)
        L = len(bin(max(nums))) - 3
        res = 0
        mask = 0
        s = set()
        for i in range(L, -1, -1):
            mask |= (1 << i)
            for num in nums:
                s.add(num & mask)
            cur = res | (1 << i)
            for prefix in s:
                if cur ^ prefix in s:
                    res = cur
                    break
            s.clear()
        return res
