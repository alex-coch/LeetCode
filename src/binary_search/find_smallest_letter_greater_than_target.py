class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        low, high = 0, len(letters) - 1
        pos = -1

        while low <= high:
            mid = low + (high - low) // 2
            if letters[mid] > target:
                pos = mid
                high = mid - 1
            else:
                low = mid + 1

        return letters[0] if pos == -1 else letters[pos]

# print(Solution().nextGreatestLetter(letters = ["c","f","j"], target = "a"))
# print(Solution().nextGreatestLetter(letters = ["c","f","j"], target = "c"))
# print(Solution().nextGreatestLetter(letters = ["x","x","y","y"], target = "z"))
print(Solution().nextGreatestLetter(letters = ["c","f","j"], target = "d"))