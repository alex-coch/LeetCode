from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        # time O(n), space O(n)
        hm = Counter(s)
        hm = {k: v for k, v in sorted(hm.items(), key=lambda item: -item[1])}
        res = ""
        for c in hm:
            print(c)
            res += c * hm[c]
        return res

        
