def guess(num: int) -> int:
    pick = 6
    if num == pick:
        return 0
    elif num > pick:
        return -1
    else:
        return 1



class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n

        while l <= r:
            mid = (l + r) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g == 1:
                l = mid + 1
            else:
                r = mid

print(Solution().guessNumber(10))