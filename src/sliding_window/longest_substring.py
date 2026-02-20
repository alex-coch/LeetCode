class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        result = 1
        window = s[0:1]
        for idx, char in enumerate(s[1:], 1):
            while char in window and len(window) > 1:
                left += 1
                window = window[1:] if len(window) > 1 else window
            if char not in window:
                window = window + char
            result = max(result, len(window))
        return result

