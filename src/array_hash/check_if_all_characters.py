from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # time O(n), space O(1)
        return False if len(set(Counter(s).values()))>1 else True


