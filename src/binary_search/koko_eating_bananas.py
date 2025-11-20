from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            total_time = sum((ceil(pile / k) for pile in piles))
            if total_time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
