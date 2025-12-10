from collections import defaultdict


class RangeFreqQuery:

    def __init__(self, arr: list[int]):
        self.mp = defaultdict(list)
        for i, v in enumerate(arr):
            self.mp[v].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        def lower_bound(positions, x):
            lo, hi = 0, len(positions)
            while lo < hi:
                mid = (lo + hi) // 2
                if positions[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def upper_bound(positions, x):
            lo, hi = 0, len(positions)
            while lo < hi:
                mid = (lo + hi) // 2
                if positions[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        positions = self.mp.get(value, [])
        left = lower_bound(positions, left)
        right = upper_bound(positions, right)
        return right - left


# Your RangeFreqQuery object will be instantiated and called as such:
obj = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
param_1 = obj.query(0, 11, 33)
