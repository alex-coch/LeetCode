class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # time O(n), space O(1)
        # left = max_length = 0
        # char_set = set()
        #
        # for right in range(len(s)):
        #     while s[right] in char_set:
        #         char_set.remove(s[left])
        #         left += 1
        #
        #     char_set.add(s[right])
        #     max_length = max(max_length, right - left + 1)
        #
        # return max_length

        # time O(n), space O(1)
        # max_length = left = 0
        # count = {}
        #
        # for right, c in enumerate(s):
        #     count[c] = 1 + count.get(c, 0)
        #     while count[c] > 1:
        #         count[s[left]] -= 1
        #         left += 1
        #
        #     max_length = max(max_length, right - left + 1)
        #
        # return max_length

        # time O(n), space O(1)
        max_length = 0
        left = 0
        last_seen = {}

        for right, c in enumerate(s):
            if c in last_seen and last_seen[c] >= left:
                left = last_seen[c] + 1

            max_length = max(max_length, right - left + 1)
            last_seen[c] = right

        return max_length
