from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time O(n), space O(1)
        if len(s) != len(t):
            return False
        count = defaultdict(int)
        for x in s:
            count[x] += 1
        for x in t:
            count[x] -= 1
        for val in count.values():
            if val != 0:
                return False
        return True

        # for i in set(s):
        #     if s.count(i) != t.count(i):
        #         return False
        # return True

