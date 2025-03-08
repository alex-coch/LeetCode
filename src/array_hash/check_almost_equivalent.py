from collections import Counter


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        # time O(n + m), space O(1)
        hm1 = Counter(word1)
        hm2 = Counter(word2)
        for k, v in hm1.items():
            if k not in hm2 and v > 3:
                return False
            if k in hm2 and abs(v - hm2[k]) > 3:
                return False
        for k, v in hm2.items():
            if k not in hm1 and v > 3:
                return False
        return True


print(Solution().checkAlmostEquivalent("zzzyyy", "iiiiii"))
        
