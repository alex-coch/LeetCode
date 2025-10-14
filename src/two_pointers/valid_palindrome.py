class Solution:
    def isPalindrome(self, s: str) -> bool:
        ms = "".join((char for char in s if char.isalnum())).lower()
        length = len(ms)//2
        for idx in range(length):
            if ms[idx] != ms[-idx-1]:
                return False
        return True
