from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_len = len(words[0])
        total_words = len(words)

        target = Counter(words)
        res = []

        for offset in range(word_len):

            left = offset
            window = {}
            count = 0

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in target:
                    window[word] = window.get(word, 0) + 1
                    count += 1

                    while window[word] > target[word]:
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == total_words:
                        res.append(left)

                else:
                    window.clear()
                    count = 0
                    left = right + word_len

        return res
