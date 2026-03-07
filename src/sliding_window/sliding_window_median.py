class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        def pos(a, x):
            l, r = 0, len(a)
            while l < r:
                m = (l + r) // 2
                if a[m] < x:
                    l = m + 1
                else:
                    r = m
            return l

        w = sorted(nums[:k])
        ans = []

        for i in range(k, len(nums) + 1):
            ans.append((w[k//2] + w[(k-1)//2]) / 2)
            if i == len(nums):
                break
            w.pop(pos(w, nums[i-k]))
            w.insert(pos(w, nums[i]), nums[i])

        return ans
