from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        hm_t = Counter(t)
        window = {}
        cnt_have = 0
        len_hm_t = len(hm_t)

        len_result = float("inf")
        left_result = 0
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in hm_t and window[char] == hm_t[char]:
                cnt_have += 1

            while cnt_have == len_hm_t:
                if (right - left + 1) < len_result:
                    len_result = right - left + 1
                    left_result = left

                left_char = s[left]
                window[left_char] -= 1
                if left_char in hm_t and window[left_char] < hm_t[left_char]:
                    cnt_have -= 1
                left += 1

        return "" if len_result == float("inf") else s[left_result: left_result + len_result]

print(Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))