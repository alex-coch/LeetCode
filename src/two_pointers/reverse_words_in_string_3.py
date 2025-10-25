class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(map(lambda word: word[::-1], s.split()))

print(Solution().reverseWords("Mr Di"))