class Solution:
    def isHappy(self, n: int) -> bool:
        # time O((log n)²), space O(log n)
        if n == 1:
            return True
        h = set()
        while n != 1:
            if n in h:
                return False
            else:
                h.add(n)
            n = sum(int(item)**2 for item in str(n))
            if n == 1:
                return True

