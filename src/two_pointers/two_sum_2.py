class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        pointer1, pointer2 = 0, len(numbers) - 1

        while pointer1 < pointer2:
            sum = numbers[pointer1] + numbers[pointer2]
            if sum == target:
                break
            if sum < target:
                pointer1 += 1
            if sum > target:
                pointer2 -= 1

        return [pointer1+1, pointer2+1]
