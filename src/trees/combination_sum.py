from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        result = []
        current = []

        def dfs(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):
                candidate = candidates[i]

                if candidate > remaining:
                    break

                current.append(candidate)
                dfs(i, remaining - candidate)
                current.pop()

        dfs(0, target)
        return result
