from collections import deque
from typing import List


class Solution:
    # DFS + Backtracking
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = []
        used = set()

        def dfs():
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return

            for num in nums:
                if num in used:
                    continue

                # Choose
                permutation.append(num)
                used.add(num)

                # Explore
                dfs()

                # Unchoose (Backtrack)
                permutation.pop()
                used.remove(num)

        dfs()
        return result

    # bfs
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     result = []
    #     queue = deque([([], set())])
    #
    #     while queue:
    #         permutation, used = queue.popleft()
    #
    #         if len(permutation) == len(nums):
    #             result.append(permutation)
    #             continue
    #
    #         for num in nums:
    #             if num not in used:
    #                 queue.append((
    #                     permutation + [num],
    #                     used | {num}
    #                 ))
    #
    #     return result

print(Solution().permute([0, 1]))
