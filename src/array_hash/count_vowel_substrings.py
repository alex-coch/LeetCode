class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        # time O(n), space O(1)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        result = 0
        start = 0
        vowel_idx = {}
        for idx, c in enumerate(word):
            if c in vowels:
                if not vowel_idx:
                    start = idx
                vowel_idx[c] = idx
                if len(vowel_idx) == 5:
                    result += min(vowel_idx.values()) - start + 1
            else:
                vowel_idx = {}

        return result


print(Solution().countVowelSubstrings("aeiouuka"))
